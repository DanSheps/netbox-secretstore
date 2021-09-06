from extras.plugins import PluginTemplateExtension
from .models import Secret

class DeviceSecrets(PluginTemplateExtension):
    model = 'dcim.device'

    def right_page(self):
        obj = self.context['object']
        return self.render('netbox_secretstore/inc/device_secrets.html', extra_context={
            'secrets': Secret.objects.filter(device=obj),
        })

class CircuitSecrets(PluginTemplateExtension):
    model = 'circuits.circuit'

    def right_page(self):
        obj = self.context['object']
        return self.render('netbox_secretstore/inc/circuit_secrets.html', extra_context={
            'secrets': Secret.objects.filter(circuit=obj),
        })

template_extensions = [DeviceSecrets, CircuitSecrets]