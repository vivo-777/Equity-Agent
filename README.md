# 🤖 AI Equity Research Agent

**An autonomous, multi-agent financial analysis system powered by Llama 3, LangGraph, and Streamlit.**

[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=flat&logo=render&logoColor=white)](https://ai-hedge-fund.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_Workflow-2E3133?style=flat)](https://langchain-ai.github.io/langgraph/)

---

## 📖 Overview

The **AI Equity Research Agent** is a sophisticated financial analysis tool designed to simulate the workflow of a human hedge fund analyst. Unlike simple chatbots, this application uses an **agentic workflow** to:

1.  **Gather Real-Time Data:** Fetches live prices, technical indicators, and financial news.
2.  **Reason & Analyze:** Uses Llama-3 (via Groq) to synthesize fundamental and technical data.
3.  **Critique & Refine:** A secondary "Risk Manager" agent reviews the initial draft for hallucinations or bias.
4.  **Visualize:** Generates interactive charts and a professional investment memo.

This project demonstrates the implementation of **Cyclic Graph Architectures (LangGraph)** and **Production-Grade Deployment (CI/CD)**.

---

## 🏗️ Architecture

The core of this application is a **State Graph** managed by LangGraph. It operates in a loop rather than a linear chain:

```mermaid
graph TD
    A[Start] --> B(Data Collector Agent)
    B --> C(Technical Analyst Agent)
    C --> D(Fundamental Analyst Agent)
    D --> E(Writer Agent - Draft Memo)
    E --> F{Risk Manager Review}
    F -- "Rejected (Needs Revision)" --> E
    F -- "Approved" --> G[Final Dashboard Output]
