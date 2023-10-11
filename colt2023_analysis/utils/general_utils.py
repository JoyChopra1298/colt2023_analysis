def sort_dictionary_by_values(dictionary, reverse=False):
    return [
        (key, value)
        for key, value in
        sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse)
    ]


def sort_dictionary_by_keys(dictionary, reverse=False):
    return [
        (key, value)
        for key, value in
        sorted(dictionary.items(), key=lambda item: item[0], reverse=reverse)
    ]
