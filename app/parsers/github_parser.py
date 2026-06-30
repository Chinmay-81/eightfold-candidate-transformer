import json
import uuid

from app.schemas.candidate import (
    Candidate,
    Provenance
)


class GitHubParser:

    SOURCE_NAME = "github"

    @staticmethod
    def parse(file_path: str) -> Candidate:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        candidate = Candidate(
            candidate_id=str(uuid.uuid4())
        )

        candidate.full_name = data.get("name")
        candidate.headline = data.get("bio")

        if data.get("html_url"):
            candidate.links.github = data["html_url"]

        languages = data.get("languages", [])

        if isinstance(languages, list):
            candidate.skills.extend(languages)

        fields = {

            "name": data.get("name"),

            "bio": data.get("bio"),

            "html_url": data.get("html_url"),

            "languages": languages

        }

        for field, value in fields.items():

            if value:

                candidate.provenance.append(

                    Provenance(
                        field=field,
                        source=GitHubParser.SOURCE_NAME,
                        confidence=0.75,
                        method="json_parser"
                    )
                    

                )

        return candidate