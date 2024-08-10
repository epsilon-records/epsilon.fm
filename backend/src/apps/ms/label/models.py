# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class LabelsContentBase(Base):
    label_name: str = Field(
        max_length=255,
        nullable=False,
        description="Labels Name",
        schema_extra={"examples": ["Electronic"]},
    )


class Labels(
    UUIDMixin,
    LabelsContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_label"
    __table_args__ = ({"comment": "Management System label information"},)
