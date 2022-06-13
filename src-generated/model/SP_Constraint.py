import openseespy.opensees as ops

def nodeTag(nodeTag, constrValues):
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



    """
    uniqueArgs = []
    ops.fix(nodeTag, *constrValues, *uniqueArgs)

def x(x, constrValues, tol):
    """
   Create homogeneous SP constriants.



   ========================   ===========================================================================

   ``x`` |float|              x-coordinate of nodes to be constrained

   ``constrValues`` |listi|   a list of constraint values (0 or 1),

                              must be preceded with ``*``.



                              * ``0`` free

                              * ``1`` fixed

   ``tol`` |float|                    user-defined tolerance (optional)

   ========================   ===========================================================================





    """
    uniqueArgs = []
    if tol=1e-10:
        uniqueArgs.append('-tol')
    ops.fixX(x, *constrValues, tol, *uniqueArgs)

def y(y, constrValues, tol):
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





    """
    uniqueArgs = []
    if tol=1e-10:
        uniqueArgs.append('-tol')
    ops.fixY(y, *constrValues, tol, *uniqueArgs)

def z(z, constrValues, tol):
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





    """
    uniqueArgs = []
    if tol=1e-10:
        uniqueArgs.append('-tol')
    ops.fixZ(z, *constrValues, tol, *uniqueArgs)

