# List 操作練習
nums = [3, 7, 2, 9]

# 請完成：
# 1. 取出第二個元素
num1 = nums.pop(1)
print(num1)
print(nums)
# 2. 將 5 加到尾巴
nums.append(5)
print(nums)
# 3. 印出排序後的結果
print(nums)



# Dict 查詢練習
student = {"name": "Wei", "age": 18, "major": "Data Science"}

# 請完成：
# 1. 印出 name
print(student["name"])
# 2. 更新 age = 19
student["age"] = 19
print(student["age"])
# 3. 新增一個 key: "school" = "University"
student["school"] = "University"
print(student["school"])
print(student)



# Function 練習
def square(n):
    return n ** 2
print(square(2))


"""
Loop 練習
請印出 1~10 的偶數
"""
for i in range(1,11):
    if i % 2 == 0:
        print(i)



# 字串處理練習
s = "I am learning AI"
# 請把句子轉成全大寫
new_s = s.upper()
print(new_s)
