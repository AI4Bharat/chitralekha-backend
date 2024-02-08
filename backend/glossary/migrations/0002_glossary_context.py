# Generated by Django 4.1.5 on 2024-02-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("glossary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="glossary",
            name="context",
            field=models.CharField(
                choices=[
                    ("general", "General"),
                    ("news", "News"),
                    ("education", "Education"),
                    ("legal", "Legal"),
                    ("government-press-release", "Government Press Release"),
                    ("healthcare", "Healthcare"),
                    ("agriculture", "Agriculture"),
                    ("automobile", "Automobile"),
                    ("tourism", "Tourism"),
                    ("financial", "Financial"),
                    ("movies", "Movies"),
                    ("subtitles", "Subtitles"),
                    ("sports", "Sports"),
                    ("technology", "Technology"),
                    ("lifestyle", "Lifestyle"),
                    ("entertainment", "Entertainment"),
                    ("art-and-culture", "Art and Culture"),
                    ("parliamentary", "Parliamentary"),
                    ("economy", "Economy"),
                    ("history", "History"),
                    ("philosophy", "Philosophy"),
                    ("religion", "Religion"),
                    ("national-security-and-defence", "National Security and Defence"),
                    ("literature", "Literature"),
                    ("geography", "Geography"),
                ],
                default="general",
                max_length=50,
                verbose_name="Context",
            ),
        ),
    ]
