# Generated by Django 4.1 on 2022-11-02 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_rename_answers_answer_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updated_at',
        ),
    ]
