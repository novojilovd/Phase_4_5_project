from os import path

def path_verify(file_path: str) -> bool:
    if path.exists(path.abspath(file_path)):
        return True
    else:
        return False


if __name__ == '__main__':
    pass