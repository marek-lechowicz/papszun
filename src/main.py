from Numberjack import *
from utilities import *
from generator import *
from read_input_file import *

s_0, m_tc, m_te, m_st = read_input_file('problems\working.txt')

model, workflow_trace, process_states, last_task_index = get_model(
    s_0, m_tc, m_te, m_st)

# solver = model.load('MiniSat')
# solver = model.load('WalkSat')
solver = model.load('Mistral')

solver.startNewSearch()

solution_count = 0

solutions = []

while solver.getNextSolution() == SAT:
    solution_count += 1
    print(workflow_trace)
    print(process_states)
    print(last_task_index)
    solutions.append((VarArray_to_list(workflow_trace),
                      Matrix_to_list(process_states)))

print(f'Solutions: {solution_count}')
