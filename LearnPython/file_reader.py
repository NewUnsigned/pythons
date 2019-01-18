
def read_file(path):
    if path:
        with open(path) as file_object:
            contents = file_object.readlines()
            return contents
    else:
        print("The path is empty!")


def read_pi():
    contents = read_file('text_files/pi_digits.txt')
    print(contents)


def read_learning():
    contents = read_file('text_files/learning_python.txt')
    print(contents)
    for line in contents:
        string = line.replace("Python", "C")
        print(string)


read_pi()
read_learning()
