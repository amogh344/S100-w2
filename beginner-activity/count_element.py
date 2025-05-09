li = [1,2,3,4,5,6,7,8,9,10,2,3,3,3]
def most_frequent(li):
    count = {}
    for i in li:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max = max(count, key=count.get)
    return max

print("Most frequent element is:", most_frequent(li))