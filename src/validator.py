import requests
from conf.constants import SUPPORTED_REQUEST_TYPES
from conf.settings import deployStatus


class ENPRequests:
    def __init__(self, endpoint_headers: dict, endpoint_body: dict, url: str, endpoint_path: str, request_type: str,
                 query_params: list):
        self._headers = endpoint_headers
        self._body = endpoint_body
        self._url = url
        self._endpoint_path = endpoint_path
        self._request_type = request_type
        self._query_params = query_params

    def _send_post_request(self):
        from data.mock_response import NotDeployNode
        if deployStatus:
            result = requests.post(
                url="http://" + self._url + self._endpoint_path,
                headers=self._headers,
                params=self._body
            )
        else:
            result = NotDeployNode(
                header=self._headers,
                request_type="POST",
                api_url=self._url,
                api_path=self._endpoint_path,
                api_body=self._body,
                query_params=self._query_params
            ).request_control()
        return result

    def _send_get_request(self):
        from data.mock_response import NotDeployNode
        if deployStatus:
            result = requests.get(
                url="http://" + self._url + self._endpoint_path,
                headers=self._headers,
                params=self._body
            )
        else:
            result = NotDeployNode(
                header=self._headers,
                request_type="GET",
                api_url=self._url,
                api_path=self._endpoint_path,
                api_body=self._body,
                query_params=self._query_params
            ).request_control()
        return result

    def return_request_object(self):
        if self._request_type == "POST":
            return self._send_post_request().request
        elif self._request_type == "GET":
            return self._send_get_request().request
        else:
            raise NotImplementedError("Request type %s is not supported, Supported types are: %s"
                                      % (self._request_type, SUPPORTED_REQUEST_TYPES))

    def return_response_object(self):
        if self._request_type == "POST":
            return self._send_post_request()
        elif self._request_type == "GET":
            return self._send_get_request()
        else:
            raise NotImplementedError("Request type %s is not supported, Supported types are: %s"
                                      % (self._request_type, SUPPORTED_REQUEST_TYPES))


class MakeRequest:
    def __init__(self, header: dict, request_type: str, api_url: str, api_path: str, api_body: dict,
                 query_params: list):
        self.header = header
        self.request_type = request_type
        self.api_url = api_url
        self.api_path = api_path
        self.api_body = api_body
        self.query_params = query_params

    @property
    def request(self):
        return self._endpoint_request.return_request_object()

    @property
    def response(self):
        return self._endpoint_request.return_response_object()

    @property
    def _endpoint_request(self):
        return ENPRequests(
            endpoint_headers=self.header,
            endpoint_body=self.api_body,
            url=self.api_url,
            endpoint_path=self.api_path,
            request_type=self.request_type,
            query_params=self.query_params
        )
