def largest_number(numbers):
    largest_even = None
    for num in numbers:
        if num % 2 == 0 and (largest_even is None or num > largest_even):
            largest_even = num
    print(largest_even)
    return largest_even


numbers=[3, 7, 11, 4, 6, 8]
largest_number(numbers)


