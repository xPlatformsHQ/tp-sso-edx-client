SSO_TP_BACKEND_NAME = 'sso_tp-oauth2'
LOGIN_URL = '/auth/login/%s/' % SSO_TP_BACKEND_NAME
SOCIAL_AUTH_EXCLUDE_URL_PATTERN = r'^/admin'

# may be not necessary
LMS_SOCIAL_AUTH_SSO_TP_OAUTH2_KEY = os.getenv('LMS_SOCIAL_AUTH_SSO_TP_OAUTH2_KEY', '__place_key_id_here__')
LMS_SOCIAL_AUTH_SSO_TP_OAUTH2_SECRET = os.getenv('LMS_SOCIAL_AUTH_SSO_TP_OAUTH2_SECRET', '__place_secret_id_here__')

# place actual sso url here
SSO_TP_URL = 'http://sso.xplocal.test'
