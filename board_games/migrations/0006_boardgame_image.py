# Generated by Django 5.0.3 on 2024-03-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0005_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='boardgame_images/'),
        ),
    ]