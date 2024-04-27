def isIso(s,t):
    if len(s) != len(t):
        return False

    s_t, t_s = {}, {}

    for schar, tchar in zip(s, t):
        
        if (schar in s_t and s_t[schar] != tchar) or (tchar in t_s and t_s[tchar] != schar):
                return False


        s_t[schar] = tchar
        t_s[tchar] = schar

    return True
        








s = "egg"
t = "add"
print(isIso(s,t))
