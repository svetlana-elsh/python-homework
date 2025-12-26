from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Subject(Base):
    __tablename__ = "subject"

    subject_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_title: Mapped[str] = mapped_column(String)
