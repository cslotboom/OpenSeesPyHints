import openseespy.opensees as ops

def PFEM():
    """


   Create a incompressible PFEM system of equations using the Umfpack solver





   ========================   ===========================================================================

   ``-compressible``          Solve using a quasi-incompressible formulation. (optional)

   ``-mumps``                 Solve using the MUMPS solver. (optional, not supported on Windows)

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if '-mumps':
        uniqueArgs.append('-compressible')
    if '-mumps':
        uniqueArgs.append('-mumps')
    ops.system('PFEM', *uniqueArgs)

