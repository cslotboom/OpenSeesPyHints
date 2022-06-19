import openseespy.opensees as ops




def convertBinaryToText(inputfile, outputfile):
    """
    Convert binary file to text file
     
    ========================   ===========================================================================  
    ``inputfile`` |str|        input file name.
    ``outputfile`` |str|       output file name.
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    uniqueArgs = []
    ops.convertBinaryToText(inputfile, outputfile, *uniqueArgs)

def convertTextToBinary(inputfile, outputfile):
    """
    Convert text file to binary file
    ========================   ===========================================================================
    ``inputfile`` |str|        input file name.
    ``outputfile`` |str|       output file name.
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    ops.convertTextToBinary(inputfile, outputfile)



def database(type, dbName):
    """
    Create a database.
    
    ===========================   =====================================================================================================================================================
    ``type`` |str|                database type:
                                  
                                  * ``'File'`` - outputs database into a file
                                  
                                  * ``'MySQL'`` - creates a SQL database
                                  
                                  * ``'BerkeleyDB'`` - creates a BerkeleyDB database
    ``dbName`` |str|              database name.
    ===========================   =====================================================================================================================================================

    
    Hints:
        untested
    
    """
    ops.database(type, dbName)

def InitialStateAnalysis(flag):
    """
    Set the initial state analysis to ``'on'`` or ``'off'``
    
    ========================   ===========================================================================
    ``flag`` |str|             ``'on'`` or ``'off'``
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    ops.InitialStateAnalysis(flag)




def loadConst(pseudoTime):
    """
    This command is used to set the loads constant in the domain and to also set the time in the domain. When setting the loads constant, the procedure will invoke setLoadConst() on all LoadPattern objects which exist in the domain at the time the command is called.

    ========================   ===========================================================================  
    ``pseudoTime`` |float|     Time domain is to be set to (optional)
    ========================   ===========================================================================
 
    .. note::

    Load Patterns added afer this command is invoked are not set to constant.
    
    Hints:
        untested
    
    """
    uniqueArgs = []
    ops.loadConst('-time', pseudoTime)



def modalDamping(factor):
    """
    Set modal damping factor. The :func:`eigen` must be called before.
    
    ========================   ===========================================================================  
    ``factor`` |float|         damping factor.   
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    ops.modalDamping(factor)



def reactions(dynamic=True, rayleigh=True):
    """
    Calculate the reactions. Call this command before the :func:`nodeReaction`.
    
    ========================   ===========================================================================
    ``'-dynamic'`` |str|       Include dynamic effects.
    ``'-rayleigh'`` |str|      Include rayleigh damping.
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    uniqueArgs = []
    if dynamic:
        uniqueArgs.append('-dynamic')
    if rayleigh:
        uniqueArgs.append('-rayleigh')
    ops.reactions(*uniqueArgs)


def removeTag(type, tag):
    """
    This commmand is used to remove components from the model.

    ========================   ===========================================================================
    ``type`` |str|             type of the object, ``'ele'``, ``'loadPattern'``, ``'parameter'``, ``'node'``, ``'timeSeries'``, ``'sp'``, ``'mp'``.
    ``tag`` |int|              tag of the object
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """

    ops.remove(type, tag)


def removeRecorders():
    """
    Remove all recorder objects.

    
    Hints:
        untested
    
    """

    ops.remove('recorders')

def removeSP(nodeTag, dofTag, patternTag = None):
    """
    Remove a sp object based on node

    ========================   ===========================================================================    
    ``nodeTag`` |int|          node tag   
    ``dof`` |int|              dof the sp constrains    
    ``patternTag`` |int|       pattern tag, (optional)   
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    uniqueArgs = []
    if patternTag:
        uniqueArgs.append(patternTag)
        
    ops.remove('sp', nodeTag, dofTag, *uniqueArgs)



def reset():
    """
    This command is used to set the state of the domain to its original state.

    .. note::

    It iterates over all components of the domain telling them to set their state back to the initial state. This is not always the same as going back to the state of the model after initial model generation, e.g. if elements have been removed.

    
    Hints:
        untested
    
    """
    ops.reset()




def restore(commitTag):
    """
    Restore data from database, which should be created through :func:`database`.
        
    ===========================   =====================================================================================================================================================
    ``commitTag`` |int|           a tag identify the commit  
    ===========================   =====================================================================================================================================================

    
    Hints:
        untested
    
    """
    ops.restore(commitTag)



def save(commitTag):
    """
    Save current state to database, which should be created through :func:`database`.
    
    ===========================   =====================================================================================================================================================
    ``commitTag`` |int|           a tag identify the commit
    ===========================   =====================================================================================================================================================

    
    Hints:
        untested
    
    """
    ops.save(commitTag)


def sdfResponse(m, zeta, k, Fy, alpha, dtF, filename, dt, uresidual=0, umaxprev=0):
    """

    It is a command that computes bilinear single degree of freedom response in C++, and is much quicker than using the OpenSees model builder.  The command implements Newmark's method with an inner Newton loop.
    
    ========================   =============================================================
    ``m`` |float|              mass
    ``zeta`` |float|           damping ratio
    ``k`` |float|              stiffness
    ``Fy`` |float|             yielding strength
    ``alpha`` |float|          strain-hardening ratio
    ``dtF`` |float|            time step for input data
    ``filename`` |str|         input data file, one force per line
    ``dt`` |float|             time step for analysis
    ``uresidual`` |float|      residual displacement at the end of previous analysis
                               (optional, default=0)
    ``umaxprev`` |float|       previous displacement (optional, default=0)
    ========================   =============================================================
    
    The command returns a list of five response quantities.
    
    Returns
    
    ========================   =============================================================
    ``umax`` |float|           maximum displacement during analysis
    ``u`` |float|              displacement at end of analysis
    ``up`` |float|             permanent residual displacement at end of analysis
    ``amax`` |float|           maximum acceleration during analysis
    ``tamax`` |float|          time when maximum accleration occurred
    ========================   =============================================================

    
    Hints:
        untested
    
    """
    ops.sdfResponse(m, zeta, k, Fy, alpha, dtF, filename, dt, uresidual, umaxprev)



def setTime(pseudoTime):
    """
    This command is used to set the time in the Domain.
    
    ========================   ===========================================================================
    ``pseudoTime`` |float|     Time domain to be set
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []
    ops.setTime(pseudoTime, *uniqueArgs)



def setNodeCoord(nodeTag, dim, value, commit = False):
    """
    set the nodal coodinate at the specified dimension.
    
    ========================   ===========================================================================
    ``nodeTag`` |int|          node tag.
    ``dim`` |int|              the dimension of the coordinate to be set.
    ``value`` |float|          coordinate value
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []
    if commit:
        uniqueArgs.append('-commit')
    ops.setNodeCoord(nodeTag, dim, value, *uniqueArgs)




def setNodeCoord(nodeTag, dim, value, commit = False):
    """
    set the nodal coodinate at the specified dimension.
    
    ========================   ===========================================================================    
    ``nodeTag`` |int|          node tag.    
    ``dim`` |int|              the dimension of the coordinate to be set. 
    ``value`` |float|          coordinate value
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []
    if commit:
        uniqueArgs.append('-commit')
    ops.setNodeCoord(nodeTag, dim, value, *uniqueArgs)




def setNodeDisp(nodeTag, dof, value, commit = False):
    """
    set the nodal displacement at the specified DOF.
    
    ========================   ===========================================================================
    ``nodeTag`` |int|          node tag.
    ``dof`` |int|              the DOF of the displacement to be set.
    ``value`` |float|          displacement value
    ``'-commit'`` |str|        commit nodal state. (optional)
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []
    if commit:
        uniqueArgs.append('-commit')
    ops.setNodeDisp(nodeTag, dof, value, *uniqueArgs)


def setNodeVel(nodeTag, dof, value, commit = False):
    """
    set the nodal velocity at the specified DOF.
    
    ========================   ===========================================================================
    ``nodeTag`` |int|          node tag.
    ``dof`` |int|              the DOF of the velocity to be set.
    ``value`` |float|          velocity value
    ``'commit'`` |bool|        commit nodal state. (optional)
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []
    if commit:
        uniqueArgs.append('-commit')
    ops.setNodeVel(nodeTag, dof, value, *uniqueArgs)


def setNodeAccel(nodeTag, dof, value, commit = False):
    """
    set the nodal acceleration at the specified DOF.
    
    ========================   ===========================================================================
    ``nodeTag`` |int|          node tag.
    ``dof`` |int|              the DOF of the acceleration to be set.
    ``value`` |float|          acceleration value
    ``'commit'`` |bool|        commit nodal state. (optional)
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []
    if commit:
        uniqueArgs.append('-commit')
    ops.setNodeAccel(nodeTag, dof, value, *uniqueArgs)



def setPrecision(precision):
    """
    Set the precision for screen output.
    
    ========================   ===========================================================================
    ``precision`` |int|        the precision number.
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    ops.setPrecision(precision)

def setElementRayleighDampingFactors(eleTag, alphaM, betaK, betaK0, betaKc):
    """
    Set the :func:`rayleigh` damping for an element.
    
    ========================   ===========================================================================
    ``eleTag`` |int|           element tag
    ``alphaM`` |float|         factor applied to elements or nodes mass matrix
    ``betaK`` |float|          factor applied to elements current stiffness matrix.
    ``betaK0`` |float|         factor applied to elements initial stiffness matrix.
    ``betaKc`` |float|         factor applied to elements committed stiffness matrix.
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    ops.setElementRayleighDampingFactors(eleTag, alphaM, betaK, betaK0, betaKc)





def start():
    """
    Start the timer
    
    Hints:
        untested
    
    """
    ops.start()


def stop():
    """
    Stop the timer and print timing information.
    
    Hints:
        untested
    
    """
    ops.stop()
    



def stripXML(inputml, outputdata, outputxml):
    """
    Strip a xml file to a data file and a descriptive file.

    ========================   ===========================================================================
    ``inputxml`` |str|         input xml file name.
    ``outputdata`` |str|       output data file name.
    ``outputxml`` |str|        output xml file name.
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    ops.stripXML(inputml, outputdata, outputxml)







def updateElementDomain():
    """
    Update elements in the domain.

    
    Hints:
        untested
    
    """
    
    ops.updateElementDomain()




def updateMaterialStage(matTag, value, paramTag=None):
    """

    This function is used in geotechnical modeling to maintain elastic 
    nDMaterial response during the application of gravity loads. The material 
    is then updated to allow for plastic strains during additional static loads
    or earthquakes.
    
    ========================   =============================================================
    ``matTag`` |int|           tag of nDMaterial
    ``value`` |int|            stage value
    ``paramTag`` |int|         tag of parameter (optional)
    ========================   =============================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []    

    if paramTag:
        uniqueArgs.append('-parameter')
        uniqueArgs.append(paramTag)
    ops.updateMaterialStage('-material', matTag, '-stage', value,  *uniqueArgs)



def wipeAnalysis():

    """
    This command is used to destroy all components of the Analysis object, i.e. 
    any objects created with system, numberer, constraints, integrator, 
    algorithm, and analysis commands.
    
    
    Hints:
        untested
    
    """

    ops.wipeAnalysis()



def wipe():
    """
    This command is used to destroy all constructed objects, i.e. all 
    components of the model, all components of the analysis and all recorders.  
    
    This command is used to start over without having to exit and restart the 
    interpreter. It causes all elements, nodes, constraints, loads to be 
    removed from the domain. In addition it deletes all recorders, analysis 
    objects and all material objects created by the model builder.
    
    
    Hints:
        untested
    
    """
    ops.wipe()

def setNumThreads(num):
    """
    set the number of threads to be used in the multi-threaded environment.
    
    ========================   ===========================================================================
    ``num`` |int|              number of threades 
    ========================   ===========================================================================

    
    Hints:
        untested
    
    """
    uniqueArgs = []
    ops.setNumThreads(num, *uniqueArgs)

def getNumThreads():
    """
    set the number of threads to be used in the multi-threaded environment.
    
    ========================   ===========================================================================
    ``num`` |int|              number of threades 
    ========================   ===========================================================================
    
    Hints:
        untested
    
    """
    ops.getNumThreads()
