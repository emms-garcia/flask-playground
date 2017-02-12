import logging
import os
from werkzeug.serving import run_simple

from playground import app

is_dev = (os.environ.get('ENVIRONMENT').upper() == 'DEVELOPMENT')
logging.basicConfig(level=logging.DEBUG if is_dev else logging.INFO)

if __name__ == '__main__':
    run_simple('0.0.0.0', 8080, app, use_reloader=is_dev)
