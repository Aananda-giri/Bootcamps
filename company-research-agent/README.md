## basic web research using langGraph
* code: [github](https://github.com/techwithtim/Advanced-Research-Agent)
* video: [youtube](https://www.youtube.com/watch?v=xekw62yQu14)

```
mkdir advanced-agent
cd advanced-agent
uv init .
uv add firecrawl-py langchain langchain-openai langgraph pydantic python-dotenv


# put to .env file
# get firecrawl api key from: https://www.firecrawl.dev/app/api-keys
FIRECRAWL_API_KEY=
OPENAI_API_KEY=


# add main.py code
uv run main.py

# we can research things like: google cloud alternatives.
```
