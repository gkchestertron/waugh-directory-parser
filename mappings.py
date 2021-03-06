# maps index from source array to the column index in the MySchoolAnywhere template
STUDENT_MAPPINGS = {
    'First Name'      : { 'source_idx': 0, 'target_idxes': [31,35,39,43,47]},
    'Grade'           : { 'source_idx': 2, 'target_idxes': [32,36,40,44,48]}}

PARENT_MAPPINGS = {
    'First Name'      : { 'source_idx': 0, 'target_idxes': [1,6,16,21]},
    'Last Name'       : { 'source_idx': 1, 'target_idxes': [2,7,17,22]},
    'Primary Email'   : { 'source_idx': 2, 'target_idxes': [5,10,20,25]},
    'Parent Phone'    : { 'source_idx': 3, 'target_idxes': [3,8,18,23]},
}

ADDRESS_MAPPINGS = {
    'Mailing Address' : { 'source_idx': 0, 'target_idxes': [11,26]},
    'City'            : { 'source_idx': 1, 'target_idxes': [12,27]},
    'State'           : { 'source_idx': 2, 'target_idxes': [13,28]},
    'Zip code'        : { 'source_idx': 3, 'target_idxes': [14,29]}}
