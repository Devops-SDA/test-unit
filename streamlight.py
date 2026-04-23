import streamlit as st

# Set page title
st.set_page_config(page_title="My Python SPA")

# Sidebar navigation (simulating multiple views in one page)
page = st.sidebar.selectbox("Choose a view", ["Home", "Data Analysis", "Settings"])

if page == "Home":
    st.title("Welcome to My App")
    st.write("This is a single-page application built with Streamlit.")
    
    # User Input
    name = st.text_input("Enter your name:")
    if st.button("Greet Me"):
        st.success(f"Hello, {name}!")

elif page == "Data Analysis":
    st.title("Data View")
    st.write("You can display charts and tables here.")
    st.line_chart([10, 20, 15, 30, 25])

elif page == "Settings":
    st.title("Settings")
    st.checkbox("Enable Notifications")

