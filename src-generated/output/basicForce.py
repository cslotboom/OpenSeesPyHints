import openseespy.opensees as ops

def eleTag(eleTag):
    """
   Returns the forces of the basic system for a beam-column element.



   ========================   ===========================================================================

   ``eleTag`` |int|           element tag.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.basicForce(eleTag, *uniqueArgs)

