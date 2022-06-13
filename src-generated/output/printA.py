import openseespy.opensees as ops

def file(filename):
    """
   print the contents of a FullGeneral system that the integrator creates to the screen or a file if the ``'-file'`` option is used. If using a static integrator, the resulting matrix is the stiffness matrix. If a transient integrator, it will be some combination of mass and stiffness matrices. The printA command can only be issued after an analyze command.



   ===========================   =====================================================================================================================================================

   ``filename`` |str|            name of file to which output is sent, by default, print to the screen. (optional)

   ``'-ret'`` |str|              return the A matrix as a list. (optional)

   ===========================   =====================================================================================================================================================

    """
    uniqueArgs = []
    if '-ret':
        uniqueArgs.append('-ret')
    ops.printA('-file', filename, *uniqueArgs)

