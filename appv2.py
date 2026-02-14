import streamlit as st
import sqlite3
import pandas as pd

# 1. Database Setup
conn = sqlite3.connect('prompts_vault.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS vault 
             (id INTEGER PRIMARY KEY, category TEXT, prompt TEXT, model TEXT, response TEXT)''')
conn.commit()

st.set_page_config(page_title="PromptVault", layout="wide")

# 2. Sidebar: Add New Entry
st.sidebar.header("📥 Save to Vault")
with st.sidebar.form("input_form", clear_on_submit=True):
    category = st.selectbox("Category", ["Coding", "Creative", "Logic", "Summarization"])
    
    # --- CHANGED: Now a text input instead of selectbox ---
    model = st.text_input("Which AI model did you use?", placeholder="e.g. GPT-4o, Claude 3.5")
    
    prompt_text = st.text_area("Your Prompt")
    response_text = st.text_area("Model's Response")
    
    if st.form_submit_button("Save to Vault"):
        if model and prompt_text: # Simple check to ensure required fields aren't empty
            c.execute("INSERT INTO vault (category, prompt, model, response) VALUES (?,?,?,?)", 
                      (category, prompt_text, model, response_text))
            conn.commit()
            st.success(f"Saved {model} entry to SQLite!")
            st.rerun()
        else:
            st.error("Please provide at least a Model Name and a Prompt.")

# 3. Main Interface: View & Filter
st.title("🗄️ AI Prompt & Response Vault")

# SAFE LOADING: Ensure 'df' is defined even if database is empty
try:
    df = pd.read_sql("SELECT * FROM vault", conn)
except Exception:
    df = pd.DataFrame(columns=['id', 'category', 'prompt', 'model', 'response'])

# 4. Display Logic
if df.empty:
    st.info("The vault is currently empty. Use the sidebar to add your first AI response!")
else:
    # Optional Filters
    search_query = st.text_input("Search your vault...", placeholder="Search prompts or models")
    
    display_df = df.copy()
    if search_query:
        # Search across both model names and prompt text
        display_df = df[
            df['prompt'].str.contains(search_query, case=False) | 
            df['model'].str.contains(search_query, case=False)
        ]

    for index, row in display_df.iterrows():
        with st.expander(f"📌 {row['model']} | {row['category']} | {row['prompt'][:40]}..."):
            st.markdown(f"**Prompt:**\n{row['prompt']}")
            st.info(f"**Response:**\n{row['response']}")
            
            if st.button("Delete Entry", key=f"del_{row['id']}"):
                c.execute("DELETE FROM vault WHERE id=?", (row['id'],))
                conn.commit()
                st.rerun()