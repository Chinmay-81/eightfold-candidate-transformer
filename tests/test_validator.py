from app.pipeline.validator import Validator

sample = {
    "name":"John Doe",
    "email":"john@gmail.com",
    "phone":"+919876543210"
}

print(Validator.validate(sample))