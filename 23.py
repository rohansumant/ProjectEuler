def abundant(n):
    sum = 1
    i = 2
    while i*i <= n:
        if n%i == 0:
            sum += i + (0 if i == n//i else n//i)
            if sum > n:
                return True
        i += 1
    return sum > n


def non_ab_nums():
    ab_nums = [i for i in range(2, 28124) if abundant(i)]

    s = set(range(1, 28124))
    for i in range(len(ab_nums)):
        for j in range(len(ab_nums)):
            ab_sum = ab_nums[i] + ab_nums[j]
            if ab_sum in s:
                s.remove(ab_sum)

    print(sum(s))

non_ab_nums()
