from django.test import TestCase

from sdp.apps import SdpConfig


class AppConfigTest(TestCase):
    def test(self):
        self.assertEqual(SdpConfig.name, 'SdP Server')
        self.assertEqual(SdpConfig.verbose_name, 'SdP Server')