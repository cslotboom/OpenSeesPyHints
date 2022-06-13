import openseespy.opensees as ops

def Linear(secant, initial, factorOnce):
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
    ops.algorithm('Linear', secant, initial, factorOnce, *uniqueArgs)

def Newton(secant, initial, initialThenCurrent):
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
    ops.algorithm('Newton', secant, initial, initialThenCurrent, *uniqueArgs)

def NewtonLineSearch(Bisection, Secant, RegulaFalsi, InitialInterpolated, tol, maxIter, minEta, maxEta):
    """


   Create a NewtonLineSearch algorithm. Introduces line search to the Newton algorithm to solve the nonlinear residual equation.



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
    ops.algorithm('NewtonLineSearch', Bisection, Secant, RegulaFalsi, InitialInterpolated, tol, maxIter, minEta, maxEta, *uniqueArgs)

def ModifiedNewton(secant, initial):
    """


   Create a ModifiedNewton algorithm. The difference to Newton is that the tangent at the initial guess is used in the iterations, instead of the current tangent.



   ================================   =============================================================

   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)

   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)

   ================================   =============================================================

    """
    uniqueArgs = []
    ops.algorithm('ModifiedNewton', secant, initial, *uniqueArgs)

def KrylovNewton(iterate, increment, maxDim):
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
    ops.algorithm('KrylovNewton', iterate, increment, maxDim, *uniqueArgs)

def SecantNewton(iterate, increment, maxDim):
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
    ops.algorithm('SecantNewton', iterate, increment, maxDim, *uniqueArgs)

def RaphsonNewton(iterate, increment):
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
    ops.algorithm('RaphsonNewton', iterate, increment, *uniqueArgs)

def PeriodicNewton(iterate, increment, maxDim):
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
    ops.algorithm('PeriodicNewton', iterate, increment, maxDim, *uniqueArgs)

def BFGS(secant, initial, count):
    """


   Create a BFGS algorithm.  The BFGS method is one of the most effective matrix-update or quasi Newton methods for iteration on a nonlinear system of equations. The method computes new search directions at each iteration step based on the initial jacobian, and subsequent trial solutions. The unlike regular Newton does not require the tangent matrix be reformulated and refactored at every iteration, however unlike ModifiedNewton it does not rely on the tangent matrix from a previous iteration.



   ================================   =============================================================

   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)

   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)

   ``count`` |int|                    Number of iterations. (optional)

   ================================   =============================================================

    """
    uniqueArgs = []
    ops.algorithm('BFGS', secant, initial, count, *uniqueArgs)

def Broyden(secant, initial, count):
    """


   Create a Broyden algorithm for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.



   ================================   =============================================================

   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)

   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)

   ``count`` |int|                    Number of iterations. (optional)

   ================================   =============================================================

    """
    uniqueArgs = []
    ops.algorithm('Broyden', secant, initial, count, *uniqueArgs)

