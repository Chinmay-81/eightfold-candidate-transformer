from app.schemas.candidate import Candidate
from app.pipeline.normalizer import CandidateNormalizer


candidate = Candidate(

    full_name="John Doe",

    emails=["JOHN@GMAIL.COM"],

    phones=["9876543210"],

    skills=[

        "python3",

        "ReactJS",

        "JS"

    ]

)

normalized = CandidateNormalizer.normalize(candidate)

print(

    normalized.model_dump_json(

        indent=4

    )

)