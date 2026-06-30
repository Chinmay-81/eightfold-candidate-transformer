from app.schemas.candidate import Candidate

candidate = Candidate(
    full_name="John Doe",
    emails=["john@gmail.com"],
    phones=["9876543210"],
    skills=["Python", "Java"]
)

print(candidate.model_dump_json(indent=4))