from pathlib import Path


def read_file_get_list(path_file: Path):
    with open(path_file, "r") as file:
        return file.readlines()
