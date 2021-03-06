import random
import unittest

import sys
sys.path.append("...")
from module.password import IDENTITY_PASSWORD, randomPassword
from module.cipher   import Cipher


class TestCipher(unittest.TestCase):
    def test_encryption(self):
        password = randomPassword()

        original_data = bytearray()
        for _ in range(0xffff):
            original_data.append(random.randint(0, 255))

        cipher = Cipher.NewCipher(password)
        data = original_data.copy()

        cipher.encode(data)
        self.assertNotEqual(data, original_data)
        cipher.decode(data)
        self.assertEqual(data, original_data)

    def test_no_encryption(self):
        password = IDENTITY_PASSWORD.copy()

        original_data = bytearray()
        for _ in range(0xffff):
            original_data.append(random.randint(0, 255))

        cipher = Cipher.NewCipher(password)
        data = original_data.copy()

        cipher.encode(data)
        self.assertEqual(data, original_data)
        cipher.decode(data)
        self.assertEqual(data, original_data)
