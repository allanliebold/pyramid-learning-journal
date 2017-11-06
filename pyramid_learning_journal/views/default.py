"""Views default.py file."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
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
    if request.method == "POST":
        form_data = request.POST
        new_entry = Entry(
            title=form_data['title'],
            body=form_data['body'],
            created=datetime.now(),
        )
        request.dbsession.add(new_entry)
        return {}
    return {}


@view_config(route_name='update', renderer='../templates/update.jinja2')
def update_view(request):
    """Update view. Edit an Entry."""
    # target = int(request.matchdict('id'))
    # for entry in ENTRIES:
    #     if entry['id'] == target:
    return {
        # 'entry': entry
    }
