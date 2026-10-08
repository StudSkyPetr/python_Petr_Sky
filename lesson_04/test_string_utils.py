import pytest

str = " "

from string_utils import StringUtils

string = StringUtils()

def test_capitalize_positive():
    string = StringUtils()
    assert string.capitalize("semafor") == "Semafor"
"""Позитивный тест: все условия соблюдены, первый символ меняется с прописной на заглавную"""

def test_capitalize_negative():
    string = StringUtils()
    assert string.capitalize("Semafor") == "Semafor"
"""Позитивный тест: все условия соблюдены, первый символ не меняется, остается заглавным"""

def test_capitalize_none():
    string = StringUtils()
    assert string.capitalize("") == ""
"""Негативный тест: на входе пустая строка"""

@pytest.mark.parametrize ('str', [" Faraon", "    Faraon"])
def test_trim_positive(str):
    string = StringUtils()
    assert string.trim(str) == "Faraon"
"""Позитивный тест: функция удаляет один или несколько пробелов в начале строки"""

def test_trim_negative():
    string = StringUtils()
    assert string.trim("semafor") == "semafor"
"""Негативный тест: в начале строки на входе нет пробелов"""

def test_conteins_positive():
    string = StringUtils()
    assert string.contains("semafor", "s") is True
"""Позитивный тест: функция нашла символ в строке"""

def test_conteins_negative():
    string = StringUtils()
    assert string.contains("semafor", "k") is False
"""Негативный тест: функция не нашла нужный символ в строке"""

def test_conteins_negative_none():
    string = StringUtils()
    assert string.contains("", " ") is False
"""Негативный тест: функция ищет пробел в пустой строке"""

def test_delete_symbol_positive():
    string = StringUtils()
    assert string.delete_symbol("Ssemafor", "s") == "Semafor"
#    assert string.delete_symbol("str", "simb") == "semfor"

def test_delete_symbol_positive():
    string = StringUtils()
    assert string.delete_symbol("KarapuzPro", "Pro") == "Karapuz"
"""Позитивные тесты (delete): функция нашла и удалила нужный или нужные символы"""

def test_delete_symbol_negative():
    string = StringUtils()
    assert string.delete_symbol("semafor", "t") == "semafor"
"""Негативный тест: функция не нашла символ, строка не изменилась"""
