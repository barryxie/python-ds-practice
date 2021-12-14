def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # return [item for item in lst if item]    

    output = []
    for item in lst:
        if item: 
            output.append(item)
    return output                 
    
            