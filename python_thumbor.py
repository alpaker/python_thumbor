#!/usr/bin/env python

from base64 import b64encode
import hmac
import hashlib

class Client(object):

    def __init__(self, key=None):
        self._key = key

    def _options_to_path_components(self, options):
        return ''

    def _base64_safe(self, s):
        return s
    
    def path(self, options):
        options_components = _options_to_path_components(options)
        options_components.append(options['image'])
        options_path = '/'.join(options_components)
        if key is None:
            signature = "unsafe"
        else:
            binhash = hmac.new(self._key, options_path, hashlib.sha1).digest()
            signature = self._base64_safe(binhash)
        components = [signature] + options_components
        return '/'.join(components)
    
class OldClient(Client):

    def __init__(self, key):
        super(Client, self).__init__(key)
        self._padded_key = (self._key * 16)[0..15]

    def path(self, options):
        options_components = _options_to_path_components(options)
        m = hashlib.md5()
        m.update(options['image'])
        options_components.append(m.digest())
        options_path = '/'.join(options_components)
        padded_path = options_path + ("{" * (16 - len(options_path_ % )))
        signature = self._base64_safe(self.encode(padded_path))
        components = [signature, options['image']]
        return '/'.join(components)
        



