# pythonChatbotApi

## Purpose
A simple python api which returns JSON data in the form of {input: ..., response: ..., accuracy: ...}.

I am using this as an educational project.

## Installation
-Clone the repository.
`git clone https://github.com/ragerlu/pythonChatbotApi.git`

## Testing
1. After Installation, the api can be tested by following the below steps.
2. In a terminal running: `python3 main.py`
3. Then going to a browser window and typing `http://127.0.0.1:5000/` into the address bar.
4. You should see 'Test Home Page' in the top left of the page.
5. Finally append `api?input=hello` to the end of the current address in the address bar.

The resulting JSON response should be {input: "hello", response: "Hey there!", accuracy: 1}.
