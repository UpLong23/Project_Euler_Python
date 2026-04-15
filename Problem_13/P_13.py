nums = []

file = open('./Problem_13/data.txt', encoding='utf-8')
for line in file: 
    nums.append(int(line))
file.close()


s = sum(nums)

print(str(s)[:10])
