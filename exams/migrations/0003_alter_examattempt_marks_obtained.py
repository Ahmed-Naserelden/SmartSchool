# Generated by Django 4.2.7 on 2023-12-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_alter_exam_level_alter_question_answer_studentanswer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examattempt',
            name='marks_obtained',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
