# Chapter 2: Harnessing the power of LLM

```
!pip install openai python-dotenv
```

1. `connecting.py`
2. `message_history.py`


## 2.2 open source llms with LM Studio
```
# Install LM studio (manjaro)

sudo pacman -S --needed base-devel git
yay -S lmstudio
```

* search page: download the model
* chat page: loading the model
* server page: serve the model: load the model and click start server button



3. `lmstudio_server.py`
* make sure configurations for server model settings matches the model type


2.3 Prompting with prompt engineering
* not well established science
* organizations like openAI have begain to document a universal set of strategies.

  1. Write clear instructions strategy
    - code: `4_prompt_engineering.py`
    - working
      - list all json files in `prompt/` directory
      - allows user to select prompt file
      - prompts are then submitted to llm and response is printed.

  2. GPT Rubber Ducking:
    - GPT2 talks with itself to clearify things playing different roles. marker that separates different pieces of text.
    - useful way of isolatinig and making llm to focusing on certain part of text. e.g. \`\`\`\<`code`\>\`\`\`
  3. Specifying steps:
    - complex prompts into spep by step instructions the llm can follow
  4. Providing Examples
    - user: tell me about python
    - assistant: python is a high level programming language developed in 1989
    - future replies: The response was only a sentence so limit all future repplies to a single sentence.

    user: --
  5. Specifying output length
    role: system
    content: summarize all replies into 10 or fewer words.
  6. Specifying output format
    role: system
    content: output should be in markdown format.

## LLM Criterias
  - Model performance
  - Model parameters (number of weights) : dictates the hardware (GPU)
  - use  case (model type)
  - training input: Data used for training. (e.g. domain specific mode;)
  - training method: RLHF, fine-tuning, distillation
  - context token size: Size the model may hold (gemini have largest context window. 10M)
  - Model speed: speed at real time in deployment
  - Model cost: project budget (running your llms vs using commercial API)

# Excercises:
  - 1. use connect.py code to use different llm (e.g. gemini)
  - 2. Exploring prompt engineering tactics
    - Experiment with variations of prompts described in 4_prompt_engineering.py
    - document results
  - 3. Downloading and runing an llm wihth LM Studio
    - download LM Studio, connect it to prompt engineering tactics
  - 4. Compare performance of commercial LLM line GPT-4 Turbo with an open source model
    - evaluate on different prompt engineering examples
  - 5. hosting alternatives for LLMS
    - contrast and compare alternatives for hosting an llm vs using commercial model
    - benifit and drawback


# References
* [claude has published their system-prompts](https://docs.anthropic.com/en/release-notes/system-prompts#feb-24th-2025)

* [openai: Best prompt engineering practices](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
* [openai: prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)
* [microsoft: prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering?tabs=chat)