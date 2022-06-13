import openseespy.opensees as ops

def tag(tag):
    """
   Return the value of a parameter



   ==============================   ===========================================================================

   ``tag`` |int|                    integer tag identifying the parameter.

   ==============================   ===========================================================================

    """
    uniqueArgs = []
    ops.getParamValue(tag, *uniqueArgs)

