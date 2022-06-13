import openseespy.opensees as ops

def precision(precision):
    """
   Set the precision for screen output.



   ========================   ===========================================================================

   ``precision`` |int|        the precision number.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.setPrecision(precision, *uniqueArgs)

