# Print natural numbers from less than 10
# i = 0
# while i<10:
#     print(i)
#     i=i+1

# while using some condition

# num = 0
# while num<10:
#     if num != 5:
#         print(num)
#     num += 1

# while loop using break keyword
# print("********   while loop using break keyword   *************")
# i=0
# while i<10:
#     if i == 6:
#         break
#     print(i)
#     i+=1

print("********   while loop using continue keyword   *************")

i = 1
while i<10:
    if i == 7:
        i = i+1
        continue
    print(i)
    i+=1