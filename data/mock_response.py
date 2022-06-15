import responses
from conf.constants import SUPPORTED_PATH_TYPES, SUCCESS, BAD_REQUEST, SUPPORTED_REQUEST_TYPES, MAXIMUM_USERNAME_LENGTH, \
    MAXIMUM_PASSWORD_LENGTH, MINIMUM_PASSWORD_LENGTH, ERROR_CODE
import requests
from src.validator import MakeRequest

"""
POST API_URL/api_path?params=<>
response: {"result: "<result>",
            "user":"info"}
"""


class NotDeployNode(MakeRequest):
    """Mock Response Creator"""

    def request_control(self):
        if self.api_path == "add":
            return self.add_response(*self.query_params)
        elif self.api_path == "subtraction":
            return self.subtraction_response(*self.query_params)
        elif self.api_path == "multiplication":
            return self.multiplication_response(*self.query_params)
        elif self.api_path == "division":
            return self.division_response(*self.query_params)
        elif self.api_path == "sum":
            return self.sum_response(*self.query_params)
        else:
            return self.not_implemented_endpoint_response()

    @responses.activate
    def not_implemented_endpoint_response(self):
        if self.request_type == "POST":
            responses.add(responses.POST, self.api_url, json={}, status=ERROR_CODE)
            return requests.post(self.api_url)
        elif self.request_type == "GET":
            responses.add(responses.GET, self.api_url, json={}, status=ERROR_CODE)
            return requests.get(self.api_url)
        else:
            raise NotImplementedError(f"Not supported request type, supported types are: {SUPPORTED_REQUEST_TYPES}")

    @responses.activate
    def add_response(self, *params):
        add_response_param = 0
        if self.request_type == "POST":
            if not self.header.get("username") or not self.header.get("password"):
                responses.add(responses.POST, self.api_url, json={},
                              status=BAD_REQUEST)
            else:
                if type(self.header.get("username")) == int or \
                        len(str(self.header.get("username"))) >= MAXIMUM_USERNAME_LENGTH or \
                        type(self.header.get("username")) == bool or self.header.get("username") == "TRUE" or \
                        self.header.get("password") == '' or type(self.header.get("password")) == bool or \
                        len(str(self.header.get("password"))) <= MINIMUM_PASSWORD_LENGTH or \
                        self.header.get("password") == "//TRUE":
                    responses.add(responses.POST, self.api_url, json={}, status=ERROR_CODE)
                else:
                    try:
                        for value in params:
                            add_response_param += int(value)
                    except ValueError:
                        responses.add(responses.POST, self.api_url,
                                      json={"result": "Input values must be integer",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)
                    else:
                        responses.add(responses.POST, self.api_url, json={"result": add_response_param,
                                                                       "user": self.header.get("username")}, status=SUCCESS)
            return requests.post(self.api_url)
        elif self.request_type == "GET":
            responses.add(responses.GET, self.api_url, json={}, status=BAD_REQUEST)
            return requests.get(self.api_url)
        else:
            raise NotImplementedError(f"Not supported request type, supported types are: {SUPPORTED_REQUEST_TYPES}")

    @responses.activate
    def multiplication_response(self, *params):
        mult_response_param = 0
        if self.request_type == "POST":
            if not self.header.get("username") or not self.header.get("password"):
                responses.add(responses.POST, self.api_url, json={}, status=BAD_REQUEST)
            else:
                if type(self.header.get("username")) == int or \
                        len(str(self.header.get("username"))) >= MAXIMUM_USERNAME_LENGTH or \
                        type(self.header.get("username")) == bool or self.header.get("username") == "TRUE" or \
                        self.header.get("password") == '' or type(self.header.get("password")) == bool or \
                        len(str(self.header.get("password"))) <= MINIMUM_PASSWORD_LENGTH or \
                        self.header.get("password") == "//TRUE":
                    responses.add(responses.POST, self.api_url, json={}, status=ERROR_CODE)
                else:
                    try:
                        for value in params:
                            mult_response_param *= value
                    except ValueError:
                        responses.add(responses.POST, self.api_url,
                                      json={"result": "Input values must be integer",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)
                    else:
                        responses.add(responses.POST, self.api_url, json={"result": mult_response_param,
                                                                      "user": self.header.get("username")}, status=200)
            return requests.post(self.api_url)
        elif self.request_type == "GET":
            responses.add(responses.GET, self.api_url, json={}, status=BAD_REQUEST)
            return requests.get(self.api_url)
        else:
            raise NotImplementedError(f"Not supported request type, supported types are: {SUPPORTED_REQUEST_TYPES}")

    @responses.activate
    def division_response(self, *params):
        if self.request_type == "POST":
            if not self.header.get("username") or not self.header.get("password"):
                responses.add(responses.POST, self.api_url, json={}, status=BAD_REQUEST)
            else:
                if type(self.header.get("username")) == int or \
                        len(str(self.header.get("username"))) >= MAXIMUM_USERNAME_LENGTH or \
                        type(self.header.get("username")) == bool or self.header.get("username") == "TRUE" or \
                        self.header.get("password") == '' or type(self.header.get("password")) == bool or \
                        len(str(self.header.get("password"))) <= MINIMUM_PASSWORD_LENGTH or \
                        self.header.get("password") == "//TRUE":
                    responses.add(responses.POST, self.api_url, json={}, status=ERROR_CODE)
                else:
                    try:
                        division_response_param = int(params[0]) / int(params[1])
                    except ZeroDivisionError:
                        responses.add(responses.POST, self.api_url,
                                      json={"result": "Zero Division Error, please dont enter second value as 0",
                                                                          "user": self.header.get("username")},
                                      status=ERROR_CODE)
                    except ValueError:
                        responses.add(responses.POST, self.api_url,
                                      json={"result": "Input values must be integer",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)
                    except IndexError:
                        responses.add(responses.POST, self.api_url,
                                      json={"result": "Index out of range",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)

                    else:
                        responses.add(responses.POST, self.api_url, json={"result": division_response_param,
                                                                      "user": self.header.get("username")}, status=200)
            return requests.post(self.api_url)
        elif self.request_type == "GET":
            responses.add(responses.GET, self.api_url, json={}, status=BAD_REQUEST)
            return requests.get(self.api_url)
        else:
            raise NotImplementedError(f"Not supported request type, supported types are: {SUPPORTED_REQUEST_TYPES}")

    @responses.activate
    def subtraction_response(self, *params):
        if self.request_type == "POST":
            if not self.header.get("username") or not self.header.get("password"):
                responses.add(responses.POST, self.api_url, json={}, status=BAD_REQUEST)
            else:
                if type(self.header.get("username")) == int or \
                        len(str(self.header.get("username"))) >= MAXIMUM_USERNAME_LENGTH or \
                        type(self.header.get("username")) == bool or self.header.get("username") == "TRUE" or \
                        self.header.get("password") == '' or type(self.header.get("password")) == bool or \
                        len(str(self.header.get("password"))) <= MINIMUM_PASSWORD_LENGTH or \
                        self.header.get("password") == "//TRUE":
                    responses.add(responses.POST, self.api_url, json={}, status=ERROR_CODE)
                else:
                    try:
                        subs_response_param = int(params[1]) - int(params[0])
                    except ValueError:
                        responses.add(responses.POST, self.api_url,
                                      json={"result": "Input values must be integer",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)
                    except IndexError:
                        responses.add(responses.POST, self.api_url,
                                      json={"result": "Index out of range",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)

                    else:
                        responses.add(responses.POST, self.api_url, json={"result": subs_response_param,
                                                                      "user": self.header.get("username")}, status=200)
            return requests.post(self.api_url)
        elif self.request_type == "GET":
            responses.add(responses.GET, self.api_url, json={}, status=BAD_REQUEST)
            return requests.get(self.api_url)
        else:
            raise NotImplementedError(f"Not supported request type, supported types are: {SUPPORTED_REQUEST_TYPES}")

    @responses.activate
    def sum_response(self, *param):
        sum_response_param = 0
        if self.request_type == "GET":
            if not self.header.get("username") or not self.header.get("password"):
                responses.add(responses.GET, self.api_url, json={}, status=BAD_REQUEST)
            else:
                if type(self.header.get("username")) == int or \
                        len(str(self.header.get("username"))) >= MAXIMUM_USERNAME_LENGTH or \
                        type(self.header.get("username")) == bool or self.header.get("username") == "TRUE" or \
                        self.header.get("password") == '' or type(self.header.get("password")) == bool or \
                        len(str(self.header.get("password"))) <= MINIMUM_PASSWORD_LENGTH or \
                        self.header.get("password") == "//TRUE":
                    responses.add(responses.GET, self.api_url, json={}, status=ERROR_CODE)
                else:
                    try:
                        for i in range(param[0]):
                            sum_response_param += i
                    except ValueError:
                        responses.add(responses.GET, self.api_url,
                                      json={"result": "Input values must be integer",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)
                    except TypeError:
                        responses.add(responses.GET, self.api_url,
                                      json={"result": "Input values must be integer",
                                            "user": self.header.get("username")},
                                      status=ERROR_CODE)

                    else:
                        responses.add(responses.GET, self.api_url, json={"result": sum_response_param,
                                                                     "user": self.header.get("username")}, status=455)
            return requests.get(self.api_url)
        elif self.request_type == "POST":
            responses.add(responses.POST, self.api_url, json={}, status=BAD_REQUEST)
            return requests.post(self.api_url)
        else:
            raise NotImplementedError(f"Not supported request type, supported types are: {SUPPORTED_REQUEST_TYPES}")


"""
test_mock = NotDeployNode(header={"username": "melih", "password": "test"}, request_type="POST", api_url="http://API_TEST", api_path="add",
                          api_body={}, query_params=[1, 2, 3, 7])

print(test_mock.request_control().json())
"""