def arithmetic_arranger(problems, solution=False):
    problems_list = [i.split() for i in problems]   #split all problems
    problems_set = set(sum(problems_list, []))      #set to difference '+', '-'
    numbers_set = problems_set.difference('+', '-') #set of numbers
    arranged_problems=''
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
    elif ('/' or '*') in problems_set:
        arranged_problems = "Error: Operator must be '+' or '-'."
    elif not all(set([num.isdigit() for num in numbers_set])):
        arranged_problems = "Error: Numbers must only contain digits."
    elif not all(set([len(num) < 5 for num in numbers_set])):
        arranged_problems = "Error: Numbers cannot be more than four digits."


    else:   #return problems list
        str_max_len = []
        for n in range(len(problems)):  # add first line
            str_max_len += str(len(problems_list[n][0])) if len(problems_list[n][0]) > len(problems_list[n][2]) \
                else str(len(problems_list[n][2]))
            arranged_problems += f"{problems_list[n][0]:>{int(str_max_len[n])+2}s}"+' '*4
        arranged_problems = arranged_problems.rstrip()+'\n'     # del all rights spaces

        for n in range(len(problems)):  # add second line
            arranged_problems += problems_list[n][1] + f"{problems_list[n][2]:>{int(str_max_len[n])+1}s}"+' '*4
        arranged_problems = arranged_problems.rstrip() + '\n'   # del all rights spaces

        for n in range(len(problems)):  # add ------ line
            arranged_problems += '-' * (int(str_max_len[n])+2) + ' '*4
        arranged_problems = arranged_problems.rstrip() # del all rights spaces

        if solution:    # return problems + result
            arranged_problems += '\n'
            solution_list = [eval(i) for i in problems]
            for n in range(len(solution_list)):  # add result line
                arranged_problems += f"{solution_list[n]:>{int(str_max_len[n]) + 2}n}" + ' ' * 4
            arranged_problems = arranged_problems.rstrip()  # del all rights spaces

    return arranged_problems