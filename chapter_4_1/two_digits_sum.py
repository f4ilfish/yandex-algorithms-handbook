def sum_of_two_digits(first_digit: int, second_digit: int) -> int:
    return first_digit + second_digit


a, b = map(int, input().split())

print(str(sum_of_two_digits(a, b)))
