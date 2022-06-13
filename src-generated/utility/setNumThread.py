import openseespy.opensees as ops

def num(num):
    """
   set the number of threads to be used in the multi-threaded environment.



   ========================   ===========================================================================

   ``num`` |int|              number of threades 

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.setNumThreads(num, *uniqueArgs)

