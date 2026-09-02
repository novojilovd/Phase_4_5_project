import re

def log_reader(line: str) -> str:
    try:
        result = re.search(' (INFO|ERROR|WARNING) ', line)
    except TypeError:
        result = None

    if result is not None:
        return str(result.group(0))
    else:
        return 'Lines with parse error'

if __name__ == '__main__':
    pass