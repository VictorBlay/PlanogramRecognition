def convert(*args):
    """
    Returns a list of tuples generated from multiple lists and tuples
    """
    for x in args:
        if not isinstance(x, list) and not isinstance(x, tuple):
            return []

    size = float("inf")
    
    for x in args:
        size = min(size, len(x))
        
    result = []
    
    for i in range(size):
        result.append(tuple([x[i] for x in args]))
        
    return result