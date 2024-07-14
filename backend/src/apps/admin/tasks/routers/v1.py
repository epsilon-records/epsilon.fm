# Built-in Dependencies
from typing import Dict, Optional, List, Optional, Annotated

# Third-Party Dependencies
from fastapi import APIRouter, Depends, Request
from arq.jobs import Job as ArqJob

# Local Dependencies
from src.apps.admin.tasks.schemas import Job, JobResult, JobDef, QueueHealth
from src.core.api.dependencies import get_current_user
from src.core.api.dependencies import rate_limiter
from src.core.exceptions.http_exceptions import (
    NotFoundException,
)
from src.apps.admin.users.schemas import (
    UserRead,
)
from src.core.utils import queue

router = APIRouter(tags=["Admin - Tasks"])


@router.post(
    "/admin/tasks",
    response_model=Job,
    status_code=201,
    dependencies=[Depends(rate_limiter)],
)
async def create_task(
    request: Request, current_user: Annotated[UserRead, Depends(get_current_user)], message: str
) -> Dict[str, str]:
    """
    Create a new background task.

    Parameters
    ----------
    message: str
        The message or data to be processed by the task.

    Returns
    ----------
    Dict[str, str]
        A dictionary containing the ID of the created task.
    """

    job = await queue.pool.enqueue_job("sample_background_task", message)  # type: ignore
    return {"id": job.job_id}


@router.get("/admin/tasks/{task_id}")
async def get_task(
    request: Request, current_user: Annotated[UserRead, Depends(get_current_user)], task_id: str
) -> Optional[JobDef]:
    """
    Get information about a specific background task.

    Parameters
    ----------
    task_id: str
        The ID of the task.

    Returns
    ----------
    Optional[Dict[str, Any]]
        A dictionary containing information about the task if found, or None otherwise.
    """

    job = ArqJob(job_id=str(task_id), redis=queue.pool)
    job_info: dict = await job.info()
    return job_info


@router.get("/admin/tasks/processed/")
async def read_processed_tasks(
    request: Request, current_user: Annotated[UserRead, Depends(get_current_user)]
) -> List[JobResult]:
    """
    Get results for all background tasks that have been processed.

    Returns
    ----------
    List[Dict[str, Any]]
        A list of dictionaries containing information about each processed task.
    """

    processed_jobs = await queue.pool.all_job_results()
    return processed_jobs


@router.get("/admin/tasks/pending/")
async def read_pending_tasks(
    request: Request, current_user: Annotated[UserRead, Depends(get_current_user)]
) -> List[JobDef]:
    """
    Get results for all background tasks that have pending processing.

    Returns
    ----------
    List[Dict[str, Any]]
        A list of dictionaries containing information about each pending task.
    """

    pending_jobs = await queue.pool.queued_jobs()
    return pending_jobs


@router.get("/admin/tasks/queue-health/")
async def read_queue_health(
    request: Request,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    queue_name: Optional[str] = None,
) -> QueueHealth:
    """
    Get the current health status of the queue, including the number of pending and processed tasks.

    Parameters
    ----------
    queue_name: Optional[str] (default: 'queue')
        The name of the queue. If not provided, defaults to 'queue'.

    Returns
    ----------
    QueueHealth
        An object containing the current health status of the queue, including the number of completed, failed, retried, and ongoing tasks, as well as the number of tasks currently queued.
    """

    if queue_name is None:
        queue_name = "queue"

    health_queue_from_redis = await queue.pool.get(f"arq:{queue_name}:health-check")

    if not health_queue_from_redis:
        raise NotFoundException(detail=f"Queue with name '{queue_name}' not found on broker.")

    queue_health = QueueHealth.from_string(health_queue_from_redis.decode("utf-8"))
    return queue_health
