from app.parsers.recruiter_parser import RecruiterCSVParser

candidates = RecruiterCSVParser.parse(
    "sample_inputs/recruiter.csv"
)

for candidate in candidates:

    print(candidate.model_dump_json(indent=4))