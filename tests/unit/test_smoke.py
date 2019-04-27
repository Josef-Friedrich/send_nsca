from unittest import TestCase, mock

import send_nsca


def mock_random_alphanumeric_bytes(bytesz):
    """mock that returns decidedly un-random alphanumeric bytes"""
    return b'0' * bytesz


class SmokeTestCase(TestCase):
    """Some random smoke tests"""

    def test_pack_packet_all(self):
        vectors = [
                ((b'test_host', b'test_service', 0, b'foo', 0), b'\x00\x03\x00\x00\xcbl\\\xad\x00\x00\x00\x00\x00\x00test_host\x00000000000000000000000000000000000000000000000000000000test_service\x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000foo\x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\x00\x00'),
                ((b'0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxy0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxy0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxy0123456789:;<=>?@ABCDEFGHIJKLMNOPQAAAAAAAAAAAAAAAA', b'test_service', 0, b'foo', 0), b'\x00\x03\x00\x00\xc5h!\xae\x00\x00\x00\x00\x00\x000123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnotest_service\x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000foo\x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\x00\x00'),
        ]
        with mock.patch('send_nsca.nsca.get_random_alphanumeric_bytes', mock_random_alphanumeric_bytes):
            for args, result in vectors:
                self.assertEqual(send_nsca.nsca._pack_packet(*args), result)
