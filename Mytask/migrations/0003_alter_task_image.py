# Generated by Django 3.2 on 2021-04-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mytask', '0002_alter_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='', upload_to='static/Mytask/images'),
        ),
    ]