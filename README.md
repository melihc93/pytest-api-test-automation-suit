# pytest-api-test-automation-suit
This repo created for doing some exercises with pytest test framework.



## Starting Tests

1. First install requirements by:`pip install -r requirements.txt`
2. In order to start tests use following command:`py run.py`
NOTE: suit created, cases added, data/mock_response.py should be modified in order to handle different kind of resquests.


### Reminder to me: run.py should include other starting argumens like: @sanity, @regression, @post, @get AND generate more cases

#### neccesary features list:
+ get docker image of project
+ create docker container for proper image of test suit
+ jenkins entegration for git repo for following feature:
  + git pull
  + docker compose - up
  + starting tests
+ create dummy back-end in docker container and synchronise its main branch with jenkins trigger
+ create jenkins pipe-line for:
  + when dummy-backend master branch pushed by any
    + git pull master/origin <dummy-backend>
    + docker compose and up <dummy-backend>
    + git pull main/api-python <test-repo>
    + docker compose and up <test-repo>
    + start tests
    + post-action: allure report
    + pytest: automatic issue reporter


# Modify and make pretty: readme.md, check code-readability, OOP