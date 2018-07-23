from pyramid.view import view_config
from pyramid.response import Response
from pyramid.response import FileResponse

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