import allure
import pytest
from hamcrest import assert_that


@pytest.mark.json
@pytest.mark.order('last')
@allure.testcase('Write data id', name='Write data id')
@allure.description('Write json data and assert id in it')
def test_write_data_id(server):
    with allure.step('reset json data to default'):
        server.json.reset_data()
    with allure.step('assert default data id'):
        assert_that(server.json.get_data_id(), 'FEFE')
    with allure.step('send test data'):
        test_data = {'status': True, 'data': {'id': 'FFFF', 'some_field': 'some_field_data'}}
        server.json.send_data(test_data)
    with allure.step('assert test data id'):
        assert_that(server.json.get_data_id(), 'FFFF')
