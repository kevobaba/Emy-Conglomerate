import os

def main():
    i = 0
    path = "C:/Users/chukwuemeka/Desktop/common wealth scholarship letters/"
    for folder in os.listdir(path):
        my_dest = "Chucks" + str(i) + ".XML" + ".Doc"
        my_source =path + folder
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if  __name__ == '__main__':
     main() 