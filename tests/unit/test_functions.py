from unittest import TestCase

from send_nsca import _bytes


class TestBytes(TestCase):

    def test_str(self):
        self.assertEqual(_bytes('hello'), b'hello')

    def test_bytes(self):
        self.assertEqual(_bytes(b'hello'), b'hello')

    def test_unicode(self):
        with self.assertRaises(UnicodeEncodeError):
            _bytes('hellö')

    def test_int(self):
        with self.assertRaises(ValueError):
            _bytes(1)
