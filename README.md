# Password Comparator with bcrypt Algorithm

This project is a simple Python script example to demonstrate the use of the bcrypt algorithm for hashing and verifying passwords. It utilizes the `bcrypt` library to offer a secure, non-obsolete (as of 2023) method of password processing.

## Installation

To use this script, you must have Python installed on your system. Additionally, the `bcrypt` module is required. You can install it using pip:

`python3 install bcrypt`

## Usage
The script operates in two steps:

1. **Hash a password** entered by the user.
2. **Verify** if a second entered password matches the hash of the first.

Run the script in a terminal or Python environment. Follow the on-screen instructions to enter and verify the passwords.

## Features

- **Password Hashing**: Uses `bcrypt` to create a secure hash of the password.
- **Password Verification**: Compares an entered password with the stored hash to confirm if they match.

## References

For more information on hashing, salting, and encryption, you can refer to the following article: [Encryption vs Hashing vs Salting](https://www.pingidentity.com/fr/resources/blog/post/encryption-vs-hashing-vs-salting.html).
