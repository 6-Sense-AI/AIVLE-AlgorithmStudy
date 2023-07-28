S = input().strip()

ans = ''

i = 0
l = len(S.split())

while i < len(S):
    if S[i] == '<':
        while i < len(S) and S[i] != '>':
            ans += S[i]
            i += 1
    elif S[i] == '>':
        ans += '>'
        i += 1
    else:
        if S[i] != ' ':
            s = ''
            while i < len(S) and S[i] != ' ' and S[i] != '<':
                s += S[i]
                i += 1
            ans += s[::-1]
        else:
            ans += ' '
            i += 1
    
print(ans)
