result = [i for i in range(1, 101) if i % 3 == 0]
print(result)



scores = [55, 78, 90, 62, 88]
new_scores = [min(num + 5, 100) for num in scores]
print(new_scores)



passed = [ok for ok in scores if ok >= 60]
print(passed)
