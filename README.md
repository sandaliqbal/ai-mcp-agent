# 🧠 AI MCP Agent

A minimal, extensible **Model Context Protocol (MCP) agent** written in Python.  
The MCP server provides tools to integrate with you-tube APIs and extract transcripts.
Also has tools to write a blog, write social post and video chapters.
This project provides a simple foundation to build custom AI-powered agents that communicate using MCP, expose tools, 
and run inside your own server environment.

---

## 🚀 Features

- ✔️ Custom Python-based MCP server  
- ✔️ Pluggable agent logic via `main.py`  
- ✔️ Modern Python project structure (`pyproject.toml`, uv/Poetry compatible)  
- ✔️ Easy to extend with tools, workflows, or integrations  
- ✔️ Lightweight & ideal for experimentation with agentic systems  

---

## 📂 Project Structure

```text
ai-mcp-agent/
├── main.py             # Entry point for running the MCP agent/server
├── mcp-server/         # Custom MCP server implementation
│   ├── prompts         # Prompts for extracting transcripts from you-tube video
│   └── server.py       # MCP server code
├── pyproject.toml      # Python dependencies + project metadata
├── uv.lock             # Locked dependency versions
├── .python-version     # Python version pin
├── .gitignore
└── README.md
```
## 🛠️ Getting Started

```bash
uv sync
```

## ▶️ Running the Server

```bash
python main.py
```

## 🙋 About

Created by Sandal Iqbal
References from @ShawhinT tutorials
