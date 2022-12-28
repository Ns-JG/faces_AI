from os import getcwd, listdir
from os.path import join
from keras.preprocessing.image import ImageDataGenerator


PATH = "/Users/Ns-JG/Desktop/Programowanie/python/AI projects Python/CyberTech/Materiały edukacyjne/Datasets/faces"
# non_smile_folder = join(PATH, "non_smile")
# smile_folder = join(PATH, "smile")
# print(f"non smile folder images count: {listdir(non_smile_folder).__len__()}")
# print(f"smile folder images count: {listdir(smile_folder).__len__()}")

smile_folder_data = ImageDataGenerator()
# non smile: picture format 35x35x603
# smile: picture format 35x35x600