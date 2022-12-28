from pickle import load, dump
from os.path import join
from os import getcwd
from keras.applications.vgg16 import *
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import image_dataset_from_directory
from keras.layers import Dense, Flatten, Input
from keras import Sequential
from keras.optimizers import Adam
from math import pow
from numpy import argmax
import matplotlib.pyplot as plt
from tensorflow import Tensor
from tensorflow import data

class AI_raw: 
    
    project_folder_path = join(getcwd(), "ASG_2_faces")
    model_dir_path = join(getcwd(), "ASG_2_faces", "models")
    train_data = join(project_folder_path, "faces", "train")

    def __init__(self, layers: int = 6) -> Sequential:

        self.model = Sequential( [ Input(shape = (35, 35)), Flatten( input_shape = (35,35) ) ] )

        divider = pow(35*35, 1.0/layers) # sqrt_layers( image size )
        layer_size = 35*35
        for _ in range(layers):
            if layer_size//divider > 2:
                layer_size //= divider
                self.model.add( Dense( layer_size, activation="relu") ); continue
            else: 
                self.model.add( Dense( 2, activation="sigmoid") ); break # final layer

        self.model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(0.001), metrics=['acc'])

        return self.model

    @staticmethod
    def load(name: str):
        return load( open(join(AI_raw.model_dir_path, name+".pkl"), 'rb') )

    def save(self, name: str) -> None: 
        with open(join(self.model_dir_path, name+".pkl"), "wb") as f:
            dump(self, f)

model: Sequential = AI_raw(5)
model.fit()

#model.compile()
model.summary()

        # self.data: data.Dataset = image_dataset_from_directory(
        #     AI_raw.train_data, 
        #     labels="inferred", 
        #     color_mode="grayscale",
        #     image_size=(35,35)
        #     )
        # print(self.data.get_single_element())
        