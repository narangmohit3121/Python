import os


def list_dir(file_path:str) -> None:

    def list_files(dir: str) -> None:
        files = os.listdir(dir)
        cur_dir = os.path.curdir
        print(cur_dir)
        # print(files)
        nonlocal tab_separator
        for file in files:
            # nonlocal tab_separator
            if os.path.isdir(file):
                tab_separator += 1
                dir = os.path.join(cur_dir, file)
                print("\t" * tab_separator, dir)
                list_files(dir)
            else:
                dir = os.path.join(cur_dir, file)
                print("\t"*tab_separator, dir)

    tab_separator = 0
    if os.path.exists(file_path):
        list_files(file_path)
    else:
        print("Path not found")





list_dir(".")