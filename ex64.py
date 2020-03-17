import os.path, time

def get_c_m_file(filename):
    print("last modified : %s" % time.ctime(os.path.getmtime(filename)))
    print("Created: %s" % time.ctime(os.path.getctime(filename)))

get_c_m_file("ex30.py")
