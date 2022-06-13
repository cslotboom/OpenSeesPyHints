import openseespy.opensees as ops

def type(type):
    """
   This command is used to create a sensitivity algorithm.



   ========================   =============================================================

   ``type`` |str|             the type of the sensitivity algorithm,

   

                              * ``'-computeAtEachStep'``  automatically compute

                                at the end of each step

                              * ``'-compuateByCommand'``  compute by

                                calling ``computeGradients``.

   ========================   =============================================================





    """
    uniqueArgs = []
    ops.sensitivityAlgorithm(type, *uniqueArgs)

