from src.endpoint_init import Endpoints
from conf.settings import conf_yaml
import pytest
from conf.constants import TEST_HEADERS
from tests.test_data import SUM_DATA, ERROR_DATA, VALID_USER_INVALID_PASS_DATA, \
    INVALID_USER_VALID_PASS_DATA
from conf.constants import BAD_REQUEST, SUCCESS, ERROR_CODE
import allure


@allure.feature('Get Feature')
class TestGet:
    test_endpoint = Endpoints(endpoint_name="GET")
    config_url = conf_yaml.get("endpoint_conf").get("ip_port")

    @pytest.fixture(autouse=True)
    def clear_test_datas(self):
        self.test_endpoint.request_type = "GET"
        yield
        self.test_endpoint.request_type = None

    def test_non_header_returns_bad_request(self):
        self.test_endpoint.header = {
            "username": "melih"
        }
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = [12]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == 400

    @pytest.mark.parametrize("valid_user, invalid_pass", VALID_USER_INVALID_PASS_DATA)
    def test_sum_response_return_error_code_when_user_input_invalid_password(self, valid_user, invalid_pass):
        self.test_endpoint.header = {
            "username": valid_user,
            "password": invalid_pass
        }
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = [23]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params", ERROR_DATA)
    def test_sum_endpoint_returns_error_when_input_parameters_out_of_scope(self, query_params):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = query_params
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    def test_sum_path_not_support_post_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = [2]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == BAD_REQUEST

    def test_sum_return_successfully_code_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = [2]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == SUCCESS

    def test_sum_return_user_inside_response_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = [12]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["user"] == self.test_endpoint.header["username"]

    @pytest.mark.parametrize("invalid_user, valid_pass", INVALID_USER_VALID_PASS_DATA)
    def test_sum_response_return_error_code_when_user_input_invalid_username(self, invalid_user, valid_pass):
        self.test_endpoint.header = {
            "username": invalid_user,
            "password": valid_pass
        }
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = [0, 1]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params, expected", SUM_DATA)
    def test_sum_endpoint_is_working_successfully(self, query_params, expected):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = query_params
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == expected

    def test_sum_endpoint_return_zero_division_error(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = [22, 0]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == ERROR_CODE
