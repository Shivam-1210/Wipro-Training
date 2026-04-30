import pytest


'''@pytest.fixture(scope='module',autouse=True)
def setup():
    print('Fixture')'''

@pytest.fixture(scope='function',autouse=True)
def setup_teardown():
    print('Starting......')
    yield
    print('Ending......')