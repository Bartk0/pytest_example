import allure
import pytest
from hamcrest import assert_that
from helpers.server_api import ApiConsts
from re import findall


@pytest.mark.common
@pytest.mark.order('last')
@allure.testcase('Check server paths', name='Check server paths')
@allure.description('Checks available server paths list')
def test_get_available_paths(server):
    with allure.step('assert available paths'):
        assert_that(findall(r'/[a-z]*', server.common.get_invalid_path()[ApiConsts.MSG]),
                    server.common.get_valid_paths_list())
