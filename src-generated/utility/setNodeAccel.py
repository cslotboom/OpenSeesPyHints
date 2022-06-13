import openseespy.opensees as ops

def nodeTag(nodeTag, dof, value):
    """
   set the nodal acceleration at the specified DOF.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``dof`` |int|              the DOF of the acceleration to be set.

   ``value`` |float|          acceleration value

   ``'-commit'`` |str|        commit nodal state. (optional)

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if '-commit':
        uniqueArgs.append('-commit')
    ops.setNodeAccel(nodeTag, dof, value, *uniqueArgs)

