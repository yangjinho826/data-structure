def josephus_problem(n, k):
    result_arr = []
    people_arr = [number for number in range (1, n+1)] 
    next_index = k - 1

    while people_arr:
        result = people_arr.pop(next_index)
        result_arr.append(result)

        if len(people_arr) != 0:
            next_index = (next_index + (k-1)) % len(people_arr)
            
    print("<", ", ".join(map(str, result_arr)), ">", sep='')

# n, k = map(int, input().split())
josephus_problem(7, 3)