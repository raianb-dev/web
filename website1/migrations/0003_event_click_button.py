# Generated by Django 4.2.7 on 2024-10-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0002_alter_event_click_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_click',
            name='button',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
