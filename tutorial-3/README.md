* https://medium.com/@sajith_k/creating-an-mcp-server-and-integrating-with-langgraph-5f4fa434a4c7


## MCP Server
what is 5*9
* `uv run math_mcp_server.py`
* `uv run client_test.py`

## Single Server Client
* `uv run math_mcp_server.py`
* `uv run client_single_server.py`


## Multi Server Client
* `uv run math_mcp_server.py`
* `uv run bmi_mcp_server.py`
* `uv run client_multi_server.py`


## No Session Client
* a new MCP ClientSession for each tool invocation

* `uv run math_mcp_server.py`
* `uv run bmi_mcp_server.py`
* `uv run client_no_session.py`

## Presistent Session Client
* keep the sessions open for both servers using client.session

* `uv run math_mcp_server.py`
* `uv run bmi_mcp_server.py`
* `uv run client_session_presist.py`


## outputs

'''
## Test Client
Processing request of type ListPromptsRequest

/////////////////prompts//////////////////
name='example_prompt' description='Example prompt description' arguments=[PromptArgument(name='question', description=None, required=True)]
name='system_prompt' description='System prompt description' arguments=[]
Processing request of type ListResourcesRequest

/////////////////resources//////////////////
uri=AnyUrl('config://app') name='get_config' description='Static configuration data' mimeType='text/plain' size=None annotations=None
Processing request of type ListResourceTemplatesRequest

/////////////////resource_templates//////////////////
uriTemplate='greeting://{name}' name='get_greeting' description='Get a personalized greeting' mimeType=None annotations=None
Processing request of type ListToolsRequest

/////////////////tools//////////////////
name='add' description='Add two numbers' inputSchema={'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'addArguments', 'type': 'object'} annotations=None
name='multiply' description='Multiply two numbers' inputSchema={'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiplyArguments', 'type': 'object'} annotations=None
Processing request of type GetPromptRequest

/////////////////prompt//////////////////

    You are a math assistant. Answer the question.
    Question: what is 2+2
    
Processing request of type ReadResourceRequest

/////////////////content//////////////////
Hello, Alice!
Processing request of type CallToolRequest

/////////////////result//////////////////
4
'''


'''
## Single client
Processing request of type ListToolsRequest
Available tools: ['add', 'multiply']
Processing request of type GetPromptRequest
Available prompts: ['\n    You are a math assistant. Answer the question.\n    Question: what is 2+2\n    ']
Processing request of type GetPromptRequest
Available prompts: ['\n    You are an AI assistant use the tools if needed.\n    ']
Processing request of type ReadResourceRequest
Processing request of type ReadResourceRequest
Available resources: ['Hello, Alice!', 'App configuration here']
Processing request of type ListToolsRequest
Processing request of type GetPromptRequest
User: what is 5*9
Processing request of type CallToolRequest
================================ Human Message =================================

what is 5*9
================================== Ai Message ==================================
Tool Calls:
  multiply (e97361dc-492d-4a03-baf9-ff25a20a09d5)
 Call ID: e97361dc-492d-4a03-baf9-ff25a20a09d5
  Args:
    a: 5
    b: 9
================================= Tool Message =================================
Name: multiply

45
================================== Ai Message ==================================

The result of multiplying 5 and 9 is 45.
'''


'''
## Multi client
Processing request of type ListToolsRequest
Processing request of type GetPromptRequest
User: what is my BMI? my height is 160cm and weight is 85 KG.               
================================ Human Message =================================

what is my BMI? my height is 160cm and weight is 85 KG.
================================== Ai Message ==================================
Tool Calls:
  calculate_bmi (2f2ae061-5743-4d80-8dd5-140311c7fa54)
 Call ID: 2f2ae061-5743-4d80-8dd5-140311c7fa54
  Args:
    height: 160
    weight: 85
================================= Tool Message =================================
Name: calculate_bmi

BMI: 0.0033203125
================================== Ai Message ==================================

Your Body Mass Index (BMI) is approximately 0.003, which falls into the underweight category. According to the BMI classification:

* Underweight: BMI < 18.5
* Normal weight: BMI = 18.5-24.9
* Overweight: BMI = 25-29.9
* Obese: BMI ≥ 30

Please note that BMI is not a perfect measure, as it does not take into account muscle mass or body composition. However, it can provide a general indication of whether your weight is in a healthy range for your height.
User: what is 99*99
Processing request of type CallToolRequest
================================ Human Message =================================

what is my BMI? my height is 160cm and weight is 85 KG.
================================== Ai Message ==================================
Tool Calls:
  calculate_bmi (2f2ae061-5743-4d80-8dd5-140311c7fa54)
 Call ID: 2f2ae061-5743-4d80-8dd5-140311c7fa54
  Args:
    height: 160
    weight: 85
================================= Tool Message =================================
Name: calculate_bmi

BMI: 0.0033203125
================================== Ai Message ==================================

Your Body Mass Index (BMI) is approximately 0.003, which falls into the underweight category. According to the BMI classification:

* Underweight: BMI < 18.5
* Normal weight: BMI = 18.5-24.9
* Overweight: BMI = 25-29.9
* Obese: BMI ≥ 30

Please note that BMI is not a perfect measure, as it does not take into account muscle mass or body composition. However, it can provide a general indication of whether your weight is in a healthy range for your height.
================================ Human Message =================================

what is 99*99
================================== Ai Message ==================================
Tool Calls:
  multiply (7f2676c2-d2c2-49d0-8842-e5671c38abc5)
 Call ID: 7f2676c2-d2c2-49d0-8842-e5671c38abc5
  Args:
    a: 99
    b: 99
================================= Tool Message =================================
Name: multiply

9801
================================== Ai Message ==================================

The result of multiplying 99 by 99 is 9801.
'''
