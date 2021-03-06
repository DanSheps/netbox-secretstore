# Generated by Django 3.2.5 on 2021-07-20 17:24

from django.conf import settings
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    replaces = [
        ('secrets', '0001_initial'),
        ('secrets', '0002_userkey_add_session_key'),
        ('secrets', '0003_unicode_literals'),
        ('secrets', '0004_tags'),
        ('secrets', '0005_change_logging'),
        ('secrets', '0006_custom_tag_models'),
        ('secrets', '0007_secretrole_description'),
        ('secrets', '0008_standardize_description'),
        ('secrets', '0009_secretrole_drop_users_groups'),
        ('secrets', '0010_custom_field_data'),
        ('secrets', '0011_secret_generic_assignments'),
        ('secrets', '0012_standardize_name_length'),
        ('secrets', '0013_standardize_models')
    ]

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0061_extras_change_logging'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretRole',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'secrets_secretrole',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserKey',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('public_key', models.TextField()),
                ('master_key_cipher', models.BinaryField(blank=True, max_length=512, null=True)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_key', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'secrets_userkey',
                'ordering': ['user__username'],
            },
        ),
        migrations.CreateModel(
            name='SessionKey',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cipher', models.BinaryField(max_length=512)),
                ('hash', models.CharField(editable=False, max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('userkey', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='session_key', to='netbox_secretstore.userkey')),
            ],
            options={
                'db_table': 'secrets_sessionkey',
                'ordering': ['userkey__user__username'],
            },
        ),
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('assigned_object_id', models.PositiveIntegerField()),
                ('name', models.CharField(blank=True, max_length=100)),
                ('ciphertext', models.BinaryField(max_length=65568)),
                ('hash', models.CharField(editable=False, max_length=128)),
                ('assigned_object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='secrets', to='netbox_secretstore.secretrole')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'db_table': 'secrets_secret',
                'ordering': ('role', 'name', 'pk'),
                'unique_together': {('assigned_object_type', 'assigned_object_id', 'role', 'name')},
            },
        ),
    ]
