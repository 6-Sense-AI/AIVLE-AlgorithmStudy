string = input()
str_list = []
answer = ''
for i in string:
   
    str_list.append(i)

print(str_list)
tag = []
back = []
for i in range(len(str_list)):
  ## 태그 있는 거 넣기
  if str_list[i]=="<":
    
    while str_list[i] !=">":
      tag.append(str_list[i])
      i+=1
    tag.append(">")

  if str_list[i] == ">":
    while str_list[i] !="<":
      back.append(str_list[i])
      i+=1
 
    

print(back)
