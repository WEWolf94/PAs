import random
from tabulate import tabulate
import time

def one_dimension(moves):
    x = 0
    counter = 0
    for i in range(moves):
        direction = random.choice(['right','left'])
        if direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        if x == 0:
            counter += 1
            break
    return counter
    
    
def two_dimension(moves):
    x = 0
    y = 0
    counter = 0
    for i in range(moves):
        direction = random.choice(['right','left','up','down'])
        if direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        if x == 0 and y == 0:
            counter += 1
            break
    return counter

def three_dimension(moves):
    x = 0
    y = 0
    z = 0 
    counter = 0
    for i in range(moves):
        direction  = random.choice(['right','left','up','down','out','in'])
        if direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'out':
            z += 1
        elif direction == 'in':
            z -= 1
        if x == 0 and y == 0 and z == 0:
            counter += 1
            break
    return counter

def main():
    move_list = [20,200,2000,20000,200000,2000000]
    
    d1_results = ['1d']
    for moves in move_list:
        final_count_1D = 0
        for i in range(100):
            final_count_1D += one_dimension(moves)
        d1_results.append(final_count_1D) 
    
    d2_results = ['2d']   
    for moves in move_list:
        final_count_2D = 0
        for i in range(100):
            final_count_2D += two_dimension(moves)
        d2_results.append(final_count_2D)
    
    d3_results = ['3d']
    start_time = time.time()
    for moves in move_list:
        final_count_3D = 0
        for i in range(100):
            final_count_3D += three_dimension(moves)
        end_time = time.time()
        d3_results.append(final_count_3D)
    elapsed_time = end_time - start_time
    
    data = [d1_results,
           d2_results,
            d3_results,
            ['Total Time for 3d in seconds',elapsed_time]]
    
    headers = ['# of steps','20','200','2000','20000','200000','20000000']
    
    table = tabulate(data, headers, tablefmt="grid")
    
    print(table)

main()

