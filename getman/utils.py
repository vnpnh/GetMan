def extract_query(query: dict) -> str:
    """
    Extract query parameters from a dictionary and return them as a string.

    Args:
        query (dict): A dictionary of query parameters.

    Returns:
        str: A string representation of the query parameters.
    """
    result = ""
    flag = 0
    for key, value in query.items():
        if flag > 0:
            result += "&"
        result += f"?{key}={value}"
        flag += 1

    return result



def all_dict_equal(items: dict) -> bool:
    """
    Check if all values (which are expected to be lists or
     other iterables) in the dictionary have the same length.

    Args:
        items (dict): A dictionary where each value is a list or similar iterable.

    Returns:
        bool: True if all values have the same length, False otherwise.
    """
    lengths = {len(v) for v in items.values()}
    return len(lengths) == 1
