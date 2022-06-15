Scenario:

- Only GET and POST requests
- user-endpoint and should use login feature and headers
- header should contain username and password, otherwise api should return "bad request"
- api endpoints:
  - ADD
  - SUBSTRACTION
  - MULTIPLICATION
  - DIVISION
- endpoint should like following template
        

    <query>?params=

- response should like following template


    result = <result>, user= <info>

- maximum 5 parameter should be entered via POST requests
- sum endpoint should get 1 input parameter and return sum of numbers from 1 to input parameter, GET request should be used for sum endpoint

#Examples

    request: POST API_URL/add?params=1,2
    
    response: result = 3, user=info
---
    request: POST API_URL/multiplication?params=3,2,3

    response: result = 18, user=info
---
    request: POST API_URL/division?params=55,11
    
    response: result= 5, user=info
---
    request: GET API_URL/sum?params=4

    response: result= 24, user=info
---
    request: GET API_URL/sum?params=5

    response: result= 120, user=info