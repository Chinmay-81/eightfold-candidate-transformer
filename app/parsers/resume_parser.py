import re
import pdfplumber
import docx
import uuid

from app.schemas.candidate import Candidate, Provenance


class ResumeParser:

    SOURCE_NAME = "resume"

    @staticmethod
    def extract_text(file_path):

        if file_path.endswith(".pdf"):

            text = ""

            with pdfplumber.open(file_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:

                        text += page_text + "\n"

            return text

        elif file_path.endswith(".docx"):

            doc = docx.Document(file_path)

            return "\n".join(
                para.text for para in doc.paragraphs
            )

        else:

            raise ValueError("Unsupported file")

    @staticmethod
    def parse(file_path):

        text = ResumeParser.extract_text(file_path)

        candidate = Candidate(
            candidate_id=str(uuid.uuid4())
        )

        email = re.search(

            r'[\w\.-]+@[\w\.-]+\.\w+',

            text
        )

        if email:

            candidate.emails.append(email.group())

            candidate.provenance.append(

                Provenance(

                    field="email",

                    source="resume",

                    confidence=0.95,

                    method="regex"

                )

            )

        phone = re.search(

            r'(\+?\d[\d -]{8,}\d)',

            text

        )

        if phone:

            candidate.phones.append(phone.group())

            candidate.provenance.append(

                Provenance(

                    field="phone",

                    source="resume",

                    confidence=0.95,

                    method="regex"

                )

            )

        lines = text.split("\n")

        if len(lines):

            candidate.full_name = lines[0]

            candidate.provenance.append(

                Provenance(

                    field="name",

                    source="resume",

                    confidence=0.90,

                    method="first_line"

                )

            )

        skill_keywords = [

            "Python",

            "Java",

            "Spring Boot",

            "React",

            "FastAPI",

            "SQL",

            "JavaScript"

        ]

        lower_text = text.lower()

        for skill in skill_keywords:

            if skill.lower() in lower_text:

                candidate.skills.append(skill)

                candidate.provenance.append(

                    Provenance(

                        field="skills",

                        source="resume",

                        confidence=0.90,

                        method="keyword_match"

                    )

                )

        return candidate