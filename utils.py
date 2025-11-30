import hashlib
import hmac
import os
import secrets
import string
from typing import Optional
import logging

logger = logging.getLogger(__name__)

def generate_secure_token(length: int = 32) -> str:
    """Generates a secure random token of specified length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash_password(password: str, salt: Optional[str] = None) -> tuple[str, str]:
    """Hashes a password using a salt and SHA-256."""
    if salt is None:
        salt = os.urandom(16).hex()

    salted_password = salt.encode('utf-8') + password.encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password, salt

def verify_password(password: str, hashed_password: str, salt: str) -> bool:
    """Verifies a password against a stored hash and salt."""
    new_hashed_password, _ = hash_password(password, salt)
    return hmac.compare_digest(hashed_password, new_hashed_password)

def validate_currency_code(currency_code: str) -> bool:
    """Validates a currency code against a list of allowed currencies."""
    # In a real-world scenario, this would be loaded from a configuration
    # file or a database. For simplicity, we'll hardcode a few.
    allowed_currencies = ["USD", "EUR", "GBP"]
    return currency_code.upper() in allowed_currencies

def mask_credit_card(card_number: str) -> str:
    """Masks a credit card number, leaving only the last 4 digits visible."""
    if not card_number or not card_number.isdigit() or len(card_number) < 4:
        return "Invalid Card Number"  # Or raise an exception

    return "*" * (len(card_number) - 4) + card_number[-4:]