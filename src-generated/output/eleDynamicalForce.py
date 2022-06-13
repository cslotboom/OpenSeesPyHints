import openseespy.opensees as ops

def eleTag(eleTag, dof):
    """
   Returns the elemental dynamic force.



   ========================   ===========================================================================

   ``eleTag`` |int|           element tag.

   ``dof`` |int|              specific dof at the element, (optional), if no ``dof`` is

                              provided, a list of values for all dofs is returned.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.eleDynamicalForce(eleTag, dof, *uniqueArgs)

