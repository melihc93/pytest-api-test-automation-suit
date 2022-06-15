from conf.constants import TEST_HEADERS
from src.validator import MakeRequest


class Endpoints:
    def __init__(self, endpoint_name: str):
        self.api_url = None
        self.header = TEST_HEADERS
        self.api_path = None
        self.request_type = endpoint_name
        self.api_body = None
        self.query_params = None

    def __make_request(self):
        return MakeRequest(
                header=self.header,
                request_type=self.request_type,
                api_url=self.api_url,
                api_path=self.api_path,
                api_body=self.api_body,
                query_params=self.query_params
        )

    @property
    def get_response(self):
        return self.__make_request().response

    @property
    def get_request(self):
        return self.__make_request().request
