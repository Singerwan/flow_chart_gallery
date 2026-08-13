import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title('Data Processing Workflow_Diagram')
with open("Data Processing WorkFlow Diagram.drawio.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=2800,width=1200)


import streamlit as st
st.set_page_config(layout="wide")
st.title('Data Visualization Chart Types Choice FlowChart')
import streamlit.components.v1 as components
with open("Data Visualization Chart Types FlowChart.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,width=1200,height=1400)

import streamlit as st
st.set_page_config(layout="wide")
st.title('DataProcessing Mindmap')
import streamlit.components.v1 as components
with open("dataprocessing.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,width=1200,height=1200)

st.title('Pandas Workflow')
with open("datadiagram.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=550,width=1200)

st.title('GeoJson File Breakdown')
with open("Geojsonfile_flowchart.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=600,width=1200)


st.title('MarkDownWorkflow To DiagramHTML')
with open("MDtoHTMLdiagram.drawio.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=900,width=1200)


st.title('GeographicMapCreation Workflow')
with open("Mapcreate.drawio copy.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=590,width=1200)

st.title('GeographicMapCreation Workflow2')
with open("Map Choropleth .drawio.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=650,width=1200)

import streamlit as st
st.set_page_config(layout="wide")
st.title('Plotly Workflow')
import streamlit.components.v1 as components
with open("plotlyworkflow.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,width=1200,height=1200)


import streamlit as st
st.set_page_config(layout="wide")
st.title('Literature Mindmap')
import streamlit.components.v1 as components
with open("literatureoverview.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,width=1200,height=1200)




