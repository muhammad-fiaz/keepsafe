# tests/test_keepsafe.py

import unittest
from keepsafe import KeepSafe


class TestKeepSafe(unittest.TestCase):
    def setUp(self):
        """Setup before each test."""
        self.ks = KeepSafe("./test.keepsafe")
        self.password = "test_password"
        self.decryption_key = self.ks.initialize_file(self.password)

    def test_add_and_get_secret_with_master_password(self):
        """Test adding and retrieving secrets with the master password."""
        self.ks.add_secret("api_key", "super_secret_api_key", password_or_decryption_key=self.password)
        secret = self.ks.get_secret("api_key", password_or_decryption_key=self.password)
        self.assertEqual(secret, "super_secret_api_key")

    def test_add_and_get_secret_with_decryption_key(self):
        """Test adding and retrieving secrets with the decryption key."""
        self.ks.add_secret("email_password", "super_secret_email_password",
                           password_or_decryption_key=self.decryption_key)
        secret = self.ks.get_secret("email_password", password_or_decryption_key=self.decryption_key)
        self.assertEqual(secret, "super_secret_email_password")

    def test_invalid_password(self):
        """Test for incorrect password handling."""
        with self.assertRaises(ValueError):
            self.ks.get_secret("api_key", password_or_decryption_key="wrong_password")

    def test_unlock_and_export(self):
        """Test unlocking the file and exporting secrets to a .env file."""
        self.ks.unlock(password=self.password, env_file_path="test.env")
        with open("test.env", "r") as f:
            lines = f.readlines()
            self.assertIn("api_key=super_secret_api_key", lines)
            self.assertIn("email_password=super_secret_email_password", lines)


if __name__ == "__main__":
    unittest.main()
