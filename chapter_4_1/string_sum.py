n = int(input())
first_string = [str(char) for char in input()]
seconds_string = [str(char) for char in input()]

result_string = []

for i in range(n):
    result_string.append(first_string[i])
    result_string.append(seconds_string[i])

print("".join(result_string))
