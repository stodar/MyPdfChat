import streamlit as st

st.title("Chat")

index = st.session_state["my_input"]

query = st.text_input("Ask question :")
submit = st.button("Submit")
if submit:
    rep = index.query(query)
    st.text_area("Answer : ", str(rep), 300)