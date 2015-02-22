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

    def test_crop(self):
        u = self.client.uri(image=IMAGE_URI, width=150, height=150,
                            original_width=300, original_height=200,
                            center=[100,100])
        self.assertEqual(u, "/KzLuf69nu6UIBIKuBRiIneiaQe8=/0x0:200x200/150x150/my.domain.com/some/image/url.jpg")

    def test_halign_valign_smart(self):
        u = self.client.uri(image=IMAGE_URI, halign='left', valign='top', smart=True)
        self.assertEqual(u, "/KS6mVuzlGE3hJ75n3JUonfGgSFM=/left/top/smart/my.domain.com/some/image/url.jpg")

    def test_empty_filters(self):
        u = self.client.uri(image=IMAGE_URI, filters=[])
        self.assertEqual(u, "/964rCTkAEDtvjy_a572k7kRa0SU=/my.domain.com/some/image/url.jpg")

    def test_trim_no_param(self):
        u = self.client.uri(image=IMAGE_URI, trim=True)
        self.assertEqual(u, "/w23BC0dUiYBFrUnuoYJe8XROuyw=/trim/my.domain.com/some/image/url.jpg")

    def test_trim_direction_param(self):
        u = self.client.uri(image=IMAGE_URI, trim=['bottom-right'])
        self.assertEqual(u, "/kXPwSmqEvPFQezgzBCv9BtPWmBY=/trim:bottom-right/my.domain.com/some/image/url.jpg")

    def test_trim_direction_and_tolerance_param(self):
        u = self.client.uri(image=IMAGE_URI, trim=['bottom-right', 15])
        self.assertEqual(u, "/TUCEIhtWfI1Uv9zjavCSl_i0A_8=/trim:bottom-right:15/my.domain.com/some/image/url.jpg")

    def test_trim_smart(self):
        u = self.client.uri(image=IMAGE_URI, trim=True, smart=True)
        self.assertEqual(u, "/qvDxNvUzB-0805ufJrLaFNdz2R0=/trim/smart/my.domain.com/some/image/url.jpg")

    def test_horizontal_crop_with_left_center(self):
        u = self.client.uri(image=IMAGE_URI, original_height=100, height=50,
                            original_width=100, width=40, center=[0,50])
        self.assertEqual(u, "/SZIT3w4Qgebv5DuVJ8G1IH1mkCU=/0x0:80x100/40x50/my.domain.com/some/image/url.jpg")

    def test_horizontal_crop_with_left_center(self):
        u = self.client.uri(image=IMAGE_URI, original_height=100, height=50,
                            original_width=100, width=40, center=[100,50])
        self.assertEqual(u, "/NEtCYehaISE7qR3zFj15CxnZoCs=/20x0:100x100/40x50/my.domain.com/some/image/url.jpg")

    def test_horizontal_crop_with_actual_center(self):
        u = self.client.uri(image=IMAGE_URI, original_height=100, height=50,
                            original_width=100, width=40, center=[50,50])
        self.assertEqual(u, "/JLH65vJTu6d-cXBmqe5hYoSD4ho=/10x0:90x100/40x50/my.domain.com/some/image/url.jpg")

    def test_vertical_crop_with_top_center(self):
        u = self.client.uri(image=IMAGE_URI, original_height=100, height=50,
                            original_width=100, width=40, center=[50,0])
        self.assertEqual(u, "/JLH65vJTu6d-cXBmqe5hYoSD4ho=/10x0:90x100/40x50/my.domain.com/some/image/url.jpg")

    def test_vertical_crop_with_bottom_center(self):
        u = self.client.uri(image=IMAGE_URI, original_height=100, height=50,
                            original_width=100, width=40, center=[50,100])
        self.assertEqual(u, "/JLH65vJTu6d-cXBmqe5hYoSD4ho=/10x0:90x100/40x50/my.domain.com/some/image/url.jpg")

    def test_vertical_crop_with_actual_center(self):
        u = self.client.uri(image=IMAGE_URI, original_height=100, height=50,
                            original_width=100, width=40, center=[50,50])
        self.assertEqual(u, "/JLH65vJTu6d-cXBmqe5hYoSD4ho=/10x0:90x100/40x50/my.domain.com/some/image/url.jpg")

    def test_no_crop_when_not_needed(self):
        u = self.client.uri(image=IMAGE_URI, original_height=100, height=50,
                            original_width=100, width=50, center=[50,0])
        self.assertEqual(u, "/trIjfr513nkGkCpKXK6qgox2jPA=/50x50/my.domain.com/some/image/url.jpg")

    def test_no_crop_when_missing_orig_height(self):
        u = self.client.uri(image=IMAGE_URI, height=40,
                            original_width=100, width=50, center=[50,50])
        self.assertEqual(u, "/veYlY0msKmemAaXpeav2kCNftmU=/50x40/my.domain.com/some/image/url.jpg")

    def test_no_crop_when_missing_orig_weight(self):
        u = self.client.uri(image=IMAGE_URI, height=40,
                            original_height=100, width=50, center=[50,50])
        self.assertEqual(u, "/veYlY0msKmemAaXpeav2kCNftmU=/50x40/my.domain.com/some/image/url.jpg")

    def test_no_crop_when_missing_width_height(self):
        u = self.client.uri(image=IMAGE_URI, original_width=100,
                            original_height=100, center=[50,50])
        self.assertEqual(u, "/964rCTkAEDtvjy_a572k7kRa0SU=/my.domain.com/some/image/url.jpg")

    def test_crop_missing_width(self):
        u = self.client.uri(image=IMAGE_URI, original_width=100, height=80,
                            original_height=100, center=[50,50])
        self.assertEqual(u, "/02BNIIJ9NYNV9Q03JHPtlP0DIDg=/0x10:100x90/0x80/my.domain.com/some/image/url.jpg")


class OldClientTest(unittest.TestCase):

    def setUp(self):
        self.client = OldClient(KEY)


if __name__ == "__main__":

    unittest.main()
