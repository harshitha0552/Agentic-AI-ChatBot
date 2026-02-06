# Agentic AI ChatBot


https://github.com/user-attachments/assets/75121dd9-0b7b-4c49-8f41-d0d95f95b838



An **Agentic AI–powered conversational chatbot** built using **Streamlit, n8n**, designed to deliver a **ChatGPT-like user experience** with real-time AI responses.

This project showcases how **Agentic AI workflows** and **automation platforms** can be integrated with a modern UI to build scalable conversational systems.

---

## 🚀 Project Overview

This application allows users to:

- Interact with an AI chatbot using a ChatGPT-style interface  
- Send user queries from Streamlit to n8n via Webhooks  
- Process queries using an AI Agent powered by Google Gemini  
- Receive real-time AI responses in the UI  
- Maintain conversation history using Streamlit session state  

---

## 🧠 Architecture & Workflow

### 🔄 End-to-End Workflow

1. **Streamlit Frontend**
   - User enters a message in a ChatGPT-like UI
   - Prompt is sent to n8n using a Webhook

2. **Webhook Node (n8n)**
   - Receives the user input from Streamlit
   - Forwards it to the AI Agent

3. **AI Agent (Agentic AI)**
   - Acts as the central orchestrator
   - Interprets user intent
   - Communicates with the LLM

4. **Google Gemini Chat Model**
   - Generates a natural language response
   - Returns structured output to the workflow

5. **Respond to Webhook**
   - Sends the AI response back to Streamlit in JSON format

6. **Streamlit UI Update**
   - Displays user and assistant messages
   - Maintains chat history using `st.session_state`

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Automation Platform**: n8n  
- **LLM**: Google Gemini Chat Model  
- **AI Orchestration**: Agentic AI (n8n AI Agent)  
- **Backend**: Python  
- **State Management**: Streamlit Session State  
- **Integration**: Webhooks  

---

## ✨ Features

- ChatGPT-style conversational UI  
- Agentic AI workflow orchestration  
- Real-time AI responses  
- Conversation memory using session state  
- Webhook-based communication  
- Clean and modular architecture  

---

## 📂 Project Structure

```bash
├── app.py      # Streamlit UI for user prompt             
├── n8n_workflow.json     # Agentic AI workflow
├── requirements.txt      # Python dependencies
└── README.md
```
## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/harshitha0552/Agentic-AI-ChatBot.git
cd Agentic-AI-ChatBot
```

## 2️⃣ Create & Activate Virtual Environment
```
python -m venv venv

Activate the environment:venv\Scripts\activate
```

## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

## 4️⃣ Start Streamlit App
```
streamlit run streamlit_app.py
```

## 4️⃣ Start n8n Workflow

- Import ChatBot.json into n8n

- Configure the Webhook URL and Google Gemini API credentials

- Activate the workflow

```
## 🔄 Workflow Breakdown

Step | Component | Description  
1 | Streamlit UI | User enters chat message  
2 | Webhook | Sends prompt to n8n  
3 | AI Agent | Orchestrates reasoning  
4 | Gemini Model | Generates response  
5 | Respond to Webhook | Returns AI output  
6 | Streamlit | Displays response  

```
## 🌟 Key Learning Outcomes

- Building ChatGPT-style UIs with Streamlit  
- Agentic AI workflow design using n8n  
- Webhook-based system integration  
- Managing state in Streamlit applications  
- Real-time LLM response handling  

# 👨‍💻 Author

Akurala Harshitha
Data Science | Agentic AI Automation
