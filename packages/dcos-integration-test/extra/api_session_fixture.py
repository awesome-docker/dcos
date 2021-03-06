"""This file has only one function: to provide a correctly configured
DcosApiSession object that will be injected into the pytest 'dcos_api_session' fixture
via the make_session_fixture() method
"""
from dcos_test_utils.dcos_api_session import DcosApiSession, DcosUser
from dcos_test_utils.helpers import CI_CREDENTIALS

from test_helpers import expanded_config


def make_session_fixture():
    args = DcosApiSession.get_args_from_env()

    exhibitor_admin_password = None
    if expanded_config['exhibitor_admin_password_enabled'] == 'true':
        exhibitor_admin_password = expanded_config['exhibitor_admin_password']

    dcos_api_session = DcosApiSession(
        auth_user=DcosUser(CI_CREDENTIALS),
        exhibitor_admin_password=exhibitor_admin_password,
        **args)
    dcos_api_session.wait_for_dcos()
    return dcos_api_session
