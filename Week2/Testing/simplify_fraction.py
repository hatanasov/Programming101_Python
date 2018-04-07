def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    for digit in range(1, nominator + 1):
        if nominator % digit == 0 and denominator % digit == 0:
            nominator //= digit
            denominator //= digit
    return (nominator, denominator)

