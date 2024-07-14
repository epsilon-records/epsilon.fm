# Local Dependencies
from src.core.logger import logging, configure_logging

# Configure logging for the tests suite
configure_logging(log_file="tests")

# Logger instance for the current module
logger = logging.getLogger(__name__)

# Unit tests imports (V1 routes)
from src.apps.auth.tests.test_v1 import *
from src.apps.system.tiers.tests.test_v1 import *
from src.apps.system.rate_limits.tests.test_v1 import *
from src.apps.admin.users.tests.test_v1 import *
from src.apps.admin.tasks.tests.test_v1 import *
from src.apps.blog.posts.tests.test_v1 import *
