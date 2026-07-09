import streamlit as st
st.title("IDENTITY ECHO INTERFACE")
st.write("Enter your details below and click transmit")
user_name = st.text_input("Enter your name" , value=None, placeholder = "what's your name?")
user_message = st.text_input("Enter your message", value=None , placeholder = "what's your message")
if st.button("TRANSMIT"):
    if not user_name:
         st.error("please enter your name")
    elif not user_message:
        st.warning("please enter your message")
    else:
        st.success(f"TRANSMISSION SUCCESSFUL!\n\n Hello {user_name}\n\n\n**Message**: {user_message}")
        character_count = len(user_message)
        token_count = character_count / 4
        st.info(f"Character Count: {character_count}\n\n\nToken Count: {token_count}")