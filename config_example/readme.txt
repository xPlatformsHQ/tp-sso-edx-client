install this as requirement to /edx/app/edxapp/venvs/edxapp  venv
pip install -e git+https://github.com/xPlatformsHQ/tp-sso-edx-client.git@a2931ef647cb98663ca2b4cc0fd3c4cb45298b88#egg=sso_edx_tp
(or later commit from lilac branch)

change etc/lms.yml and app/edxapp/edx-platform/lms/envs/common.py
accordingly to config_example

config plugin as described at png image:
http://edx.site/admin/third_party_auth/oauth2providerconfig/

maybe it will work )
