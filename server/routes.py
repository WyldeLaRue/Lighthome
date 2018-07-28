

def setup(config):
    config.add_route('home', '/')

    static_routes(config)
    route_prefixes(config)


def static_routes(config):
    config.add_static_view(name='static', path='../frontend/static')
    config.add_static_view(name='src', path='../frontend/src')


def route_prefixes(config):
    config.include(lights_api_endpoints,   route_prefix='/api/{version_number}/lights')


# prefix: /api/version/lights/
def lights_api_endpoints(config):
    config.add_route('get_pattern_library', '/get_pattern_library')
    config.add_route('set_pattern',         '/set_pattern/{pattern_id}')
