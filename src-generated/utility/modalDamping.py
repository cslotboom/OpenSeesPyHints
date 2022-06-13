import openseespy.opensees as ops

def factor(factor):
    """
   Set modal damping factor. The :func:`eigen` must be called before.



   ========================   ===========================================================================

   ``factor`` |float|         damping factor.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.modalDamping(factor, *uniqueArgs)

