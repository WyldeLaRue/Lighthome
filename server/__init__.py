from pyramid.config import Configurator

from lights import process
from . import routes


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. """

    
    light_queue = process.create_light_controller_process()

    config = Configurator(settings=settings)
    routes.setup(config)
    config.scan()

    return config.make_wsgi_app()
