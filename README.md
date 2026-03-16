# PRP AI Agent (Mentra)

This project is developed as part of the **Bachelor of Data Science Capstone Project I** at **SP Jain School of Global Management**.

**Mentra** is a prototype AI assistant designed to support the **Professional Readiness Program (PRP)** by providing students and mentors with fast, reliable, and personalized career guidance.

The system centralizes PRP-related information and automates repetitive mentor queries, allowing mentors to focus more on personalized coaching instead of answering the same administrative questions repeatedly.

Mentra integrates conversational AI, a structured database, and a lightweight web interface to create a single access point for professional readiness support.

---

# Overview

Students frequently ask similar questions related to:

- CV and resume improvement  
- LinkedIn profile optimization  
- Cover letter writing  
- Interview preparation  
- PRP event participation  
- Immigration and work rights  
- Professional skill development  

PRP mentors often spend a large portion of their time answering repetitive questions.

**Mentra solves this by acting as a conversational assistant that:**

- Answers common PRP-related questions.
- Provides career preparation guidance.
- Retrieves information from PRP datasets.
- Helps students navigate mentoring opportunities.
- Reduces administrative workload for mentors.

The system uses anonymized or sample PRP data to demonstrate how an AI assistant could streamline communication between students and PRP staff.

---

# Key Features

Mentra provides several core capabilities.

## Conversational PRP Support

Students can ask questions about PRP activities, career preparation, and mentoring through a chat interface.

## Career Readiness Guidance

The agent provides structured advice on:

- CV improvement
- LinkedIn optimization
- Cover letter writing
- Interview preparation

## PRP Data Integration

Mentra connects to a **Supabase PostgreSQL database** containing anonymized PRP data such as:

- event schedules
- attendance records
- mentoring sessions
- readiness metrics

## Mentor Redirection

If a query requires personalized guidance, Mentra recommends scheduling a session with a PRP mentor.

## Administrative Automation

The system can support tasks such as:

- attendance summaries
- event information retrieval
- mentoring session lookup

---

# System Architecture

Mentra follows a layered architecture consisting of four main components.

## 1. User Layer (Frontend)

Students and mentors interact with the system through a **chat-based interface**.

Responsibilities:

- Accept user queries
- Display AI responses
- Provide basic interaction features

Technologies:

- Streamlit or React
- HTML / CSS / JavaScript

---

## 2. Application Layer (Backend)

The backend acts as the coordination layer between the user interface, AI model, and database.

Responsibilities:

- prompt engineering
- query interpretation
- workflow orchestration
- API communication

Technologies:

- Python
- FastAPI
- LangChain / LangGraph

---

## 3. AI Processing Layer

This layer powers the reasoning capability of the system.

Responsibilities:

- interpret user questions
- generate contextual responses
- integrate external knowledge sources

Technologies:

- OpenAI API
- Gemini / Claude
- embedding models
- vector storage

---

## 4. Data Layer

The data layer stores PRP-related datasets used by the agent.

Responsibilities:

- storing structured program data
- managing access permissions
- enabling secure queries

Technologies:

- Supabase (PostgreSQL)
- Row Level Security (RLS)

---

# High-Level Workflow


Student / Mentor
↓
Frontend Chat Interface
↓
FastAPI Backend
↓
LangChain / LangGraph Agent
↓
LLM API (OpenAI / Gemini / Claude)
↓
Supabase Database (PRP Data)
↓
Response Processor
↓
Frontend Display


This architecture allows Mentra to combine conversational AI with structured institutional data to deliver contextual responses.

---

# Folder Structure

```
prp-ai-agent/

backend/ # FastAPI backend and business logic
main.py
routes/
services/

frontend/ # Streamlit or React interface
app.py
components/

supabase/ # SQL setup and database schema
schema_enums.sql
core_tables.sql
booking_system.sql
indexes.sql
rls_policies.sql
views.sql
seed_data.sql

data/ # Sample or anonymized PRP data
sample_prp.csv

venv/ # Python virtual environment (not committed)

.env # Environment variables

requirements.txt # Python dependencies

README.md # Project documentation

.gitignore

```


---

# Setting Up the Project

## 1. Clone the repository

```bash
git clone https://github.com/drheaa/mentra-prp-ai-agent
cd mentra-prp-ai-agent
```

## 2. Create a virtual environment

- macOS / Linux
```bash 
python3 -m venv venv
source venv/bin/activate
```

- Windows
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```
## 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Set up environment variables
Create a .env file in the root directory.

```env
SUPABASE_URL=https://<project-id>.supabase.co
SUPABASE_ANON_KEY=<anon-key>
SUPABASE_SERVICE_ROLE_KEY=<service-role-key>

OPENAI_API_KEY=<openai-key>

ENV=development
PORT=8000
SECRET_KEY=<random-string>
LOG_LEVEL=info
```

## 5. Run the backend server

```bash
npm run dev
```

## 6. Run the frontend interface

```bash
streamlit run frontend/app.py
```

-----

# Database Setup

All SQL files required for the database are located in the supabase/ folder.

Run them sequentially using the Supabase SQL editor or CLI.


-----

# Tech Stack

## Backend

- Python

- FastAPI

- LangChain / LangGraph

## Frontend

- Streamlit or React

- HTML / CSS / JavaScript

## Database

- Supabase (PostgreSQL)

## AI / NLP

- GROQ AI API

- Hugging Face

## Tools
- Git / GitHub

- VS Code


----

# Project Scope

Mentra is a prototype system built for academic purposes.

Included in scope:

- conversational AI prototype

- PRP data integration

- chat interface

- database security using RLS

Out of scope:

- full institutional deployment

- handling real student data

- production infrastructure

--- 

# Team

- Devanshi Rhea Aucharaz

- Makhabat Zhyrgalbekova

- Trisha Mukherjee