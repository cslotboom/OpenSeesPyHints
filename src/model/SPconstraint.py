import openseespy.opensees as ops

def fix(nodeTag, constrValues= [0,0,0]):
    """
    Create a homogeneous SP constriant.  
        
    ========================   ===========================================================================   
    ``nodeTag`` |int|          tag of node to be constrained    
    ``constrValues`` |listi|   a list of constraint values (0 or 1),    
                               must be preceded with ``*``.       
    
                               * ``0`` free
    
                               * ``1`` fixed    
    ========================   ===========================================================================

    For example, 
   
    .. code-block:: python
   
       # fully fixed  
       vals = [1,1,1]   
       fix(nodeTag, *vals)

    Hints:
        untested
    
    """
    ops.fix(nodeTag, *constrValues)

def fixX(x, constrValues, tol=None):
    """
    Create homogeneous SP constriants.
    
    ========================   ===========================================================================
    ``x`` |float|              x-coordinate of nodes to be constrained
    ``constrValues`` |listi|   a list of constraint values (0 or 1).
    
                               * ``0`` free
    
                               * ``1`` fixed
    ``tol`` |float|                    user-defined tolerance (optional)
    ========================   ===========================================================================

    Hints:
        untested
    
    """
    uniqueArgs = []
    uniqueArgs.append('-tol')
    uniqueArgs.append(tol)
    ops.fixX(x, *constrValues, *uniqueArgs)

def fixY(y, constrValues, tol=None):
    """
    Create homogeneous SP constriants.
    
    ========================   ===========================================================================
    ``y`` |float|              y-coordinate of nodes to be constrained
    ``constrValues`` |listi|   a list of constraint values (0 or 1),
                               must be preceded with ``*``.
    
                               * ``0`` free
    
                               * ``1`` fixed
    ``tol`` |float|                    user-defined tolerance (optional)
    ========================   ===========================================================================

    Hints:
        untested
    
    """
    uniqueArgs = []
    uniqueArgs.append('-tol')
    uniqueArgs.append(1e-10)
    ops.fixY(y, *constrValues, *uniqueArgs)


def fixZ(z, constrValues, tol=None):
    """
    Create homogeneous SP constriants.
    
    ========================   ===========================================================================
    ``z`` |float|              z-coordinate of nodes to be constrained
    ``constrValues`` |listi|   a list of constraint values (0 or 1),
                               must be preceded with ``*``.
    
                               * ``0`` free
    
                               * ``1`` fixed
    ``tol`` |float|                    user-defined tolerance (optional)
    ========================   ===========================================================================
    Hints:
        untested
    
    """
    uniqueArgs = []
    uniqueArgs.append('-tol')
    uniqueArgs.append(1e-10)
    ops.fixZ(z, *constrValues, *uniqueArgs)



