num = int(input())
people = []
for _ in range(num):
    a,b = input().split(" ")
    people.append([int(a),b])
people.sort(key=lambda x: x[0])
# print(people)
for i in range(num):
    print(people[i][0],people[i][1])