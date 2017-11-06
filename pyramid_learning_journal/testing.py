"""Testing for Learning Journal."""

import pytest
from datetime import datetime
from faker import Faker
from pyramid import testing
import transaction
from pyramid_learning_journal.models import (
    Entry,
    get_tm_session,
)
from pyramid_learning_journal.models.meta import Base


FAKE_FACTORY = Faker()
ENTRY_LIST = [Entry(
    title="Test Entry",
    body=FAKE_FACTORY.text(100),
    created=datetime.now(),
) for i in range(20)]


@pytest.fixture(scope="session")
def testapp(request):
    """Create an instance for testing."""
    from webtest import TestApp
    from pyramid_learning_journal import main

    app = main({}, **{"sqlalchemy.url": "postgres:///test_entries"})
    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    request.addfinalizer(tearDown)

    return testapp


@pytest.fixture
def fill_the_db(testapp):
    """Add items to the database."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(ENTRY_LIST)

    return dbsession


@pytest.fixture
def add_models(dummy_request):
    """Add model instances to the database."""
    dummy_request.dbsession.add_all(ENTRY_LIST)


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


def test_model_gets_added(db_session):
    """Test adding model to database."""
    assert len(db_session.query(Entry).all()) == 0
    model = Entry(
        title="Test Entry",
        body="This is a test entry.",
        created=datetime.now(),
    )
    db_session.add(model)
    assert len(db_session.query(Entry).all()) == 1


def test_list_view_returns_dict(dummy_request):
    """List view returns response."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_count_matching_database(dummy_request):
    """List view matches database count."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    query = dummy_request.dbsession.query(Entry)
    assert len(response['entries']) == query.count()


# def test_list_view_returns_empty_when_database_empty(dummy_request):
#     """List view returns empty when no data in database."""
#     from pyramid_learning_journal.views.default import list_view
#     response = list_view(dummy_request)
#     assert len(response['entries']) == 0


# def test_create_view(dummy_request):
#     """Create view."""
#     from pyramid_learning_journal.views.default import create_view
#     response = create_view(dummy_request)
#     assert isinstance(response, dict)
