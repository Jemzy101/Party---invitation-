import streamlit as st

st.title("🎉 Jemzy Party Invitation")

name = st.text_input("What is your name?")

password = st.text_input(
    "Please enter the password:",
    type="password"
)

if st.button("Submit"):

    if password == "jemzy party":

        st.success("Welcome to Jemzy Party!")

        st.write("You are invited,", name)

        st.subheader("Party Details")

        st.write("💰 Party Fee: ₦5,000,000")
        st.write("⭐ Premium VIP Seat")
        st.write("📅 Date: 21st November, 2026")

    else:
        st.error("Sorry, you aren't invited to the party.")
