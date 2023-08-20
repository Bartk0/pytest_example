import pytest
from collections import namedtuple
from helpers.config import Config, CfgPath, Options
from helpers.server_api import XML, JSON, CommonMethods


@pytest.fixture(scope='session', autouse=True)
def init():
    Config()


def pytest_addoption(parser):
    parser.addoption(Options.SERVER_ADDRESS, action="store", default='', type=str,
                     help="base_http hostname or IP address")
    parser.addoption(Options.SERVER_PORT, action="store", default='', type=str, help="base_http port")


@pytest.fixture(scope='session')
def console_options(request):
    options = namedtuple('options', ['host', 'port'])
    host = request.config.getoption(Options.SERVER_ADDRESS)
    port = request.config.getoption(Options.SERVER_PORT)
    return options(host=host, port=port)


@pytest.fixture(scope='session', autouse=True)
def server(console_options):
    server = namedtuple('options', ['host', 'port', 'xml', 'json', 'common'])
    if not console_options.host == '':
        host = console_options.host
    else:
        host = Config.get_raw_value(CfgPath.SERVER_ADDRESS)

    if not console_options.port == '':
        port = console_options.port
    else:
        port = Config.get_raw_value(CfgPath.SERVER_PORT)

    xml = XML(host, port)
    json = JSON(host, port)
    common = CommonMethods(host, port)
    return server(host=host, port=port, xml=xml, json=json, common=common)


@pytest.fixture(scope='session', autouse=True)
def reset_server_data(server):
    pass
    yield
    server.xml.reset_data()
    server.json.reset_data()
