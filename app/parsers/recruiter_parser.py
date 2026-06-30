import pandas as pd
import uuid

from app.schemas.candidate import (
    Candidate,
    Experience,
    Provenance
)


class RecruiterCSVParser:

    SOURCE_NAME = "recruiter_csv"

    @staticmethod
    def parse(csv_path: str):

        df = pd.read_csv(csv_path)

        candidates = []

        for _, row in df.iterrows():

            candidate = Candidate(
                candidate_id=str(uuid.uuid4()),
                full_name=row.get("name"),
                emails=[row.get("email")] if pd.notna(row.get("email")) else [],
                phones=[str(row.get("phone"))] if pd.notna(row.get("phone")) else [],
            )

            company = row.get("current_company")
            title = row.get("title")

            if pd.notna(company) or pd.notna(title):

                candidate.experience.append(
                    Experience(
                        company=company,
                        title=title
                    )
                )

            fields = [
                "name",
                "email",
                "phone",
                "current_company",
                "title"
            ]

            for field in fields:

                if pd.notna(row.get(field)):

                    candidate.provenance.append(

                        Provenance(
                            field=field,
                            source=RecruiterCSVParser.SOURCE_NAME,
                            confidence=0.85,
                            method="csv_parser"
                        )
                    )

            candidates.append(candidate)

        return candidates
        