import pytest
from conf.constants import TEST_HEADERS
from src.endpoint_init import Endpoints
from conf.settings import conf_yaml
from tests.test_data import ADD_DATA, ERROR_DATA,\
    INVALID_PATH_DATA, INVALID_REQUEST_TYPE_DATA, SUB_DATA, \
    MULT_DATA, DIV_DATA, VALID_USER_INVALID_PASS_DATA, INVALID_USER_VALID_PASS_DATA, SUM_DATA
from conf.constants import BAD_REQUEST, SUCCESS, ERROR_CODE
import allure


@allure.feature('Post Feature')
class TestPost:
    test_endpoint = Endpoints(endpoint_name="POST")
    config_url = conf_yaml.get("endpoint_conf").get("ip_port")

    @pytest.fixture(autouse=True)
    def clear_test_datas(self):
        self.test_endpoint.request_type = "POST"
        yield
        self.test_endpoint.request_type = None

    @pytest.mark.parametrize("query_params, expected", ADD_DATA)
    def test_add_endpoint_is_working_successfully(self, query_params, expected):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = query_params
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == expected

    def test_non_header_returns_bad_request(self):
        self.test_endpoint.header = {
            "username": "melih"
        }
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [1]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == BAD_REQUEST

    @pytest.mark.parametrize("query_params", ERROR_DATA)
    def test_add_endpoint_returns_error_when_input_parameters_out_of_scope(self, query_params):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [query_params]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    def test_add_path_not_support_get_request(self):
        self.test_endpoint.request_type = "GET"
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [1, 2, 3]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == BAD_REQUEST

    def test_add_return_successfully_code_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [1, 2, 3, 4, 5]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == SUCCESS

    def test_add_return_user_inside_response_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [1, 2, 3, 4, 5]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["user"] == self.test_endpoint.header["username"]

    @pytest.mark.parametrize("invalid_username, valid_password", INVALID_USER_VALID_PASS_DATA)
    def test_add_response_return_error_code_when_user_input_invalid_username(self, invalid_username, valid_password):
        self.test_endpoint.header = {
            "username": invalid_username,
            "password": valid_password
        }
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [1, 2, 1232, -322]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("valid_username, invalid_password", VALID_USER_INVALID_PASS_DATA)
    def test_add_response_return_error_code_when_user_input_invalid_password(self, valid_username, invalid_password):
        self.test_endpoint.header = {
            "username": valid_username,
            "password": invalid_password
        }
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [122, 2, 1232, -322]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("invalid_path", INVALID_PATH_DATA)
    def test_sending_unsupported_path(self, invalid_path):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = invalid_path
        self.test_endpoint.query_params = [23, 32]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("invalid_request_type", INVALID_REQUEST_TYPE_DATA)
    def test_sending_unsupported_request_type(self, invalid_request_type):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.request_type = invalid_request_type
        self.test_endpoint.api_path = "add"
        self.test_endpoint.query_params = [123, -322]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("valid_user, invalid_pass", VALID_USER_INVALID_PASS_DATA)
    def test_subtraction_response_return_error_code_when_user_input_invalid_password(self, valid_user, invalid_pass):
        self.test_endpoint.header = {
            "username": valid_user,
            "password": invalid_pass
        }
        self.test_endpoint.api_path = "subtraction"
        self.test_endpoint.query_params = [654, -44, 3222, 44]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params", ERROR_DATA)
    def test_subtraction_endpoint_returns_error_when_input_parameters_out_of_scope(self, query_params):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "subtraction"
        self.test_endpoint.query_params = [query_params]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    def test_subtraction_path_not_support_get_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "subtraction"
        self.test_endpoint.query_params = [23, 2]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == BAD_REQUEST

    def test_subtraction_return_successfully_code_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "subtraction"
        self.test_endpoint.query_params = [1, 2, 3, 4, 5]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == SUCCESS

    def test_subtraction_return_user_inside_response_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "subtraction"
        self.test_endpoint.query_params = [754, 56, -1232]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["user"] == self.test_endpoint.header["username"]

    @pytest.mark.parametrize("invalid_user, valid_pass", INVALID_USER_VALID_PASS_DATA)
    def test_subtraction_response_return_error_code_when_user_input_invalid_username(self, invalid_user, valid_pass):
        self.test_endpoint.header = {
            "username": invalid_user,
            "password": valid_pass
        }
        self.test_endpoint.api_path = "subtraction"
        self.test_endpoint.query_params = [22, 123]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params, expected", SUB_DATA)
    def test_subtraction_endpoint_is_working_successfully(self, query_params, expected):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "subtraction"
        self.test_endpoint.query_params = query_params
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == expected

    @pytest.mark.parametrize("valid_user, invalid_pass", VALID_USER_INVALID_PASS_DATA)
    def test_multiplication_response_return_error_code_when_user_input_invalid_password(self, valid_user, invalid_pass):
        self.test_endpoint.header = {
            "username": valid_user,
            "password": invalid_pass
        }
        self.test_endpoint.api_path = "multiplication"
        self.test_endpoint.query_params = [1, 0, 1123222, -3255]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params", ERROR_DATA)
    def test_multiplication_endpoint_returns_error_when_input_parameters_out_of_scope(self, query_params):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "multiplication"
        self.test_endpoint.query_params = [query_params]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    def test_multiplication_path_not_support_get_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "multiplication"
        self.test_endpoint.query_params = [2181129, 1993]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == BAD_REQUEST

    def test_multiplication_return_successfully_code_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "multiplication"
        self.test_endpoint.query_params = [233]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == SUCCESS

    def test_multiplication_return_user_inside_response_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "multiplication"
        self.test_endpoint.query_params = [-1, 1, 1]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["user"] == self.test_endpoint.header["username"]

    @pytest.mark.parametrize("invalid_user, valid_pass", INVALID_USER_VALID_PASS_DATA)
    def test_multiplication_response_return_error_code_when_user_input_invalid_username(self, invalid_user, valid_pass):
        self.test_endpoint.header = {
            "username": invalid_user,
            "password": valid_pass
        }
        self.test_endpoint.api_path = "multiplication"
        self.test_endpoint.query_params = [0, 1]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params, expected", MULT_DATA)
    def test_multiplication_endpoint_is_working_successfully(self, query_params, expected):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "multiplication"
        self.test_endpoint.query_params = query_params
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == expected

    @pytest.mark.parametrize("valid_user, invalid_pass", VALID_USER_INVALID_PASS_DATA)
    def test_division_response_return_error_code_when_user_input_invalid_password(self, valid_user, invalid_pass):
        self.test_endpoint.header = {
            "username": valid_user,
            "password": invalid_pass
        }
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = [23, 3]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params", ERROR_DATA)
    def test_division_endpoint_returns_error_when_input_parameters_out_of_scope(self, query_params):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = [query_params]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    def test_division_path_not_support_get_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = [0, 22]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == BAD_REQUEST

    def test_division_return_successfully_code_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = [2]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == SUCCESS

    def test_division_return_user_inside_response_for_valid_request(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = [-1, 1, 1]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["user"] == self.test_endpoint.header["username"]

    @pytest.mark.parametrize("invalid_user, valid_pass", INVALID_USER_VALID_PASS_DATA)
    def test_division_response_return_error_code_when_user_input_invalid_username(self, invalid_user, valid_pass):
        self.test_endpoint.header = {
            "username": invalid_user,
            "password": valid_pass
        }
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = [0, 1]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params, expected", DIV_DATA)
    def test_division_endpoint_is_working_successfully(self, query_params, expected):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = query_params
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == expected

    def test_division_endpoint_return_zero_division_error(self):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "division"
        self.test_endpoint.query_params = [22, 0]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == ERROR_CODE


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
        self.test_endpoint.query_params = [query_params]
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
        self.test_endpoint.query_params = [22]
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.status_code == ERROR_CODE

    @pytest.mark.parametrize("query_params, expected", SUM_DATA)
    def test_sum_endpoint_is_working_successfully(self, query_params, expected):
        self.test_endpoint.header = TEST_HEADERS
        self.test_endpoint.api_path = "sum"
        self.test_endpoint.query_params = query_params
        self.test_endpoint.api_url = self.config_url
        assert self.test_endpoint.get_response.json()["result"] == expected

