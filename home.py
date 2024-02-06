import sys

from classification import classify
from newsscraping import datascrap

sys.path.insert(1,r"C:\Users\Vinoth\PycharmProjects\RiceExportsDataAnalysis\venv\Lib\site-packages")
import streamlit_option_menu
import streamlit as st

st.set_page_config(layout="wide", page_title="News Classifier")
selected=streamlit_option_menu.option_menu("Menu",["About", "Data collection", "Classifier", "Contact"],
                                           menu_icon = "cast",
                                           default_index = 0,
                                           orientation="horizontal")

if selected=="About":
    st.title(":red[News Classifier:]")
    st.subheader(":green[Tools and Tech:]")
    st.markdown("Python, NLP, Streamlit, NewsApi")
    st.subheader("About:")
    st.markdown("""
    A news classifier machine learning model that is trained to accurately categorize news articles into various topics or classes. 
    The classifier analyzes the content and language of an article and assigns it to the most appropriate category based on its characteristics, keywords, and context.
    The purpose of a news classifier is to automate the process of organizing and sorting news articles, making it easier for users to search for and access articles of interest. 
    By categorizing articles into different topics such as politics, sports, finance, entertainment, technology, etc., 
    The classifier helps users quickly find the type of news they are interested in.""")
if selected=="Data collection":
    datascrap()
if selected=="Classifier":
    classify()
if selected=='Contact':
    col1, col2=st.columns([0.5,1.5], gap='small')
    with col2:
        st.subheader("Name: :green[Vinoth Palanivel]")
        st.write("Degree: :green[Bachelor of Engineering in Electrical and Electronics Engineering]")
        st.write("E-mail: :green[vinothchennai97@gmail.com]")
        st.write("Mobile: :green[7904197698 or 9677112815]")
        st.write("Linkedin: :orange[https://www.linkedin.com/in/vinoth-palanivel-265293211/]")
        st.write("Github: :orange[https://github.com/Vinoth0208/]")