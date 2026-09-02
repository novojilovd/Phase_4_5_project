from log_reader import log_reader
import pytest

def test_log_reader_none() -> None:
    assert not log_reader('') is None, 'Функция log_reader может вернуть None'

def test_log_reader_empty() -> None:
    assert log_reader('TESTERRORTEST') == 'ERROR', 'В функции log_reader нет проверки на границы слова'

def test_log_reader_typeerror() -> None:
    assert isinstance(log_reader(123), str), 'В функцию log_reader нет обработки не строковых литералов'
