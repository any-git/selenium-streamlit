from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st


@st.cache_resource
def get_driver(options):
    return webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=options
    )


options = Options()
options.add_argument("--headless")

url = st.text_input("URL")
if url:
    driver = get_driver(options)
    driver.get(url)
    st.code(driver.page_source)
    driver.quit()
