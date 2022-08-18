import json
#https://www.django-rest-framework.org/api-guide/renderers/
from rest_framework.renderers import JSONRenderer

class ProfileJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    #https://www.django-rest-framework.org/api-guide/renderers/#custom-renderers
    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)
        
        return json.dumps({"profile": data})