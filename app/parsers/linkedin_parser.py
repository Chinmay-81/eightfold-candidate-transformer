import json
import uuid

from app.schemas.candidate import (
    Candidate,
    Experience,
    Education,
    Provenance
)


class LinkedInParser:

    SOURCE_NAME = "linkedin"

    @staticmethod
    def parse(file_path: str):

        with open(file_path, "r", encoding="utf-8") as file:

            data = json.load(file)

        candidate = Candidate(

            candidate_id=str(uuid.uuid4())

        )

        candidate.full_name = data.get("name")

        candidate.headline = data.get("headline")

        location = data.get("location")

        if location:

            parts = [

                part.strip()

                for part in location.split(",")

            ]

            if len(parts) >= 2:

                candidate.location.city = parts[0]

                candidate.location.country = parts[-1]

        for exp in data.get("experience", []):

            candidate.experience.append(

                Experience(

                    company=exp.get("company"),

                    title=exp.get("title"),

                    start=exp.get("start"),

                    end=exp.get("end"),

                    summary=exp.get("summary")

                )

            )

        for edu in data.get("education", []):

            candidate.education.append(

                Education(

                    institution=edu.get("institution"),

                    degree=edu.get("degree"),

                    field=edu.get("field"),

                    end_year=edu.get("end_year")

                )

            )

        for field in [

            "name",

            "headline",

            "location"

        ]:

            if data.get(field):

                candidate.provenance.append(

                    Provenance(

                        field=field,

                        source=LinkedInParser.SOURCE_NAME,

                        confidence=0.95,

                        method="json_parser"

                    )

                )

        return candidate
        