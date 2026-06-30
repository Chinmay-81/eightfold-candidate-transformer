from app.parsers.github_parser import GitHubParser

candidate = GitHubParser.parse(
    "sample_inputs/github.json"
)

print(candidate.model_dump_json(indent=4))