import multiprocessing

from pyramid.config import Configurator

from . import routes
from lights import process

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. """
    create_light_process()

    config = Configurator(settings=settings)
    routes.setup(config)
    config.scan()

    return config.make_wsgi_app()



def create_light_process():
    try:                                            #
        multiprocessing.set_start_method('spawn')   #   Need this to prevent crash
    except RuntimeError:                            #
        pass                                        #
    process.light_process_manager.create_process()
    process.light_process_manager.start()