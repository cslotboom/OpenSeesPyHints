import openseespy.opensees as ops

def nodeTag(nodeTag, dof, value):
    """
   set the nodal displacement at the specified DOF.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``dof`` |int|              the DOF of the displacement to be set.

   ``value`` |float|          displacement value

   ``'-commit'`` |str|        commit nodal state. (optional)

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if '-commit':
        uniqueArgs.append('-commit')
    ops.setNodeDisp(nodeTag, dof, value, *uniqueArgs)

