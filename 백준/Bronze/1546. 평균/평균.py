N = int(input())
scores = list(map(float, input().split()))
maxV = -1
for score in scores:
    if score > maxV:
        maxV = score
for i in range(len(scores)):
    scores[i] = scores[i] / maxV * 100
avg = sum(scores) / N
print(avg)