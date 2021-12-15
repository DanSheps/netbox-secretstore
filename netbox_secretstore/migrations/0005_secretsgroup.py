# Generated by Django 3.2.9 on 2021-12-12 04:26

import django.core.serializers.json
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0065_imageattachment_change_logging'),
        ('netbox_secretstore', '0004_auto_20211212_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretsGroup',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('secrets', models.ManyToManyField(blank=True, related_name='groups', to='netbox_secretstore.Secret')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
    ]
