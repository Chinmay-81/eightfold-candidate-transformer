from app.schemas.candidate import Candidate

from app.utils.phone import normalize_phone
from app.utils.email import normalize_email
from app.utils.skills import normalize_skill
from app.utils.country import normalize_country


class CandidateNormalizer:

    @staticmethod
    def normalize(candidate: Candidate) -> Candidate:

        # Normalize emails
        candidate.emails = [

            normalize_email(email)

            for email in candidate.emails

            if normalize_email(email)

        ]
        

        # Normalize phones
        candidate.phones = [

            normalize_phone(phone)

            for phone in candidate.phones

            if normalize_phone(phone)

        ]

        # Normalize skills
        candidate.skills = [

            normalize_skill(skill)

            for skill in candidate.skills

            if normalize_skill(skill)

        ]

        # Normalize country
        if candidate.location.country:

            candidate.location.country = normalize_country(

                candidate.location.country

            )

        return candidate