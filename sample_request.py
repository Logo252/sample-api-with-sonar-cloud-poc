from pydantic import BaseModel, HttpUrl, validator


class SampleRequest(BaseModel):
    parameter1: str = "png"

    @validator("parameter1")
    def validate_format(cls, value):
        supported_values = ["test1", "test2", "test3", "test4"]

        if value not in supported_values:
            raise ValueError(f"Invalid 'parameter1' parameter. Supported values: {', '.join(supported_values)}")
        return value
