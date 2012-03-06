import newrelic.agent
from django.conf import settings


class NewRelicMiddleware(object):

    def debug(self, message):
        if self.debug_enabled:
            print '[new relic extensions]: %s' % message

    def add(self, key, value):
        if callable(value):
            value = value()
        if self.debug_enabled:
            print '%s: %s' % (key, value)
        else:
            newrelic.agent.add_custom_parameter(key, value)

    def process_response(self, request, response):

        enabled = getattr(settings, 'NEW_RELIC_EXTENSIONS_ENABLED', False)
        if not enabled:
            return response

        attributes = getattr(settings, 'NEW_RELIC_EXTENSIONS_ATTRIBUTES', None)
        self.debug_enabled = getattr(settings, 'NEW_RELIC_EXTENSIONS_DEBUG', True)

        if not attributes:
            self.debug('No attributes specified.')
            return response

        for key in attributes.keys():

            value = getattr(request, key, None)
            if not value:
                self.debug("HttpRequest instance doesn't have '%s' attribute."
                        % key)
                continue

            if isinstance(attributes[key], dict):
                for subkey in attributes[key].keys():
                    subvalue = getattr(value, subkey, None)
                    if not subvalue:
                        self.debug("'%s' doesn't have '%s' attribute." % (key,
                            subkey))
                        continue
                    self.add(attributes[key][subkey], subvalue)
            else:
                self.add(attributes[key], value)

        return response
