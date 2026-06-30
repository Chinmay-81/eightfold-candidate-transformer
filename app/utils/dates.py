"""
Date normalization.
"""

from datetime import datetime


SUPPORTED_FORMATS = [

    "%Y-%m-%d",

    "%d-%m-%Y",

    "%d/%m/%Y",

    "%Y/%m/%d",

    "%b %Y",

    "%B %Y"

]


def normalize_date(date_string):

    if not date_string:

        return None

    for fmt in SUPPORTED_FORMATS:

        try:

            return datetime.strptime(

                date_string,

                fmt

            ).strftime("%Y-%m")

        except ValueError:

            continue

    return date_string