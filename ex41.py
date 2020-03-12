import os.path

def check_file_exists(file):
    print(os.path.isfile(file))


check_file_exists('ex38.py')
check_file_exists('teste.yyyyy')
