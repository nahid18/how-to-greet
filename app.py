import streamlit as st
import streamlit.components.v1 as components
import requests
import re

st.set_page_config(
    page_title="How to Greet a Professor",
    page_icon="🧊",
)

def fetch_tweet_html(tweet_url):
    api_url = f"https://publish.twitter.com/oembed?url={tweet_url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["html"]

def main():
    st.title("How to Greet a Professor?")
    name = st.text_input("Enter a name:", placeholder="Andrew Akbashev")
    if st.button("Parse"):
        p = re.compile(r'^(\s+)?(Mr(\.)?|Mrs(\.)?)?(?P<FIRST_NAME>.+)(\s+)(?P<LAST_NAME>.+)$', re.IGNORECASE)
        m = p.match(name)
        if m is not None:
            first_name = m.group('FIRST_NAME')
            last_name = m.group('LAST_NAME')
            output = f"Dear Prof. {last_name.strip()}"
            st.success("Parsed successfully!")
            st.code(output, language='python')
            st.balloons()
        else:
            st.warning("Invalid name format.")
    
    tweet_url = "https://twitter.com/Andrew_Akbashev/status/1679155216132784129"
    tweet_html = fetch_tweet_html(tweet_url)
    if tweet_html:
        components.html(tweet_html, height=700)
    else:
        st.warning("Failed to load tweet.")

if __name__ == "__main__":
    main()

