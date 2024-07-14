# Local Dependencies
from src.core.common.crud import CRUDBase
from src.apps.epsilon.tracks.models import Track
from src.apps.epsilon.tracks.schemas import (
    TrackCreateInternal,
    TrackUpdate,
    TrackUpdateInternal,
    TrackDelete,
)

# Define CRUD operations for the 'Track' model
CRUDTrack = CRUDBase[Track, TrackCreateInternal, TrackUpdate, TrackUpdateInternal, TrackDelete]

# Create an instance of CRUDTrack for the 'Track' model
crud_tracks = CRUDTrack(Track)
