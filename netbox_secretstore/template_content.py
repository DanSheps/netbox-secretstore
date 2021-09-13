from extras.plugins import PluginTemplateExtension
from .models import Secret


class Secrets(PluginTemplateExtension):

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

class DeviceSecrets(Secrets):
    model = 'dcim.Device'

class VMSecrets(Secrets):
    model = 'virtualization.VirtualMachine'

template_extensions = [DeviceSecrets, VMSecrets]