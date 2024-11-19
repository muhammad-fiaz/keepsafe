<h1 align="center">Keepsafe: Securely store and distribute sensitive information like passwords and keys</h1>
<p align="center">
  <img src="https://img.shields.io/pypi/v/keepsafe" alt="PyPI Version" />
  <img src="https://img.shields.io/pypi/dm/keepsafe" alt="PyPI Downloads" />
  <img src="https://img.shields.io/pypi/l/keepsafe" alt="License" />
  <img src="https://img.shields.io/github/workflow/status/muhammad-fiaz/keepsafe/CI" alt="Build Status" />
  <img src="https://img.shields.io/pypi/pyversions/keepsafe" alt="Python Versions" />
  <img src="https://img.shields.io/github/issues/muhammad-fiaz/keepsafe" alt="Issues" />
  <img src="https://img.shields.io/github/issues-pr/muhammad-fiaz/keepsafe" alt="Pull Requests" />
  <img src="https://img.shields.io/github/last-commit/muhammad-fiaz/keepsafe" alt="Last Commit" />
  <img src="https://img.shields.io/github/contributors/muhammad-fiaz/keepsafe" alt="Contributors" />
  <a href="https://github.com/sponsors/muhammad-fiaz">
    <img src="https://img.shields.io/badge/sponsor-muhammad--fiaz-ff69b4" alt="Sponsor" />
  </a>
</p>




Keepsafe is a Python library that helps you securely store and retrieve sensitive information like passwords, API keys, and other secrets. It uses encryption techniques to ensure that your sensitive data is safe, and only accessible using the correct master password or decryption key.

## Features

- Securely store and retrieve secrets (e.g., passwords, API keys).
- Encryption based on `Fernet` and `PBKDF2` for password-based key derivation.
- Supports adding secrets using either the master password or decryption key.
- Export secrets to `.env` files for use in applications.
- Easily integrated into existing projects.

## Installation

You can install `keepsafe` via `pip` from PyPI:

```bash
pip install keepsafe
```

## Usage

### Initialize a new file with a master password

First, create a `Keepsafe` object and initialize the file:

```python
from keepsafe import KeepSafe

ks = KeepSafe("./secrets.keepsafe")
decryption_key = ks.initialize_file(password="your_master_password")
```

### Add secrets

You can add secrets either using the master password or the decryption key:

```python
ks.add_secret("api_key", "super_secret_api_key", password_or_decryption_key="your_master_password")
ks.add_secret("email_password", "super_secret_email_password", password_or_decryption_key=decryption_key)
```

### Retrieve secrets

You can retrieve secrets using the master password or the decryption key:

```python
api_key = ks.get_secret("api_key", password_or_decryption_key="your_master_password")
email_password = ks.get_secret("email_password", password_or_decryption_key=decryption_key)

print(f"API Key: {api_key}")
print(f"Email Password: {email_password}")
```

### Export secrets to `.env` file

To unlock the file and export all secrets to a `.env` file:

```python
ks.unlock(password="your_master_password", env_file_path=".env")
```

This will export the secrets into the `.env` file, where each secret will be written as `KEY=VALUE`.

## Testing

To run tests, you can use `pytest`. This package includes basic tests to verify that the core functionality works as expected.

Run the tests with:

```bash
pytest
```

## License

Keepsafe is distributed under the MIT License. See `LICENSE` for more information.

## Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Create a new Pull Request.

## Contact

For any issues, bugs, or feature requests, please open an issue on the [GitHub repository](https://github.com/muhammad-fiaz/keepsafe).

