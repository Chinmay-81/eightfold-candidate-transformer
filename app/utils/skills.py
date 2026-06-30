"""
Skill normalization.
"""

SKILL_MAP = {

    "py": "Python",

    "python3": "Python",

    "reactjs": "React",

    "react.js": "React",

    "js": "JavaScript",

    "javascript": "JavaScript",

    "spring": "Spring Boot",

    "springboot": "Spring Boot",

    "spring boot": "Spring Boot"

}


def normalize_skill(skill: str):

    if not skill:

        return None

    key = skill.strip().lower()

    return SKILL_MAP.get(key, skill.strip())