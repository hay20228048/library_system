import os
#These are the replacement of from main import app
#To avoid getting (E   ModuleNotFoundError: No module named 'main')
#When trying to run pytest
import sys

import pytest

#It manually adds the project root to Python path.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_management.app.main import app

#If you don't want to change the system files, you can simply run the pytest using (PYTHONPATH=. pytest -v) command.




@pytest.fixture
def client():
    return app.test_client()



