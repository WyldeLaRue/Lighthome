from pyramid.config import Configurator
from pyramid.response import Response

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view(name='static', path='../frontend')
    config.add_route('home', '/')
    # config.add_route('react', '/test')
    # config.add_view(hello_world, route_name='react')
    config.scan()
    return config.make_wsgi_app()

