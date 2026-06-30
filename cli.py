import typer

from app.pipeline.pipeline import CandidatePipeline

app = typer.Typer()


@app.command()
def run(
    recruiter_csv: str,
    resume: str,
    github: str,
    linkedin: str,
    config: str,
):

    result = CandidatePipeline.run(
        recruiter_csv,
        resume,
        github,
        linkedin,
        config
    )

    print(result)


if __name__ == "__main__":
    app()