from pyramid.config import Configurator

import multiprocessing
from . import routes

from lights import controller

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
    controller.light_controller.create_process()
    controller.light_controller.start()