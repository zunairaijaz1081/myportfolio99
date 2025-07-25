# Generated by Django 4.2.23 on 2025-07-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_contact_remove_follow_follower_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to='service_icons/')),
            ],
        ),
    ]
