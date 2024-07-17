# Local Dependencies
from src.core.common.crud import CRUDBase
from src.apps.e.artists.models import Artist
from src.apps.e.artists.schemas import (
    ArtistCreateInternal,
    ArtistUpdate,
    ArtistUpdateInternal,
    ArtistDelete,
)

# Define CRUD operations for the 'Artist' model
CRUDArtist = CRUDBase[
    Artist, ArtistCreateInternal, ArtistUpdate, ArtistUpdateInternal, ArtistDelete
]

# Create an instance of CRUDArtist for the 'Artist' model
crud_artists = CRUDArtist(Artist)
