"""
Country normalization.
"""

import pycountry


def normalize_country(country):

    if not country:

        return None

    try:

        result = pycountry.countries.lookup(country)

        return result.alpha_2

    except LookupError:

        return country