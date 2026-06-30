from app.parsers.recruiter_parser import RecruiterCSVParser
from app.parsers.resume_parser import ResumeParser
from app.parsers.github_parser import GitHubParser
from app.parsers.linkedin_parser import LinkedInParser

from app.pipeline.normalizer import CandidateNormalizer
from app.pipeline.merger import MergeEngine
from app.pipeline.confidence import ConfidenceEngine


csv_candidate = RecruiterCSVParser.parse(
    "sample_inputs/recruiter.csv"
)[0]

resume_candidate = ResumeParser.parse(
    "sample_inputs/resume.docx"
)

github_candidate = GitHubParser.parse(
    "sample_inputs/github.json"
)

linkedin_candidate = LinkedInParser.parse(
    "sample_inputs/linkedin.json"
)

merged = MergeEngine.merge([

    CandidateNormalizer.normalize(csv_candidate),

    CandidateNormalizer.normalize(resume_candidate),

    CandidateNormalizer.normalize(github_candidate),

    CandidateNormalizer.normalize(linkedin_candidate)

])

merged = ConfidenceEngine.calculate(merged)

print(

    merged.model_dump_json(

        indent=4

    )

)