from sqlmodel import Field, SQLModel


class WebPage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str
    title: str
