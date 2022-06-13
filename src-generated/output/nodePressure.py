import openseespy.opensees as ops

def nodeTag(nodeTag):
    """
   Returns the fluid pressures at a specified node if this is a fluid node.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.nodePressure(nodeTag, *uniqueArgs)

