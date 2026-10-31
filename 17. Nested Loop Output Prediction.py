""" Nested Loop Output Prediction
Predict the exact output without executing the code.

for i in range(1,5):
    for j in range(1,5):
        if i * j > 6:
            break
        if(i + j)%2 == 0:
            continue
        print(i, j, end="|")
    print()""""

#Answer
"""1 2|1 4|
2 1|2 3|
3 2|
4 1|"""
