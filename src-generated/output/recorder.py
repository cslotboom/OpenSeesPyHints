import openseespy.opensees as ops

def EnvelopeNode(filename=None, filename=None, nSD, tsTag=None, deltaT, *nodeTags, startNode=None, endNode=None, regionTag=None, *dofs, respType):
    """


   The EnvelopeNode recorder type records the min, max and absolute max of a number of nodal response quantaties.



   ===========================   =====================================================================================================================================================

   ``filename`` |str|            name of file to which output is sent. file output is either in xml format (``'-xml'`` option), or

                                 textual (``'-file'`` option) which must pre-exist.

   ``nSD`` |int|                 number of significant digits (optional)

   ``'-time'`` |str|             using this option places domain time in first entry of each data line, default is to have time ommitted, (optional)

   ``'-closeOnWrite'`` |str|     using this option will instruct the recorder to invoke a close on the data handler after every timestep. 

                                 If this is a file it will close the file on every step and then re-open it for the next step. 

                                 Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) 

   ``deltaT`` |float|            time interval for recording. will record when next step is ``deltaT`` greater than last recorder step. 

                                 (optional, default: records at every time step)

   ``tsTag`` |int|               the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional)  

   ``nodeTags`` |listi|          list of tags of nodes whose response is being recorded (optional)

   ``startNode`` |int|           tag for start node whose response is being recorded (optional)

   ``endNode`` |int|             tag for end node whose response is being recorded (optional)     

   ``regionTag`` |int|           a region tag; to specify all nodes in the previously defined region. (optional)

   ``dofs`` |listi|              the specified dof at the nodes whose response is requested.                                            

   ``resType`` |lists|           a string indicating response required. Response types are given in table below

   

                                 * ``'disp'``     displacement

                                 * ``'vel'``      velocity

                                 * ``'accel'``    acceleration

                                 * ``'incrDisp'`` incremental displacement

                                 * ``'reaction'`` nodal reaction

                                 * ``'eigen i'``  eigenvector for mode i

   ===========================   =====================================================================================================================================================



    """
    uniqueArgs = []
    if filename:
        uniqueArgs.append('-file')
        uniqueArgs.append(filename)
    if filename:
        uniqueArgs.append('-xml')
        uniqueArgs.append(filename)
    if nSD=6:
        uniqueArgs.append('-precision')
    if tsTag:
        uniqueArgs.append('-timeSeries')
        uniqueArgs.append(tsTag)
    if '-dT':
        uniqueArgs.append('-time')
    if deltaT=0.0:
        uniqueArgs.append('-dT')
    if '-node':
        uniqueArgs.append('-closeOnWrite')
    if nodeTags=[]:
        uniqueArgs.append('-node')
    if startNode:
        uniqueArgs.append('-nodeRange')
        uniqueArgs.append(startNode)
        uniqueArgs.append(endNode)
    if regionTag:
        uniqueArgs.append('-region')
        uniqueArgs.append(regionTag)
    if dofs=[]:
        uniqueArgs.append('-dof')
    ops.recorder('EnvelopeNode', nSD, deltaT, *nodeTags, *dofs, respType, *uniqueArgs)

def Element(filename=None, filename=None, filename=None, nSD, tsTag=None, deltaT, *eleTags, startEle=None, endEle=None, regionTag=None, args=None):
    """


   The Element recorder type records the response of a number of elements at every converged step. The response recorded is element-dependent and also depends on the arguments which are passed to the setResponse() element method.



   ===========================   =====================================================================================================================================================

   ``filename`` |str|            name of file to which output is sent. file output is either in xml format (``'-xml'`` option), 

                                 textual (``'-file'`` option) or binary (``'-binary'`` option) which must pre-exist.

   ``nSD`` |int|                 number of significant digits (optional)

   ``'-time'`` |str|             using this option places domain time in first entry of each data line, default is to have time ommitted, (optional)

   ``'-closeOnWrite'`` |str|     using this option will instruct the recorder to invoke a close on the data handler after every timestep. 

                                 If this is a file it will close the file on every step and then re-open it for the next step. 

                                 Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) 

   ``deltaT`` |float|            time interval for recording. will record when next step is ``deltaT`` greater than last recorder step. 

                                 (optional, default: records at every time step)

   ``tsTag`` |int|               the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional)  

   ``eleTags`` |listi|           list of tags of elements whose response is being recorded (optional)

   ``startEle`` |int|            tag for start node whose response is being recorded (optional)

   ``endEle`` |int|              tag for end node whose response is being recorded (optional)     

   ``regionTag`` |int|           a region tag; to specify all nodes in the previously defined region. (optional)

   ``args`` |list|               arguments which are passed to the setResponse() element method, all arguments must be in string format even for double and integer numbers because internally the setResponse() element method only accepts strings.

   ===========================   =====================================================================================================================================================



.. note::



   The setResponse() element method is dependent on the element type, and is described with the :meth:`element` Command.

    """
    uniqueArgs = []
    if filename:
        uniqueArgs.append('-file')
        uniqueArgs.append(filename)
    if filename:
        uniqueArgs.append('-xml')
        uniqueArgs.append(filename)
    if filename:
        uniqueArgs.append('-binary')
        uniqueArgs.append(filename)
    if nSD=6:
        uniqueArgs.append('-precision')
    if tsTag:
        uniqueArgs.append('-timeSeries')
        uniqueArgs.append(tsTag)
    if '-dT':
        uniqueArgs.append('-time')
    if deltaT=0.0:
        uniqueArgs.append('-dT')
    if '-ele':
        uniqueArgs.append('-closeOnWrite')
    if eleTags=[]:
        uniqueArgs.append('-ele')
    if startEle:
        uniqueArgs.append('-eleRange')
        uniqueArgs.append(startEle)
        uniqueArgs.append(endEle)
    if regionTag:
        uniqueArgs.append('-region')
        uniqueArgs.append(regionTag)
        uniqueArgs.append(args)
    ops.recorder('Element', nSD, deltaT, *eleTags, *uniqueArgs)

def EnvelopeElement(filename=None, filename=None, filename=None, nSD, tsTag=None, deltaT, *eleTags, startEle=None, endEle=None, regionTag=None, args=None):
    """


   The Envelope Element recorder type records the response of a number of elements at every converged step. The response recorded is element-dependent and also depends on the arguments which are passed to the setResponse() element method. When the object is terminated, through the use of a wipe, exit, or remove the object will output the min, max and absolute max values on 3 seperate lines of the output file for each quantity.



   ===========================   =====================================================================================================================================================

   ``filename`` |str|            name of file to which output is sent. file output is either in xml format (``'-xml'`` option), 

                                 textual (``'-file'`` option) or binary (``'-binary'`` option) which must pre-exist.

   ``nSD`` |int|                 number of significant digits (optional)

   ``'-time'`` |str|             using this option places domain time in first entry of each data line, default is to have time ommitted, (optional)

   ``'-closeOnWrite'`` |str|     using this option will instruct the recorder to invoke a close on the data handler after every timestep. 

                                 If this is a file it will close the file on every step and then re-open it for the next step. 

                                 Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) 

   ``deltaT`` |float|            time interval for recording. will record when next step is ``deltaT`` greater than last recorder step. 

                                 (optional, default: records at every time step)

   ``tsTag`` |int|               the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional)  

   ``eleTags`` |listi|           list of tags of elements whose response is being recorded (optional)

   ``startEle`` |int|            tag for start node whose response is being recorded (optional)

   ``endEle`` |int|              tag for end node whose response is being recorded (optional)     

   ``regionTag`` |int|           a region tag; to specify all nodes in the previously defined region. (optional)

   ``args`` |list|               arguments which are passed to the setResponse() element method

   ===========================   =====================================================================================================================================================



.. note::



   The setResponse() element method is dependent on the element type, and is described with the :meth:`element` Command.

    """
    uniqueArgs = []
    if filename:
        uniqueArgs.append('-file')
        uniqueArgs.append(filename)
    if filename:
        uniqueArgs.append('-xml')
        uniqueArgs.append(filename)
    if filename:
        uniqueArgs.append('-binary')
        uniqueArgs.append(filename)
    if nSD=6:
        uniqueArgs.append('-precision')
    if tsTag:
        uniqueArgs.append('-timeSeries')
        uniqueArgs.append(tsTag)
    if '-dT':
        uniqueArgs.append('-time')
    if deltaT=0.0:
        uniqueArgs.append('-dT')
    if '-ele':
        uniqueArgs.append('-closeOnWrite')
    if eleTags=[]:
        uniqueArgs.append('-ele')
    if startEle:
        uniqueArgs.append('-eleRange')
        uniqueArgs.append(startEle)
        uniqueArgs.append(endEle)
    if regionTag:
        uniqueArgs.append('-region')
        uniqueArgs.append(regionTag)
        uniqueArgs.append(args)
    ops.recorder('EnvelopeElement', nSD, deltaT, *eleTags, *uniqueArgs)

def PVD(filename, precision, dT, res):
    """


   Create a PVD recorder.



   ========================   =============================================================

   ``filename`` |str|         the name for ``filename.pvd`` and ``filename/`` directory,

                              which must pre-exist.

   ``precision`` |int|        the precision of data. (optional)

   ``dT`` |float|             the time interval for recording. (optional)

   ``res`` |lists|            a list of |str| of responses to be recorded, (optional)



                              * ``'disp'``

                              * ``'vel'``

                              * ``'accel'``

                              * ``'incrDisp'``

                              * ``'reaction'``

                              * ``'pressure'``

                              * ``'unbalancedLoad'``

                              * ``'mass'``

                              * ``'eigen'``

   ========================   =============================================================



    """
    uniqueArgs = []
    if precision=10:
        uniqueArgs.append('-precision')
    if dT=0.0:
        uniqueArgs.append('-dT')
    ops.recorder('PVD', filename, precision, dT, *res, *uniqueArgs)

def BgPVD(filename, precision, dT, res):
    """


   Create a PVD recorder for background mesh. This recorder is same as the

   PVD recorder, but will be automatically called in background mesh and

   is able to record wave height and velocity.



   ========================   =============================================================

   ``filename`` |str|         the name for ``filename.pvd`` and ``filename/`` directory,

                              which must pre-exist.

   ``precision`` |int|        the precision of data. (optional)

   ``dT`` |float|             the time interval for recording. (optional)

   ``res`` |lists|            a list of |str| of responses to be recorded, (optional)



                              * ``'disp'``

                              * ``'vel'``

                              * ``'accel'``

                              * ``'incrDisp'``

                              * ``'reaction'``

                              * ``'pressure'``

                              * ``'unbalancedLoad'``

                              * ``'mass'``

                              * ``'eigen'``

   ========================   =============================================================



    """
    uniqueArgs = []
    if precision=10:
        uniqueArgs.append('-precision')
    if dT=0.0:
        uniqueArgs.append('-dT')
    ops.recorder('BgPVD', filename, precision, dT, *res, *uniqueArgs)

def Collapse(nodeTag=None, fileNameinf=None, nTagbotn=None, nTagmidn=None, nTagtopn=None, globgrav=None, eleTags=None, start=None, end=None, regionTag=None, dT=None, fileName=None, massValues=None, gAcc=None, gDir=None, gPat=None, secTags=None, critType=None, critValue=None):
    """


   A progressive collapse algorithm is developed by Talaat, M and Mosalam, K.M. in [1-3] and is implemented in

   OpenSeesPy interpreter. The different applications of said algorithm are exemplified in references [4-7].

   This algorithm is developed using element removal which relies on the dynamic equilibrium and the subsequent

   transient change in the system kinematics. The theoretical background of the routine is detailed in the references

   mentioned herein.





   ===========================   =====================================================================================================================================================

   ``nodeTag`` |int|             node tag

   ``fileNameinf`` |str|         is the file used to input the displacement interaction curve. Two columns of data are input in this file where only positive values are input. First column is the OOP displacement in ascending order and second column is the corresponding IP displacement. Full interaction should be defined. In other words, first value of OOP displacement and last value of IP displacement should be zero.

   ``fileName`` |str|            is the file name for element removal log. Only one log file is constructed for all collapse recorder commands (i.e. for all removals). The first file name input to a collapse recorder command is used and any subsequent file names are ignored.

   ``globgrav`` |float|          is the global axis of the model in the direction of gravity. 1, 2 and 3 should be input for X, Y and Z axes, respectively.

   ``critType`` |lists|          criterial type

   

                                 * ``'INFILLWALL'`` no value required

                                 * ``'minStrain'`` value required

                                 * ``'maxStrain'`` value required

                                 * ``'axialDI'`` value required

                                 * ``'flexureDI'`` value required

                                 * ``'axialLS'``  value required

                                 * ``'shearLS'``  value required

   ===========================   =====================================================================================================================================================



The progressive collapse algorithm is thus implemented within OpenSeesPy for an automatic removal of

elements which have “numerically” collapse during an ongoing dynamic simulation. Main elements of the

progressive collapse routine are illustrated in Figures 1 and 2. The implementation is supported in Python as a

relatively new OpenSees module. Following each converged step of the dynamic analysis, the algorithm is called

to check each element respectively for possible violation given a user-defined removal criteria. The routine calls

for the activation of the element removal sequence before accessing the main analysis module on the subsequent

analysis step. Activation of the element removal algorithm includes updating nodal masses, checking if the

removal of the collapsed element results in leaving behind dangling nodes or floating elements, which must be

removed as well and removing all associated element and nodal forces, imposed displacements, and constraints.





.. image:: ../_static/flowchart.png



.. image:: ../_static/elementremoval.png



 

Furthermore, the aforementioned infill wall element and its removal criteria are defined for force- and

displacement-based distributed plasticity fiber elements and lumped plasticity beam–column elements with fiber-

discretized plastic hinges. Current version of OpenSeesPy considers only the removal of the infill wall model

described

in

(https://opensees.berkeley.edu/wiki/index.php/Infill_Wall_Model_and_Element_Removal#New_Command_in_

OpenSees_Interpreter).

Implementation of the removal of the elements representing the aforementioned infill wall analytical model in the

progressive collapse algorithm is performed through defining a removal criterion for the beam-column elements

of this model. This criterion is based on the interaction between the in-plane (IP) and out-of-plane (OOP)

displacements. IP displacement is the relative horizontal displacement between the top and bottom nodes of the

diagonal element. OOP displacement is that of the middle node (where the OOP mass is attached) with respectto the chord which connects the top and bottom nodes. The user is free to choose any interaction relationship

between IP and OOP displacements. In the example highlighted above, the interaction between in-plane and

out-of-plane is taken into consideration with regards to the displacement interaction between the two

mechanisms, where the IP and OOP displacement capacities are obtained using the FEMA 356 formulation for

collapse prevention level. During the nonlinear time history simulation, when the mentioned combination of

displacements from the analysis exceeds the interaction curve, the two beam-column elements and the middle

node, representing the unreinforced masonry infill wall, are removed.



For the example illustrated in the next Figure, the existing Python command and its arguments in the OpenSeesPy interpreter

with respect to the infill wall removal is described such that:



.. code-block:: python



   recorder('Collapse', '-ele', ele1, '-time', '-crit', 'INFILLWALL', '-file', filename, '-file_infill', filenameinf, '-global_gravaxis, globgrav, '-checknodes', nodebot, nodemid, nodetop)



   recorder('Collapse', '-ele', ele2, '-time', '-crit', 'INFILLWALL', '-file', filename, '-file_infill', filenameinf, '-global_gravaxis, globgrav, '-checknodes', nodebot, nodemid, nodetop)



   recorder('Collapse', '-ele', ele1, ele2, '-node', nodemid)







.. image:: ../_static/collapserecorder.png





.. note::



   it might seem that node inputs are unnecessary. However, when there are shear springs in the model, nodetop and nodebot should be the nodes of the springs which connect to the beams, since the shear spring deformation contributes to the IP displacement of the infill wall. These nodes are not the nodes of the diagonal element. Therefore, it is necessary to input these nodes.



References



1. Talaat, M. and Mosalam, K.M. (2008), “Computational Modeling of Progressive Collapse in Reinforced

Concrete Frame Structures”, Pacific Earthquake Engineering Research Center, PEER 2007/10.

2. Talaat, M. and Mosalam, K.M. (2009), “Modeling Progressive Collapse in Reinforced Concrete Buildings

Using Direct Element Removal”, Earthquake Engineering and Structural Dynamics, 38(5): 609-634.

3. Talaat, M. and Mosalam, K.M. (2009), Chapter20: How to Simulate Column Collapse and Removal in As-

built and Retrofitted Building Structures?, in Seismic Risk Assessment and Retrofitting - with special emphasis

on existing low-rise structures, Ilki, A, Karadogan, F, Pala, S & Yuksel, E (Eds), ISBN 978-90-481-2680-4,

Springer.

4. Talaat, M. and Mosalam, K.M. (2006), “Progressive Collapse Modeling of Reinforced Concrete Framed

Structures Containing Masonry Infill Walls”, Proceedings of the 2nd NEES/E-Defense Workshop on Collapse

Simulation of Reinforced Concrete Building Structures, Kobe, Japan.

5. Talaat, M. and Mosalam, K.M. (2007), “Towards Modeling Progressive Collapse in Reinforced Concrete

Buildings”, Proceedings of SEI-ASCE 2007 Structures Congress, Long Beach, California, USA.

6. Mosalam, K.M., Talaat, M., and Park, S. (2008), “Modeling Progressive Collapse in Reinforced Concrete

Framed Structures”, Proceedings of the 14th World Conference on Earthquake Engineering, Beijing, China,

October 12-17, Paper S15-018.

7. Mosalam, K.M., Park, S., Günay, M.S. (2009), “Evaluation of an Element Removal Algorithm for Reinforced

Concrete Structures Using Shake Table Experiments,” Proceedings of the 2nd International Conference on

Computational Methods in structural Dynamics and Earthquake Engineering (COMPDYN 2009), Island of

Rhodes, Greece, June 22-24.

    """
    uniqueArgs = []
    if nodeTag:
        uniqueArgs.append('-node')
        uniqueArgs.append(nodeTag)
    if fileNameinf:
        uniqueArgs.append('-file_infill')
        uniqueArgs.append(fileNameinf)
    if nTagbotn:
        uniqueArgs.append('-checknodes')
        uniqueArgs.append(nTagbotn)
        uniqueArgs.append(nTagmidn)
        uniqueArgs.append(nTagtopn)
    if globgrav:
        uniqueArgs.append('-global_gravaxis')
        uniqueArgs.append(globgrav)
    if '-eles':
        uniqueArgs.append('-secondary')
    if eleTags:
        uniqueArgs.append('-eles')
        uniqueArgs.append(eleTags)
    if start:
        uniqueArgs.append('-eleRage')
        uniqueArgs.append(start)
        uniqueArgs.append(end)
    if regionTag:
        uniqueArgs.append('-region')
        uniqueArgs.append(regionTag)
    if '-dT':
        uniqueArgs.append('-time')
    if dT:
        uniqueArgs.append('-dT')
        uniqueArgs.append(dT)
    if fileName:
        uniqueArgs.append('-file')
        uniqueArgs.append(fileName)
    if massValues:
        uniqueArgs.append('-mass')
        uniqueArgs.append(massValues)
    if gAcc:
        uniqueArgs.append('-g')
        uniqueArgs.append(gAcc)
        uniqueArgs.append(gDir)
        uniqueArgs.append(gPat)
    if secTags:
        uniqueArgs.append('-section')
        uniqueArgs.append(secTags)
    if critType:
        uniqueArgs.append('-crit')
        uniqueArgs.append(critType)
        uniqueArgs.append(critValue)
    ops.recorder('Collapse', *uniqueArgs)

