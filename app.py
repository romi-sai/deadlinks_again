import streamlit as st
import requests
try:
    from bs4 import BeautifulSoup
except :
    from BeautifulSoup import BeautifulSoup 
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Deadlink Checker", page_icon=":sign_of_the_horns:",layout="wide")

def streamlit_menu(example=1):
    if example == 1:
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected


selected = streamlit_menu(example=1)

if selected == "Home":
    st.subheader("Hi I am Romika! 🥳")
    st.write("A student from the University at Buffalo, pursuing my MS in AI :sign_of_the_horns:")
    st.write("This website checks for deadlinks upto three depths for each link found on the website you are trying to check.")
if selected == "Check Links":
    st.title("Dead Link Checker (Depth = 3)")
    st.write("This website was created using the tutorial [here](https://www.youtube.com/watch?v=VqgUkExPvLY&t=35s).")
    
    visited_links = set() 
    
    def check_links(url, depth=0):
        if depth >= 3:
            return
    
        if url in visited_links: 
            return
        visited_links.add(url)
    
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            return
    
        if response.status_code == 404:
            st.warning("Broken link: " + str(url))
    
        soup = BeautifulSoup(response.content, "html.parser")
    
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("http"):
                check_links(href, depth + 1)
    
    url = st.text_input("Enter URL to check for dead links:")
    
    if st.button("Check"):
        if url:
            visited_links.clear()
            try:
                check_links(url)
                st.success("Link checking completed.")
            except Exception as e:
                st.error("An error occurred: " + str(e))
    else:
        st.warning("Please enter a valid URL.")
if selected == "Contact":
    st.title("You have selected " + str(selected))
