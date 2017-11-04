"""Testing for Learning Journal."""

from pyramid import testing
from pyramid_learning_journal.data.entry_data import ENTRIES
import pytest


@pytest.fixture
def dummy_request():
    """Create a dummy request."""
    return testing.DummyRequest()


@pytest.fixture()
def testapp():
    """Create an instance for testing."""
    from pyramid_learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_list_view_returns_dict():
    """List view returns response."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, dict)


def test_list_view_returns_len_content(dummy_request):
    """List view response has correct amount of content."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['entries']) == len(ENTRIES)


def test_create_view(dummy_request):
    """Create view."""
    from pyramid_learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert isinstance(response, dict)
