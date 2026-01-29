import os
#original_position = os.getcwd()
#path_to_folder = 
def go_places(pathway):
    original_location = os.getcwd()
    os.chdir(pathway)
    print(os.listdir())
    os.chdir(original_location)