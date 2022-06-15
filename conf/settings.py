import os
import yaml

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_PATH, "conf/config.yaml")

with open(CONFIG_PATH, 'r') as f:
    conf_yaml = yaml.safe_load(f)
    deployStatus = conf_yaml.get("deploy").get("status")


