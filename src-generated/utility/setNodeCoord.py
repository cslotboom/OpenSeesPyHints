import openseespy.opensees as ops

def nodeTag(nodeTag, dim, value):
    """
   set the nodal coodinate at the specified dimension.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``dim`` |int|              the dimension of the coordinate to be set.

   ``value`` |float|          coordinate value

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.setNodeCoord(nodeTag, dim, value, *uniqueArgs)

