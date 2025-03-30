# Ch.5 Empowering Agents with actions

- SK to host our first agent system
- ChatGPT Plugins: proxies for actions
  - plutin encapsulates one or more abilities like calling an API, scraping a website
  - Actions are therefore extensions of plugins - they give plugin its abilities.
    Action: Anything an agent can do
- Openai introduced interface between functions/plugins an llm cound action.

## adding function to LLM api call

```q
response = client.chat.completions.create(
    model="gpt4-1006-preview"
)
```

## Sample request flow

- user: makes a request to llm using tools
- GPT: selects function to call and generates parameters
- Execute function with parameters
- GPT:
  - input: conversation with result of function execution
  - output: returns response in natural language.

# Semantic kernel

- open source project from microsoft to build ai applications we call agents.
- used to define actions (called semantic plugins) which is wrapper for skills and functions.
- functional model: known as skills or plugins

## Semantic kernal as interactive service agent.

- TMDB api key (www.themoviedb.org)
- sk can create plugins for us automatically.
-

* `plugins/Movies/tmdb.py`
* testing: `6_test_tmdb_service.py`: uncomment one at a time.

# References

- [code](https://github.com/cxbxmxcx/GPT-Agents/tree/main/chapter_05)
-
