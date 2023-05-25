from typing import Union, Any






def arithmetic_arranger(arithmetic_problems, show_answers=False) -> Union[str, Any]:
    """
Create a function that receives a list of strings that are arithmetic problems
and returns the problems arranged vertically and side-by-side.
The function should optionally take a second argument.
When the second argument is set to True, the answers should be displayed.
    :return:
    """
    first_line = second_line = third_line = fourth_line = f''
    result = 0
    arith_prob = list(arithmetic_problems)
    if len(arith_prob) > 5:
        return 'Error: Too many problems.'
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
                resul = first_operand + second_operand
            else:
                result = first_operand - second_operand
        first_line += f'    {" "*(2 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])) - len(next_problem[0]))}{next_problem[0]}'
        second_line += f'    {next_problem[1]}{" "*(1 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])) - len(next_problem[2]))}{next_problem[2]}'
        third_line += f'    {"-"*(2 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])))}'
        if show_answers == True:
            # TODO: Arreglar la cuarta linea que no imprime correctmente
            fourth_line += f'    {" "*(2 + (len(next_problem[0]) if int(next_problem[0]) > int(next_problem[2]) else len(next_problem[2])) - len(str(result)))}{str(result)}'

    return print(first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line)

