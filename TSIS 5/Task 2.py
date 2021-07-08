import os


def get_parent_directory(dir_path: str):
    home = '/home/'
    if dir_path[1:-1].split('/')[0] == 'home' and dir_path[1:-1].split('/')[1] == '':
        return home
    for direct in dir_path[1:-1].split('/')[1:len(dir_path[1:-1].split('/')) - 1]:
        home += direct + '/'
    return home


def main(path):
    while True:
        counter = 0
        files_dict = dict()
        for i in os.listdir(path):
            counter += 1
            files_dict[counter] = i

        for k, v in files_dict.items():
            print(k, " > ", v)
        file_number = int(input("Number of file/directory(you can write 0 "
                                "for went to parent directory and -1 for exit from program): "))
        if file_number == 0:
            path = get_parent_directory(path)
            main(path)
        if file_number == -1:
            print("Goodbye :)")
            exit(0)
        try:
            file_path = path + files_dict[file_number]
            if os.path.isdir(file_path):
                file_path += "/"
                while True:
                    directories = next(os.walk(file_path))[1]
                    files = next(os.walk(file_path))[2]
                    print("1: Rename directory, 2: print number of files, "
                          "3: print number of directories, 4: list content of the directory",
                          "5: add file to this directory, 6: add new directory to this directory,"
                          "7: cancel menu, 8: back to parent directory")
                    option = int(input())
                    if option == 1:
                        new_name = input("Get a new name: ")
                        os.rename(file_path, file_path.replace(file_path.split('/')[-2], new_name))
                        file_path = file_path.replace(file_path.split('/')[-2], new_name)
                    elif option == 2:
                        print(len(directories))
                    elif option == 3:
                        print(len(files))
                    elif option == 4:
                        for i in os.listdir(file_path):
                            print(i)
                    elif option == 5:
                        new_name = input("Get a name of file: ")
                        with open(os.path.join(file_path, new_name), 'w') as fp:
                            pass
                    elif option == 6:
                        new_name = input("Get a name of directory: ")
                        os.mkdir(file_path + "/" + new_name)
                    elif option == 7:
                        break
                    elif option == 8:
                        path = get_parent_directory(file_path)
                        main(path)
                path = file_path
            elif os.path.isfile(file_path):
                while True:
                    print("1: delete file, 2: rename file, "
                          "3: add content to this file, 4: rewrite content of this file",
                          "5: return to the parent directory, 6: cancel menu")
                    option = int(input())
                    if option == 1:
                        os.remove(file_path)
                        main(get_parent_directory(file_path))
                    elif option == 2:
                        new_name = input("New file name")
                        os.renames(file_path, get_parent_directory(file_path) + new_name)
                        file_path = get_parent_directory(file_path) + new_name
                    elif option == 3:
                        with open(file_path, "a") as file_object:
                            append_text = input()
                            file_object.write(append_text)
                    elif option == 4:
                        with open(file_path, "w") as file_object:
                            append_text = input()
                            file_object.write(append_text)
                    elif option == 5:
                        path = get_parent_directory(file_path)
                        main(path)
                    elif option == 6:
                        break
                path = get_parent_directory(file_path)
        except KeyError:
            Exception("Введите корректный номер файла/директория")


if __name__ == '__main__':
    path = '/home/'  # for unix based os
    # path = 'C/' # for windows based os
    print("Welcome to my own far manager, let's start?\n")
    option = input("Yes/No: ")
    if option == "Yes" or option == "Y" or option == "yes" or option == 'y':
        main(path)
    else:
        print("Ok, goodbye:)")
        exit(0)
