# Generated by Django 2.2.7 on 2019-12-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20191227_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='archive',
            field=models.BooleanField(default=True),
        ),
    ]
