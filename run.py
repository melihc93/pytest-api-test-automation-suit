from argparse import RawDescriptionHelpFormatter
import argparse
import pytest
from conf.settings import conf_yaml

# Parse operations will develop later on
parser = argparse.ArgumentParser(
    description="TRENDYOL API CASE\n"
                "Version: {0}\n"
                "This program runs provided Trendyol-API-Study-Case Scenarios.\n".format((conf_yaml["api_test"]["version"])),
    formatter_class=RawDescriptionHelpFormatter
)

parser.add_argument(
    "-d",
    "--deploy_status",
    type=str,
    help="is the code deployed to proper environment or not, default: True",
    default=True
)

args = parser.parse_args()
pytest.main(["tests/test_post.py", "--alluredir=allure-report/"])

