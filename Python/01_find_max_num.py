def find_max_num(array):
    max_number = array[0]

    for i in range(1, len(array)):
        if array[i] > max_number:
            max_number = array[i]

    return max_number


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
