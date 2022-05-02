data = []
with open('reviews.txt', 'r') as f: # C:/Users/oldbi/iCloud/test/review.py
    for line in f:
        data.append(line)


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), ' 筆留言長度小於100')
print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print(good)
print('一共有', len(good), ' 筆留言提到good')
