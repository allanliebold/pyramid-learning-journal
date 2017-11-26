"""Views default.py file."""
from pyramid.view import view_config
from pyramid.security import remember, forget
from pyramid_learning_journal.security import check_credentials
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid_learning_journal.models.entries import Entry
from datetime import datetime


@view_config(route_name='list', renderer='../templates/list.jinja2')
def list_view(request):
    """List view. Home page that displays all entries."""
    entries = request.dbsession.query(Entry).all()
    return {"entries": entries}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Detail view to display a specific Entry."""
    target = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(target)
    if entry:
        return {
            "title": entry.title,
            "created": entry.created,
            "id": entry.id,
            "body": entry.body
        }
    else:
        raise HTTPNotFound


@view_config(route_name='create', renderer='../templates/create.jinja2')
def create_view(request):
    """Create view for writing a new Entry."""
    if request.method == "POST" and request.POST:
        form_names = ["title", "body"]

        if sum([key in request.POST for key in form_names]) == len(form_names):

            if '' not in list(request.POST.values()):
                form_data = request.POST
                new_entry = Entry(
                    title=form_data['title'],
                    body=form_data['body'],
                    created=datetime.now(),
                )
            request.dbsession.add(new_entry)
            return {}
    data = request.POST
    return data


@view_config(route_name='update', renderer='../templates/update.jinja2')
def update_view(request):
    """Update view. Edit an Entry."""
    target = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(target)
    if not entry:
        raise HTTPNotFound
    if request.method == "GET":
        return {
            'entry': entry.to_dict()
        }
    if request.method == "POST" and request.POST:
        entry.title = request.POST['title']
        entry.body = request.POST['body']
        entry.created = datetime.now()
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=entry.id))


@view_config(route_name='private', renderer='string', permission='secret')
def private(request):
    return "Private view"


@view_config(route_name='public', renderer='string')
def public(request):
    return "Public view"


@view_config(route_name='delete')
def delete_view(request):
    """Delete an entry. Not functional yet."""
    target = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(target)
    if entry:
        request.dbsession.delete(Entry)
    else:
        raise HTTPNotFound


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    """User login."""
    if request.method == 'POST':
        username = request.params.get('username', '')
        password = request.params.get('password', '')
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('list'), headers=headers)
    return {}


@view_config(route_name='logout')
def logout(request):
    """Logout view."""
    headers = forget(request)
    return HTTPFound(request.route_url('list'), headers=headers)
