import openseespy.opensees as ops

def PFEM():
    """


   Create a PFEM Integrator.

    """
    uniqueArgs = []
    ops.integrator('PFEM', *uniqueArgs)

