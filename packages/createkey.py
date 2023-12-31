import hashlib
import secrets

def generate_random_hash_key():
    """Generate a random hash key using SHA-256."""
    random_string = secrets.token_hex(16)  # Generates a random string of 32 characters
    hash_object = hashlib.sha256(random_string.encode())
    hash_key = hash_object.hexdigest()
    return hash_key

# Example usage
random_hash_key = generate_random_hash_key()
print(f"Random Hash Key: {random_hash_key}")
