def fast_modular_exponentiation(a, b, n):
    """Finds the result of a^b mod n."""
    binary = ''
    power = 0
    mods_powers = {}
    while b >= 2 ** power:
        power += 1
    #Finds the binary representation of b
    for p in range(power - 1, -1, -1):
        if b >= 2 ** p:
           binary += '1'
           b -= 2 ** p
        else:
           binary += '0'
    #Stores a to the powers of two
    mods_powers[0] = a % n
    for exp in range(1, power):
        mods_powers[exp] = (mods_powers[exp - 1] ** 2) % n

    result = 1
    #Multiplies result by values in mods_powers based on the binary of b
    for key in range(0, len(binary)):
        if binary[-1 - key] == '1':
            result *= mods_powers[len(binary) - key]

    return result % n
