# Generated by Django 4.1 on 2022-11-01 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('descriptions', '0002_alter_description_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='waste_bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
