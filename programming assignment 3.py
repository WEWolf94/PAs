import numpy as np

# problem #1
p = np.poly1d([2,3,0,1])
print(p)
v = np.polyval(p,2)
print(v)

#problem #2
p = np.poly1d([1,0,1])
print(p)
d = np.polyder(p)
print(d)
dv = np.polyval(d,1)
print(dv)


func = input('enter a polynomial function split by commas:')
func = func.split(',')
for i in func:
    func.insert(func.index(i), float(i))
    func.remove(i)

   
def eval_poly(func,number):
    p_v = np.polyval(func,number)
    return p_v

def eval_der(func,number):
    p_d = np.polyder(func)
    p_d_v = np.polyval(p_d,number)
    return p_d_v

x_n = float(input('what is your number for x_1: '))
def newtons_method(func, x_n, i=2):
    f_x = eval_poly(func, x_n)
    f_x_prime = eval_der(func, x_n)
    
    x_n_p1 = x_n - float(f_x) / float(f_x_prime)
    
    print(f'x_{i} = {x_n_p1:.3f}')
    
    if round(x_n_p1,3) - round(x_n,3) == 0:
        return x_n_p1
    else:
        return newtons_method(func, x_n_p1, i+1)
    
    
root=newtons_method(func, x_n, i=2)
x_r = np.roots(func)
print(f'The final value with the stablized thousandths place is {root:.3f}')
print(f'The roots of the function are {x_r}')


