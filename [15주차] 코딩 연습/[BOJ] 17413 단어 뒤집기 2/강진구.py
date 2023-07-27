s_lst = input().strip().split('>')

ans = ''

tag = {}
word = {}

for i,s in enumerate(s_lst):
    for j,t in enumerate(s.split('<')):
        if j%2==0:
            if t != '':
                word[i+j] = t
        else:
            if i != 0:
                tag[i+j] = t
            else:
                tag[i] = t

w_max = max(word.keys())
t_max = max(tag.keys())

m = max(w_max, t_max)

for i in range(m+1):
    if i in tag.keys():
        ans += '<'
        ans += tag[i]
        ans += '>'
    else:
        l = len(word[i].split())
        for j,w in enumerate(word[i].split()):
            if j < l-1:
                ans += w[::-1]
                ans += ' '
            else:
                ans += w[::-1]

print(ans)
# for s in s_lst:
#     if '<' in s:
#         lst = s.split('<')
#         for i,l in enumerate(lst):
#             if i%2 == 0:
#                 l_ = len(l)
#                 for idx,j in enumerate(l.split()):
#                     if idx < l_-1:
#                         ans += j[::-1]
#                         ans += ' '
#                     else:
#                         ans += j[::-1]
#                 ans += '<'
#             else:
#                 ans += l
#         ans += '>'
#     else:
#         lst = s.split()
#         for l in lst:
#             ans += l[::-1]
#             ans += ' '

# print(ans)
