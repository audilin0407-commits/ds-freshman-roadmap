result = []

for i in range(1, 101):
    # 在這裡加入你的條件
    if i % 3 == 0:
        result.append(i)

print(result)



s = "I love learning data science with AI"
new_s = s.split()
num = 0
for n in new_s:
    num += 1
print(num)
