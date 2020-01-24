from os import environ
from buba import Buba

if __name__ == '__main__':
    config = Buba(env_name='APP_ENV', prefix='CONFIG', splitter='::')
    assert config.app_name == 'my_app'
    assert config.db.host == 'localhost_default'
    assert config.db.user == 'user_development'
    assert config.db.password == 'password_development'

    environ['APP_ENV'] = 'production'
    config.load()

    assert config.app_name == 'my_app'
    assert config.db.host == 'localhost_default'
    assert config.db.user == 'user_production'
    assert config.db.password == 'password_production'

    environ['APP_ENV'] = 'production'
    environ['CONFIG::DB::HOST'] = 'production_host'
    environ['CONFIG::APP_NAME'] = 'production_app_name'
    config.load()

    assert config.app_name == 'production_app_name'
    assert config.db.host == 'production_host'
    assert config.db.user == 'user_production'
    assert config.db.password == 'password_production'
