#!/usr/bin/env python

import unittest
import sys
from os.path import join, abspath, dirname

sys.path.append(abspath(join(dirname(__file__), '..')))

from python_thumbor import Client, OldClient

KEY = 'my-security-key'
IMAGE_URI = 'my.domain.com/some/image/url.jpg'

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(KEY)

    def test_no_opts(self):
        u = self.client.uri(image=IMAGE_URI)
        self.assertEqual(u, "/964rCTkAEDtvjy_a572k7kRa0SU=/my.domain.com/some/image/url.jpg")

    def test_width(self):
        u = self.client.uri(image=IMAGE_URI, width=300)
        self.assertEqual(u, "/eFwrBWryxtRw9hDSbQPhi5iLpo8=/300x0/my.domain.com/some/image/url.jpg")

    def test_width_height(self):
        u = self.client.uri(image=IMAGE_URI, width=200, height=300)
        self.assertEqual(u, "/TrM0qqfcivb6VxS3Hxlxn43W21k=/200x300/my.domain.com/some/image/url.jpg")

    def test_width_height_smart(self):
        u = self.client.uri(image=IMAGE_URI, width=200, height=300, smart=True)
        self.assertEqual(u, "/hdzhxXzK45DzNTru5urV6x6xxSs=/200x300/smart/my.domain.com/some/image/url.jpg")

    def test_width_height_fit_in(self):
        u = self.client.uri(image=IMAGE_URI, width=200, height=300, fit_in=True)
        self.assertEqual(u, "/LOv6ArMOJA2VRpfMQjjs4xSyZpM=/fit-in/200x300/my.domain.com/some/image/url.jpg")

    def test_flip(self):
        u = self.client.uri(image=IMAGE_URI, flip=True)
        self.assertEqual(u, "/rlI4clPR-p-PR2QAxj5ZWiTfvH4=/-0x0/my.domain.com/some/image/url.jpg")

    def test_flop(self):
        u = self.client.uri(image=IMAGE_URI, flop=True)
        self.assertEqual(u, "/-4dmGj-TwIEqTAL9_9yEqUM8cks=/0x-0/my.domain.com/some/image/url.jpg" )

    def test_flip_flop(self):
        u = self.client.uri(image=IMAGE_URI, flip=True, flop=True)
        self.assertEqual(u, "/FnMxpQMmxiMpdG219Dsj8pD_4Xc=/-0x-0/my.domain.com/some/image/url.jpg")

    def test_flip_width(self):
        u = self.client.uri(image=IMAGE_URI, flip=True, width=300)
        self.assertEqual(u, "/ccr2PoSYcTEGL4_Wzt4u3wWVRKU=/-300x0/my.domain.com/some/image/url.jpg")

    def test_flop_height(self):
        u = self.client.uri(image=IMAGE_URI, flop=True, height=300)
        self.assertEqual(u, "/R5K91tkyNgXO65F6E0txgA6C9lY=/0x-300/my.domain.com/some/image/url.jpg")

    def test_halign_left(self):
        u = self.client.uri(image=IMAGE_URI, halign="left")
        self.assertEqual(u, "/GTJE3wUt3sURik0O9Nae8sfI928=/left/my.domain.com/some/image/url.jpg")

    def test_halign_center(self):
        u = self.client.uri(image=IMAGE_URI, halign="center")
        self.assertEqual(u, "/964rCTkAEDtvjy_a572k7kRa0SU=/my.domain.com/some/image/url.jpg")

    def test_valign_top(self):
        u = self.client.uri(image=IMAGE_URI, valign="top")
        self.assertEqual(u, "/1QQo5ihObuhgwl95--Z3g78vjiE=/top/my.domain.com/some/image/url.jpg")

    def test_valign_middle(self):
        u = self.client.uri(image=IMAGE_URI, valign="middle")
        self.assertEqual(u, "/964rCTkAEDtvjy_a572k7kRa0SU=/my.domain.com/some/image/url.jpg")

    def test_valign_halign(self):
        u = self.client.uri(image=IMAGE_URI, valign="top", halign="middle")
        self.assertEqual(u, "/xcKQX02B7vTRHHuDWF3h4l7Rb0k=/middle/top/my.domain.com/some/image/url.jpg")

    def test_meta(self):
        u = self.client.uri(image=IMAGE_URI, meta=True)
        self.assertEqual(u, "/WvIJFDJDePgIl5hZcLgtrzIPxfY=/meta/my.domain.com/some/image/url.jpg")
                         

class OldClientTest(unittest.TestCase):

    def setUp(self):
        self.client = OldClient(KEY)

    
if __name__ == "__main__":

    unittest.main()
