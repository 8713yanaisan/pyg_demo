import pandas as pd
import streamlit as st
import plotly.express as px
import pygwalker as pyg

st.set_page_config(layout="wide", initial_sidebar_state="auto")
st.title("PyGWaller作成")
# サイドバー
# ファイルアップロード
uploaded_file = st.sidebar.file_uploader("Excelファイルアップロード") 


# xlsxファイルを読み込む
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    


pyg.walk(df, env='Streamlit')