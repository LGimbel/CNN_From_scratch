import nbformat
from nbconvert import HTMLExporter
with open('classifer.ipynb', 'r', encoding='utf-8') as f:
    notebook_content = nbformat.read(f, as_version=4)
html_exporter = HTMLExporter()
html_exporter.template_name = 'classic'
body, resources = html_exporter.from_notebook_node(notebook_content)
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(body)