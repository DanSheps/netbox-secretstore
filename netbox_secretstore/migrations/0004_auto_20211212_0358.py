# Generated by Django 3.2.9 on 2021-12-12 03:58

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0065_imageattachment_change_logging'),
        ('netbox_secretstore', '0003_modify_objectchange_records'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='secret_type',
            field=models.CharField(default='password', max_length=32),
        ),
        migrations.AddField(
            model_name='secretrole',
            name='access_type',
            field=models.CharField(default='Generic', max_length=32),
        ),
        migrations.AddField(
            model_name='secretrole',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
    ]
