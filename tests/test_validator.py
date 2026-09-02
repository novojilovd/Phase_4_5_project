import validator

def test_file_path_validator():
    assert not validator.path.exists(''), '''
    При отсутствии переданого пути к файлу, путь считается корректным
    '''

def test_dir_exists_validator():
    assert validator.path.isdir(validator.path.abspath('')), '''
    При передаче пустого пути к файлу, абсолютный путь не считается директорией
    '''

