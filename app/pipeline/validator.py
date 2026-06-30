"""
Output Validator
"""

from email_validator import validate_email, EmailNotValidError


class Validator:

    @staticmethod
    def validate(output: dict):

        errors = []

        # Required fields
        if not output.get("name"):
            errors.append("Missing name")

        if not output.get("email"):
            errors.append("Missing email")

        # Email validation
        email = output.get("email")

        if email:
            try:
                validate_email(email)
            except EmailNotValidError:
                errors.append("Invalid email")

        # Phone validation
        phone = output.get("phone")

        if phone and not phone.startswith("+"):
            errors.append("Phone must be in E.164 format")

        return errors