import allure
import pytest
from hamcrest import assert_that, equal_to
from helpers.server_api import DataConsts


@pytest.mark.xml
@pytest.mark.order('last')
@allure.testcase('Write data id', name='Write data id')
@allure.description('Write xml data and assert id in it')
def test_write_empty_data(server):
    with allure.step('reset json data to default'):
        server.xml.reset_data()
    with allure.step('assert default data id'):
        assert_that(server.xml.read_data(), DataConsts.XML_DEFAULT)
    with allure.step('send empty test data'):
        test_data = ''
        server.xml.send_data(test_data)
    with allure.step('assert empty data'):
        assert_that(server.xml.read_data(), equal_to(''))
