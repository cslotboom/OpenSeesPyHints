# from . algorithm import *
from . import algorithm

# from . constraints import *
from . import constraints

# from . integrator import *
from . import integrator

# from . system import *
from . import numberer


# from . system import *
from . import system

# from . test import *
from . import test


import openseespy.opensees as ops


def analysis(analysisType):
    """
    This command is used to construct the Analysis object, which defines what type of analysis is to be performed.
    
    * determine the predictive step for time t+dt
    * specify the tangent matrix and residual vector at any iteration
    * determine the corrective step based on the displacement increment dU
    
    ================================   ===========================================================================
    
    analysisType |str|                 char string identifying type of analysis object to be constructed. Currently 3 valid options:
    
                                       #. ``'Static'`` - for static analysis
                                       #. ``'Transient'`` - for transient analysis constant time step
                                       #. ``'VariableTransient'`` - for transient analysis with variable time step
                                       #. ``'PFEM'`` - for :ref:`PFEM-Analysis`.
    ================================   ===========================================================================
    
    .. note::
    
    If the component objects are not defined before hand, the command 
    automatically creates default component objects and issues warning messages
    to this effect. The number of warning messages depends on the number of 
    component objects that are undefined.
    
    Hints:
        untested

    """
    ops.analysis(analysisType)
    
    
def analyze(numIncr=1, dt=0.0, dtMin=0.0, dtMax=0.0, Jd=0):
    """
    Perform the analysis. Return ``0`` if successful, ``<0`` if **NOT** successful
    
    ===============================   ======================================================================================
    
    ``numIncr`` |int|                 Number of analysis steps to perform. (required except for :ref:`PFEM-Analysis`)
    ``dt`` |float|                    Time-step increment. (required for Transient analysis and VariableTransient analysis.`)  
    ``dtMin`` |float|                 Minimum time steps. (required for VariableTransient analysis)    
    ``dtMax`` |float|                 Maximum time steps (required for VariableTransient analysis)    
    ``Jd`` |float|                    Number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge (required for VariableTransient analysis)
    
    ===============================   ======================================================================================

    Hints:
        untested

    """
    ops.analyze(numIncr, dt, dtMin, dtMax, Jd)


def  eigen(solver='-genBandArpack', numEigenvalues = None):
    """
    Eigen value analysis. Return a list of eigen values.
    
    ================================   ===========================================================================
    
    numEigenvalues |int|               number of eigenvalues required
    solver |str|                       optional string detailing type of solver: ``'-genBandArpack'``, ``'-symmBandLapack'``, ``'-fullGenLapack'``, (optional)
    
    ================================   ===========================================================================

    .. note::

    
    #. The eigenvectors are stored at the nodes and can be printed out using a 
    ode Recorder, the nodeEigenvector command, or the Print command.
    #. The default eigensolver is able to solve only for N-1 eigenvalues, 
    where N is the number of inertial DOFs. When running into this limitation 
    the -fullGenLapack solver can be used instead of the default Arpack solver.

    Hints:
        untested

    """
    uniqueArgs = []
    if numEigenvalues:
        uniqueArgs.append(numEigenvalues)
    
    ops.eigen(solver, *uniqueArgs)