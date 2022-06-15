ADD_DATA = [
    ([1, 2], 3),

]

SUB_DATA = [
    [(3, 2), 1],

]

DIV_DATA = [
    [(4, 2), 2],

]

MULT_DATA = [
    [(1, 2), 2],

]

SUM_DATA = [
    [4, 6],
    [0, 0]

]

ERROR_DATA = [
    "errorstring",
    "1",
    (1, 2, 3, 4, 5, 6),
    "false",
    "true",
    False,
    True,
    "//",
    "#",
]

INVALID_USER_VALID_PASS_DATA = [
    (True, "1234a"),
    ("TRUE", "testerTester1"),
    ("iamverylonginputdata123iamverylonginputdata123iamverylonginputdata123iamverylonginputdata123iamverylonginputdata123", "SoftwareTester123"),
    (123, "@€>£#1232a")
]

VALID_USER_INVALID_PASS_DATA = [
    ("melihcelik123", " "),
    ("tryingtowriteTests", "short"),
    ("tester_321", True),
    ("iAmValidUsername__", "//TRUE")
]
INVALID_HEADER_DATA = [
    True,
    "TRUE",
    "iamverylonginputdata123iamverylonginputdata123iamverylonginputdata123iamverylonginputdata123iamverylonginputdata123",
    123
]

VALID_PASSWORD_DATA = [
    "123234a",
    "testerTester",
    "SoftwareTest123"
    "!'^@@Test"
]

INVALID_PASSWORD_DATA = [
    "",
    "short",
    True,
    "//TRUE"
]

VALID_HEADER_DATA = [
    "melihcelik123",
    "tryingtowriteTests",
    "tester_321",
    "iAmValidUsername__"
]

INVALID_PATH_DATA = [
    "test",
    "123",
    1,
    True,
    "sub"
]

INVALID_REQUEST_TYPE_DATA = [
    "PUT",
    "PATCH",
    "DELETE"
]