"""
Projection Engine

Converts the internal Candidate object
into any client-specific JSON using config.json.
"""
import json

from app.schemas.candidate import Candidate


class ProjectionEngine:

    @staticmethod
    def _get_value(candidate, expression):
       
        if "[" in expression:

            field = expression.split("[")[0]

            index = int(
                expression.split("[")[1][:-1]
            )

            value = getattr(candidate, field)

            if len(value) > index:
                return value[index]

            return None

        return getattr(candidate, expression, None)

    @staticmethod
    def project(candidate: Candidate,
                config_path: str):

        with open(config_path,
                  "r",
                  encoding="utf-8") as file:

            config = json.load(file)

        output = {}

        for field in config["fields"]:

            source = field["from"]

            destination = field["path"]

            value = ProjectionEngine._get_value(
                candidate,
                source
            )

            if value is None:

                if config["on_missing"] == "null":

                    output[destination] = None

            else:

                output[destination] = value

        if config.get("include_confidence"):

            output["overall_confidence"] = (
                candidate.overall_confidence
            )

        return output