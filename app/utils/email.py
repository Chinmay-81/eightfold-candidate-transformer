"""
Email normalization utilities.
"""

from typing import Optional


def normalize_email(email: Optional[str]) -> Optional[str]:
    """
    Convert email to lowercase and remove surrounding spaces.

    Example:
        JOHN@GMAIL.COM -> john@gmail.com
    """

    if not email:
        return None

    return email.strip().lower()