# Do some distortions on our pictures in order to resize them to 64 * 64 pixels, and convert them to tensors Normalized RGB values(0, 1)                     





transofrmer_train = transforms.Compose(
    [
        transforms.Resize((128, 128)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.ToTensor(),

        
    ]

    
)
transofrmer_test = transforms.Compose(
    [
        transforms.Resize((128, 128)),
        transforms.ToTensor(),

        
    ]

    
)
