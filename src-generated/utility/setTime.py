import openseespy.opensees as ops

def pseudoTime(pseudoTime):
    """
   This command is used to set the time in the Domain.



   ========================   ===========================================================================

   ``pseudoTime`` |float|     Time domain to be set

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.setTime(pseudoTime, *uniqueArgs)

