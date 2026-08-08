import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title('Data Processing Workflow_Diagram')
with open("Data Processing WorkFlow Diagram.drawio.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=2850,width=1200)


st.title('Pandas Workflow')
with open("datadiagram.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
components.html(html_content,height=600,width=1200)

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


