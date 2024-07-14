# Third-Party Dependencies
from arq.connections import ArqRedis

# ArqRedis connection pool for caching
pool: ArqRedis | None = None
