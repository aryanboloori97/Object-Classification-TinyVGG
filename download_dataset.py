from pathlib import Path
import requests
from tqdm import tqdm
import zipfile
import os

class DownloadFile(object):

    def __init__(self):
        pass
        
       
    @staticmethod
    def download(url, file_name, folder_name='Data'):
        # Download and locate the file
        folder_path = Path(f'./{folder_name}/')
        file_path = folder_path / file_name

        if folder_path.is_dir():
            print(f'Folder {folder_path} already exists!')
        else:
            print('Folder Not found.... Creating one')
            folder_path.mkdir(parents=True, exist_ok=True)

        if not (file_path).exists():
            with open(folder_path/ file_path, 'wb') as f:
                print('Downloading the file...')
                req = requests.get('https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/data/pizza_steak_sushi.zip')
                total_size_in_bytes= int(req.headers.get('content-length', 0))
                block_size = 1024 #1 Kibibyte
                progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                for data in req.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)
            progress_bar.close()
        else:
            print("Dataset : 'pizza_stake_sushi' Aready exists!")
            
            
    @staticmethod
    def unzip(file_path, keep_zip=True):
            with zipfile.ZipFile(file_path, 'r') as f_2:
                f_2.extractall(file_path.parent)
            if not keep_zip:
                os.remove(file_path)
        
