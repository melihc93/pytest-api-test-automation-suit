# HTTP Request Constants
SUCCESS = 200
BAD_REQUEST = 400
ERROR_CODE = 123  # will be implemented later

# Validations
SUPPORTED_REQUEST_TYPES = ["POST", "GET"]
SUPPORTED_PATH_TYPES = {
    "API_URL": ["add", "subs", "mult", "div", "sum"]
}

# HEADER
TEST_HEADERS = {
    "username": "not_defined",
    "password": "not_defined"
}

# Username and Password
MAXIMUM_USERNAME_LENGTH = 14
MAXIMUM_PASSWORD_LENGTH = 14
MINIMUM_PASSWORD_LENGTH = 7
