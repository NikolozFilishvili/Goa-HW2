def permutations(s):
    ls = set([s])
    if len(s) == 2:
        ls.add(s[1] + s[0])

    elif len(s) > 2:
        for i, num in enumerate(s):
            for ss in permutations(s[:i] + s[i+1:]):
                ls.add(num + ss)
                
    return list(ls)            