def transform(legacy_data):
    new_dict = {} 
    for key, value in legacy_data.items():
        for data in value:
            new_dict[data.lower()] = key
    return new_dict
