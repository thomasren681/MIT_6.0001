# Problem Set 4A
# Name: Thomas Ren
# Collaborators: None
# Time Spent: x: About a quarter to an hours

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    >>> get_permutations('def')
    ['def', 'edf', 'efd', 'dfe', 'fde', 'fed']
    >>> get_permutations('ijk')
    ['ijk', 'jik', 'jki', 'ikj', 'kij', 'kji']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return list(sequence)
    else:
        insert_str = sequence[0]
        sequence = sequence[1:]
        permutation = []
        latter_permutation = get_permutations(sequence)
        for string in latter_permutation:
            string_list = list(string)
            length = len(string)+1
            for i in range(length):
                temp = string_list.copy()
                temp.insert(i,insert_str)
                temp_str = ''.join(temp)
                permutation.append(temp_str)

        return permutation


if __name__ == '__main__':
#    #EXAMPLE
#     example_input = 'abc'
#     print('Input:', example_input)
#     print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#     print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'def'
    print('Input:', example_input)
    print('Expected Output:', ['def', 'edf', 'efd', 'efd', 'fed', 'fde'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'ijk'
    print('Input:', example_input)
    print('Expected Output:', ['ijk', 'jik', 'jki', 'ikj', 'kij', 'kji'])
    print('Actual Output:', get_permutations(example_input))