# Generated by Django 3.2.16 on 2023-01-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0007_auto_20221228_0519"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "New"),
                    ("SELECTED_SOURCE", "Selected Source"),
                    ("INPROGRESS", "Inprogress"),
                    ("COMPLETE", "Complete"),
                ],
                default=None,
                max_length=35,
                verbose_name="Task Status",
            ),
        ),
    ]