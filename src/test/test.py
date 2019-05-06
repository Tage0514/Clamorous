list1=[('a', 'b', 'c', 1), ('a', 'e', 'f', 2)]
tuple1=('a', 'b', 'c')
 #如何判断tuple1是list1[0]的子集

 
d_dict = {}
for i in list1:
    d_dict[i[:3]] = i[-1]

if tuple1 in d_dict.keys():
    print(d_dict[tuple1])



def judge(data,temp):
