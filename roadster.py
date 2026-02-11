import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    a1 = 546.8
    a2 = 50.31
    a3 = 0.2584
    a4 = 0.008210
    return a1*(v**-1)+a2+a3*v+a4*(v**2) 

print(consumption(4))

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x, route, n):   
    steps = np.linspace(0,x,n+1)
    v = velocity(steps, route)
    f = 1/v
    h = (x-0)/n
    T = (h/2)*(f[0] + 2 * np.sum(f[1:-1]) + f[-1])
    return T

res = time_to_destination(15.5, 'speed_anna.npz', 2)
print(res)


### PART 2B ###
def total_consumption(x, route, n):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    steps = np.linspace(0,x,n+1)
    v = velocity(steps, route)
    f = consumption(v)
    h = (x-0)/n
    T = (h/2)*(f[0] + 2 * np.sum(f[1:-1]) + f[-1])
    return T  

res1 = total_consumption(15.4, 'speed_anna.npz', 2)
print(f'svar 2b: {res1}')

### PART 2C ###

n_steps = np.array([10, 20, 40, 80, 160, 320])

n1 = total_consumption(15.4, 'speed_anna.npz', 10)
n2 = total_consumption(15.4, 'speed_anna.npz', 20)
n3 = total_consumption(15.4, 'speed_anna.npz', 40)
n4 = total_consumption(15.4, 'speed_anna.npz', 80)
n5 = total_consumption(15.4, 'speed_anna.npz', 160)
n6 = total_consumption(15.4, 'speed_anna.npz', 320)
n7 = total_consumption(15.4, 'speed_anna.npz', 640)

errors = [np.abs(n7 - val) for val in [n1, n2, n3, n4, n5, n6]]

# Plotta dina beräknade fel
plt.loglog(n_steps, errors, '-o', label='Beräknat fel (Trapetsmetoden)')

# Skapa en hjälplinje för O(1/n^2) för att jämföra med teorin
# Vi utgår från första felet och minskar det med (1/n^2)
plt.loglog(n_steps, errors[0] * (n_steps[0]/n_steps)**2, '--', label='Teoretisk lutning O(1/n²)')

plt.xlabel('Antal delintervall n')
plt.ylabel('Integrationsfel')
plt.title('Konvergensstudie: Trapetsmetoden')
plt.legend()
plt.show()



### PART 3A ###
def distance(T, route): 
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('distance not implemented yet!')

### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')
