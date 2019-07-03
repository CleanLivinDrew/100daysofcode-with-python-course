NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return(list({name.title() for name in names}))

def reverse(name):
    first, last = name.split()
    return(f'{last} {first}')

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    rev_names = [reverse(name) for name in names]
    rev_names.sort()
    rev_names.reverse()
    flipped = [reverse(name) for name in rev_names]
    return(flipped)
    


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    len_list = [name.split()[0] for name in names]
    return(min(len_list, key=len))

shortest_first_name(NAMES)

