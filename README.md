"# AI_SDLC_ASSISTANT" 

# 🧠 AI SDLC Assistant

An intelligent, microservices-based AI Assistant that helps automate and guide the Software Development Life Cycle (SDLC) using Generative AI. It supports document understanding, chat-based Q&A, code suggestion, and architectural recommendations.

---

## 🚀 Project Features

- 📄 Ingest project documents (e.g., requirements, designs, plans)
- 💬 AI-powered chatbot to answer SDLC-related questions
- 📐 Suggestion engine for design patterns, architecture, and tools
- 🧠 RAG-based architecture using OpenAI GPT-4
- 📦 Vector storage of embeddings using `pgvector` in PostgreSQL
- 🖥️ Frontend: React UI for user interaction and admin dashboard
- ⚙️ Backend: FastAPI with modular microservices architecture

---

## 🧱 Architecture Overview

```text
             ┌───────────────┐
             │  React UI     │
             └────┬──────────┘
                  │
         ┌────────▼─────────┐
         │   API Gateway    │
         └────────┬─────────┘
       ┌──────────▼────────────┐
       │      FastAPI Backend   │
       └────────┬──────────────┘
                │
 ┌──────────────▼──────────────┐
 │   Vector DB (PostgreSQL +   │
 │        pgvector)            │
 └──────────────┬──────────────┘
                │
     ┌──────────▼─────────┐
     │    OpenAI GPT-4    │
     └────────────────────┘



⚒️ Tech Stack
Layer	Tech Stack
Frontend	React, Tailwind CSS, shadcn/ui
Backend	FastAPI, Python 3.10+
AI Engine	OpenAI GPT-4 (or Azure OpenAI)
Vector DB	PostgreSQL 14+ with pgvector extension
Storage	AWS S3 / Azure Blob Storage (PDFs, docs)
Hosting	AWS EC2/App Runner OR Azure App Service

📦 Setup Instructions
1. Clone Repository
bash
git clone https://github.com/your-org/ai-sdlc-assistant.git
cd ai-sdlc-assistant


📁 Folder Structure
text
Copy
Edit
ai-sdlc-assistant/
├── backend/
│   ├── main.py
│   ├── services/
│   ├── database/
│   └── utils/
├── frontend/
│   ├── src/
│   └── public/
├── docs/
│   └── architecture-diagrams/
├── .env
├── README.md

