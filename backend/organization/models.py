from django.db import models
from django.conf import settings
from django.db import models, transaction
from django.core.mail import send_mail
import secrets
import string


class Organization(models.Model):
    """
    Model for organizations
    """

    title = models.CharField(
        verbose_name="organization_title", max_length=512, null=False
    )

    email_domain_name = models.CharField(
        verbose_name="organization_email_domain", max_length=512, null=True
    )

    is_active = models.BooleanField(
        verbose_name="organization_is_active",
        default=True,
        help_text=("Designates whether an organization is active or not."),
    )

    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="organization_created",
        verbose_name="created_by",
    )

    organization_owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="organization_owned",
        verbose_name="organization_owner",
    )

    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)

    def __str__(self):
        return self.title + ", id=" + str(self.pk)


class Invite(models.Model):
    """
    Invites to invite users to organizations.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="invite_users",
        on_delete=models.CASCADE,
        null=True,
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        null=True,
        related_name="invite_oganization",
        verbose_name="organization",
    )

    invite_code = models.CharField(
        verbose_name="invite_code", max_length=256, null=True, unique=True
    )

    def __str__(self):
        return (
            str(self.user.email)
            + " for "
            + str(self.organization.title)
            + " organization"
        )

    @classmethod
    def create_invite(cls, organization=None, users=None):
        with transaction.atomic():
            for user in users:
                try:
                    invite = Invite.objects.get(user=user)
                except:
                    invite = Invite.objects.create(organization=organization, user=user)
                    invite.invite_code = cls.generate_invite_code()
                    invite.save()
                send_mail(
                    "Invitation to join Organization",
                    f"Hello! You are invited to {organization.title}. Your Invite link is: https://chitralekha.ai4bharat.org/#/invite/{invite.invite_code}",
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                )

    # def has_permission(self, user):
    #     if self.organization.created_by.pk == user.pk or user.is_superuser:
    #         return True
    #     return False

    @classmethod
    def generate_invite_code(cls):
        return "".join(
            secrets.choice(string.ascii_uppercase + string.digits) for i in range(10)
        )
