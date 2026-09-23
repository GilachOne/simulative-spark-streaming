from pathlib import Path
import nbformat
from nbclient import NotebookClient

path = Path('toxic_comments.ipynb')
notebook = nbformat.read(path, as_version=4)
client = NotebookClient(notebook, timeout=900, kernel_name='python3', resources={'metadata':{'path':'.'}})
try:
    client.execute()
finally:
    nbformat.write(notebook, path)
print('Notebook executed:', path)
