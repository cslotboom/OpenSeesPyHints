import openseespy.opensees as ops

def patternTag(patternTag):
    """
   Returns the load factor :math:`\lambda` for the pattern



   ========================   ===========================================================================

   ``patternTag`` |int|       pattern tag.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.getLoadFactor(patternTag, *uniqueArgs)

