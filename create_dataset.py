
# Create datasets using ImageFolder
train_data = datasets.ImageFolder(root=train_path,
                                  transform=transofrmer_train,
                                  target_transform=None)


test_data = datasets.ImageFolder(root=test_path,
                                 transform=transofrmer_test,
                                  )

print(f'Train Data:{train_data} \n Test Data:{test_data}')
print(f'-----Check Sizes---- \nTrain Data: {len(train_data)} \nTest Data: {len(test_data)}')
