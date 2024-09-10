from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st

options = Options()
options.add_argument("--headless")


@st.cache_resource
def get_driver():
    return webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=options
    )


url = st.text_input("URL")
if url:
    driver = get_driver()
    driver.get(url)
    st.code(driver.page_source)
    driver.quit()
