import random
import string

def generate_random_text(length=10):
    """Generate a random string of letters and digits."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage
print(generate_random_text(20))
