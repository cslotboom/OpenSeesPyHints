import openseespy.opensees as ops

def eleTag(eleTag, secNum):
    """
   Returns the weights of integration points of a section for a beam-column element.



   ========================   ===========================================================================

   ``eleTag`` |int|           element tag.

   ``secNum`` |int|           section number, i.e. the Gauss integration number

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.sectionWeight(eleTag, secNum, *uniqueArgs)

