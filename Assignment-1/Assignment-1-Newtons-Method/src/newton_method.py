"""
Project:        Newton Method
Author:         Kote Batonisashvili
Description:    Assignment 1.1 main newtonian math portion. This will be used as an import for pytest and notebook.
"""

# Standard Imports
import numpy as np


'''
Main function for Newtonian Method. We take in the following parameters:
    eq_functions: The equations that we are solving for. This is a lambda function that takes in x and returns the equations.
    jacobian: The jacobian of the equations.
    lower_bound: The lower bound selected by user.
    upper_bound: The upper bound selected by user.
    TOL: The tolerance of the solution. This is set to 1e-8 by default, however it is adjustable.
    ITER: The maximum number of iterations. This is set to 100 by default, however it is adjustable.
'''
def newtonian(eq_functions, jacobian, lower_bound, upper_bound, TOL=1e-8, ITER=100):

    x = np.array([lower_bound, upper_bound])
    # Checking if the lower and upper limits are chosen properly.
    if lower_bound >= upper_bound:
        raise ValueError("Please make sure your lower bound is less than your upper bound.")
    else:
        for i in range(ITER):    
            Rx = eq_functions(x)
            Jx = jacobian(x)

            if np.linalg.norm(Rx) < TOL:    #Checking convergence
                return x
            delta_x = np.linalg.solve(Jx, -Rx)
            x = x + delta_x
            
        raise RuntimeError("Could not converge within iteration limit. Please raise the iterations, or change your upper/lower bounds")