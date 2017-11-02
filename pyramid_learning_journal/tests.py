from pyramid.response import Response
import os
import io

HERE = os.path.dirname(__file__)


def list_view(request):
    path = os.path.join(HERE, '../templates/index.html')
    with io.open(path) as file:
        return Response(file.read())


def detail_view(request):
    path = os.path.join(HERE, '../templates/detail.html')
    with io.open(path) as file:
        return Response(file.read())


def create_view(request):
    path = os.path.join(HERE, '../templates/create.html')
    with io.open(path) as file:
        return Response(file.read())


def update_view(request):
    path = os.path.join(HERE, '../templates/update.html')
    with io.open(path) as file:
        return Response(file.read())
