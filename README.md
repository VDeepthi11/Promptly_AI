# 🗄️ PromptVault

**PromptVault** is a lightweight web application built with **Python, Streamlit, SQLite, and Pandas** that helps users save, organize, search, edit, and manage AI prompts along with their responses. It provides a simple and interactive interface for maintaining a personal prompt library with persistent local storage.

---

## ✨ Features

* ➕ Create and save AI prompts with responses
* 📖 View all saved prompts in an organized layout
* ✏️ Edit and update existing prompts
* 🗑️ Delete prompts when no longer needed
* 🔍 Search prompts by prompt text or AI model
* 🏷️ Categorize prompts (Coding, Creative, Logic, Summarization)
* 🤖 Track the AI model used for each prompt
* 💾 Store data locally using SQLite
* ⚡ Interactive and user-friendly interface built with Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **SQLite**
* **Pandas**

---

## 📌 CRUD Operations

| Operation  | Description                         |
| ---------- | ----------------------------------- |
| **Create** | Save new prompts and AI responses   |
| **Read**   | View all stored prompts             |
| **Update** | Edit existing prompts and responses |
| **Delete** | Remove prompts from the vault       |

---

## 🗂️ Database Schema

| Column     | Description           |
| ---------- | --------------------- |
| `id`       | Primary Key           |
| `category` | Prompt category       |
| `prompt`   | User prompt           |
| `model`    | AI model used         |
| `response` | AI-generated response |

---

## 🚀 Run Locally

1. Clone the repository

```bash
git clone https://github.com/VDeepthi11/Promptly_AI.git
```

2. Navigate to the project folder

```bash
cd Promptly_AI
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run appv2.py
```

---

## 📷 Application Features

* Create Prompt
* View Prompt Library
* Search Prompt History
* Update Existing Prompts
* Delete Prompts
* SQLite Database Integration

---

## 📚 Learning Outcomes

This project demonstrates:

* Python Programming
* Streamlit Web Application Development
* SQLite Database Integration
* SQL CRUD Operations
* Database Connectivity
* Data Handling with Pandas
* Interactive User Interface Design

---

⭐ **PromptVault** is a simple, lightweight, and beginner-friendly CRUD application that showcases full-stack Python development using Streamlit and SQLite while helping users efficiently organize and reuse AI prompts.
