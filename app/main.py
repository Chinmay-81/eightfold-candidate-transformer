import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File

from app.pipeline.pipeline import CandidatePipeline

app = FastAPI(
    title="Eightfold AI Candidate Transformer"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def save_upload(upload_file: UploadFile) -> str:
    file_path = UPLOAD_DIR / upload_file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return str(file_path)


@app.post("/transform")
async def transform(

    recruiter_csv: UploadFile = File(...),

    resume: UploadFile = File(...),

    github_json: UploadFile = File(...),

    linkedin_json: UploadFile = File(...),

    config_json: UploadFile = File(...)

):

    recruiter_path = save_upload(recruiter_csv)
    resume_path = save_upload(resume)
    github_path = save_upload(github_json)
    linkedin_path = save_upload(linkedin_json)
    config_path = save_upload(config_json)

    return CandidatePipeline.run(

        recruiter_path,

        resume_path,

        github_path,

        linkedin_path,

        config_path

    )