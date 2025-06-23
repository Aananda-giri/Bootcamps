
# 1. [Video: why everyone's talking about MCP](https://www.youtube.com/watch?v=_d0duu3dED4)

MCP: open standard by anthropic, that allow integration between ai models with external data sources and tools like: github, slack, google-drive, ...

Architecture:
client server architecture with three key components


1. Host: llm service providers like: claude, gemini

2. Client: components within host that establish connection with external servers

  - Roots premitives:
    - provides restricted access to local file system 
    - creating a secure channel for file access: documents, data file, code file
    
  - Sampling Premitive:
    - enable server to request llms help when needed
    - e.g. when analyzing database schema, to generate relevant query for database inference.
  
3. Server: seperate processes that provides context, tools and prompts to these clients.
  - Prompt
    - instruction templates that can be injected into llm context
    - they guide how model should approach certain task or data

  - Resources
    - structured data objects that can be inicluded in llm's context window
    - allow model to reference external information
  
  - Tools
    - executable functions that llm can call to: retrieve information, perform actions outside its context like querying database of modifying files



# video2: [I gave claude access to my server - fireship](https://www.youtube.com/watch?v=HyzlYwjoXOQ)
- official standard for openai agents sdk





## todo:
- learn about openai agents sdk

