# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class SubgenreContentBase(Base):
    subgenre_name: str = Field(
        max_length=255,
        nullable=False,
        description="Subgenre Name",
        schema_extra={"examples": ["Minimal Techno"]},
    )


class Subgenre(
    UUIDMixin,
    SubgenreContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_subgenre"
    __table_args__ = ({"comment": "Management System subgenre information"},)
