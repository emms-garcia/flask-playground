import os

DATABASE = 'DATABASE'
PASSWORD = 'PASSWORD'
SECRET_KEY = 'SECRET_KEY'
USERNAME = 'USERNAME'

CONFIG = {
    'DEVELOPMENT': {
        DATABASE: 'quickstart.db',
        PASSWORD: 'default'
        SECRET_KEY: 'WOWSOKEYMUCHSECRETWOW',
        USERNAME: 'admin',
    },
    'PRODUCTION': {
        # Nothing here yet.
    }
}
