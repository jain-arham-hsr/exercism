def factors(value):
    factors = []
    val = value
    while val != 1:
        for num in range(2, int(val)+1):
            if (float(val)/float(num)).is_integer():
                val /= num
                factors.append(num)
                break
    return factors