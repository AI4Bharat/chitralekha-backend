# Generated by Django 3.2.16 on 2022-12-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("translation", "0010_alter_translation_translation_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translation",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="translation.translation",
                verbose_name="Parent Translation",
            ),
        ),
    ]
