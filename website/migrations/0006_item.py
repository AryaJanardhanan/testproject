# Generated by Django 5.0.6 on 2024-06-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_f_name_profile_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('des', models.TextField(max_length=400)),
            ],
        ),
    ]