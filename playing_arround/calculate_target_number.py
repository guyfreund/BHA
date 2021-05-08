from copy import deepcopy


def can_calculate(numbers, accumulator, target_number, expression):
    if not numbers:
        if accumulator == target_number:
            print('match: (0' + expression + ')')
            return True

        return False

    expressions = [False]

    for number in numbers:
        new_numbers = deepcopy(numbers)
        new_numbers.remove(number)

        if all([
            accumulator != 0,
            number != 0,
            number != 1,
            accumulator % number == 0
        ]):
            div_exp_str = "(" + expression + f"/{number})"
            div_exp = can_calculate(new_numbers, accumulator / number, target_number, div_exp_str)
            expressions.append(div_exp)

        if accumulator != 0:
            mul_exp_str = "(" + expression + f"*{number})"
            mul_exp = can_calculate(new_numbers, accumulator * number, target_number, mul_exp_str)
            expressions.append(mul_exp)

        add_exp_str = "(" + expression + f"+{number})"
        add_exp = can_calculate(new_numbers, accumulator + number, target_number, add_exp_str)
        expressions.append(add_exp)

        dec_exp_str = "(" + expression + f"-{number})"
        dec_exp = can_calculate(new_numbers, accumulator - number, target_number, dec_exp_str)
        expressions.append(dec_exp)

    return any(expressions)


def main():
    numbers = [1, 2, 3, 4]
    target_number = 222
    print(can_calculate(numbers, 0, target_number, ""))


if __name__ == "__main__":
    main()
