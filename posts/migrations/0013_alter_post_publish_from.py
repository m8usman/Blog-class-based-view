# Generated by Django 4.0.3 on 2022-04-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_publish_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
