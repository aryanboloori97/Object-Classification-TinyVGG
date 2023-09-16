# Crate Dataloaders

no_of_cpus = os.cpu_count()
train_dataloader = DataLoader(train_data, batch_size=32, num_workers=no_of_cpus, shuffle=True, drop_last=True) 
test_dataloader = DataLoader(test_data, batch_size=32, num_workers=no_of_cpus, drop_last=True) 
