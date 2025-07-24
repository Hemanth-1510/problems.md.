def is_overlap(m1, m2):
    l1, r1 = m1['positions']
    l2, r2 = m2['positions']
    overlap = max(0, min(r1, r2) - max(l1, l2))
    return overlap > (r2 - l2) / 2

def combine_lists(list1, list2):
    merged = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []
    for curr in merged:
        if not result:
            result.append(curr)
        elif is_overlap(result[-1], curr):
            result[-1]['values'] += curr['values']
        else:
            result.append(curr)
    return result

# Input
import json
list1 = json.loads(input())  # Ex: [{"positions":[0,5],"values":[1,2,3]}]
list2 = json.loads(input())  # Ex: [{"positions":[4,8],"values":[4,5]}]
print(combine_lists(list1, list2))
