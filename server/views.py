from pyramid.view import view_config
from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render

from lights import patterns

# @view_config(route_name='home', renderer='templates/mytemplate.jinja2')
# def my_view(request):
#     return {'project': 'hello_pyramid'}




# I really don't know why this works like it does... 
@view_config(route_name='home')
def test_page(request):
    response = FileResponse(
        'frontend/index.html',
        request=request,
        content_type='text/html'
        )
    return response




@view_config(route_name='getPatternInfo', renderer='json')
def getPatternInfo(request):
    pattern_library = patterns.pattern_library
    pattern_library_as_dict = dict( (key, vars(value) ) for key,value in pattern_library.items() )
    return pattern_library_as_dict