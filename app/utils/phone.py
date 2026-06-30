"""
Phone normalization utilities.
"""

import phonenumbers
from typing import Optional


def normalize_phone(phone: Optional[str],
                    default_region: str = "IN") -> Optional[str]:

    if not phone:
        return None

    try:

        parsed = phonenumbers.parse(
            str(phone),
            default_region
        )

        if phonenumbers.is_valid_number(parsed):

            return phonenumbers.format_number(

                parsed,

                phonenumbers.PhoneNumberFormat.E164

            )

    except Exception:

        pass

    return None