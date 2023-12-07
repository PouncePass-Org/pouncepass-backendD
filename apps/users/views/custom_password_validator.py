from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    """
    Validate whether the password meets the following criteria:
    - At least 15 characters
    - Contains a lower case letter
    - Contains an upper case letter
    - Contains a digit
    - Contains a special character
    """
    def validate(self, password, user=None):
        if len(password) < 15:
            raise ValidationError("Password must be at least 15 characters long.")

        if not re.findall('[a-z]', password):
            raise ValidationError("Password must contain at least one lower case letter.")

        if not re.findall('[A-Z]', password):
            raise ValidationError("Password must contain at least one upper case letter.")

        if not re.findall('[0-9]', password):
            raise ValidationError("Password must contain at least one digit.")

        if not re.findall('[^a-zA-Z0-9]', password):
            raise ValidationError("Password must contain at least one special character.")

    def get_help_text(self):
        return "Your password must be at least 15 characters long and contain at least one lower case letter, one upper case letter, one digit, and one special character."
