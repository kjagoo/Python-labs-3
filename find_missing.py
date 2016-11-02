def find_missing(a,b):
    
    
    if a==[] and b==[]:
      return 0
    elif a==b:
      return 0
    else:
        
      c = set(a).union(set(b))
      d = set(a).intersection(set(b))
      return list(c - d)[0] 
