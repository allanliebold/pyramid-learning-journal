"""Testing for Learning Journal."""

from pyramid import testing
from pyramid_learning_journal.data.entry_data import ENTRIES
import pytest


@pytest.fixture()
def testapp():
    """Create an instance for testing."""
    from pyramid_learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_root_contents(testapp):
    """Test contents of root page contents."""
    from pyramid_learning_journal.data.entry_data import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("article"))


def test_list_view_returns_dict():
    """List view returns response."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, dict)


def test_list_view_returns_len_content():
    """List view response has correct amount of content."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert len(response['entries']) == len(ENTRIES)


def test_detail_view():
    """Test detail view returns dictionary of values."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    info = detail_view(request)
    assert isinstance(info, dict)


def test_detail_view_response_contains_expense_attrs():
    """Test detail view returns entry."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    info = detail_view(request)
    for key in ["created", "title", "text"]:
        assert key in info.keys()
