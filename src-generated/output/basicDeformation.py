import openseespy.opensees as ops

def eleTag(eleTag):
    """
   Returns the deformation of the basic system for a beam-column element.



   ========================   ===========================================================================

   ``eleTag`` |int|           element tag.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.basicDeformation(eleTag, *uniqueArgs)

