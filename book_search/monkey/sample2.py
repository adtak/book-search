from book_search.monkey import depends


def my_function():
    return depends.get_text()
