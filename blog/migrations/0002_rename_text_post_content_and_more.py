# Generated by Django 4.1 on 2022-09-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
