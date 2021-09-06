from django.db.models import Q


#
# Secrets
#

SECRET_ASSIGNMENT_MODELS = Q(
    Q(app_label='dcim', model='device') |
    Q(app_label='virtualization', model='virtualmachine')
    Q(app_label='circuits', model='circuit')
)

SECRET_PLAINTEXT_MAX_LENGTH = 65535
