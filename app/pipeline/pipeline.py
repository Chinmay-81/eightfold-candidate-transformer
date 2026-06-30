from app.parsers.recruiter_parser import RecruiterCSVParser
from app.parsers.resume_parser import ResumeParser
from app.parsers.github_parser import GitHubParser
from app.parsers.linkedin_parser import LinkedInParser

from app.pipeline.normalizer import CandidateNormalizer
from app.pipeline.merger import MergeEngine
from app.pipeline.confidence import ConfidenceEngine
from app.pipeline.projection import ProjectionEngine
from app.pipeline.validator import Validator


class CandidatePipeline:

    @staticmethod
    def run(
        recruiter_csv: str,
        resume_file: str,
        github_json: str,
        linkedin_json: str,
        config_json: str
    ):

        candidates = []

        # Recruiter CSV
        recruiter_candidates = RecruiterCSVParser.parse(recruiter_csv)

        for candidate in recruiter_candidates:
            candidates.append(
                CandidateNormalizer.normalize(candidate)
            )

        # Resume
        resume_candidate = ResumeParser.parse(resume_file)
        candidates.append(
            CandidateNormalizer.normalize(resume_candidate)
        )

        # GitHub
        github_candidate = GitHubParser.parse(github_json)
        candidates.append(
            CandidateNormalizer.normalize(github_candidate)
        )

        # LinkedIn
        linkedin_candidate = LinkedInParser.parse(linkedin_json)
        candidates.append(
            CandidateNormalizer.normalize(linkedin_candidate)
        )

        # Merge
        merged = MergeEngine.merge(candidates)

        # Confidence
        merged = ConfidenceEngine.calculate(merged)

        # Projection
        output = ProjectionEngine.project(
            merged,
            config_json
        )

        # Validation
        errors = Validator.validate(output)

        return {
            "candidate": output,
            "validation_errors": errors
        }