num_list=[]
for i in range(1,26):
     num_list.append(i)
print(num_list)

 result=""
 start=0
 end=5
 for i in range(5):
     for j in range(start,end):
         result = result+" "+str(num_list[j])
     result=result+"\n"
     start = start + 5
     end = end + 5

print(result)

total = 0
for num in range(1001):
    if num%2==0 and num%5 !=0:
        total += num

print(total)
