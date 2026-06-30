from collections import defaultdict

from app.schemas.candidate import Candidate


class ConfidenceEngine:

    @staticmethod
    def calculate(candidate: Candidate):

        if not candidate.provenance:
            candidate.overall_confidence = 0.0
            return candidate

        grouped = defaultdict(list)

        for item in candidate.provenance:
            grouped[item.field].append(item.confidence)

        field_scores = {}

        for field, scores in grouped.items():
            field_scores[field] = round(
                max(scores),
                2
            )

        candidate.field_confidence = field_scores

        candidate.overall_confidence = round(

            sum(field_scores.values())

            / len(field_scores),

            2

        )

        return candidate