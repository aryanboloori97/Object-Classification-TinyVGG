from random import choice
from PIL import Image



def show_image_with_PIL(path):

    list_of_train_images = list(path.glob('./*/*.jpg'))
    random_image_path = choice(list_of_train_images)
    class_name = random_image_path.parent.stem
    img = Image.open(random_image_path)
    print(f"Image Path: {random_image_path}\nImage Class:{class_name}\nImage Width:{img.width}\nImage Heigth:{img.height}\n")
          
    
    return img

    

show_image_with_PIL(train_path)



def show_images_matplotlib(path):
    
    list_of_train_images = list(path.glob('./*/*.jpg'))
    random_image_path = choice(list_of_train_images)
    img = Image.open(random_image_path)
    image_array = np.asarray(img)
    class_name = random_image_path.parent.stem
    plt.imshow(image_array)
    plt.axis(False)
    plt.title(f"{class_name} --> Size: [{img.height}, {img.width}, {image_array.shape[2]}] - [heigth, width, channels]")
    print(f"Image Path: {random_image_path}")

    return None

def show_transformed_images(path, number, transformer=None, seed=42):

    random_images = {}
    list_of_image_paths = list(path.glob('*/*.jpg'))
    
    for _ in range(number):
        random_image_path = choice(list_of_image_paths)
        class_name = random_image_path.parent.stem
        random_images[random_image_path] = class_name

    for path, class_name in random_images.items():
        fig, ax = plt.subplots(1, 2)
        img = Image.open(path)
        image_array = np.asarray(img)
        # image_transformed = transformer(image_array)
        fig.suptitle(f"Class : {class_name}", fontsize=15)
        ax[0].imshow(image_array)
        ax[0].axis(False)
        ax[0].set_title(f'Original\nsize: {img.height} * {img.width}')
        transformed_image = transformer(img).permute(1, 2, 0)
        ax[1].imshow(transformed_image)
        ax[1].axis(False)
        ax[1].set_title(f'Transformed\nsize: {transformed_image.shape[0]} * {transformed_image.shape[1]}')

