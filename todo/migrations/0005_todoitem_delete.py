# Generated by Django 2.2.7 on 2019-12-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20191229_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]