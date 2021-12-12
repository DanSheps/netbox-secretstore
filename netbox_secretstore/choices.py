from utilities.choices import ChoiceSet

class SecretsAccessTypeChoices(ChoiceSet):
    TYPE_GENERIC = "Generic"

    TYPE_CONSOLE = "Console"
    TYPE_GNMI = "gNMI"
    TYPE_HTTP = "HTTP(S)"
    TYPE_NETCONF = "NETCONF"
    TYPE_REST = "REST"
    TYPE_RESTCONF = "RESTCONF"
    TYPE_SNMP = "SNMP"
    TYPE_SSH = "SSH"

    CHOICES = (
        (TYPE_GENERIC, "Generic"),
        (TYPE_CONSOLE, "Console"),
        (TYPE_GNMI, "gNMI"),
        (TYPE_HTTP, "HTTP(S)"),
        (TYPE_NETCONF, "NETCONF"),
        (TYPE_REST, "REST"),
        (TYPE_RESTCONF, "RESTCONF"),
        (TYPE_SNMP, "SNMP"),
        (TYPE_SSH, "SSH"),
    )

class SecretsTypeChoices(ChoiceSet):

    TYPE_KEY = "key"
    TYPE_PASSWORD = "password"
    TYPE_SECRET = "secret"
    TYPE_TOKEN = "token"
    TYPE_USERNAME = "username"

    CHOICES = (
        (TYPE_KEY, "Key"),
        (TYPE_PASSWORD, "Password"),
        (TYPE_SECRET, "Secret"),
        (TYPE_TOKEN, "Token"),
        (TYPE_USERNAME, "Username"),
    )
