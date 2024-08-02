# Generated by Django 4.1.5 on 2024-06-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0017_alter_task_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.CharField(
                choices=[
                    ("TRANSCRIPTION_EDIT", "Transcription Edit"),
                    ("TRANSCRIPTION_REVIEW", "Transcription Review"),
                    ("TRANSLATION_EDIT", "Translation Edit"),
                    ("TRANSLATION_REVIEW", "Translation Review"),
                    ("VOICEOVER_EDIT", "VoiceOver Edit"),
                    ("VOICEOVER_REVIEW", "VoiceOver Review"),
                    ("TRANSLATION_VOICEOVER_EDIT", "Translation VoiceOver Edit"),
                    ("TRANSLATION_VOICEOVER_REVIEW", "Translation VoiceOver Review"),
                ],
                max_length=35,
            ),
        ),
    ]