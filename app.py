import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from lib.utils import reflection_response

st.set_page_config(page_title="Reflection 70B", page_icon='🤖')

st.header("Chat With Reflection 70B")

# initialize session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        AIMessage(content="Hello there👋, how can I help you today?")
    ]

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message('AI'):
            st.info(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

# accept user input
user_question = st.chat_input("Start typing...")
if user_question is not None and user_question != "":
    st.session_state.chat_history.append(HumanMessage(content=user_question))
    
    with st.chat_message("Human"):
        st.markdown(user_question)
        
    response = reflection_response(user_question)
    
    # Remove any unwanted prefixes from the response
    # response = response.replace("AI response:", "").replace("chat response:", "").replace("bot response:", "").strip()
 
    with st.chat_message("AI"):
        st.write(response)
        
    st.session_state.chat_history.append(AIMessage(content=response))

