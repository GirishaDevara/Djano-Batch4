# Generated by Django 3.0.8 on 2020-08-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_email_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='img',
            field=models.ImageField(null=True, upload_to='attachments/'),
        ),
    ]
