import openseespy.opensees as ops

def eleTag(eleTag, secNum):
    """
   Returns the section stiffness matrix for a beam-column element.

   A list of values in the row order will be returned.



   ========================   ===========================================================================

   ``eleTag`` |int|           element tag.

   ``secNum`` |int|           section number, i.e. the Gauss integration number

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.sectionStiffness(eleTag, secNum, *uniqueArgs)

