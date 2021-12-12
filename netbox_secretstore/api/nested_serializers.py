from netbox.api import WritableNestedSerializer
from rest_framework import serializers

from netbox_secretstore.models import Secret, SecretRole, SecretsGroup

__all__ = [
    'NestedSecretRoleSerializer',
    'NestedSecretSerializer',
    'NestedSecretsGroupSerializer'
]


class NestedSecretSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_secretstore-api:secret-detail')

    class Meta:
        model = Secret
        fields = ['id', 'url', 'display', 'name']


class NestedSecretRoleSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_secretstore-api:secretrole-detail')
    secret_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = SecretRole
        fields = ['id', 'url', 'display', 'name', 'slug', 'secret_count']


class NestedSecretsGroupSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_secretstore-api:secretsgroup-detail')

    class Meta:
        model = SecretsGroup
        fields = ['id', 'url', 'display', 'name', 'slug']
