# Generated by Django 4.2.6 on 2023-10-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_assignments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
