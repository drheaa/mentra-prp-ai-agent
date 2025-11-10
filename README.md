# PRP AI Agent (Mentra)

This project is developed as part of the **Bachelor of Data Science Capstone Project I** at **SP Jain School of Global Management**.  

The AI agent, named **Mentra**, is designed to support the **Professional Readiness Program (PRP)** by providing students and mentors with a single platform for quick, reliable, and personalized assistance.

---

## Overview

Students often ask similar questions about their CVs, LinkedIn profiles, cover letters, interviews, immigration and work rights, and skill development. Mentors spend valuable time answering these repetitive queries instead of focusing on one-on-one coaching.

**Mentra** acts as a conversational assistant that:
- Answers questions about professional readiness, PRP events, and mentoring.
- Helps with career preparation topics such as CVs, LinkedIn, and interviews.
- Redirects students to schedule one-on-one sessions with mentors when needed.
- Automates routine administrative tasks like attendance tracking and progress summaries.
- Connects to anonymized PRP data through a secure Supabase database.

---

## Folder Structure

- prp-ai-agent/
- │
- ├── backend/ # FastAPI backend and business logic
- │ ├── main.py
- │ ├── routes/
- │ └── services/
- │
- ├── frontend/ # Streamlit or React interface
- │ ├── app.py
- │ └── components/
- │
- ├── supabase/ # SQL setup and database schema
- │ ├── schema_enums.sql
- │ ├── core_tables.sql
- │ ├── booking_system.sql
- │ ├── indexes.sql
- │ ├── rls_policies.sql
- │ ├── views.sql
- │ └── seed_data.sql
- │
- ├── data/ # Sample or anonymized PRP data
- │ └── sample_prp.csv
- │
- ├── venv/ # Python virtual environment (not committed to Git)
- ├── .env # Environment variables (Supabase URL, keys)
- ├── requirements.txt # Python dependencies
- ├── README.md # Project documentation
- └── .gitignore

---

## Setting Up the Project

### 1. Clone or download the repository

```bash
git clone https://github.com/drheaa/mentra-prp-ai-agent
cd prp-ai-agent
```bash

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```bash

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```bash

### 4. Set up the environment file
> Create a file named .env inside prp-ai-agent/ and add your Supabase credentials:

```bash
touch .env

vim .env  #opens in bash/wsl itself

#

or code .env    #opens in vscode

```bash

>Then, paste the following and edit the keys:

# -------- SUPABASE CONFIG --------
SUPABASE_URL=https://<your-project-id>.supabase.co
SUPABASE_ANON_KEY=<your-anon-public-key>
SUPABASE_SERVICE_ROLE_KEY=<your-service-role-key>
SUPABASE_DB_URL=postgresql://postgres:<your-db-password>@<your-project-id>.supabase.co:5432/postgres?sslmode=require
# -------- LLM / AI CONFIG --------
# OpenAI or compatible endpoint (e.g. LangChain, LangGraph)
OPENAI_API_KEY=<your-openai-api-key>
LANGCHAIN_API_KEY=<your-langchain-or-langgraph-api-key>
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
# -------- APP CONFIG --------
ENV=development
PORT=8000
SECRET_KEY=<random-string-for-fastapi>
LOG_LEVEL=info
```bash

### 5. Run the backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```bash

### 6. Run the frontend (Streamlit)

```bash
streamlit run frontend/app.py
```bash

---

## Database Setup (Supabase)

All SQL files are located in the supabase/ folder.
Run them in order using the Supabase SQL editor or CLI:

```bash
cd supabase
sudo apt install postgresql-client
```bash

```bash
chmod +x run_all.sh    # make the script executable
bash run_all.sh        # run the databse setup
```bash

This creates all the PRP tables, views, and policies for testing the AI agent.

## Features

1) Conversational query handling for PRP students and mentors.

2) Integration with anonymized PRP and JPT data.

3) Mentor session scheduling with Zoom link placeholders.

4) Role-based access through Supabase Row-Level Security (RLS).

5) Lightweight design using open-source tools only.

---

## How Mentra Works

Mentra connects three main layers to provide real-time support to PRP students and mentors.

1. User Interaction Layer (Frontend):
Students and mentors chat with Mentra through a Streamlit or React interface. They can ask questions about PRP activities, career preparation, or schedule one-on-one mentoring sessions.

2. AI Processing Layer (Backend):
The FastAPI backend uses Python, LangChain, and OpenAI APIs to understand the user’s query. It checks the intent (for example, CV advice, event info, or booking requests) and retrieves or updates the relevant information from the Supabase database.

3. Data Layer (Supabase):
All PRP data, including events, attendance, mentoring sessions, skill levels, and booking schedules, is stored in a secure Supabase Postgres database with Row-Level Security. The database ensures that students only access their own data while mentors and admins have appropriate access rights.

Simple Flow Diagram:

- Student/Mentor → Frontend (Chat UI)
-         ↓
-      FastAPI Backend → LangChain → OpenAI API
-         ↓
-      Supabase Database (PRP Data + Bookings)
-         ↓
-   Response / Action (Answer or Schedule Session)

--- 

## Tech Stack

Backend: Python, FastAPI, LangChain
Frontend: Streamlit or React
Database: Supabase (PostgreSQL)
AI/NLP: OpenAI API, spaCy, Hugging Face
Other Tools: Pandas, NumPy, GitHub, VS Code, Figma

--- 

## Team

Trisha Mukherjee
Devanshi Rhea Aucharaz 
Makhabat Zhyrgalbekova