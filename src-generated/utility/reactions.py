import openseespy.opensees as ops

def dynamic():
    """
   Calculate the reactions. Call this command before the :func:`nodeReaction`.



   ========================   ===========================================================================

   ``'-dynamic'`` |str|       Include dynamic effects.

   ``'-rayleigh'`` |str|      Include rayleigh damping.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if '-rayleigh':
        uniqueArgs.append('-rayleigh')
    ops.reactions('-dynamic', *uniqueArgs)

