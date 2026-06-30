from typing import List, Optional
from pydantic import BaseModel, EmailStr


class Location(BaseModel):
    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None


class Links(BaseModel):
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None
    other: List[str] = []


class Experience(BaseModel):
    company: Optional[str] = None
    title: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    summary: Optional[str] = None


class Education(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    field: Optional[str] = None
    end_year: Optional[int] = None


class Provenance(BaseModel):
    field: str
    source: str
    confidence: float
    method: str


class Candidate(BaseModel):
    candidate_id: Optional[str] = None

    full_name: Optional[str] = None

    emails: List[EmailStr] = []

    phones: List[str] = []

    location: Location = Location()

    links: Links = Links()

    headline: Optional[str] = None

    years_experience: Optional[int] = None

    skills: List[str] = []

    experience: List[Experience] = []

    education: List[Education] = []

    provenance: List[Provenance] = []

    field_confidence: dict[str, float] = {}

    overall_confidence: float = 0.0 