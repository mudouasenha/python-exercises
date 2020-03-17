import os
def get_abs_path(filename):
    return os.path.abspath(filename)

print(get_abs_path("ex61.py"))
