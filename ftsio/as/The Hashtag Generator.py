def generate_hashtag(s):
    nlist = s.split()
    if len(nlist) > 140 or not (s):
        return False
    
    
    h = '#'
    for word in nlist:
        h += word.title()
        
    if len(h) > 140 or not (s):
        return False
    return h 