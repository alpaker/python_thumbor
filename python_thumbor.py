#!/usr/bin/env python

from base64 import b64encode
import hmac
import hashlib

from Crypto.Cipher import AES

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
            hashed_path = hmac.new(self._key, options_path, hashlib.sha1).digest()
            signature = self._base64_safe(hashed_path)
        components = [signature] + options_components
        return '/'.join(components)
    
class OldClient(Client):

    def __init__(self, key):
        padded_key = (key * 16)[0..15]
        self._encryptor = AES.new(padded_key, AES.MODE_EBC)

    def path(self, options):
        options_components = _options_to_path_components(options)
        hasher = hashlib.md5()
        hasher.update(options['image'])
        options_components.append(hasher.digest())
        options_path = '/'.join(options_components)
        padded_path = options_path + ("{" * (16 - len(options_path_ % )))
        cyphertext = self._encryptor.encrypt(padded_path)
        signature = self._base64_safe(cyphertext)
        components = [signature, options['image']]
        return '/'.join(components)
        



