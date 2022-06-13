import openseespy.opensees as ops

def Plain(patternTag, tsTag, fact=None):
    """


   This commnand allows the user to construct a LoadPattern object. Each plain load pattern is associated with a TimeSeries object and can contain multiple NodalLoads, ElementalLoads and SP_Constraint objects. The command to generate LoadPattern object contains in { } the commands to generate all the loads and the single-point constraints in the pattern. To construct a load pattern and populate it, the following command is used:







   ========================   =============================================================

   ``patternTag`` |int|       unique tag among load patterns.

   ``tsTag`` |int|            the tag of the time series to be used in the load pattern

   ``fact`` |float|           constant factor. (optional)

   ========================   =============================================================





.. note::



   the commands below to generate all the loads and sp constraints will be

   included in last called pattern command.





.. toctree::

   :maxdepth: 2



   load

   eleload

   sp

    """
    uniqueArgs = []
    if fact:
        uniqueArgs.append('-fact')
        uniqueArgs.append(fact)
    ops.pattern('Plain', patternTag, tsTag, *uniqueArgs)

def UniformExcitation(patternTag, dir, dispSeriesTag=None, velSeriesTag=None, accelSeriesTag=None, vel0=None, fact=None):
    """
   

   The UniformExcitation pattern allows the user to apply a uniform excitation to a model acting in a certain direction. The command is as follows:



   ========================   =============================================================

   ``patternTag`` |int|       unique tag among load patterns

   ``dir`` |int|              direction in which ground motion acts

      

                              #. corresponds to translation along the global X axis

                              #. corresponds to translation along the global Y axis

                              #. corresponds to translation along the global Z axis

                              #. corresponds to rotation about the global X axis

                              #. corresponds to rotation about the global Y axis

                              #. corresponds to rotation about the global Z axis

                              

   ``dispSeriesTag`` |int|    tag of the TimeSeries series defining the displacement

                              history. (optional)

   ``velSeriesTag`` |int|     tag of the TimeSeries series defining the velocity

                              history. (optional)

   ``accelSeriesTag`` |int|   tag of the TimeSeries series defining the acceleration

                              history. (optional)

   ``vel0`` |float|           the initial velocity (optional, default=0.0)

   ``fact`` |float|           constant factor (optional, default=1.0)

   ========================   =============================================================





.. note::



   #. The responses obtained from the nodes for this type of excitation are RELATIVE values, and not the absolute values obtained from a multi-support case.

   #. must set one of the disp, vel or accel time series 



    """
    uniqueArgs = []
    if dispSeriesTag:
        uniqueArgs.append('-disp')
        uniqueArgs.append(dispSeriesTag)
    if velSeriesTag:
        uniqueArgs.append('-vel')
        uniqueArgs.append(velSeriesTag)
    if accelSeriesTag:
        uniqueArgs.append('-accel')
        uniqueArgs.append(accelSeriesTag)
    if vel0:
        uniqueArgs.append('-vel0')
        uniqueArgs.append(vel0)
    if fact:
        uniqueArgs.append('-fact')
        uniqueArgs.append(fact)
    ops.pattern('UniformExcitation', patternTag, dir, *uniqueArgs)

def MultipleSupport(patternTag):
    """


   The Multi-Support pattern allows similar or different prescribed ground motions to be input at various supports in the structure. In OpenSees, the prescribed motion is applied using single-point constraints, the single-point constraints taking their constraint value from user created ground motions.

   ===================================   ===========================================================================

   ``patternTag`` |int|                  integer tag identifying pattern

   ===================================   ===========================================================================





.. note::



   #. The results for the responses at the nodes are the ABSOLUTE values, and not relative values as in the case of a UniformExciatation.

   #. The non-homogeneous single point constraints require an appropriate choice of constraint handler.







.. toctree::

   :maxdepth: 2



   groundMotion

   interpolatedGroundMotion

   imposedMotion

    """
    uniqueArgs = []
    ops.pattern('MultipleSupport', patternTag, *uniqueArgs)

