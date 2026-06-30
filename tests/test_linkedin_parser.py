from app.parsers.linkedin_parser import LinkedInParser

candidate = LinkedInParser.parse(
    "sample_inputs/linkedin.json"
)

print(candidate.model_dump_json(indent=4))