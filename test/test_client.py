#!/usr/bin/env python

import unittest
import sys
from os.path import join, abspath, dirname

sys.path.append(abspath(join(dirname(__file__), '..')))

from python_thumbor import Client, OldClient

KEY = 'my-security-key'
IMAGE_URI = 'my.domain.com/some/image/url.jpg'
from data import TEST_DATA

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(KEY)

    def test_validate_center_option(self):
        self.assertRaises(TypeError, self.client.uri, IMAGE_URI, center=True)
        self.assertRaises(ValueError, self.client.uri, IMAGE_URI, center=[0])

    def test_validate_fit_options(self):
        self.assertRaises(ValueError, self.client.uri, IMAGE_URI, fit_in=True)

class OldClientTest(unittest.TestCase):

    def setUp(self):
        self.client = OldClient(KEY)

def make_fn(opts, expected):
    def fn(self):
        actual = self.client.uri(IMAGE_URI, **opts)
        self.assertEquals(expected, actual)
    return fn

for (testcase, data) in TEST_DATA.items():
    name = "test_%s" % testcase
    opts = data['opts']
    setattr(ClientTest, name, make_fn(opts, data['new']))
    setattr(OldClientTest, name, make_fn(opts, data['old']))

if __name__ == "__main__":

    unittest.main()
