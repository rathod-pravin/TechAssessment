# Generated by Django 3.2 on 2021-04-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mytask', '0005_task_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='phone_no',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]