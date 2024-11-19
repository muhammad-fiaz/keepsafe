import os
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode


class KeepSafe:
    def __init__(self, filepath=None):
        """
        Initialize KeepSafe with a file path.
        By default, the file will be created in the root directory of the project.
        """
        if filepath is None:
            # Set default file location in the project's root directory
            filepath = os.path.join(os.getcwd(), ".keepsafe")
        self.filepath = filepath
        self.data = {}
        self.file_key = None
        self.master_password = None

    def _derive_key(self, password, salt):
        """Derive an encryption key from a password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return urlsafe_b64encode(kdf.derive(password.encode()))

    def initialize_file(self, password):
        """Initialize a new .keepsafe file with a password."""
        if os.path.exists(self.filepath):
            print(f"Warning: {self.filepath} already exists. If you proceed, the file will be overwritten.")

        # Proceed with initialization, overwriting if the file exists
        salt = os.urandom(16)
        self.file_key = Fernet.generate_key()
        password_key = self._derive_key(password, salt)

        fernet = Fernet(password_key)
        encrypted_file_key = fernet.encrypt(self.file_key)

        self.data = {
            "salt": urlsafe_b64encode(salt).decode(),
            "encrypted_file_key": encrypted_file_key.decode(),
            "secrets": {}
        }
        self._save_file()
        print("File successfully initialized.")

        # Set master password automatically when initializing the file
        self.master_password = password  # Set the master password

        # Generate decryption key and display it
        decryption_key = self.file_key.decode()  # This is the decryption key
        print(f"Decryption key generated: {decryption_key}")
        return decryption_key

    def _load_file(self):
        """Load and decrypt the .keepsafe file."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(".keepsafe file does not exist.")

        with open(self.filepath, "r") as f:
            self.data = json.load(f)

    def _save_file(self):
        """Save the encrypted .keepsafe file."""
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def unlock_file(self, password):
        """Unlock the file using the password."""
        if self.master_password is None:
            raise ValueError("Master password must be set before unlocking the file.")

        self._load_file()
        salt = urlsafe_b64decode(self.data["salt"])
        password_key = self._derive_key(password, salt)

        fernet = Fernet(password_key)
        try:
            self.file_key = fernet.decrypt(self.data["encrypted_file_key"].encode())
        except:
            raise ValueError("Incorrect password.")
        print("File successfully unlocked.")

    def get_decryption_key(self):
        """Generate and return a temporary decryption key for read-only access."""
        if not self.file_key:
            raise ValueError("Unlock the file first.")
        return self.file_key.decode()

    def add_secret(self, key, value, password_or_decryption_key):
        """Encrypt and add a secret to the file (can be done with master password or decryption key)."""

        if not self.file_key:
            raise ValueError("Unlock the file first.")

        # If using master password, verify and proceed
        if password_or_decryption_key == self.master_password:
            fernet = Fernet(self.file_key)
            encrypted_value = fernet.encrypt(value.encode()).decode()
            self.data["secrets"][key] = encrypted_value
            self._save_file()
            print(f"Secret for {key} added successfully with master password.")

        # If using decryption key, verify and proceed
        elif password_or_decryption_key == self.get_decryption_key():
            fernet = Fernet(self.file_key)
            encrypted_value = fernet.encrypt(value.encode()).decode()
            self.data["secrets"][key] = encrypted_value
            self._save_file()
            print(f"Secret for {key} added successfully with decryption key.")

        else:
            raise ValueError("Invalid password or decryption key for adding secrets.")

    def get_secret(self, key, password_or_decryption_key):
        """Retrieve a secret using the master password or decryption key."""
        if password_or_decryption_key == self.master_password:
            # Use master password to unlock and get the secret
            fernet = Fernet(self.file_key)
            encrypted_value = self.data["secrets"].get(key)
            if not encrypted_value:
                raise ValueError(f"No secret found for key: {key}")
            return fernet.decrypt(encrypted_value.encode()).decode()

        elif password_or_decryption_key == self.get_decryption_key():
            # Use decryption key to get the secret
            fernet = Fernet(password_or_decryption_key.encode())
            encrypted_value = self.data["secrets"].get(key)
            if not encrypted_value:
                raise ValueError(f"No secret found for key: {key}")
            return fernet.decrypt(encrypted_value.encode()).decode()

        else:
            raise ValueError("Invalid password or decryption key for retrieving secrets.")

    def set_master_password(self, new_master_password):
        """Set or change the master password for file encryption and access."""
        self.master_password = new_master_password
        print("Master password has been set.")

    def access_file(self, filepath, decryption_key):
        """Access the file using the decryption key (read-only access)."""
        self._load_file()
        fernet = Fernet(decryption_key.encode())
        secrets = {}
        for key, encrypted_value in self.data["secrets"].items():
            secrets[key] = fernet.decrypt(encrypted_value.encode()).decode()
        print("File accessed with decryption key.")
        return secrets

    def unlock(self, password, env_file_path=".env"):
        """Unlock the file and export secrets to a .env file using the master password."""
        # First, unlock the file with the master password
        self.unlock_file(password)

        # Extract the secrets and write them to the .env file
        with open(env_file_path, "w") as env_file:
            for key, encrypted_value in self.data["secrets"].items():
                decrypted_value = self.get_secret(key, self.get_decryption_key())
                env_file.write(f"{key}={decrypted_value}\n")

        print(f"Secrets successfully exported to {env_file_path}")

