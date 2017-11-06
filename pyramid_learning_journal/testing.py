"""Testing for Learning Journal."""

import pytest
from pyramid import testing
import transaction
from pyramid_learning_journal.models import (
    Entry,
    get_tm_session,
)
from pyramid_learning_journal.models.meta import Base


@pytest.fixture
def testapp():
    """Create an instance for testing."""
    from pyramid_learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


@pytest.fixture(scope="session")
def configuration(request):
    """Set up Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres:///test_entries'
    })
    config.include("pyramid_learning_journal.models")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a database session."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Create a dummy request."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_dict(dummy_request):
    """List view returns response."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


# def test_list_view_returns_len_content(dummy_request):
#     """List view response has correct amount of content."""
#     from pyramid_learning_journal.views.default import list_view
#     response = list_view(dummy_request)
#     assert len(response['entries']) == len(ENTRIES)


# def test_create_view(dummy_request):
#     """Create view."""
#     from pyramid_learning_journal.views.default import create_view
#     response = create_view(dummy_request)
#     assert isinstance(response, dict)
