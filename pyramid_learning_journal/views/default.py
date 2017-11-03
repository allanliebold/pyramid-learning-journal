"""Views default.py file."""
from pyramid.view import view_config
from pyramid_learning_journal.data.entry_data import ENTRIES


@view_config(route_name='list', renderer='../templates/list.jinja2')
def list_view(request):
    """List view."""
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Detail view."""
    return {
        "title": "Day 11",
        "creation_date": "October 30, 2017",
        "content": ("We got our introduction to the Pyramid framework today."
                    "It doesn't seem to be too complicated... but I don't want"
                    " to make any assumptions about how simple this will be "
                    "to learn. At first glance it seems like you're given the basic"
                    " structure and you just make changes and add in what you "
                    "want... like some sort of framework. Yeah. I followed along "
                    "decently with the example during lecture, but I need to go "
                    "over it again. Other than that we learned about the "
                    "Double-Ended Queue, or Deque. Nothing too crazy or very "
                    "different from what we've done so far with data structures.")
    }


@view_config(route_name='create', renderer='../templates/create.jinja2')
def create_view(request):
    """Create view."""
    return 'Create View'


@view_config(route_name='update', renderer='../templates/update.jinja2')
def update_view(request):
    """Update view."""
    return 'Update View'
