#for 문 한방에 쓰기
a_list = [1,3,2,5,1,2]

# b_list = []
# for a in a_list:
#     b_list.append(a*2)
    
b_list = [a*2 for a in a_list] #a_list 돌리는데 그거에2배해서 b_list에 넣어줘라
print(b_list)

