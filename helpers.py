from copy import copy
from mappings import *

def split_row(row):
    new_row = copy(row)
    and_split = map(lambda x: x.strip(), new_row[3].split('&'))

    if len(and_split) > 1:
        space_split = and_split[0].split(' ')

        if len(space_split) < 2:
            space_split[0] += ' {}'.format(and_split[1].split(' ')[1])
            and_split[0] = space_split[0]

    new_row[3] = and_split

    return new_row

def do_mapping(mappings, rows, target_row):
    pointer = 0
    for row in rows:
        for map_idx in mappings:
            mapping = mappings[map_idx]
            if mapping['source_idx'] >= len(row) or pointer >= len(mapping['target_idxes']):
                continue
            target_idx = mapping['target_idxes'][pointer]
            target_row[target_idx] = row[mapping['source_idx']]

        pointer += 1

def map_house(last_name, house):
    target_row = ['' for x in xrange(61)]
    target_row[0] = last_name.strip()
    parents = map(lambda x: [x.split(' ')[0], ' '.join(x.split(' ')[1:])], list(set([j for i in house['rows'] for j in i[3]])))
    addresses = map(lambda x: x.split('%,%'), list(set(['{0}%,%{1}%,%{2}%,%{3}'.format(x[4],x[5],x[6],x[7]) for x in house['rows']])))

    # add phone numbers
    for i in range(len(house['rows'])):
        if i >= len(parents):
            continue
        parent = parents[i]
        email = house['rows'][i][8]
        phone_number = house['rows'][i][9]
        while len(parent) < 2:
            parent.append('')
        parent.append(email)
        parent.append(phone_number)

    # map students
    do_mapping(STUDENT_MAPPINGS, house['rows'], target_row)

    #map parents
    do_mapping(PARENT_MAPPINGS, parents, target_row)

    # map addresses
    do_mapping(ADDRESS_MAPPINGS, addresses, target_row)

    return target_row
