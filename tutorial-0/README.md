* run the server
  * `cd weather-server`
  * `uv run weather.py`

* run the client
  * `cd mcp-client`
  * `uv run client.py`


'''
## Example OutputL
Processing request of type ListToolsRequest

Connected to server with tools: ['get_alerts', 'get_forecast']

MCP Client Started!
Type your queries or 'quit' to exit.

Query: what is the weather line in CA?
DEBUG: Tool get_alerts called with kwargs: {'state': 'CA'}
Processing request of type CallToolRequest
HTTP Request: GET https://api.weather.gov/alerts/active/area/CA "HTTP/1.1 200 OK"

what is the weather line in CA?

[TextContent(type='text', text='\nEvent: Coastal Flood Advisory\nArea: San Francisco; North Bay Interior Valleys; San Francisco Bay Shoreline\nSeverity: Minor\nDescription: * WHAT...Minor coastal flooding expected during nocturnal high\ntide.\n\n* WHERE...Bayshore locations along the San Francisco Bay and San\nPablo Bay.\n\n* WHEN...From 8 PM Monday to 1 AM PDT Tuesday.\n\n* IMPACTS...Flooding of lots, parks, and roads with only\nisolated road closures expected.\n\n* ADDITIONAL DETAILS...Low lying areas within the San Francisco\nBay Area may see minor coastal flooding as a result during\nnocturnal high tide. San Francisco high tide is 7.03 ft at 10:08\nPM Monday.\nInstructions: If travel is required, allow extra time as some roads may be\nclosed. Do not drive around barricades or through water of\nunknown depth. Take the necessary actions to protect flood-prone\nproperty.\n\n---\n\nEvent: Air Quality Alert\nArea: Coachella Valley\nSeverity: Unknown\nDescription: * WHAT...The South Coast AQMD has issued an air quality alert due to\nharmful levels of particle pollution from windblown dust.\n\n* WHERE...in the Coachella Valley. Levels of particle pollution can\nvary by time and location depending on emissions and local weather\nconditions.\n\n* WHEN...from 5 PM Sunday to 8 AM Tuesday.\n\n* IMPACTS... Particle pollution can get deep into the lungs and\ncause serious health problems such as asthma attacks, heart and lung\ndisease symptoms, and increased risk of lung infections. Everyone\ncan be affected, but sensitive groups such as people with lung or\nheart disease, older adults, people who are pregnant, children, and\nthose who spend a lot of time outdoors are at greater risk.\nInstructions: To protect your health, check air quality levels and act as needed:\n\n* When Air Quality Index (AQI) levels are "Unhealthy for Sensitive\nGroups" (orange), sensitive groups as specified above should\nlimit\nextended or intense outdoor activity.\n* When AQI is "Unhealthy" (red), everyone may experience health\nimpacts. Sensitive groups should avoid extended time outdoors.\n* When AQI is "Very Unhealthy" (purple), sensitive groups should\navoid\nall outdoor physical activity. Everyone else should avoid\nextended\nor intense outdoor activity.\n* When AQI is "Hazardous" (maroon), everyone should avoid all\noutdoor\nphysical activity.\n\n* ADDITIONAL DETAILS...\n\nTo help keep indoor air clean when air quality is poor:\n\n* Keep windows and doors closed\n* Run your air conditioner and/or an air purifier\n* Do not use whole house fans or swamp coolers that bring in\noutside\nair if you have other methods to stay cool\n* Avoid other sources of pollution such as fireplaces, candles,\nincense, grilling, and gasoline-powered lawn and garden equipment\n\nTo help minimize outdoor particle pollution levels:\n\n* Carpool, telecommute, reduce trips, or take public transportation\n* Slow down if driving on dirt roads\n* Stabilize loose soils\n\nTo view current and forecasted air quality levels, visit the South\nCoast Air Quality Management District website at aqmd.gov or\ndownload the mobile app at www.aqmd.gov/mobileapp. Additional\ndetails for this air quality alert may be available at\nwww.aqmd.gov/advisory.\n\nFor the latest air quality forecasts and information, visit the\nwebsite at aqmd.gov.\n', annotations=None)]
The current weather conditions in California are as follows:

* Coastal Flood Advisory: Minor coastal flooding is expected during the nocturnal high tide from 8 PM Monday to 1 AM PDT Tuesday. Affected areas include Bayshore locations along the San Francisco Bay and San Pablo Bay. Flooding of lots, parks, and roads with isolated road closures is expected.
* Air Quality Alert: A hazardous air quality alert has been issued for the Coachella Valley due to harmful levels of particle pollution from windblown dust. The alert is in effect from 5 PM Sunday to 8 AM Tuesday.

Residents are advised to take necessary precautions to protect themselves and their property from the flooding, and to minimize their exposure to poor air quality by keeping windows and doors closed, running air conditioners and air purifiers, and avoiding outdoor activities when possible.

Query: 
'''