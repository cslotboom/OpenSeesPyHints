import openseespy.opensees as ops

def nodeTag(nodeTag, paramTag):
    """
   Returns the current pressure sensitivity to a parameter at a specified node.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag

   ``paramTag`` |int|         parameter tag

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.sensNodePressure(nodeTag, paramTag, *uniqueArgs)

