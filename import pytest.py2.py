import pytest

def get_unique_elements(input_list):
    """Возвращает список уникальных элементов из входного списка с использованием set."""
    return list(set(input_list))

def test_empty_list():
    assert get_unique_elements([]) == []

def test_list_with_duplicates():
    assert sorted(get_unique_elements([1, 2, 2, 3, 4, 4, 5])) == sorted([1, 2, 3, 4, 5])

def test_list_without_duplicates():
    assert sorted(get_unique_elements([1, 2, 3, 4, 5])) == sorted([1, 2, 3, 4, 5])

def test_list_with_mixed_types():
    assert sorted(get_unique_elements([1, 'a', 1, 'b', 'a', 2])) == sorted([1, 'a', 'b', 2])

def test_list_with_none():
    assert sorted(get_unique_elements([None, 1, None, 2])) == sorted([None, 1, 2])

