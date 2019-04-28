from .nsca_test_case import NSCATestCase, ServiceCheckResult

import send_nsca


class ConvenienceFunctionTest(NSCATestCase):
    crypto_method = 1

    def assertions(self, status, message):
        checks = self.expect_checks(1)
        self.assertEqual(len(checks), 1)
        self.assertEqual(
            checks[0],
            ServiceCheckResult(
                host_name='myhost',
                service_name='myservice',
                status=status,
                output=message))

    def test_send_nsca(self):
        send_nsca.send_nsca(
            0,
            b'myhost',
            b'myservice',
            b'Without pycrypto',
            **self.nsca_sender_args)
        self.assertions(0, 'Without pycrypto')
