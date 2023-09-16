
class TinyVGG(nn.Module):


    def __init__(self,
                 in_image_size: Tuple[int, int],
                 in_shape: int,
                 out_shape: int,
                 hidden_units:int=10,
                 no_blocks: int=10,
                 kernel_size_convolution: Tuple[int, int]=(3, 3),
                 kernel_size_maxpool: Tuple[int, int]=(2, 2),
                 stride_convolution: int=1,
                 stride_maxpool: int=2,
                 padding_convolution:int=1,
                 padding_maxpool:int=1,
                 activation_function: Union['relu', 'leaky_relu', 'sigmoid', 'tanh']= 'relu',
                 logit_activation: bool= False,
                 ):

        """
        
        in_image_size: Size of the image. For example: 64 * 64 should be reformed in this way(64, 64)
        in_shape: The number of color channels. For example: 3 RGD- Red, Green, Blue
        out_shape: The number of output channels. For example if you have a classification model with 3 labels, your output channels should be 3,
        each of which represents the probability corresponding to that label.
        hidden_units: The number of units or neurons in each hidden layer
        no_blocks: The number of blocks
        kernel_size: The size of filter
        activation_function: Sigmoid, leaky_relu, sigmoid, tanh
        logit_activation: Consider activation function for the last units in last layer(output)
        
        
        
        
        
        
        """
        
        super().__init__()
        list_of_blocks = []
        shape = in_image_size[0]
        first_layer = True
        
        for item in range(no_blocks):
            if item > 0:
                in_shape = hidden_units
            else:
                in_shape = in_shape
                
            block = [nn.Conv2d(in_channels=in_shape,
                              out_channels=hidden_units,
                              kernel_size=kernel_size_convolution[0],
                              stride=stride_convolution,
                              padding=padding_convolution),
                     nn.LeakyReLU(),
                     nn.Conv2d(in_channels=hidden_units,
                              out_channels=hidden_units,
                              kernel_size=kernel_size_convolution[0],
                              stride=stride_convolution,
                              padding=padding_convolution),                   
                     nn.LeakyReLU(),
                     nn.MaxPool2d(kernel_size=kernel_size_maxpool[0],
                                  stride=stride_maxpool,
                                  padding=padding_maxpool)]

            shape = np.floor(((shape-kernel_size_convolution[0] + 2*padding_convolution) / stride_convolution) + 1)
            shape = np.floor(((shape-kernel_size_convolution[0] + 2*padding_convolution) / stride_convolution) + 1)
            shape = np.floor(((shape-kernel_size_maxpool[0] + 2*padding_maxpool) / stride_maxpool) + 1)
            list_of_blocks.extend(block)


        last_layer = [torch.nn.Flatten(), torch.nn.Linear(in_features=int(shape*shape*hidden_units), out_features=out_shape)]
        list_of_blocks.extend(last_layer)
        self.final_block = torch.nn.Sequential(*list_of_blocks)

        
    def forward(self, X:torch.tensor):
       
        return self.final_block(X)
                
