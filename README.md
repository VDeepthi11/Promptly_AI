# 🗄️ PromptVault

**PromptVault** is a lightweight web application built with **Python, Streamlit, SQLite, and Pandas** that helps users save, organize, search, edit, and manage AI prompts along with their responses. It provides a simple and interactive interface for maintaining a personal prompt library with persistent local storage.

---

## 🌐 Live Demo

🚀 **Try the application online:**

**https://promptlyai-ct.streamlit.app/**

---

## ✨ Features

* ➕ Create and save AI prompts with responses
* 📖 View all saved prompts
* ✏️ Edit and update existing prompts
* 🗑️ Delete prompts
* 🔍 Search prompts by prompt text or AI model
* 🏷️ Organize prompts by category
* 🤖 Track the AI model used
* 💾 Store data using SQLite
* ⚡ Clean and interactive Streamlit interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* SQLite
* Pandas

---

## 📌 CRUD Operations

| Operation  | Description                    |
| ---------- | ------------------------------ |
| **Create** | Save new prompts and responses |
| **Read**   | View stored prompts            |
| **Update** | Edit existing prompts          |
| **Delete** | Remove prompts from the vault  |

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

## 💻 Run Locally

```bash
git clone https://github.com/VDeepthi11/Promptly_AI.git

cd Promptly_AI

pip install -r requirements.txt

streamlit run appv2.py
```

---

## 📚 Skills Demonstrated

* Python Programming
* Streamlit Web Application Development
* SQLite Database Integration
* SQL CRUD Operations
* Database Connectivity
* Data Handling with Pandas
* Interactive UI Development

---

⭐ PromptVault demonstrates a complete CRUD application built with Python, Streamlit, SQLite, and Pandas, showcasing database integration, web application development, and interactive user interface design.
