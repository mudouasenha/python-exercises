from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/home/matheus.gomes') if isfile(join('/home/matheus.gomes', f))]

print(files_list)
