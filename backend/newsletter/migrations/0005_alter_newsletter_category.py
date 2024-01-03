# Generated by Django 4.1.5 on 2024-01-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newsletter", "0004_subscribedusers_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("RELEASE", "Release"),
                    ("DOWNTIME", "Downtime"),
                    ("GENERAL", "General"),
                ],
                default=None,
                max_length=35,
                null=True,
                verbose_name="Category of newsletter",
            ),
        ),
    ]
