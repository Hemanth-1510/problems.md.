def indian_format(num):
    s = f"{num:.10f}".rstrip('0').rstrip('.')  # Handle decimals cleanly
    int_part, _, frac = s.partition('.')
    if len(int_part) <= 3:
        return int_part + ('.' + frac if frac else '')
    head = int_part[:-3]
    last = int_part[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ','.join(parts + [last]) + ('.' + frac if frac else '')

# Input
num = float(input())
print(indian_format(num))
