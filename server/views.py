from pyramid.view import view_config
from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render

from lights import patterns
from lights.process import light_process_manager
from outlets import outlets


# I really don't know why this works like it does... 
@view_config(route_name='home')
def index(request):
    print('HTTP Request -- home')
    PATH = "/home/tristan/Lighthome/frontend/static/index.html"
#   response = FileResponse(
#       'frontend/static/index.html',
#       request=request,
#       content_type='text/html'
#    )
    return FileResponse(PATH, request=request)

@view_config(route_name='get_pattern_library', renderer='json')
def get_pattern_library(request):
    pattern_library = patterns.pattern_library
    pattern_library_as_dict = dict( (key, vars(value) ) for key,value in pattern_library.items() )
    return pattern_library_as_dict

@view_config(route_name='set_pattern')
def set_pattern(request):
    pattern_id = request.matchdict['pattern_id']
    print("setting pattern to: " + pattern_id)
    light_process_manager.change_state({"pattern": pattern_id})
    return Response('OK')


@view_config(route_name='set_outlet_state')
def set_outlet_state(request):
    print("POST request: set_outlet_state")
    body = request.json_body
    new_state = body['targetState']
    print("targetState=", new_state)
    outlet_id = request.matchdict['outlet_id']
    outlets.send_outlet_signal(new_state, outlet_id)
    response = Response(
        status = 204
    )
    return response


@view_config(route_name='get_outlet_state', renderer='json')
def get_outlet_state(request):
    response = Response(
        json = {'currentState': 'On', 'test': 'hell0 world'},
        content_type = "application/json",
        status = 200
    )
    return  response








