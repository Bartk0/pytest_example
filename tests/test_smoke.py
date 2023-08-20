import allure
import pytest
from hamcrest import assert_that
from helpers.server_api import DataConsts, ApiConsts


@pytest.mark.smoke
@pytest.mark.order('first')
@allure.testcase('Smoke test', name='Smoke test')
@allure.description('Asserts invalid path response data')
def test_smoke(server):
    with allure.step('request invalid path'):
        response_data = server.common.get_invalid_path()
    with allure.step('assert server response'):
        assert_that(response_data[ApiConsts.MSG], DataConsts.RESPONSE_UNKNOWN_PATH)
