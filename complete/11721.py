string_input = input()
length_input = len(string_input)
for i in range(1,length_input):
    print(string_input[i*10-10:i*10])
length_input = length_input//10