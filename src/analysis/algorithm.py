import openseespy.opensees as ops

def Linear(secant=False, initial=False, factorOnce=False):
    """

    Create a Linear algorithm which takes one iteration to solve the system of equations.   
    
    ================================   =============================================================
    
    ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
    
    ``initial`` |bool|                 Flag to indicate to use initial stiffness. (optional)
    
    ``factorOnce`` |bool|              Flag to indicate to only set up and    
                                       factor matrix once. (optional)
    
    ================================   =============================================================
    
    .. note::
    
    As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the -factorOnce option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.

    """
    uniqueArgs = []
    
    if secant:
        uniqueArgs.append(secant)
    
    if initial:
        uniqueArgs.append(initial)
    
    if factorOnce:
        uniqueArgs.append(factorOnce)
                        
    ops.algorithm('Linear', *uniqueArgs)

def Newton(secant=True, initial=True, initialThenCurrent=True):
    """


    Create a Newton-Raphson algorithm. The Newton-Raphson method is the most widely used and most robust method for solving nonlinear algebraic equations.
    
    
    
    ================================   =============================================================
    
    ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
    
    ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
    
    ``initialThenCurrent`` |bool|      Flag to indicate to use initial stiffness    
                                       on first step, then use current stiffness    
                                       for subsequent steps. (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if secant:
        uniqueArgs.append(secant)
    
    if initial:
        uniqueArgs.append(initial)
    
    if initialThenCurrent:
        uniqueArgs.append(initialThenCurrent)
        
    ops.algorithm('Newton', *uniqueArgs)


def ModifiedNewton(secant=True, initial=True):
    """

    Create a ModifiedNewton algorithm. The difference to Newton is that the 
    tangent at the initial guess is used in the iterations, instead of the 
    current tangent.    
     
    ================================   =============================================================
    ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
    ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if secant:
        uniqueArgs.append(secant)
    
    if initial:
        uniqueArgs.append(initial)

        
    ops.algorithm('ModifiedNewton', *uniqueArgs)




def NewtonLineSearch(Bisection=False, Secant=False, RegulaFalsi=False, InitialInterpolated=True, tol=None, maxIter=None, minEta=None, maxEta=None):
    """

    Create a NewtonLineSearch algorithm. Introduces line search to the Newton 
    algorithm to solve the nonlinear residual equation.
    
    ================================   =============================================================
    
    ``Bisection`` |bool|               Flag to use Bisection line search. (optional)
    
    ``Secant`` |bool|                  Flag to use Secant line search. (optional)
    
    ``RegulaFalsi`` |bool|             Flag to use RegulaFalsi line search. (optional)
    
    ``InitialInterpolated`` |bool|     Flag to use InitialInterpolated line search.(optional)
    
    ``tol`` |float|                    Tolerance for search. (optional)
    
    ``maxIter`` |float|                Max num of iterations to try. (optional)
    
    ``minEta`` |float|                 Min :math:`\eta` value. (optional)
    
    ``maxEta`` |float|                 Max :math:`\eta` value. (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if Bisection:
        uniqueArgs.append(Bisection)
    
    if Secant:
        uniqueArgs.append(Secant)
    
    if RegulaFalsi:
        uniqueArgs.append(RegulaFalsi)
    
    if InitialInterpolated:
        uniqueArgs.append(InitialInterpolated)
    
    if Bisection:
        uniqueArgs.append(Bisection)
    
    if Secant:
        uniqueArgs.append(Secant)
    
    if RegulaFalsi:
        uniqueArgs.append(RegulaFalsi)
    
    if InitialInterpolated:
        uniqueArgs.append(InitialInterpolated)
                
    if tol:
        uniqueArgs.append(tol)
                
    if maxIter:
        uniqueArgs.append(maxIter)    
                
    if minEta:
        uniqueArgs.append(minEta)    
                
    if maxEta:
        uniqueArgs.append(maxEta)    

    ops.algorithm('NewtonLineSearch', *uniqueArgs)


def KrylovNewton(iterate=False, increment=False, maxDim=None):
    """

    Create a KrylovNewton algorithm which uses a Krylov subspace accelerator to accelerate the convergence of the ModifiedNewton.
        
    ================================   =============================================================
    
    ``iterate`` |str|                  Tangent to iterate on,    
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ``increment`` |str|                Tangent to increment on,    
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ``maxDim`` |int|                   Max number of iterations until     
                                       the tangent is reformed and    
                                       the acceleration restarts. (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if iterate:
        uniqueArgs.append(iterate)    
                
    if increment:
        uniqueArgs.append(increment)    
                
    if maxDim:
        uniqueArgs.append(maxDim)        
    
    ops.algorithm('KrylovNewton', *uniqueArgs)

def SecantNewton(iterate=None, increment=None, maxDim=None):
    """

    Create a SecantNewton algorithm which uses the two-term update to accelerate the convergence of the ModifiedNewton.
    
    The default "cut-out" values recommended by Crisfield (R1=3.5, R2=0.3) are used.
    
    ================================   =============================================================
    
    ``iterate`` |str|                  Tangent to iterate on,
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ``increment`` |str|                Tangent to increment on,
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ``maxDim`` |int|                   Max number of iterations until
                                       the tangent is reformed and
                                       the acceleration restarts. (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if iterate:
        uniqueArgs.append(iterate)    
                
    if increment:
        uniqueArgs.append(increment)    
                
    if maxDim:
        uniqueArgs.append(maxDim)        
        
    
    ops.algorithm('SecantNewton', *uniqueArgs)

def RaphsonNewton(iterate=None, increment=None):
    """
    
    Create a RaphsonNewton algorithm which uses Raphson accelerator.
    
    ================================   =============================================================
    
    ``iterate`` |str|                  Tangent to iterate on,
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ``increment`` |str|                Tangent to increment on,
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if iterate:
        uniqueArgs.append(iterate)    
                
    if increment:
        uniqueArgs.append(increment)    
                
    ops.algorithm('RaphsonNewton', *uniqueArgs)

def PeriodicNewton(iterate=None, increment=None, maxDim=None):
    """

    Create a PeriodicNewton algorithm using periodic accelerator.

    ================================   =============================================================
    
    ``iterate`` |str|                  Tangent to iterate on,
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ``increment`` |str|                Tangent to increment on,
                                       ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
    
    ``maxDim`` |int|                   Max number of iterations until
                                       the tangent is reformed and
                                       the acceleration restarts. (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if iterate:
        uniqueArgs.append(iterate)    
                
    if increment:
        uniqueArgs.append(increment)    
                
    if maxDim:
        uniqueArgs.append(maxDim)        
        
    ops.algorithm('PeriodicNewton', *uniqueArgs)

def BFGS(secant=False, initial=False, count=None):
    """

    Create a BFGS algorithm.  The BFGS method is one of the most effective 
    matrix-update or quasi Newton methods for iteration on a nonlinear system 
    of equations. The method computes new search directions at each iteration 
    step based on the initial jacobian, and subsequent trial solutions. 
    The unlike regular Newton does not require the tangent matrix be 
    reformulated and refactored at every iteration, however unlike 
    ModifiedNewton it does not rely on the tangent matrix from a previous iteration.
    
    ================================   =============================================================
    
    ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
    
    ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
    
    ``count`` |int|                    Number of iterations. (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []
    
    if secant:
        uniqueArgs.append(secant)    
                
    if initial:
        uniqueArgs.append(initial)    
                
    if count:
        uniqueArgs.append(count)        

    ops.algorithm('BFGS', *uniqueArgs)

def Broyden(secant=False, initial=False, count=None):
    """

    Create a Broyden algorithm for general unsymmetric systems which performs 
    successive rank-one updates of the tangent at the first iteration of 
    the current time step.
    
    ================================   =============================================================
    
    ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
    
    ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
    
    ``count`` |int|                    Number of iterations. (optional)
    
    ================================   =============================================================

    """
    uniqueArgs = []

    if secant:
        uniqueArgs.append(secant)    
                
    if initial:
        uniqueArgs.append(initial)    
                
    if count:
        uniqueArgs.append(count)      
        
    ops.algorithm('Broyden', *uniqueArgs)

