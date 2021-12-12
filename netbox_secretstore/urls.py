from django.urls import path
from extras.views import ObjectChangeLogView, ObjectJournalView

from .views import *

urlpatterns = [

    # Secret roles
    path('secret-roles/', SecretRoleListView.as_view(), name='secretrole_list'),
    path('secret-roles/add/', SecretRoleEditView.as_view(), name='secretrole_add'),
    path('secret-roles/import/', SecretRoleBulkImportView.as_view(), name='secretrole_import'),
    path('secret-roles/edit/', SecretRoleBulkEditView.as_view(), name='secretrole_bulk_edit'),
    path('secret-roles/delete/', SecretRoleBulkDeleteView.as_view(), name='secretrole_bulk_delete'),
    path('secret-roles/<int:pk>/', SecretRoleView.as_view(), name='secretrole'),
    path('secret-roles/<int:pk>/edit/', SecretRoleEditView.as_view(), name='secretrole_edit'),
    path('secret-roles/<int:pk>/delete/', SecretRoleDeleteView.as_view(), name='secretrole_delete'),
    path('secret-roles/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='secretrole_changelog', kwargs={'model': SecretRole}),

    # Secrets
    path('secrets/', SecretListView.as_view(), name='secret_list'),
    path('secrets/add/', SecretEditView.as_view(), name='secret_add'),
    path('secrets/import/', SecretBulkImportView.as_view(), name='secret_import'),
    path('secrets/edit/', SecretBulkEditView.as_view(), name='secret_bulk_edit'),
    path('secrets/delete/', SecretBulkDeleteView.as_view(), name='secret_bulk_delete'),
    path('secrets/<int:pk>/', SecretView.as_view(), name='secret'),
    path('secrets/<int:pk>/edit/', SecretEditView.as_view(), name='secret_edit'),
    path('secrets/<int:pk>/delete/', SecretDeleteView.as_view(), name='secret_delete'),
    path('secrets/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='secret_changelog', kwargs={
        'model': Secret}),
    path('secrets/<int:pk>/journal/', ObjectJournalView.as_view(), name='secret_journal', kwargs={'model': Secret}),

    # Secrets group
    path('secrets-group/', SecretsGroupListView.as_view(), name='secretsgroup_list'),
    path('secrets-group/add/', SecretsGroupEditView.as_view(), name='secretsgroup_add'),
    path('secrets-group/import/', SecretsGroupBulkImportView.as_view(), name='secretsgroup_import'),
    path('secrets-group/edit/', SecretsGroupBulkEditView.as_view(), name='secretsgroup_bulk_edit'),
    path('secrets-group/delete/', SecretsGroupBulkDeleteView.as_view(), name='secretsgroup_bulk_delete'),
    path('secrets-group/<int:pk>/', SecretsGroupView.as_view(), name='secretsgroup'),
    path('secrets-group/<int:pk>/edit/', SecretsGroupEditView.as_view(), name='secretsgroup_edit'),
    path('secrets-group/<int:pk>/delete/', SecretsGroupDeleteView.as_view(), name='secretsgroup_delete'),

    # User
    path('user-key/', UserKeyView.as_view(), name='userkey'),
    path('user-key/edit/', UserKeyEditView.as_view(), name='userkey_edit'),
    path('session-key/delete/', SessionKeyDeleteView.as_view(), name='sessionkey_delete'),
]
