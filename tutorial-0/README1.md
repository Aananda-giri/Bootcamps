# MCP: Model Context Protocol

## Introduction

🔗 [Read the full introduction](https://modelcontextprotocol.io/introduction)

Model Context Protocol (MCP) standardizes how applications provide context to Large Language Models (LLMs).
Think of it as the **USB-C for AI applications**—a unified way to connect tools and data to LLMs.

* Enables apps to share structured context with LLMs in a consistent format
* Bridges local data sources and external APIs
* Allows tools to be securely invoked via LLMs

### General Architecture

MCP uses a modular client-server architecture:

* **MCP Hosts** – Applications like Claude Desktop, IDEs, or AI tools that want to access data via MCP
* **MCP Clients** – Lightweight agents that maintain direct 1:1 connections with servers
* **MCP Servers** – Modular programs that expose capabilities (like data or tools) using the MCP protocol
* **Local Data Sources** – Files, databases, and services on the user's machine
* **Remote Services** – External APIs and internet-connected systems that MCP servers can interact with

---

## For Server Developers

🔗 [Server Quickstart Guide](https://modelcontextprotocol.io/quickstart/server)

When building an MCP server, you define:

* **Resources** – File-like data streams (e.g., API responses, local file contents)
* **Tools** – Functions that can be invoked by the LLM (with user permission)
* **Prompts** – Predefined, reusable task templates designed to guide the model

### Example Tools

* `get-alerts`: Retrieve recent system or application alerts
* `get-forecast`: Access weather or other predictive data

