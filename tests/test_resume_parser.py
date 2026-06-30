from app.parsers.resume_parser import ResumeParser

candidate = ResumeParser.parse(
    "sample_inputs/resume.docx"
)

print(candidate.model_dump_json(indent=4))