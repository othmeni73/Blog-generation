import streamlit as st
import langchain
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


## function to get response from my llama 2 model
def getLlamaResponse(input_text,no_words,blog_style):
    prompt = PromptTemplate(input_variables=['input_text','no_words','blog_style'], template = 'write a blog having the topic {input_text} with {no_words} words in the style of {blog_style}')
    llm = CTransformers(model = '/llama2.bin',model_type = 'llama', config = {'temperature':0.5})
    response = llm(prompt.format(input_text=input_text,no_words=no_words,blog_style=blog_style))
    return response


st.set_page_config(page_title="generate blog", page_icon="🔗", layout="centered", initial_sidebar_state="collapsed")
st.header("Generate Blogs")

input_text = st.text_input("enter the blog topic")

## creating two more columns for additional two fields 

col1, col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("enter the number of words")
with col2:
    blog_style = st.selectbox("select the blog style", ["Researchers", "Data Scientists", "common people"])

## creating a button to generate the blog
submit = st.button("Generate Blog")
if submit:
    st.write("Generating Blog...")
    st.write(getLlamaResponse(input_text,no_words,blog_style))
