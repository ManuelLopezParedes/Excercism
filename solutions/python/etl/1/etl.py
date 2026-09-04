def transform(legacy_data):
    new_dict = {} 
    for key, value in legacy_data.items():
        for data in value:
            new_dict[data.lower()] = key
    return new_dict

print(transform({1: ['A', 'E', 'I', 'O', 'U', 'L'], 
       2: ['D', 'G'], 
       3: ['B', 'C', 'M', 'P'], 
       4: ['F', 'H', 'V', 'W', 'Y']}))