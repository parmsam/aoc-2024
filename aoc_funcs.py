#%%writefile aoc_funcs.py

def read_aoc_input(data: str, data_type: str = 'string'):
    assert isinstance(data, str), f'Invalid data type: {type(data)}. Must be str.'
    assert data_type in ['string', 'int'], f'Invalid type: {type}. Must be int or char. '
    
    data = data.splitlines()
    
    if data_type == 'string':
        data = [list(i) for i in data]
        pass
    elif data_type == 'int':
        data = [i.split() for i in data]
        data = [[int(x) for x in row] for row in data]
    
    return data
