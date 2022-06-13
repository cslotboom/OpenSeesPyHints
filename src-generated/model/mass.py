import openseespy.opensees as ops

def nodeTag(nodeTag, massValues):
    """
   This command is used to set the mass at a node





   ========================   =============================================================

   ``nodeTag`` |int|          integer tag identifying node whose mass is set

   ``massValues`` |listf|     ndf nodal mass values corresponding to each DOF

   ========================   =============================================================

    """
    uniqueArgs = []
    ops.mass(nodeTag, *massValues, *uniqueArgs)

