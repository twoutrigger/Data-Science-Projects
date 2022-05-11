from sudoku_generator import generate_board
import pulp as plp

def add_default_sudoku_constraints(prob, grid_vars, rows, cols, grids, values):

    # Constraint to ensure only one value is filled for a cell
    for row in rows:
        for col in cols:
                prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][col][value] for value in values]),
                                        sense=plp.LpConstraintEQ, rhs=1, name=f"constraint_sum_{row}_{col}"))


    # Constraint to ensure that values from 1 to 9 is filled only once in a row
    for row in rows:
        for value in values:
            prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][col][value]*value  for col in cols]),
                                        sense=plp.LpConstraintEQ, rhs=value, name=f"constraint_uniq_row_{row}_{value}"))

    # Constraint to ensure that values from 1 to 9 is filled only once in a column
    for col in cols:
        for value in values:
            prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][col][value]*value  for row in rows]),
                                        sense=plp.LpConstraintEQ, rhs=value, name=f"constraint_uniq_col_{col}_{value}"))


    # Constraint to ensure that values from 1 to 9 is filled only once in the 3x3 grid
    for grid in grids:
        grid_row  = int(grid/3)
        grid_col  = int(grid%3)

        for value in values:
            prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[grid_row*3+row][grid_col*3+col][value]*value  for col in range(0,3) for row in range(0,3)]),
                                        sense=plp.LpConstraintEQ, rhs=value, name=f"constraint_uniq_grid_{grid}_{value}"))

def add_diagonal_sudoku_constraints(prob, grid_vars, rows, cols, values):

        # Constraint from top-left to bottom-right - numbers 1 - 9 should not repeat
        for value in values:
                prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][row][value]*value  for row in rows]),
                                            sense=plp.LpConstraintEQ, rhs=value, name=f"constraint_uniq_diag1_{value}"))


        # Constraint from top-right to bottom-left - numbers 1 - 9 should not repeat
        for value in values:
                prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][len(rows)-row-1][value]*value  for row in rows]),
                                            sense=plp.LpConstraintEQ, rhs=value, name=f"constraint_uniq_diag2_{value}"))

def add_prefilled_constraints(prob, input_sudoku, grid_vars, rows, cols, values):
    for row in rows:
        for col in cols:
            if(input_sudoku[row][col] != 0):
                prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][col][value]*value  for value in values]),
                                                    sense=plp.LpConstraintEQ,
                                                    rhs=input_sudoku[row][col],
                                                    name=f"constraint_prefilled_{row}_{col}"))

def extract_solution(grid_vars, rows, cols, values):
    solution = [[0 for col in cols] for row in rows]
    grid_list = []
    for row in rows:
        for col in cols:
            for value in values:
                if plp.value(grid_vars[row][col][value]):
                    solution[row][col] = value
    return solution

def print_solution(solution, rows,cols):
    # Print the final result
    # print(f"\nFinal result:")

    print("\n\n+ ----------- + ----------- + ----------- +",end="")
    for row in rows:
        print("\n",end="\n|  ")
        for col in cols:
            num_end = "  |  " if ((col+1)%3 == 0) else "   "
            print(solution[row][col],end=num_end)

        if ((row+1)%3 == 0):
            print("\n\n+ ----------- + ----------- + ----------- +",end="")

def solve_sudoku(input_sudoku, diagonal = False ):
    # Create the linear programming problem
    prob = plp.LpProblem("Sudoku_Solver")

    rows = range(0,9)
    cols = range(0,9)
    grids = range(0,9)
    values = range(1,10)

    # Decision Variable/Target variable
    grid_vars = plp.LpVariable.dicts("grid_value", (rows,cols,values), cat='Binary')

    # Set the objective function
    # Sudoku works only on the constraints - feasibility problem
    # There is no objective function that we are trying maximize or minimize.
    # Set a dummy objective
    objective = plp.lpSum(0)
    prob.setObjective(objective)

    # Create the default constraints to solve sudoku
    add_default_sudoku_constraints(prob, grid_vars, rows, cols, grids, values)

    # Add the diagonal constraints if flag is set
    if (diagonal):
        add_diagonal_sudoku_constraints(prob, grid_vars, rows, cols, values)

    # Fill the prefilled values from input sudoku as constraints
    add_prefilled_constraints(prob, input_sudoku, grid_vars, rows, cols, values)


    # Solve the problem
    prob.solve()

    # Print the status of the solution
    solution_status = plp.LpStatus[prob.status]
    print(f'Solution Status = {plp.LpStatus[prob.status]}')

    # Extract the solution if an optimal solution has been identified
    if solution_status == 'Optimal':
        solution = extract_solution(grid_vars, rows, cols, values)

        print(f'\n\n\nGenerated Sudoku Board:')
        print_solution(input_sudoku, rows,cols)

        print(f'\n\n\nProposed Solution:')
        print_solution(solution, rows,cols)

# example board for testing
# normal_sudoku = [
#                     [3,0,0,8,0,0,0,0,1],
#                     [0,0,0,0,0,2,0,0,0],
#                     [0,4,1,5,0,0,8,3,0],
#                     [0,2,0,0,0,1,0,0,0],
#                     [8,5,0,4,0,3,0,1,7],
#                     [0,0,0,7,0,0,0,2,0],
#                     [0,8,5,0,0,9,7,4,0],
#                     [0,0,0,1,0,0,0,0,0],
#                     [9,0,0,0,0,7,0,0,6]
#                 ]

board = generate_board()

solve_sudoku(input_sudoku=board, diagonal=False)
