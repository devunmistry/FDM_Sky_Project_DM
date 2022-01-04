from unittest import mock
import pytest

from sky_project import Router

@pytest.fixture
def router_a():
    router_a = Router()
    return router_a


def test_Router_createsRouterObject_whenRouterObjectInstantiated(router_a):
    router = Router()
    result = isinstance(router, Router)
    assert result == True

def test_configureLoopback_callsNcclientManagerConnectssh_whenConfigureLoopbackCalled2(router_a):
    with mock.patch("sky_project.manager") as mocked__manager: #at instance where manager called, replaced with mock
        router = Router()
        router.configure_loopback()
        result = mocked__manager.connect_ssh.assert_called_once_with(
            host='192.168.0.101',
            port='830', username='cisco',
            password='cisco',
            hostkey_verify=False,
            device_params={'name': 'csr'}) #asserts if mocked manager.connect_ssh called with correct arguements
        assert result == None