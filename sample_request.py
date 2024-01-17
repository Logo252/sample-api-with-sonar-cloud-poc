from pydantic import BaseModel, HttpUrl, validator


class SampleRequest(BaseModel):
    parameter1: str = "png"

    @validator("parameter1")
    def validate_format(cls, value):
        supported_formats = ["png", "svg", "eps", "pdf", "txt"]

        if value not in supported_formats:
            raise ValueError(f"Invalid 'parameter1' parameter. Supported formats: {', '.join(supported_formats)}")
        return value
