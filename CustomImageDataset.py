
class CustomImageDataset(torch.utils.data.Dataset):


    def __init__(self, target_dir, transformer=None):
        self.target_dir = target_dir
        self.list_of_pictures = list(target_dir.glob('*/*.jpg'))
        self.transformer = transformer


    def show_random_image(self):
        random_image_path = choice(self.list_of_pictures)
        img = Image.open(random_image_path)
        image_array = np.asarray(img)
        class_name = random_image_path.parent.stem
        plt.imshow(image_array)
        plt.axis(False)
        plt.title(f"Image Path: {random_image_path} - [{class_name}] --> Size: [{img.height}, {img.width}, {image_array.shape[2]}] - [heigth, width, channels]")


    def len_of_each_class(self):
        class_names = {entry.name:0 for entry in list(os.scandir(self.target_dir))}
        for class_ in class_names.keys():
            class_names[class_] = len(list(os.scandir(self.target_dir / class_)))
    
        return class_names
            
    def __len__(self):
        sum_ = 0
        for class_ in os.scandir(self.target_dir):
            sum_ += len(list(os.scandir(self.target_dir / class_.name)))
        return sum_

    def __getitem__(self, idx):
        img = Image.open(self.list_of_pictures[idx])
        return self.transformer(img)
