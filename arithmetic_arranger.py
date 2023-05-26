def arithmetic_arranger(arithmetic_problems: list[str], show_answers: bool = False) -> str:
    """
Create a function that receives a list of strings that are arithmetic problems
and returns the problems arranged vertically and side-by-side.
The function should optionally take a second argument.
When the second argument is set to True, the answers should be displayed.
    :return: A string with the problems arranged vertically and side-by-side.
    """
    first_line = second_line = third_line = fourth_line = f''
    arith_prob = list(arithmetic_problems)
    if len(arith_prob) > 5:
        return 'Error: Too many problems.'
    try:
        for it in range(0, len(arith_prob)):
            next_problem = str(arith_prob[it]).split()
            if next_problem[1] != '+' and next_problem[1] != '-':
                return f'Error: Operator must be \'+\' or \'-\'.'
            elif int(next_problem[0]) > 9999 or int(next_problem[2]) > 9999:
                return f'Error: Numbers cannot be more than four digits.'
            else:
                first_operand = int(next_problem[0])
                second_operand = int(next_problem[2])
                if str(next_problem[1]) == '+':
                    result = first_operand + second_operand
                else:
                    result = first_operand - second_operand
            first_line += f'    {" " * (2 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])) - len(next_problem[0]))}{next_problem[0]}'
            second_line += f'    {next_problem[1]}{" " * (1 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])) - len(next_problem[2]))}{next_problem[2]}'
            third_line += f'    {"-" * (2 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])))}'
            if show_answers:
                fourth_line += f'    {" " * (2 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])) - len(str(result)))}{str(result)}'
    except ValueError:
        return f'Error: Numbers must only contain digits.'
    except IndexError:
        return f'Error: Must enter at least one exercise.'

    return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
