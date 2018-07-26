from pyramid.config import Configurator
from pyramid.response import Response

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view(name='static', path='../frontend')
    routes(config)
    # config.add_route('react', '/test')
    # config.add_view(hello_world, route_name='react')
    config.scan()
    return config.make_wsgi_app()





def routes(config):
    config.add_route('home', '/')



    config.include(lights_api_endpoints,   route_prefix='/api/{version_number}/lights')


# handles everything with url prefix: /api/version/lights/
def lights_api_endpoints(config):
    config.add_route('get_pattern_library', '/get_pattern_library')
    config.add_route('set_pattern',         '/set_pattern/{pattern_id}')
