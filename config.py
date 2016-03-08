import os

try:
    from local_config import *

except ImportError:

    twilio_sid = os.environ.get('TWILIO_SID', '')
    twilio_token = os.environ.get('TWILIO_TOKEN', '')
    twilio_number = os.environ.get('TWILIO_NUMBER', '')

    fieldbook_user = os.environ.get('FIELDBOOK_USER', '')
    fieldbook_pass = os.environ.get('FIELDBOOK_PASS', '')
    fieldbook_url = os.environ.get('FIELDBOOK_URL', '')

    website_user = os.environ.get('WEBSITE_USER', 'user')
    website_pass = os.environ.get('WEBSITE_PASS', 'pass')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME', 'slot-session')

    CACHE_REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    CACHE_DEFAULT_TIMEOUT = int(os.getenv('CACHE_DEFAULT_TIMEOUT', '300'))

    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

    # We need the following variables to be boolean so we just check for a value against the environment variable
    # to mean True and then take absence of either a value or the variable to mean False

    demo_mode = bool(os.environ.get('DEMO_MODE', False))

    debug_mode = bool(os.environ.get('DEBUG_MODE', False))