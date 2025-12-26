def minion_game(string):
    string = string.upper()
    k = 0
    s = 0
    v = "AEIOU"
    
    for i in range(len(string)):
        if string[i] in v:
            k += len(string)-i
        else:
            s += len(string)-i
            
    if k > s:
        print("Kevin", k)
    elif s > k:
        print("Stuart", s)
    else:
        print("Draw")
