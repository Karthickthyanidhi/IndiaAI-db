import streamlit as st
import pandas as pd
import datetime
#from Pillow import Image
import imageio.v2 as imageio
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel("data1.xlsx",engine="openpyxl")
print(df)

st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
#image = Image.open('NIELIT-LOGO.png')
image = imageio.imread('NIELIT1-LOGO.jpg')

col1, col2 = st.columns([0.15,0.5])
with col1:
    st.image(image,width=300)

html_title = """
    <style>
    .title-test {
    font-weight:bold;
    padding:5px;
    border-radius:6px;
    }
    </style>
    <center><h1 class="title-test">IndiaAI Dashboard</h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html=True)

col3, col4, col5 = st.columns([0.1,0.45,0.45])
with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by:  \n {box_date}")

with col4:
    fig = px.bar(df, x = "State", y = "Gender", labels={"Gender" : "Gender {$}"},
                 title = "Statewise Gender Data", hover_data=["Gender"],
                 template="gridon",height=500)
    st.plotly_chart(fig,use_container_width=True)


with col5:
    fig1 = px.bar(df, x = "State", y = "Category", title="Statewise Category Data",
                   template="gridon",hover_data=["Category"],orientation='h') 
    st.plotly_chart(fig1,use_container_width=True)
