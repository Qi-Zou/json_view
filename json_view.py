import streamlit as st
import json

st.title('JSON Viewer')

# 输入json
json_input = st.text_area('Input JSON', value='{}', height=300)

# 展示json
st.json(json.loads(json_input))
