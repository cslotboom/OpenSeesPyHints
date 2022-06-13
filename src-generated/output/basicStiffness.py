import openseespy.opensees as ops

def eleTag(eleTag):
    """
   Returns the stiffness of the basic system for a beam-column element.

   A list of values in row order will be returned.



   ========================   ===========================================================================

   ``eleTag`` |int|           element tag.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.basicStiffness(eleTag, *uniqueArgs)

