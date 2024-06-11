# Generated by Django 3.2.16 on 2023-02-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("voiceover", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="voiceover",
            name="voice_over_type",
            field=models.CharField(
                choices=[
                    ("MACHINE_GENERATED", "Machine Generated"),
                    ("MANUALLY_CREATED", "Manually Created"),
                ],
                max_length=35,
                verbose_name="Voice Over Type",
            ),
        ),
    ]
