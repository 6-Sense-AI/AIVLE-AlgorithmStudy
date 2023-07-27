## 반복문 간격 썼는데 왜 안댐~~~ 개열받잖슴~~

answer = ''

sentences = [list(input()) for _ in range(5)]

for i in range(len(sentences)):
  for j in range(0,len(sentences),5): 
    answer += sentences[i][j]

print(sentences)
print(answer)

