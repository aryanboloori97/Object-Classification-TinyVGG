
# Download and locate the dataset
data_path = Path('./Data/')
image_path = data_path / 'pizza_stake_suchi'


if image_path.is_dir():
    print(f'Folder {image_path} already exists!')
else:
    print('Data folder Not found.... Creating one')
    image_path.mkdir(parents=True, exist_ok=True)

if not (image_path).exists():
    with open(image_path/ 'pizza_stake_sushi.zip', 'wb') as f:
        print('Downloading the dataset...')
        req = requests.get('https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/data/pizza_steak_sushi.zip')
        total_size_in_bytes= int(req.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        for data in req.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    print('Dwonloading zip file finished....Starting uzipping it....!')
    with zipfile.ZipFile(image_path / 'pizza_stake_sushi.zip', 'r') as f_2:
        f_2.extractall(image_path)
    os.remove(image_path / 'pizza_stake_sushi.zip')
else:
    print("Dataset : 'pizza_stake_sushi' Aready exists!")
