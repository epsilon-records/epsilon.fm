# Built-in Dependencies
from typing import Any, Dict, Tuple, Optional, List
from datetime import datetime

# Third-Party Dependencies
from pydantic import BaseModel, field_validator

# Local Dependencies
from src.core.common.models import Base


class Job(Base):
    id: str


class JobResult(BaseModel):
    function: str
    args: List[Any]
    kwargs: Dict[str, Any]
    job_try: int
    enqueue_time: datetime
    score: Optional[int]
    success: bool
    result: Any
    start_time: datetime
    finish_time: datetime
    queue_name: str
    job_id: Optional[str]

    @field_validator("score")
    def adjust_score(cls, v: Optional[int]) -> Optional[int]:
        return None if v is None else v


class JobDef(BaseModel):
    function: str
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    job_try: Optional[int]
    enqueue_time: datetime
    score: Optional[int]

    @field_validator("job_try")
    def adjust_job_try(cls, v: str) -> str:
        return 0 if v is None else v


class QueueHealth(BaseModel):
    date: datetime
    job_complete: int
    job_failed: int
    job_retried: int
    job_ongoing: int
    queued: int

    @classmethod
    def from_string(cls, data: str) -> Optional["QueueHealth"]:
        parts = data.split()
        date_string = parts.pop(0)  # Remove and obtain the first part as the date
        time_string = parts.pop(0)  # Obtain the second part time
        current_year = datetime.now().year  # Get the current year
        date_time_string = (
            f"{date_string} {current_year} {time_string}"  # Create the full date and time string
        )
        date_time = datetime.strptime(
            date_time_string, "%b-%d %Y %H:%M:%S"
        )  # Convert the string into a Datetime object
        stats = {}
        for part in parts:
            key, value = part.replace("j_", "job_").split("=")
            stats[key] = int(value)
        return cls(date=date_time, **stats)
