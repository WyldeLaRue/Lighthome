from pyramid.view import view_config
from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render

from lights import patterns

# I really don't know why this works like it does... 
@view_config(route_name='home')
def index(request):
    response = FileResponse(
        'frontend/static/index.html',
        request=request,
        content_type='text/html'
        )
    return response




@view_config(route_name='get_pattern_library', renderer='json')
def get_pattern_library(request):
    pattern_library = patterns.pattern_library
    pattern_library_as_dict = dict( (key, vars(value) ) for key,value in pattern_library.items() )
    return pattern_library_as_dict

@view_config(route_name='set_pattern')
def set_pattern(request):
    pattern_id = request.matchdict['pattern_id']
    print("setting pattern to: " + pattern_id)
    return Response('OK')


