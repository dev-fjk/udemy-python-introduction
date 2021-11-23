"""
https://pypi.org/ に登録されているライブラリは pipコマンドでインストールできる
py -m pip install tqdm
py -m pip uninstall tqdm

py -m pip freeze でインストールしたライブラリ一覧が閲覧できる
"""

import time

from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(1)
