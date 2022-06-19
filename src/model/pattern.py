import openseespy.opensees as ops

def Plain(patternTag, tsTag, fact=None):
    """
    This commnand allows the user to construct a LoadPattern object. Each plain 
    load pattern is associated with a TimeSeries object and can contain multiple
    NodalLoads, ElementalLoads and SP_Constraint objects. The command to 
    generate LoadPattern object contains in { } the commands to generate all 
    the loads and the single-point constraints in the pattern. To construct a 
    load pattern and populate it, the following command is used:
    
    ========================   =============================================================
    ``patternTag`` |int|       unique tag among load patterns.
    ``tsTag`` |int|            the tag of the time series to be used in the load pattern
    ``fact`` |float|           constant factor. (optional)
    ========================   =============================================================

    .. note::
    
       the commands below to generate all the loads and sp constraints will be
       included in last called pattern command.

    """
    uniqueArgs = []
    if fact:
        uniqueArgs.append('-fact')
        uniqueArgs.append(fact)
    ops.pattern('Plain', patternTag, tsTag, *uniqueArgs)



def load(nodeTag, loadValues):
    """
    This command is used to construct a NodalLoad object and add it to the enclosing LoadPattern.
    
    ========================   =============================================================
    ``nodeTag`` |int|          tag of node to which load is applied.
    ``loadValues`` |float|     ndf reference load values.
    ========================   =============================================================


    .. note::
        
        The load values are reference loads values. It is the time series that 
        provides the load factor. The load factor times the reference values is 
        the load that is actually applied to the node.



    Hint:
        untested

    """

    ops.load(nodeTag, *loadValues)

def load(nodeTag, loadValues):
    """
    This command is used to construct a NodalLoad object and add it to the enclosing LoadPattern.
    
    ========================   =============================================================
    ``nodeTag`` |int|          tag of node to which load is applied.
    ``loadValues`` |float|     ndf reference load values.
    ========================   =============================================================


    .. note::
        
        The load values are reference loads values. It is the time series that 
        provides the load factor. The load factor times the reference values is 
        the load that is actually applied to the node.



    Hint:
        untested

    """

    ops.load(nodeTag, *loadValues)



def eleLoad(eleTags, eleTag1=None, eleTag2=None, Wy=None, Wz=None, 
            Wx=None, Px=None, Py=None, Pz=None, xL=None,  tempPts=None):
    """
    eleLoad('-ele', *eleTags, '-range', eleTag1, eleTag2, '-type', '-beamUniform', Wy, <Wz>, Wx=0.0, '-beamPoint',Py,<Pz>,xL,Px=0.0,'-beamThermal',*tempPts)

    The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.
    
    ========================   =============================================================
    ``eleTags`` |listi|        tag of PREVIOUSLY DEFINED element
    ``eleTag1`` |int|          element tag
    ``eleTag2`` |int|          element tag
    ``Wx`` |float|             mag of uniformily distributed ref load acting in direction
                               along member length. (optional)
    ``Wy`` |float|             mag of uniformily distributed ref load acting in local y
                               direction of element
    ``Wz`` |float|             mag of uniformily distributed ref load acting in local z
                               direction of element. (required only for 3D)
    ``Px`` |float|             mag of ref point load acting in direction along member
                               length. (optional)
    ``Py`` |float|             mag of ref point load acting in local y direction of element
    ``Pz`` |float|             mag of ref point load acting in local z direction of
                               element. (required only for 3D)
    ``xL`` |float|             location of point load relative to node I,
                               prescribed as fraction of element length
    ``tempPts`` |listf|        temperature points:
                               ``temPts = [T1, y1, T2, y2, ..., T9, y9]``
                               Each point ``(T1, y1)`` define a temperature and
                               location. This command may accept 2,5 or 9
                               temperature points.
    ========================   =============================================================

    .. note::
    
    
       #. The load values are reference load values, it is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the element.
       #. At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.

    Hint:
        untested

    """
    uniqueArgs = []
    if eleTag1:
        uniqueArgs.append('-range')
        uniqueArgs.append(eleTag1)
        uniqueArgs.append(eleTag2)
    uniqueArgs.append('-type')
    if Wy:
        uniqueArgs.append('-beamUniform')
        uniqueArgs.append(Wy)
    if Wz:
        uniqueArgs.append(Wz)
    if Wx:
        uniqueArgs.append(Wx)
    if Py:
        uniqueArgs.append('-beamPoint')
        uniqueArgs.append(Py)
    if Pz:
        uniqueArgs.append(Pz)
    if xL:
        uniqueArgs.append(xL)         
    if Px:
        uniqueArgs.append(Px)
    if tempPts:
        uniqueArgs.append('-beamThermal')
        uniqueArgs.append(tempPts)

    ops.eleLoad('-ele', *eleTags, *uniqueArgs)



def sp(nodeTag, dof, dofValues):
    """
    This command is used to construct a NodalLoad object and add it to the enclosing LoadPattern.
    
    ========================   =============================================================
    ``nodeTag`` |int|          tag of node to which load is applied.
    ``dof`` |int|              the degree-of-freedom at the node to which constraint is applied (1 through ndf)
    ``dofValues `` |float|     ndf reference constraint values.
    ========================   =============================================================


    .. note::
        
        The dofValue is a reference value, it is the time series that provides
        the load factor. The load factor times the reference value is the 
        constraint that is actually applied to the node.



    Hint:
        untested

    """

    ops.sp(nodeTag, dof, *dofValues)



def UniformExcitation(patternTag, dir, dispSeriesTag=None, velSeriesTag=None, accelSeriesTag=None, vel0=None, fact=None):
    """  
    The UniformExcitation pattern allows the user to apply a uniform excitation 
    to a model acting in a certain direction. The command is as follows:
      
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
       
       #. The responses obtained from the nodes for this type of excitation are 
       RELATIVE values, and not the absolute values obtained from a multi-support case.
    
       #. must set one of the disp, vel or accel time series 


    Hints:
        untested

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

    The Multi-Support pattern allows similar or different prescribed ground 
    motions to be input at various supports in the structure. In OpenSees, the 
    prescribed motion is applied using single-point constraints, the 
    single-point constraints taking their constraint value from user created ground motions.
    
    ===================================   ===========================================================================
    ``patternTag`` |int|                  integer tag identifying pattern
    ===================================   ===========================================================================

    .. note::
    
       #. The results for the responses at the nodes are the ABSOLUTE values, and not relative values as in the case of a UniformExciatation.
    
       #. The non-homogeneous single point constraints require an appropriate choice of constraint handler.

    Hints:
        untested

    """
    ops.pattern('MultipleSupport', patternTag)






def Plain(gmTag, dispSeriesTag=None, velSeriesTag=None, accelSeriesTag=None, tsInt='Trapezoidal', factor=1.0):
    """
    This command is used to construct a plain GroundMotion object. Each GroundMotion object is associated with a number of TimeSeries objects, which define the acceleration, velocity and displacement records for that ground motion. T
    
    ========================   =============================================================
    ``gmTag`` |int|            unique tag among ground motions in load pattern
    ``dispSeriesTag`` |int|    tag of the TimeSeries series defining the displacement
                               history. (optional)
    ``velSeriesTag`` |int|     tag of the TimeSeries series defining the velocity
                               history. (optional)
    ``accelSeriesTag`` |int|   tag of the TimeSeries series defining the acceleration
                               history. (optional)
    ``tsInt`` |str|            ``'Trapezoidal'`` or ``'Simpson'``
                               numerical integration method
    ``factor`` |float|         constant factor. (optional)
    ========================   =============================================================


    .. note::
    
       #. The displacements are the ones used in the ImposedMotions to set nodal response.
       #. If only the acceleration TimeSeries is provided, numerical integration will be used to determine the velocities and displacements.
       #. For earthquake excitations it is important that the user provide the displacement time history, as the one generated using the trapezoidal method will not provide good results.
       #. Any combination of the acceleration, velocity and displacement time-series can be specified.

    Hints:
        untested

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
    if tsInt:
        uniqueArgs.append('-int')
        uniqueArgs.append(accelSeriesTag)
           
    # if factor:
    uniqueArgs.append('-fact')
    uniqueArgs.append(factor)
        
        
    ops.groundMotion(gmTag, 'Plain', *uniqueArgs)


def Interpolated(gmTag, gmTags, facts = None):
    """
    This command is used to construct an interpolated GroundMotion object, where the motion is determined by combining several previously defined ground motions in the load pattern.


    ========================   =============================================================
    ``gmTag`` |int|            unique tag among ground motions in load pattern
    ``gmTags`` |listi|         the tags of existing ground motions in pattern to be used for interpolation
    ``facts`` |listf|          the interpolation factors. (optional)
    ========================   =============================================================
    Hints:
        untested

    """
    uniqueArgs = []
    if facts:
        uniqueArgs.append('-fact')
        uniqueArgs.append(facts)


    ops.groundMotion(gmTag, 'Interpolated', *gmTags, *uniqueArgs)



