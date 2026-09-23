from pathlib import Path
from urllib.request import urlretrieve

Path('data').mkdir(exist_ok=True)
url = 'https://huggingface.co/datasets/google/civil_comments/resolve/main/data/validation-00000-of-00001.parquet'
urlretrieve(url, 'data/civil_comments.parquet')
print('Downloaded Civil Comments (Google, CC0).')
