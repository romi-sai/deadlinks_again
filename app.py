import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Deadlink Checker", page_icon=":tada:",layout="wide")


#header
st.subheader("Hi I am Romika! :partying_face:")
st.write("A student from the University at Buffalo, pursuing my MS in AI :sign_of_the_horns:")
st.write("This website checks for deadlinks upto five depths for each link found on the website you are trying to check.")
st.write("This website was created using the tutorial [here](https://www.youtube.com/watch?v=VqgUkExPvLY&t=35s).")

# Create a text input widget for the user to enter the URL

# Create a button to initiate the link checking

st.title("Dead Link Checker (Depth = 5)")

visited_links = set()  # set to keep track of visited links

def check_links(url, depth=0):
    if depth >= 5:  # maximum depth reached
        return

    if url in visited_links:  # link already visited, skip
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
    check_links(url)
    st.success("Link checking completed.")
else:
    st.warning("Please enter a valid URL.")
