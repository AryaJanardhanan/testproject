# Generated by Django 5.0.6 on 2024-07-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]