from search_algorithms import binary_search, insertion_sort


def test_sort_keeps_duplicates():
    assert insertion_sort([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_binary_search_handles_edges():
    values = [1, 4, 7, 10]
    assert binary_search(values, 1)
    assert binary_search(values, 10)
    assert not binary_search(values, 5)
