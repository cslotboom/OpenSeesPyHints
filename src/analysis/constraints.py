import openseespy.opensees as ops

def Plain():
    """

    This command is used to construct a Plain constraint handler. 
    A plain constraint handler can only enforce homogeneous single point 
    constraints (fix command) and multi-point constraints constructed where the 
    constraint matrix is equal to the identity (equalDOF command). The following 
    is the command to construct a plain constraint handler:
    
     .. note::
    
    As mentioned, this constraint handler can only enforce homogeneous single 
    point constraints (fix command) and multi-pont constraints where the 
    constraint matrix is equal to the identity (equalDOF command).

    """
    uniqueArgs = []
    ops.constraints('Plain', *uniqueArgs)

def Lagrange(alphaS, alphaM):
    """

    This command is used to construct a LagrangeMultiplier constraint handler, 
    which enforces the constraints by introducing Lagrange multiplies to the 
    system of equation. The following is the command to construct a plain 
    constraint handler:
    
    ================================   ===========================================================================
    
    ``alphaS`` |float|                 :math:`\alpha_S` factor on single points.
    
    ``alphaM`` |float|                 :math:`\alpha_M` factor on multi-points.
    
    ================================   ===========================================================================
    
    .. note::
    
    The Lagrange multiplier method introduces new unknowns to the system of 
    equations. The diagonal part of the system corresponding to these new 
    unknowns is 0.0. This ensure that the system IS NOT symmetric positive 
    definite.

    """
    uniqueArgs = []
    ops.constraints('Lagrange', alphaS, alphaM, *uniqueArgs)

def Penalty(alphaS, alphaM):
    """

    This command is used to construct a Penalty constraint handler, which 
    enforces the constraints using the penalty method. The following is the 
    command to construct a penalty constraint handler:

    ================================   ===========================================================================
    
    ``alphaS`` |float|                 :math:`\alpha_S` factor on single points.
    
    ``alphaM`` |float|                 :math:`\alpha_M` factor on multi-points.
    
    ================================   ===========================================================================
    
    .. note::
   
    
    The degree to which the constraints are enforced is dependent on the penalty 
    values chosen. Problems can arise if these values are too small 
    (constraint not enforced strongly enough) or too large 
    (problems associated with conditioning of the system of equations).

    """
    uniqueArgs = []
    ops.constraints('Penalty', alphaS, alphaM, *uniqueArgs)

def Transformation():
    """

    This command is used to construct a transformation constraint handler, 
    which enforces the constraints using the transformation method. The following 
    is the command to construct a transformation constraint handler

    .. note::
    
    
        * The single-point constraints when using the transformation method are done directly. The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.
        * Great care must be taken when multiple constraints are being enforced as the transformation method does not follow constraints:
        
            #. If a node is fixed, constrain it with the fix command and not equalDOF or other type of constraint.
            #. If multiple nodes are constrained, make sure that the retained node is not constrained in any other constraint.
        
        And remember if a node is constrained to multiple nodes in your model it probably means you have messed up.

    """
    uniqueArgs = []
    ops.constraints('Transformation', *uniqueArgs)

