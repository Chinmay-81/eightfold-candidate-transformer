from typing import List, Optional

from app.schemas.candidate import Candidate
from app.config.source_priority import SOURCE_PRIORITY


class MergeEngine:

    @staticmethod
    def merge(candidates: List[Candidate]) -> Candidate:

        merged = Candidate()

        merged.full_name = MergeEngine._choose_string(
            candidates,
            "full_name"
        )

        merged.headline = MergeEngine._choose_string(
            candidates,
            "headline"
        )

        merged.emails = MergeEngine._merge_unique_lists(
            candidates,
            "emails"
        )

        merged.phones = MergeEngine._merge_unique_lists(
            candidates,
            "phones"
        )

        merged.skills = MergeEngine._merge_unique_lists(
            candidates,
            "skills"
        )

        merged.experience = MergeEngine._merge_unique_lists(
            candidates,
            "experience"
        )

        merged.education = MergeEngine._merge_unique_lists(
            candidates,
            "education"
        )

        merged.provenance = MergeEngine._merge_unique_lists(
            candidates,
            "provenance"
        )

        merged.location = MergeEngine._merge_location(
            candidates
        )

        merged.links = MergeEngine._merge_links(
            candidates
        )

        merged.years_experience = MergeEngine._choose_string(
            candidates,
            "years_experience"
        )

        return merged

    @staticmethod
    def _candidate_priority(candidate: Candidate):

        if not candidate.provenance:
            return 0

        source = candidate.provenance[0].source

        return SOURCE_PRIORITY.get(
            source,
            0
        )

    @staticmethod
    def _choose_string(

        candidates,

        field

    ):

        best = None

        highest = -1

        for candidate in candidates:

            value = getattr(candidate, field)

            if value:

                priority = MergeEngine._candidate_priority(
                    candidate
                )

                if priority > highest:

                    highest = priority

                    best = value

        return best

    @staticmethod
    def _merge_unique_lists(

        candidates,

        field

    ):

        merged = []

        seen = set()

        for candidate in candidates:

            values = getattr(

                candidate,

                field

            )

            for value in values:

                key = str(value)

                if key not in seen:

                    seen.add(key)

                    merged.append(value)

        return merged

    @staticmethod
    def _merge_location(candidates):
        

        for candidate in sorted(

            candidates,

            key=MergeEngine._candidate_priority,

            reverse=True

        ):

            if candidate.location.country:

                return candidate.location

        return candidates[0].location


    @staticmethod
    def _merge_links(candidates):

        links = candidates[0].links.__class__()

        for candidate in candidates:

            if candidate.links.github:

                links.github = candidate.links.github

            if candidate.links.linkedin:

                links.linkedin = candidate.links.linkedin

            if candidate.links.portfolio:

                links.portfolio = candidate.links.portfolio

            links.other.extend(

                candidate.links.other

            )

        links.other = list(

            dict.fromkeys(

                links.other

            )

        )

        return links