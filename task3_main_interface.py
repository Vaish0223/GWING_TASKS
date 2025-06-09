import streamlit as st
import nbformat
from nbconvert import PythonExporter

# Load and convert notebook
with open("Untitled.ipynb") as f:
    notebook = nbformat.read(f, as_version=4)
py_exporter = PythonExporter()
py_code, _ = py_exporter.from_notebook_node(notebook)

# Execute notebook code in Streamlit
exec(py_code)



st.title("Plagiarism Detector Model")
st.subheader("GWING TASK 3 ACCOMPLISHED")

Lang=st.text_input("Enter your text to be detected")
if st.button("Check Plagiarism"):
    if Lang:
        check=detect(Lang.strip()) 
        st.success(f"Plagiarism Score: {check}")
    else:
        st.warning("Please enter some text.")
    
st.write("**If the output is incorrect try to refresh the page for exact results.")
