install this as requirement to /edx/app/edxapp/venvs/edxapp venv
pip install -e git+https://github.com/xPlatformsHQ/tp-sso-edx-client.git@e307f066f64da6aa5cd02e4183160745d07f2bb7#egg=sso_edx_tp
(or later commit from lilac branch)

change etc/lms.yml and app/edxapp/edx-platform/lms/envs/common.py
accordingly to config_example

configure plugin as shown at plugin_config_example.png image:
http://edx.test.site/admin/third_party_auth/oauth2providerconfig/

configure SSO client as shown at sso_side_config_example.png image:
http://sso.test.site/admin/oauth2/client/

restart lms

maybe it will work )

notes up to 2021-08-08:
1. login_analytics function in /edx/app/edxapp/edx-platform/common/djangoapps/third_party_auth/pipeline.py
   needs to be patched like this: https://gist.github.com/leon-id/bc1231589254c036fb5df4883b6bf7aa
   in order to allow tracking cases when user is not defined (before auth is not finished)
   in hawthorn this was not called at all if settings.LMS_SEGMENT_KEY was not set
2. logout does not work, you need to delete cookies by hand (should be fixed of course)
