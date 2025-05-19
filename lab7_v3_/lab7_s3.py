# import unittest

def build_tabl(needle):
    m = len(needle)
    alph = set(needle)
    transit = [{} for _ in range(m + 1)]

    for q in range(m + 1):
        for a in alph:
            k = min(m, q + 1)
            while k > 0 and not (needle[:k] == (needle[:q] + a)[-k:]):
                k -= 1
            transit[q][a] = k
    return transit

def matcher(H_stack, needle):
    if not needle or not H_stack:
        return []

    transit = build_tabl(needle)
    state = 0
    rslt = []

    for i in range(len(H_stack)):
        a = H_stack[i]
        if a in transit[state]:
            state = transit[state][a]
        else:
            state = 0
        if state == len(needle):
            rslt.append(i - len(needle) + 1)
    
    return rslt


if __name__ == "__main__":
    
    H_stack = input("H_stack : ")
    
    needle = input("needle : ")
    
    indexes = matcher(H_stack, needle)
    
    print("Finded (position) : ", indexes)
    