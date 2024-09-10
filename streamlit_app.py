from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st


@st.cache_resource
def get_driver():
    return webdriver.Firefox(service=Service(GeckoDriverManager().install()))


options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

url = st.text_input("URL")
if url:
    driver = get_driver()
    driver.get(url)
    st.code(driver.page_source)
