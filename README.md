# Discontinuation of plugin

This mod will be discontinued in favour of https://github.com/Onemind-Services-LLC/netbox-secrets

This will be left up for historical reasons however it is recommended to migrate to the new plugin.

Netbox Secret Store
---

This is the continuation of the secrets app.

Installation
----

* Install NetBox as per NetBox documentation
* Add to local_requirements.txt:
  * `netbox-secretstore`
* Install requirements: `./venv/bin/pip install -r local_requirements.txt`
* Add to PLUGINS in NetBox configuration:
  * `'netbox_secretstore',`
* Run migration: `./venv/bin/python netbox/manage.py migrate`
* Run collectstatic: `./venv/bin/python netbox/manage.py collectstatic --no-input`

