"""Test for pyramid journal."""
from pyramid import testing
from pyramid.response import Response


def test_list_view_returns_response():
    """List view returns a Response object."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, Response)


def test_list_view_ok():
    """List view response has a status 200 OK."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert response.status_code == 200


def test_list_view_type():
    """List view response body is html."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert response.content_type == 'text/html'


def test_create_view_ok():
    """Create view response has a status 200 OK."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert response.status_code == 200


def test_create_view_type():
    """Create view response body is html."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert response.content_type == 'text/html'
