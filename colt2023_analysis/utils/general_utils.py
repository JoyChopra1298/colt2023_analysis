def sort_dictionary_by_values(dictionary):
    return {
        key: value for key, value in sorted(dictionary.items(), key=lambda item: item[1])
    }
