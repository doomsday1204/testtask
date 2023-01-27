from datetime import timedelta
from typing import Optional


from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.schema import date


class URLBase(BaseModel):
    target_url: str
    lifetime: date = Field(default=(date.today() + timedelta(days=90)))


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True


class URLInfo(URL):
    url: str
    admin_url: str
    lifetime: Optional[date]
