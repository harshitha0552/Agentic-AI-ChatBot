import streamlit as st
import requests

st.title("ChatBot")
st.subheader("How can I help you?")

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

prompt = st.chat_input("Ask anything")

if prompt:
    st.session_state["conversation"].append({"role":"user","data":prompt})

    response = requests.post(
        url="https://harshitha2468.app.n8n.cloud/webhook/5ace1238-e259-48fa-8b99-d3da7ec8b2fa",
        json={"prompt": prompt}
    )

    if response.status_code == 200:
        st.session_state["conversation"].append({"role":"ai","data":response.json()["output"]})
    else:
        st.session_state["conversation"].append(f"Error: {response.status_code} - {response.text}")


for conv in st.session_state["conversation"]:
    with st.chat_message(conv["role"]):
        st.write(conv["data"])