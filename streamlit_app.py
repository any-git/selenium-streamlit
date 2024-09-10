import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st

os.system("apt download firefox-esr")
files = os.listdir()
st.code(files)
firefox_deb = [file for file in files if ".deb" in file]
os.system(f"dpkg -x {firefox_deb[0]}")

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.binary_location = "./usr/bin/firefox"


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
