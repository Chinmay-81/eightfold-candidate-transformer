# Multi-Source Candidate Data Transformer

**Eightfold Engineering Intern Assignment**

This project transforms candidate information collected from multiple structured and unstructured sources into a single canonical candidate profile.

The pipeline parses candidate data from multiple inputs, normalizes inconsistent values, merges information using source priority, assigns confidence scores, validates the final profile, and generates configurable JSON output.

---

## Features

- Parse multiple candidate data sources
  - Recruiter CSV
  - Resume (DOCX/PDF)
  - GitHub JSON
  - LinkedIn JSON
- Canonical candidate schema
- Data normalization
- Merge & conflict resolution
- Confidence scoring
- Provenance tracking
- Configurable output using runtime JSON configuration
- Output validation
- REST API using FastAPI

---

# Project Structure

```text
eightfold-transformer/
│
├── app/
│   ├── parsers/
│   │   ├── recruiter_parser.py
│   │   ├── resume_parser.py
│   │   ├── github_parser.py
│   │   └── linkedin_parser.py
│   │
│   ├── pipeline/
│   │   ├── normalizer.py
│   │   ├── merger.py
│   │   ├── confidence.py
│   │   ├── projection.py
│   │   ├── validator.py
│   │   └── pipeline.py
│   │
│   ├── schemas/
│   ├── utils/
│   └── main.py
│
├── sample_inputs/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# Pipeline

```
Recruiter CSV
Resume
GitHub JSON
LinkedIn JSON
        │
        ▼
Source Detection & Parsing
        ▼
Canonical Candidate Model
        ▼
Normalization
        ▼
Merge & Conflict Resolution
        ▼
Confidence + Provenance
        ▼
Projection (Runtime Config)
        ▼
Validation
        ▼
Final JSON Output
```

---

# Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Pandas
- pdfplumber
- python-docx
- phonenumbers
- pycountry

---

# Installation

Clone the repository

```bash
git clone https://github.com/Chinmay-81/eightfold-candidate-transformer.git

cd eightfold-transformer
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start FastAPI server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

Upload

- recruiter.csv
- resume.docx
- github.json
- linkedin.json
- config.json

Click **Execute** to generate the transformed candidate profile.

---

# Sample Input Sources

The repository contains sample files inside

```
sample_inputs/
```

- recruiter.csv
- resume.docx
- github.json
- linkedin.json
- config.json

---

# Sample Output

The pipeline generates a unified candidate profile similar to:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+919876543210",
  "skills": [
    "Python",
    "Java",
    "FastAPI",
    "React"
  ],
  "overall_confidence": 0.91
}
```

---

# Running Tests

Example

```bash
python -m tests.test_recruiter_parser

python -m tests.test_resume_parser

python -m tests.test_github_parser

python -m tests.test_linkedin_parser

python -m tests.test_projection
```

---

# Design Decisions

- Every input source is converted into the same canonical candidate model before any processing.
- Each pipeline stage performs a single responsibility.
- Runtime configuration controls the output schema without changing application code.
- Source priority is used to resolve conflicting values during merging.
- Provenance and confidence scores improve traceability of the generated profile.

---

# Assumptions

- Recruiter CSV follows the expected column format.
- GitHub and LinkedIn data are provided as JSON exports.
- Resume contains extractable text.
- Phone numbers can be normalized using the default region when required.

---

# Future Improvements

- OCR support for scanned resumes
- AI-assisted resume parsing
- Better duplicate detection
- Database integration
- Authentication & authorization
- Docker deployment
- Logging & monitoring

---

## Author

**Chinmay Nayak**

Eightfold Engineering Intern Assignment
