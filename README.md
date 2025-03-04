# Random Text Generator

## Overview
This is a simple Python script that generates a random string containing letters, digits, and punctuation characters. You can specify the length of the generated string as an argument to the function.

## Features
- Generates a random string with customizable length.
- Includes uppercase and lowercase letters, digits, and special characters.
- Easy to use and modify.

## Requirements
This script uses Python's built-in `random` and `string` modules, so no external dependencies are required.

## Usage
1. Copy the script into a Python file (e.g., `random_text.py`).
2. Run the script using Python:

```bash
python random_text.py
```

## Code
```python
import random
import string

def generate_random_text(length=10):
    """Generate a random string of letters and digits."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage
print(generate_random_text(20))
```

## Example Output
```
@A8s!ZxPq#2lK3fT&9N^
```

## Customization
You can modify the script to include or exclude certain types of characters. For example, to generate a string with only letters and digits:

```python
characters = string.ascii_letters + string.digits
```

## License
This project is open-source and free to use.
