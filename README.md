PySecureTools
Overview
PySecureTools is a Python toolkit for encryption, IP retrieval, and PDF decryption.

Features
crypt.py – Generates and stores an encryption key.
ip.py – Retrieves local and public IP addresses.
pdf_pass.py – Decrypts password-protected PDFs and extracts text.
encrypt_decrypt.py – Encrypts and decrypts messages using a secret key.
Installation
bash
Copy
Edit
pip install cryptography requests PyPDF2
Usage
Run crypt.py to generate an encryption key.
Use encrypt_decrypt.py to encrypt/decrypt messages.
Execute ip.py to get local and public IPs.
Modify pdf_pass.py with the PDF path and password, then run it to decrypt.
License
MIT License.
