# TODO 1 - read from input
#      2 - unitary test for every function
#      3 - look for optimization in storage space and execution time 

input1 = "a/3, a/4, a/128, a/129, b/65, b/66, c/1, c/10, c/42".replace(',', '')
input2 = "a/1, a/2, a/3, a/4, a/5, a/126, a/127, b/100, c/2, c/3, d/1".replace(',', '') 

def store(string):
    uniq_ids = []
    ids_dict = {}

    for e in string.split():
        (idu, nbr) = e.split('/')
        if idu not in uniq_ids:
            uniq_ids.append(idu)
        if idu not in ids_dict.keys():
            ids_dict[idu] = set()
        ids_dict[idu].add(int(nbr))
    return uniq_ids, ids_dict

def compare(string1, string2):
    if len(string1) < len(string2):
        return -1
    elif len(string1) > len(string2):
        return 1
    elif len(string1) == len(string2):
        if string1 < string2:
            return -1
        elif string1 > string2:
            return 1
        else:
            return 0

def merge(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
       if compare(a[i], b[j]) == -1:
            result.append(a[i])
            i += 1
       elif compare(a[i], b[j]) == 1: 
            result.append(b[j])
            j += 1
       else:
            if a[i] not in result:
                result.append(a[i])
            i += 1
            j += 1
    result += a[i:] + b[j:]
    return result
    
def put_everything_in_place():
    (uids1, ids_vals1) = store(input1)
    (uids2, ids_vals2) = store(input2)

    uids = merge(uids1, uids2)
    uid_vals = {}
    for id in uids:    
        s = list()
        if ids_vals1.has_key(id) and ids_vals2.has_key(id):
            s = ids_vals1[id].union(ids_vals2[id])
        elif ids_vals1.has_key(id):
            s = ids_vals1[id]
        elif ids_vals2.has_key(id):
            s = ids_vals2[id]
    
        if s <> list():
            s = sorted(list(s))
        uid_vals[id] = s

	# print it
        for e in uid_vals[id]:
            print "%s/%d, "%(id, e),

put_everything_in_place()
    





    
