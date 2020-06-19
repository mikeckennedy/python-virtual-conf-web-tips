from pyramid.config import Configurator


def main(_, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        init_includes(config)
        configure_secure(config)

    return config.make_wsgi_app()


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('.routes')
    config.scan()


def configure_secure(config):
    name = '.infrastructure.secure_tween.set_secure_headers'
    config.add_tween(name)
