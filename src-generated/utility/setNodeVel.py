import openseespy.opensees as ops

def nodeTag(nodeTag, dof, value):
    """
   set the nodal velocity at the specified DOF.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``dof`` |int|              the DOF of the velocity to be set.

   ``value`` |float|          velocity value

   ``'-commit'`` |str|        commit nodal state. (optional)

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if '-commit':
        uniqueArgs.append('-commit')
    ops.setNodeVel(nodeTag, dof, value, *uniqueArgs)

