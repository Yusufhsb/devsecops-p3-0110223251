import hashlib

def generate_secure_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()