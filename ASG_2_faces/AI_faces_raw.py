from pickle import load, dump
from os.path import join
from os import getcwd



# main path .../
class AI_faces_raw: 
    
    model_dir_path = join(getcwd(), "ASG_2_faces", "models")

    def __init__(self) -> None:
        pass


    @staticmethod
    def load(name: str):
        return load( open(join(AI_faces_raw.model_dir_path, name+".pkl"), 'rb') )

    def save(self, name: str) -> None: 
        with open(join(self.model_dir_path, name+".pkl"), "wb") as f:
            dump(self, f)