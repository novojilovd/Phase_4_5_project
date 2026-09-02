import argparse
import sys
from collections import Counter
import validator as vl
import log_reader as lr
import json_module as jm

if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog = 'log_parser.py', description = '''Анализ файла с логом программы''')
    parse.add_argument('filename', help = 'Путь к файлу с логом')
    parse.add_argument('--json-export', default = 0, help = '''Запись результата в JSON (по умолчанию отключено). 
                                                                            Значения 0 или 1''')
    args = parse.parse_args()

    if not vl.path_verify(args.filename):
        print('Указанный вами файл не существует. Проверьте корректность имени и/или пути к файлу.\n')
        print(parse.print_help())
        sys.exit(0)

    counter = Counter()

    with open(args.filename) as f:
        for line in f:
            counter[lr.log_reader(line)] += 1

    print(f'Анализ лог файла {args.filename}:')
    for k, v in counter.items():
        print(f'{k}: {v}')

    result_json = {str(args.filename): dict()}
    result_json[str(args.filename)].update(counter)

    if args.json_export == 1:
        jm.json_export(result_json)


