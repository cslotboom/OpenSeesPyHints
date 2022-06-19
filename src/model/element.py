import openseespy.opensees as ops

def zeroLength(eleTag, eleNodes, matTags=None, dirs=None, rFlag=0, vecx=None, vecyp=None):
    """
    
    This command is used to construct a zeroLength element object, which is defined by two nodes at the same location. 
    The nodes are connected by multiple UniaxialMaterial objects to represent the force-deformation relationship for the element.
    
    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag
    
    ``eleNodes`` |listi|                  a list of two element nodes
    
    ``matTags`` |listi|                   a list of tags associated with previously-defined UniaxialMaterials
    
    ``dirs`` |listi|                      a list of material directions:
    
                                          * 1,2,3 - translation along local x,y,z axes, respectively;
    
                                          * 4,5,6 - rotation about local x,y,z axes, respectively
    
    ``rFlag`` |float|                     optional, default = 0 NO RAYLEIGH DAMPING (default), 1 include Rayleigh damping
    
    ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)
    
    ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional)
    ===================================   ===========================================================================

    .. note::
    
       If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.
    
    .. seealso::
    
       `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLength_Element>`_

    """
    
    
    uniqueArgs = []
    if matTags:
        uniqueArgs.append('-mat')
        uniqueArgs += matTags
    if dirs:
        uniqueArgs.append('-dir')
        uniqueArgs += dirs
    if rFlag==1:
        uniqueArgs.append('-doRayleigh')
        uniqueArgs.append(rFlag)
    if vecx:
        uniqueArgs.append('-orient')
        uniqueArgs += vecx
        uniqueArgs += vecyp
    ops.element('zeroLength', eleTag, *eleNodes, *uniqueArgs)

# def zeroLengthND(eleTag, eleNodes, matTag, uniTag=None, vecx=None, vecyp=None):
#     """


#    This command is used to construct a zeroLengthND element object, which is defined by two nodes at the same location. 
#    The nodes are connected by a single NDMaterial object to represent the force-deformation relationship for the element.



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``matTag`` |int|                      tag associated with previously-defined ndMaterial object

#    ``uniTag`` |int|                      tag associated with previously-defined UniaxialMaterial object which may be used to represent uncoupled behavior orthogonal to the plane of the NDmaterial response. SEE NOTES 2 and 3.

#    ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)

#    ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional)

#    ===================================   ===========================================================================





# .. note::



#    #. The zeroLengthND element only represents translational response between its nodes

#    #. If the NDMaterial object is of order two, the response lies in the element local x-y plane and the UniaxialMaterial object may be used to represent the uncoupled behavior orthogonal to this plane, i.e. along the local z-axis.

#    #. If the NDMaterial object is of order three, the response is along each of the element local exes.

#    #. If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

#    #. The valid queries to a zero-length element when creating an ElementRecorder object are 'force', 'deformation', and 'material matArg1 matArg2 ...'



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthND_Element>`_

#     """
#     uniqueArgs = []
#     if uniTag:
#         uniqueArgs.append(uniTag)
#     if vecx:
#         uniqueArgs.append('-orient')
#         uniqueArgs.append(*vecx)
#         uniqueArgs.append(vecyp)
#     ops.element('zeroLengthND', eleTag, *eleNodes, matTag, *uniqueArgs)

# def zeroLengthSection(eleTag, eleNodes, secTag, vecx=None, vecyp=None, rFlag=None):
#     """


#    This command is used to construct a zero length element object, which is defined by two nodes at the same location. The nodes are connected by a single section object to represent the force-deformation relationship for the element.







#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``secTag`` |int|                      tag associated with previously-defined Section object

#    ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)

#    ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional)

#    ``rFlag`` |float|                     optional, default = 0



#                                          * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)

#                                          * ``rFlag`` = 1 include rayleigh damping

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthSection_Element>`_

#     """
#     uniqueArgs = []
#     if vecx:
#         uniqueArgs.append('-orient')
#         uniqueArgs.append(*vecx)
#         uniqueArgs.append(*vecyp)
#     if rFlag:
#         uniqueArgs.append('-doRayleigh')
#         uniqueArgs.append(rFlag)
#     ops.element('zeroLengthSection', eleTag, *eleNodes, secTag, *uniqueArgs)

# def CoupledZeroLength(eleTag, eleNodes, dirn1, dirn2, matTag, rFlag=1=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``matTag`` |float|                    tags associated with previously-defined UniaxialMaterial

#    ``dirn1``  ``dirn2`` |int|              the two directions, 1 through ndof.

#    ``rFlag`` |float|                     optional, default = 0



#                                          * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)

#                                          * ``rFlag`` = 1 include rayleigh damping



#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/CoupledZeroLength_Element>`_

#     """
#     uniqueArgs = []
#     if rFlag=1:
#         uniqueArgs.append(rFlag=1)
#     ops.element('CoupledZeroLength', eleTag, *eleNodes, dirn1, dirn2, matTag, *uniqueArgs)

# def zeroLengthContact2D(eleTag, eleNodes, Kn, Kt, mu, Nx=None, Ny=None):


#    This command is used to construct a zeroLengthContact2D element, which is Node-to-node frictional contact element used in two dimensional analysis and three dimensional analysis:







#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of a constrained and a retained nodes

#    ``Kn`` |float|                        Penalty in normal direction

#    ``Kt`` |float|                        Penalty in tangential direction

#    ``mu`` |float|                        friction coefficient

#    ===================================   ===========================================================================





#     uniqueArgs = []
#     if Nx:
#         uniqueArgs.append('-normal')
#         uniqueArgs.append(Nx)
#         uniqueArgs.append(Ny)
#     ops.element('zeroLengthContact2D', eleTag, *eleNodes, Kn, Kt, mu, *uniqueArgs)

# def zeroLengthContact3D(eleTag, eleNodes, Kn, Kt, mu, c, dir):


#    This command is used to construct a zeroLengthContact3D element, which is Node-to-node frictional contact element used in two dimensional analysis and three dimensional analysis:







#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of a constrained and a retained nodes

#    ``Kn`` |float|                        Penalty in normal direction

#    ``Kt`` |float|                        Penalty in tangential direction

#    ``mu`` |float|                        friction coefficient

#    ``c`` |float|                         cohesion (not available in 2D)

#    ``dir`` |int|                         Direction flag of the contact plane (3D), it can be:



#                                          * 1 Out normal of the master plane pointing to +X direction

#                                          * 2 Out normal of the master plane pointing to +Y direction

#                                          * 3 Out normal of the master plane pointing to +Z direction

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContact_Element>`_

#     uniqueArgs = []
#     ops.element('zeroLengthContact3D', eleTag, *eleNodes, Kn, Kt, mu, c, dir, *uniqueArgs)

# def zeroLengthContactNTS2D(eleTag, sNdNum=None, mNdNum=None, NodesTags=None, kn=None, kt=None, phi=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``sNdNum`` |int|                      Number of Slave Nodes

#    ``mNdNum`` |int|                      Number of Master nodes

#    ``NodesTags`` |listi|                 Slave and master node tags respectively

#    ``kn`` |float|                        Penalty in normal direction

#    ``kt`` |float|                        Penalty in tangential direction

#    ``phi`` |float|                       Friction angle in degrees

#    ===================================   ===========================================================================





# .. note::



#    #. The contact element is node-to-segment (NTS) contact. The relation follows Mohr-Coulomb frictional law: :math:`T = N \times \tan(\phi)`, where :math:`T` is the tangential force, :math:`N` is normal force across the interface and :math:`\phi` is friction angle.

#    #. For 2D contact, slave nodes and master nodes must be 2 DOF and notice that the slave and master nodes must be entered in counterclockwise order.

#    #. The resulting tangent from the contact element is non-symmetric. Switch to the non-symmetric matrix solver if convergence problem is experienced.

#    #. As opposed to node-to-node contact, predefined normal vector for node-to-segment (NTS) element is not required because contact normal will be calculated automatically at each step.

#    #. contact element is implemented to handle large deformations.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContactNTS2D>`_

#     """
#     uniqueArgs = []
#     if sNdNum:
#         uniqueArgs.append('-sNdNum')
#         uniqueArgs.append(sNdNum)
#     if mNdNum:
#         uniqueArgs.append('-mNdNum')
#         uniqueArgs.append(mNdNum)
#     if NodesTags:
#         uniqueArgs.append('-Nodes')
#         uniqueArgs.append(NodesTags)
#         uniqueArgs.append(kn)
#         uniqueArgs.append(kt)
#         uniqueArgs.append(phi)
#     ops.element('zeroLengthContactNTS2D', eleTag, *uniqueArgs)

# def zeroLengthInterface2D(eleTag, sNdNum=None, mNdNum=None, sdof=None, mdof=None, NodesTags=None, kn=None, kt=None, phi=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``sNdNum`` |int|                      Number of Slave Nodes

#    ``mNdNum`` |int|                      Number of Master nodes

#    ``sdof``, ``mdof`` |int|              Slave and Master degree of freedom

#    ``NodesTags`` |listi|                 Slave and master node tags respectively

#    ``kn`` |float|                        Penalty in normal direction

#    ``kt`` |float|                        Penalty in tangential direction

#    ``phi`` |float|                       Friction angle in degrees

#    ===================================   ===========================================================================





# .. note::



#    #. The contact element is node-to-segment (NTS) contact. The relation follows Mohr-Coulomb frictional law: :math:`T = N \times \tan(\phi)`, where :math:`T` is the tangential force, :math:`N` is normal force across the interface and :math:`\phi` is friction angle.

#    #. For 2D contact, slave nodes and master nodes must be 2 DOF and notice that the slave and master nodes must be entered in counterclockwise order.

#    #. The resulting tangent from the contact element is non-symmetric. Switch to the non-symmetric matrix solver if convergence problem is experienced.

#    #. As opposed to node-to-node contact, predefined normal vector for node-to-segment (NTS) element is not required because contact normal will be calculated automatically at each step.

#    #. contact element is implemented to handle large deformations.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthInterface2D>`_

#     """
#     uniqueArgs = []
#     if sNdNum:
#         uniqueArgs.append('-sNdNum')
#         uniqueArgs.append(sNdNum)
#     if mNdNum:
#         uniqueArgs.append('-mNdNum')
#         uniqueArgs.append(mNdNum)
#     if sdof:
#         uniqueArgs.append('-dof')
#         uniqueArgs.append(sdof)
#         uniqueArgs.append(mdof)
#     if NodesTags:
#         uniqueArgs.append('-Nodes')
#         uniqueArgs.append(NodesTags)
#         uniqueArgs.append(kn)
#         uniqueArgs.append(kt)
#         uniqueArgs.append(phi)
#     ops.element('zeroLengthInterface2D', eleTag, *uniqueArgs)

# def zeroLengthImpact3D(eleTag, eleNodes, direction, initGap, frictionRatio, Kt, Kn, Kn2, Delta_y, cohesion):
#     """


#    This command constructs a node-to-node zero-length contact element in 3D space to simulate the impact/pounding and friction phenomena.







#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of a constrained and a retained nodes

#    ``direction`` |int|

#                                          * ``1`` if out-normal vector of master plane points to +X direction

#                                          * ``2`` if out-normal vector of master plane points to +Y direction

#                                          * ``3`` if out-normal vector of master plane points to +Z direction

#    ``initGap`` |float|                   Initial gap between master plane and slave plane

#    ``frictionRatio`` |float|             Friction ratio in two tangential directions (parallel to master and slave planes)

#    ``Kt`` |float|                        Penalty in two tangential directions

#    ``Kn`` |float|                        Penalty in normal direction (normal to master and slave planes)

#    ``Kn2`` |float|                       Penalty in normal direction after yielding based on Hertz impact model

#    ``Delta_y`` |float|                   Yield deformation based on Hertz impact model

#    ``cohesion`` |float|                  Cohesion, if no cohesion, it is zero

#    ===================================   ===========================================================================



# .. note::



#    #. This element has been developed on top of the "zeroLengthContact3D". All the notes available in "zeroLengthContact3D" wiki page would apply to this element as well. It includes the definition of master and slave nodes, the number of degrees of freedom in the domain, etc.

#    #. Regarding the number of degrees of freedom (DOF), the end nodes of this element should be defined in 3DOF domain. For getting information on how to use 3DOF and 6DOF domain together, please refer to OpenSees documentation and forums or see the zip file provided in the EXAMPLES section below.

#    #. This element adds the capabilities of "ImpactMaterial" to "zeroLengthContact3D."

#    #. For simulating a surface-to-surface contact, the element can be defined for connecting the nodes on slave surface to the nodes on master surface.

#    #. The element was found to be fast-converging and eliminating the need for extra elements and nodes in the modeling process.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthImpact3D>`_

#     """
#     uniqueArgs = []
#     ops.element('zeroLengthImpact3D', eleTag, *eleNodes, direction, initGap, frictionRatio, Kt, Kn, Kn2, Delta_y, cohesion, *uniqueArgs)

def Truss(eleTag, eleNodes, A, matTag, rho=None, cFlag=None, rFlag=None):
    """

    One way is to specify an area and a UniaxialMaterial identifier:
        
    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``A`` |float|                         cross-sectional area of element

    ``matTag`` |int|                      tag associated with previously-defined UniaxialMaterial

    ``rho`` |float|                       mass per unit length, optional, default = 0.0

    ``cFlag`` |float|                     consistent mass flag, optional, default = 0

                                          * ``cFlag`` = 0 lumped mass matrix (default)

                                          * ``cFlag`` = 1 consistent mass matrix

    ``rFlag`` |float|                     Rayleigh damping flag, optional, default = 0

                                          * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)

                                          * ``rFlag`` = 1 include Rayleigh damping

    ===================================   ===========================================================================
 
    .. note::
       
        #. The truss element DOES NOT include geometric nonlinearities, even when used with beam-columns utilizing P-Delta or Corotational transformations.
    
        #. When constructed with a UniaxialMaterial object, the truss element considers strain-rate effects, and is thus suitable for use as a damping element.
    
        #. The valid queries to a truss element when creating an ElementRecorder object are 'axialForce,' 'forces,' 'localForce', deformations,' 'material matArg1 matArg2...,' 'section sectArg1 sectArg2...' There will be more queries after the interface for the methods involved have been developed further.
           
    .. seealso::

    `wiki <https://openseespydoc.readthedocs.io/en/latest/src/trussEle.html>`_
    
    `Notes <http://opensees.berkeley.edu/wiki/index.php/Truss_Element>`_
  
    
    
    """
    uniqueArgs = []
    if rho:
        uniqueArgs.append('-rho')
        uniqueArgs.append(rho)
    if cFlag:
        uniqueArgs.append('-cMass')
        uniqueArgs.append(cFlag)
    if rFlag:
        uniqueArgs.append('-doRayleigh')
        uniqueArgs.append(rFlag)
    ops.element('Truss', eleTag, *eleNodes, A, matTag, *uniqueArgs)




def TrussSection(eleTag, eleNodes, secTag, rho=None, cFlag=None, rFlag=None):
    """
    the other is to specify a Section identifier:

    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``secTag`` |int|                      tag associated with previously-defined Section

    ``rho`` |float|                       mass per unit length, optional, default = 0.0

    ``cFlag`` |float|                     consistent mass flag, optional, default = 0

                                          * ``cFlag`` = 0 lumped mass matrix (default)

                                          * ``cFlag`` = 1 consistent mass matrix

    ``rFlag`` |float|                     Rayleigh damping flag, optional, default = 0

                                          * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)

                                          * ``rFlag`` = 1 include Rayleigh damping

    ===================================   ===========================================================================


    .. note::
        
        #. The truss element DOES NOT include geometric nonlinearities, even when used with beam-columns utilizing P-Delta or Corotational transformations.
    
        #. When constructed with a UniaxialMaterial object, the truss element considers strain-rate effects, and is thus suitable for use as a damping element.
    
        #. The valid queries to a truss element when creating an ElementRecorder object are 'axialForce,' 'forces,' 'localForce', deformations,' 'material matArg1 matArg2...,' 'section sectArg1 sectArg2...' There will be more queries after the interface for the methods involved have been developed further.
    
    .. seealso::
    
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/trussEle.html>`_
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Truss_Element>`_
    """
    uniqueArgs = []
    if rho:
        uniqueArgs.append('-rho')
        uniqueArgs.append(rho)
    if cFlag:
        uniqueArgs.append('-cMass')
        uniqueArgs.append(cFlag)
    if rFlag:
        uniqueArgs.append('-doRayleigh')
        uniqueArgs.append(rFlag)
    ops.element('TrussSection', eleTag, *eleNodes, secTag, *uniqueArgs)

def corotTruss(eleTag, eleNodes, A, matTag, rho=None, cFlag=None, rFlag=None):
    """

    One way is to specify an area and a UniaxialMaterial identifier:
    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``A`` |float|                         cross-sectional area of element

    ``matTag`` |int|                      tag associated with previously-defined UniaxialMaterial

    ``rho`` |float|                       mass per unit length, optional, default = 0.0

    ``cFlag`` |float|                     consistent mass flag, optional, default = 0

                                          * ``cFlag`` = 0 lumped mass matrix (default)
                                          * ``cFlag`` = 1 consistent mass matrix

    ``rFlag`` |float|                     Rayleigh damping flag, optional, default = 0

                                          * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)
                                          * ``rFlag`` = 1 include Rayleigh damping

    ===================================   ===========================================================================
    
    .. note::  
    
        #. When constructed with a UniaxialMaterial object, the corotational truss element considers strain-rate effects, and is thus suitable for use as a damping element.
        #. The valid queries to a truss element when creating an ElementRecorder object are 'axialForce,' 'stiff,' deformations,' 'material matArg1 matArg2...,' 'section sectArg1 sectArg2...' There will be more queries after the interface for the methods involved have been developed further.
        #. CorotTruss DOES NOT include Rayleigh damping by default.
    
    
    .. seealso::    
    
    `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/corotTruss.html>`_
    
    `Notes <http://opensees.berkeley.edu/wiki/index.php/Corotational_Truss_Element>`_
    """


    uniqueArgs = []
    if rho:
        uniqueArgs.append('-rho')
        uniqueArgs.append(rho)
    if cFlag:
        uniqueArgs.append('-cMass')
        uniqueArgs.append(cFlag)
    if rFlag:
        uniqueArgs.append('-doRayleigh')
        uniqueArgs.append(rFlag)
    ops.element('corotTruss', eleTag, *eleNodes, A, matTag, *uniqueArgs)

def corotTrussSection(eleTag, eleNodes, secTag, rho=None, cFlag=None, rFlag=None):
    """

    the other is to specify a Section identifier:

    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``secTag`` |int|                      tag associated with previously-defined Section

    ``rho`` |float|                       mass per unit length, optional, default = 0.0

    ``cFlag`` |float|                     consistent mass flag, optional, default = 0

                                          * ``cFlag`` = 0 lumped mass matrix (default)
                                          * ``cFlag`` = 1 consistent mass matrix

    ``rFlag`` |float|                     Rayleigh damping flag, optional, default = 0

                                          * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)
                                          * ``rFlag`` = 1 include Rayleigh damping

    ===================================   ===========================================================================

    .. note::  
    
        #. When constructed with a UniaxialMaterial object, the corotational truss element considers strain-rate effects, and is thus suitable for use as a damping element.
        #. The valid queries to a truss element when creating an ElementRecorder object are 'axialForce,' 'stiff,' deformations,' 'material matArg1 matArg2...,' 'section sectArg1 sectArg2...' There will be more queries after the interface for the methods involved have been developed further.
        #. CorotTruss DOES NOT include Rayleigh damping by default.
    
    
    .. seealso::    
    
    `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/corotTruss.html>`_
    
    `Notes <http://opensees.berkeley.edu/wiki/index.php/Corotational_Truss_Element>`_
    """
    
    
    uniqueArgs = []
    if rho:
        uniqueArgs.append('-rho')
        uniqueArgs.append(rho)
    if cFlag:
        uniqueArgs.append('-cMass')
        uniqueArgs.append(cFlag)
    if rFlag:
        uniqueArgs.append('-doRayleigh')
        uniqueArgs.append(rFlag)
    ops.element('corotTrussSection', eleTag, *eleNodes, secTag, *uniqueArgs)

def elasticBeamColumn2D(eleTag, eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag, mass=None, cMass=False, releaseCode=0):
    """

    This command is used to construct an elasticBeamColumn element object. 
    The arguments for the construction of an elastic beam-column element depend on the dimension of the problem, (ndm)

    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``Area`` |float|                      cross-sectional area of element

    ``E_mod`` |float|                     Young's Modulus

    ``G_mod`` |float|                     Shear Modulus

    ``Jxx`` |float|                       torsional moment of inertia of cross section

    ``Iy`` |float|                        second moment of area about the local y-axis

    ``Iz`` |float|                        second moment of area about the local z-axis

    ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object

    ``mass`` |float|                      element mass per unit length (optional, default = 0.0)

    ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)

    ``'releaseCode'`` |int|               moment release (optional, 2d only, 0=no release (default), 1=release at I, 2=release at J, 3=release at I and J)
    ===================================   ===========================================================================

    .. seealso::
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html>`_
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element>`_
    """

    uniqueArgs = []
    if mass:
        uniqueArgs.append('-mass')
        uniqueArgs.append(mass)
    if cMass:
        uniqueArgs.append('-cMass')
    ops.element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag, *uniqueArgs)

def elasticBeamColumn3D(eleTag, eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag, mass=None, cMass=False):

    """
    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``Area`` |float|                      cross-sectional area of element

    ``E_mod`` |float|                     Young's Modulus

    ``G_mod`` |float|                     Shear Modulus

    ``Jxx`` |float|                       torsional moment of inertia of cross section

    ``Iy`` |float|                        second moment of area about the local y-axis

    ``Iz`` |float|                        second moment of area about the local z-axis

    ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object

    ``mass`` |float|                      element mass per unit length (optional, default = 0.0)

    ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)
    ===================================   ===========================================================================

    .. seealso::
        
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html>`_
            
        `Wiki2 <https://opensees.github.io/OpenSeesDocumentation/user/manual/model/elements/elasticBeamColumn.html?highlight=elasticbeamcolumn>`_

        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element>`_
    """

    uniqueArgs = []
    uniqueArgs = []
    if mass:
        uniqueArgs.append('-mass')
        uniqueArgs.append(mass)
    if cMass:
        uniqueArgs.append('-cMass')
    ops.element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag, *uniqueArgs)

# def ModElasticBeam2d(eleTag, eleNodes, Area, E_mod, Iz, K11, K33, K44, transfTag, massDens=None, cMass=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``Area`` |float|                         cross-sectional area of element

#    ``E_mod`` |float|                         Young's Modulus

#    ``Iz`` |float|                        second moment of area about the local z-axis

#    ``K11`` |float|                       stiffness modifier for translation

#    ``K33`` |float|                       stiffness modifier for translation

#    ``K44`` |float|                       stiffness modifier for rotation

#    ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object

#    ``massDens`` |float|                  element mass per unit length (optional, default = 0.0)

#    ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element_with_Stiffness_Modifiers>`_

#     """
#     uniqueArgs = []
#     if massDens:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(massDens)
#         uniqueArgs.append(cMass)
#     ops.element('ModElasticBeam2d', eleTag, *eleNodes, Area, E_mod, Iz, K11, K33, K44, transfTag, *uniqueArgs)

def ElasticTimoshenkoBeam2D(eleTag, eleNodes, E_mod, G_mod, Area, Iz, Avy, transfTag, massDens=None, cMass=None):
    """
    
    This command is used to construct an ElasticTimoshenkoBeam element object. 
    A Timoshenko beam is a frame member that accounts for shear deformations. 
    The arguments for the construction of an elastic Timoshenko beam element 
    depend on the dimension of the problem, ndm:
    For a two-dimensional problem:
        
    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``E_mod`` |float|                     Young's Modulus

    ``G_mod`` |float|                     Shear Modulus

    ``Area`` |float|                      cross-sectional area of element

    ``Iz`` |float|                        second moment of area about the local z-axis

    ``Avy`` |float|                       Shear area for the local y-axis

    ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object

    ``massDens`` |float|                  element mass per unit length (optional, default = 0.0)

    ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)
    ===================================   ===========================================================================

    .. seealso::
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/ElasticTimoshenkoBeam.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Timoshenko_Beam_Column_Element>`_
    """

    uniqueArgs = []
    if massDens:
        uniqueArgs.append('-mass')
        uniqueArgs.append(massDens)
    if cMass:
        uniqueArgs.append('-cMass')
    ops.element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Avy, transfTag, *uniqueArgs)

def ElasticTimoshenkoBeam(eleTag, eleNodes, E_mod, G_mod, Area, Jxx, Iy, Iz, Avy, Avz, transfTag, massDens=None, cMass=None):

    """
    
    This command is used to construct an ElasticTimoshenkoBeam element object. 
    A Timoshenko beam is a frame member that accounts for shear deformations. 
    The arguments for the construction of an elastic Timoshenko beam element 
    depend on the dimension of the problem, ndm:
    For a three-dimensional problem:
        
    ===================================   ===========================================================================
    ``eleTag`` |int|                      unique element object tag

    ``eleNodes`` |listi|                  a list of two element nodes

    ``E_mod`` |float|                     Young's Modulus

    ``G_mod`` |float|                     Shear Modulus

    ``Area`` |float|                      cross-sectional area of element

    ``Jxx`` |float|                       torsional moment of inertia of cross section

    ``Iy`` |float|                        second moment of area about the local y-axis

    ``Iz`` |float|                        second moment of area about the local z-axis

    ``Avy`` |float|                       Shear area for the local y-axis

    ``Avz`` |float|                       Shear area for the local z-axis

    ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object

    ``massDens`` |float|                  element mass per unit length (optional, default = 0.0)

    ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)
    ===================================   ===========================================================================

    .. seealso::
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/ElasticTimoshenkoBeam.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Timoshenko_Beam_Column_Element>`_
    """

    uniqueArgs = []
    if massDens:
        uniqueArgs.append('-mass')
        uniqueArgs.append(massDens)
    if cMass:
        uniqueArgs.append('-cMass')
    ops.element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Jxx, Iy, Iz, Avy, Avz, transfTag, *uniqueArgs)
    uniqueArgs = []
    if massDens:
        uniqueArgs.append('-mass')
        uniqueArgs.append(massDens)
        uniqueArgs.append(cMass)
    ops.element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Jxx, Iy, Iz, Avy, Avz, transfTag, *uniqueArgs)

def dispBeamColumn(eleTag, eleNodes, transfTag, integrationTag, cMass = False, mass = None):
    """
    Create a dispBeamColumn element.

    ========================   =============================================================
    ``eleTag`` |int|           tag of the element

    ``eleNodes`` |listi|         list of two node tags

    ``transfTag`` |int|        tag of transformation

    ``integrationTag`` |int|   tag of :func:`beamIntegration`

    ``'-cMass'``               to form consistent mass matrix (optional, default = lumped mass matrix)

    ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)

    ========================   =============================================================

    """
    uniqueArgs = []
    if '-mass':
        uniqueArgs.append('-cMass')
    if mass:
        uniqueArgs.append('-mass')
        uniqueArgs.append(mass)
    ops.element('dispBeamColumn', eleTag, *eleNodes, transfTag, integrationTag, mass, *uniqueArgs)

def forceBeamColumn(eleTag, eleNodes, transfTag, integrationTag, maxIter=None, tol=None, mass=None):
    """
    Create a ForceBeamColumn element.

    ========================   =============================================================
    ``eleTag`` |int|           tag of the element

    ``eleNodes`` |listi|       a list of two element nodes

    ``transfTag`` |int|        tag of transformation

    ``integrationTag`` |int|   tag of :func:`beamIntegration`

    ``maxIter`` |int|          maximum number of iterations to undertake to satisfy element compatibility (optional)

    ``tol`` |float|            tolerance for satisfaction of element compatibility (optional)

    ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)
    ========================   =============================================================

    .. seealso::
        
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/ElasticTimoshenkoBeam.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Timoshenko_Beam_Column_Element>`_

    """
    uniqueArgs = []
    if maxIter:
        uniqueArgs.append('-iter')
        uniqueArgs.append(maxIter)
        # uniqueArgs.append(tol)
    if tol:
        uniqueArgs.append(tol)
    if mass:
        uniqueArgs.append('-mass')
        uniqueArgs.append(mass)
    ops.element('forceBeamColumn', eleTag, *eleNodes, transfTag, integrationTag, maxIter, tol, mass, *uniqueArgs)

# def nonlinearBeamColumn(eleTag, eleNodes, numIntgrPts, secTag, transfTag, maxIter, tol, mass, intType=None):
#     """


#    Create a nonlinearBeamColumn element. This element is for backward compatability.



#    ========================   =============================================================

#    ``eleTag`` |int|           tag of the element

#    ``eleNodes`` |listi|       a list of two element nodes

#    ``numIntgrPts`` |int|      number of integration points.

#    ``secTag`` |int|           tag of section

#    ``transfTag`` |int|        tag of transformation

#    ``maxIter`` |int|          maximum number of iterations to undertake to satisfy element compatibility (optional)

#    ``tol`` |float|            tolerance for satisfaction of element compatibility (optional)

#    ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)

#    ``intType`` |str|          integration type (optional, default is ``'Lobatto'``)



#                               * ``'Lobatto'``

#                               * ``'Legendre'``

#                               * ``'Radau'``

#                               * ``'NewtonCotes'``

#                               * ``'Trapezoidal'``

#    ========================   =============================================================



#     """
#     uniqueArgs = []
#     if maxIter=10:
#         uniqueArgs.append('-iter')
#     if mass=0.0:
#         uniqueArgs.append('-mass')
#     if intType:
#         uniqueArgs.append('-integration')
#         uniqueArgs.append(intType)
#     ops.element('nonlinearBeamColumn', eleTag, *eleNodes, numIntgrPts, secTag, transfTag, maxIter, tol, mass, *uniqueArgs)

# def dispBeamColumnInt(eleTag, eleNodes, numIntgrPts, secTag, transfTag, cRot, massDens=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``numIntgrPts`` |int|                 number of integration points along the element.

#    ``secTag`` |int|                      identifier for previously-defined section object

#    ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object

#    ``cRot`` |float|                      identifier for element center of rotation (or center of curvature distribution). Fraction of the height distance from bottom to the center of rotation (0 to 1)

#    ``massDens`` |float|                  element mass density (per unit length), from which a lumped-mass matrix is formed (optional, default=0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Flexure-Shear_Interaction_Displacement-Based_Beam-Column_Element>`_

#     """
#     uniqueArgs = []
#     if massDens:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(massDens)
#     ops.element('dispBeamColumnInt', eleTag, *eleNodes, numIntgrPts, secTag, transfTag, cRot, *uniqueArgs)

# def MVLEM(eleTag, Dens, eleNodes, m, c, thick=None, widths=None, rho=None, matConcreteTags=None, matSteelTags=None, matShearTag=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``Dens`` |float|                      Wall density

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``m`` |int|                           Number of element macro-fibers

#    ``c`` |float|                         Location of center of rotation from the iNode, ``c`` = 0.4 (recommended)

#    ``thick`` |listf|                     a list of ``m`` macro-fiber thicknesses

#    ``widths`` |listf|                    a list of ``m`` macro-fiber widths

#    ``rho`` |listf|                       a list of m reinforcing ratios corresponding to macro-fibers; for each fiber: :math:`rho_i = A_{s,i}/A_{gross,i} (1 < i < m)`

#    ``matConcreteTags`` |listi|           a list of ``m`` uniaxialMaterial tags for concrete

#    ``matSteelTags`` |listi|              a list of ``m`` uniaxialMaterial tags for steel

#    ``matShearTag`` |int|                 Tag of uniaxialMaterial for shear material

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/MVLEM_-_Multiple-Vertical-Line-Element-Model_for_RC_Walls>`_

   

#         Kolozvari K., Orakcal K., and Wallace J. W. (2015a). "New opensees models for simulating nonlinear flexural and coupled shear-flexural behavior of RC walls and columns", Computers and Structures, Volume 196, February 2018, Pages 246-262, `doi <https://doi.org/10.1016/j.compstruc.2017.10.010>`_



#     """
#     uniqueArgs = []
#     if thick:
#         uniqueArgs.append('-thick')
#         uniqueArgs.append(thick)
#     if widths:
#         uniqueArgs.append('-width')
#         uniqueArgs.append(widths)
#     if rho:
#         uniqueArgs.append('-rho')
#         uniqueArgs.append(rho)
#     if matConcreteTags:
#         uniqueArgs.append('-matConcrete')
#         uniqueArgs.append(matConcreteTags)
#     if matSteelTags:
#         uniqueArgs.append('-matSteel')
#         uniqueArgs.append(matSteelTags)
#     if matShearTag:
#         uniqueArgs.append('-matShear')
#         uniqueArgs.append(matShearTag)
#     ops.element('MVLEM', eleTag, Dens, *eleNodes, m, c, *uniqueArgs)

# def SFI_MVLEM(eleTag, eleNodes, m, c, thick=None, widths=None, mat_tags=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``m`` |int|                           Number of element macro-fibers

#    ``c`` |float|                         Location of center of rotation with from the iNode, ``c`` = 0.4 (recommended)

#    ``Thicknesses`` |listf|               a list of m macro-fiber thicknesses

#    ``Widths`` |listf|                    a list of m macro-fiber widths

#    ``Material_tags`` |listi|             a list of m macro-fiber nDMaterial1 tags

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SFI_MVLEM_-_Cyclic_Shear-Flexure_Interaction_Model_for_RC_Walls>`_

   

#         Kolozvari K., Orakcal K., and Wallace J. W. (2015a). "New opensees models for simulating nonlinear flexural and coupled shear-flexural behavior of RC walls and columns", Computers and Structures, Volume 196, February 2018, Pages 246-262, `doi <https://doi.org/10.1016/j.compstruc.2017.10.010>`_



#         Kolozvari K., Orakcal K., and Wallace J. W. (2015a). ”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls. I: Theory”, ASCE Journal of Structural Engineering, 141(5), 04014135 `doi <https://ascelibrary.org/doi/10.1061/%28ASCE%29ST.1943-541X.0001059>`_



#         Kolozvari K., Tran T., Orakcal K., and Wallace, J.W. (2015c). ”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls. II: Experimental Validation”, ASCE Journal of Structural Engineering, 141(5), 04014136 `doi <https://ascelibrary.org/doi/10.1061/%28ASCE%29ST.1943-541X.0001083>`_



#         Kolozvari K., Orakcal K., and Wallace J. W. (2015c). "Shear-Flexure Interaction Modeling of reinforced Concrete Structural Walls and Columns under Reversed Cyclic Loading", Pacific Earthquake Engineering Research Center, University of California, Berkeley, PEER Report No. 2015/12



#         Kolozvari K. (2013). “Analytical Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls”, PhD Dissertation, University of California, Los Angeles.
#     """
#     uniqueArgs = []
#     if thick:
#         uniqueArgs.append('-thick')
#         uniqueArgs.append(thick)
#     if widths:
#         uniqueArgs.append('-width')
#         uniqueArgs.append(widths)
#     if mat_tags:
#         uniqueArgs.append('-mat')
#         uniqueArgs.append(mat_tags)
#     ops.element('SFI_MVLEM', eleTag, *eleNodes, m, c, *uniqueArgs)

# def beamColumnJoint(eleTag, eleNodes, Mat1Tag, Mat2Tag, Mat3Tag, Mat4Tag, Mat5Tag, Mat6Tag, Mat7Tag, Mat8Tag, Mat9Tag, Mat10Tag, Mat11Tag, Mat12Tag, Mat13Tag, eleWidthFac=1.0=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes

#    ``Mat1Tag`` |int|                     uniaxial material tag for left bar-slip spring at node 1

#    ``Mat2Tag`` |int|                     uniaxial material tag for right bar-slip spring at node 1

#    ``Mat3Tag`` |int|                     uniaxial material tag for interface-shear spring at node 1

#    ``Mat4Tag`` |int|                     uniaxial material tag for lower bar-slip spring at node 2

#    ``Mat5Tag`` |int|                     uniaxial material tag for upper bar-slip spring at node 2

#    ``Mat6Tag`` |int|                     uniaxial material tag for interface-shear spring at node 2

#    ``Mat7Tag`` |int|                     uniaxial material tag for left bar-slip spring at node 3

#    ``Mat8Tag`` |int|                     uniaxial material tag for right bar-slip spring at node 3

#    ``Mat9Tag`` |int|                     uniaxial material tag for interface-shear spring at node 3

#    ``Mat10Tag`` |int|                    uniaxial material tag for lower bar-slip spring at node 4

#    ``Mat11Tag`` |int|                    uniaxial material tag for upper bar-slip spring at node 4

#    ``Mat12Tag`` |int|                    uniaxial material tag for interface-shear spring at node 4

#    ``Mat13Tag`` |int|                    uniaxial material tag for shear-panel

#    ``eleHeightFac`` |float|              floating point value (as a ratio to the total height of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0)

#    ``eleWidthFac`` |float|               floating point value (as a ratio to the total width of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamColumnJoint_Element>`_

#     """
#     uniqueArgs = []
#     if eleWidthFac=1.0:
#         uniqueArgs.append(eleHeightFac=1.0)
#         uniqueArgs.append(eleWidthFac=1.0)
#     ops.element('beamColumnJoint', eleTag, *eleNodes, Mat1Tag, Mat2Tag, Mat3Tag, Mat4Tag, Mat5Tag, Mat6Tag, Mat7Tag, Mat8Tag, Mat9Tag, Mat10Tag, Mat11Tag, Mat12Tag, Mat13Tag, *uniqueArgs)

# def ElasticTubularJoint(eleTag, eleNodes, Brace_Diameter, Brace_Angle, E, Chord_Diameter, Chord_Thickness, Chord_Angle):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``Brace_Diameter`` |float|            outer diameter of brace

#    ``Brace_Angle`` |float|               angle between brace and chord axis 0 < Brace_Angle < 90

#    ``E`` |float|                         Young's Modulus

#    ``Chord_Diameter`` |float|            outer diameter of chord

#    ``Chord_Thickness`` |float|           thickness of chord

#    ``Chord_Angle`` |float|               angle between chord axis and global x-axis 0 < Chord_Angle < 180

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ElasticTubularJoint_Element>`_

#     """
#     uniqueArgs = []
#     ops.element('ElasticTubularJoint', eleTag, *eleNodes, Brace_Diameter, Brace_Angle, E, Chord_Diameter, Chord_Thickness, Chord_Angle, *uniqueArgs)

# def Joint2D(eleTag, eleNodes, Mat2=None, Mat3=None, Mat4=None, MatC, LrgDspTag, DmgTag=None, Dmg1 Dmg2 Dmg3 Dmg4 DmgC=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of five element nodes = ``[nd1,nd2,nd3,nd4,ndC]``. ``ndC`` is the central node of beam-column joint. (the tag ``ndC`` is used to generate the internal node, thus, the node should not exist in the domain or be used by any other node)

#    ``Mat1`` |int|                        uniaxial material tag for interface rotational spring at node 1. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)

#    ``Mat2`` |int|                        uniaxial material tag for interface rotational spring at node 2. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)

#    ``Mat3`` |int|                        uniaxial material tag for interface rotational spring at node 3. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)

#    ``Mat4`` |int|                        uniaxial material tag for interface rotational spring at node 4. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)

#    ``MatC`` |int|                        uniaxial material tag for rotational spring of the central node that describes shear panel behavior

#    ``LrgDspTag`` |int|                   an integer indicating the flag for considering large deformations:

#                                          * ``0`` - for small deformations and constant geometry

#                                          * ``1`` - for large deformations and time varying geometry

#                                          * ``2`` - for large deformations ,time varying geometry and length correction

#    ``DmgTag`` |int|                      damage model tag

#    ``Dmg1`` |int|                        damage model tag for Mat1

#    ``Dmg2`` |int|                        damage model tag for Mat2

#    ``Dmg3`` |int|                        damage model tag for Mat3

#    ``Dmg4`` |int|                        damage model tag for Mat4

#    ``DmgC`` |int|                        panel damage model tag

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Joint2D_Element>`_

#     """
#     uniqueArgs = []
#     if Mat2:
#         uniqueArgs.append(Mat1)
#         uniqueArgs.append(Mat2)
#         uniqueArgs.append(Mat3)
#         uniqueArgs.append(Mat4)
#     if DmgTag:
#         uniqueArgs.append('-damage')
#         uniqueArgs.append(DmgTag)
#     if Dmg1 Dmg2 Dmg3 Dmg4 DmgC:
#         uniqueArgs.append('-damage')
#         uniqueArgs.append(Dmg1 Dmg2 Dmg3 Dmg4 DmgC)
#     ops.element('Joint2D', eleTag, *eleNodes, MatC, LrgDspTag, *uniqueArgs)

# def twoNodeLink(eleTag, eleNodes, matTags=None, dir=None, vecx=None, vecyp=None, pDeltaVals=None, shearDist=None, doRayleigh=None, m=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``matTags`` |listi|                   a list of tags associated with previously-defined UniaxialMaterial objects

#    ``dirs`` |listi|                      a list material directions:



#                                          * 2D-case: ``1`` , ``2`` - translations along local x,y axes; ``3`` - rotation about local z axis

#                                          * 3D-case: ``1``, ``2``, ``3`` - translations along local x,y,z axes; ``4``, ``5``, ``6`` - rotations about local x,y,z axes

#    ``vecx`` |listf|                      vector components in global coordinates defining local x-axis (optional)

#    ``vecyp`` |listf|                      vector components in global coordinates defining local y-axis (optional)

#    ``pDeltaVals`` |listf|                   P-Delta moment contribution ratios, size of ratio vector is 2 for 2D-case and 4 for 3D-case (entries: ``[My_iNode, My_jNode, Mz_iNode, Mz_jNode]``) ``My_iNode`` + ``My_jNode`` <= 1.0, ``Mz_iNode`` + ``Mz_jNode`` <= 1.0. Remaining P-Delta moments are resisted by shear couples. (optional)

#    ``sDratios`` |listf|                  shear distances from iNode as a fraction of the element length, size of ratio vector is 1 for 2D-case and 2 for 3D-case. (entries: ``[dy_iNode, dz_iNode]``) (optional, default = ``[0.5, 0.5]``)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the element (optional, default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Two_Node_Link_Element>`_

#     """
#     uniqueArgs = []
#     if matTags:
#         uniqueArgs.append('-mat')
#         uniqueArgs.append(matTags)
#     if dir:
#         uniqueArgs.append('-dir')
#         uniqueArgs.append(dir)
#     if vecx:
#         uniqueArgs.append('-orient')
#         uniqueArgs.append(*vecx)
#         uniqueArgs.append(*vecyp)
#     if pDeltaVals:
#         uniqueArgs.append('-pDelta')
#         uniqueArgs.append(*pDeltaVals)
#     if shearDist:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(*shearDist)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     ops.element('twoNodeLink', eleTag, *eleNodes, *uniqueArgs)

# def elastomericBearingPlasticity(eleTag, eleNodes, kInit, qd, alpha1, alpha2, mu, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None):


#    For a three-dimensional problem





#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``qd`` |float|                        characteristic strength

#    ``alpha1`` |float|                    post yield stiffness ratio of linear hardening component

#    ``alpha2`` |float|                    post yield stiffness ratio of non-linear hardening component

#    ``mu`` |float|                        exponent of non-linear hardening component

#    ``PMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial

#                                          in axial direction

#    ``TMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial

#                                          in torsional direction

#    ``MyMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial

#                                          in moment direction around local y-axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial

#                                          in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local

#                                          x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local

#                                          y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element

#                                          length (optional, default = 0.5)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional,

#                                          default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastomeric_Bearing_(Plasticity)_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     ops.element('elastomericBearingPlasticity', eleTag, *eleNodes, kInit, qd, alpha1, alpha2, mu, y1, y2, *uniqueArgs)

# def elastomericBearingPlasticity(eleTag, eleNodes, kInit, qd, alpha1, alpha2, mu, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None):


#    For a three-dimensional problem





#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``qd`` |float|                        characteristic strength

#    ``alpha1`` |float|                    post yield stiffness ratio of linear hardening component

#    ``alpha2`` |float|                    post yield stiffness ratio of non-linear hardening component

#    ``mu`` |float|                        exponent of non-linear hardening component

#    ``PMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial

#                                          in axial direction

#    ``TMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial

#                                          in torsional direction

#    ``MyMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial

#                                          in moment direction around local y-axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial

#                                          in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local

#                                          x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local

#                                          y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element

#                                          length (optional, default = 0.5)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional,

#                                          default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastomeric_Bearing_(Plasticity)_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     ops.element('elastomericBearingPlasticity', eleTag, *eleNodes, kInit, qd, alpha1, alpha2, mu, y1, y2, *uniqueArgs)

# def ElastomericBearingBoucWen(eleTag, eleNodes, kInit, qd, alpha1, alpha2, mu, eta, beta, gamma, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, orientVals=None, shearDist=None, doRayleigh=None, mass=None):


#    For a three-dimensional problem



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``qd`` |float|                        characteristic strength

#    ``alpha1`` |float|                    post yield stiffness ratio of linear hardening component

#    ``alpha2`` |float|                    post yield stiffness ratio of non-linear hardening component

#    ``mu`` |float|                        exponent of non-linear hardening component

#    ``eta`` |float|                       yielding exponent (sharpness of hysteresis loop corners) (default = 1.0)

#    ``beta`` |float|                      first hysteretic shape parameter (default = 0.5)

#    ``gamma`` |float|                     second hysteretic shape parameter (default = 0.5)

#    ``PMatTag``  |int|                    tag associated with previously-defined

#                                          UniaxialMaterial in axial direction

#    ``TMatTag``  |int|                    tag associated with previously-defined

#                                          UniaxialMaterial in torsional direction

#    ``MyMatTag``  |int|                   tag associated with previously-defined

#                                          UniaxialMaterial in moment direction around local y-axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial

#                                          in moment direction around local z-axis

#    ``orientVals`` |listi|                vector components in global coordinates

#                                          defining local x-axis (optional),

#                                          vector components in global coordinates defining

#                                          local y-axis (optional)

#    ``shearDist`` |float|                 shear distance from iNode as a fraction

#                                          of the element length (optional, default = 0.5)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the

#                                          bearing (optional, default = no Rayleigh damping

#                                          contribution)

#    ``mass`` |float|                      element mass (optional, default = 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastomeric_Bearing_(Bouc-Wen)_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if orientVals:
#         uniqueArgs.append('-orient')
#         uniqueArgs.append(*orientVals)
#     if shearDist:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(shearDist)
#         uniqueArgs.append(doRayleigh)
#     if mass:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(mass)
#     ops.element('ElastomericBearingBoucWen', eleTag, *eleNodes, kInit, qd, alpha1, alpha2, mu, eta, beta, gamma, *uniqueArgs)

# def ElastomericBearingBoucWen(eleTag, eleNodes, kInit, qd, alpha1, alpha2, mu, eta, beta, gamma, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, orientVals=None, shearDist=None, doRayleigh=None, mass=None):


#    For a three-dimensional problem



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``qd`` |float|                        characteristic strength

#    ``alpha1`` |float|                    post yield stiffness ratio of linear hardening component

#    ``alpha2`` |float|                    post yield stiffness ratio of non-linear hardening component

#    ``mu`` |float|                        exponent of non-linear hardening component

#    ``eta`` |float|                       yielding exponent (sharpness of hysteresis loop corners) (default = 1.0)

#    ``beta`` |float|                      first hysteretic shape parameter (default = 0.5)

#    ``gamma`` |float|                     second hysteretic shape parameter (default = 0.5)

#    ``PMatTag``  |int|                    tag associated with previously-defined

#                                          UniaxialMaterial in axial direction

#    ``TMatTag``  |int|                    tag associated with previously-defined

#                                          UniaxialMaterial in torsional direction

#    ``MyMatTag``  |int|                   tag associated with previously-defined

#                                          UniaxialMaterial in moment direction around local y-axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial

#                                          in moment direction around local z-axis

#    ``orientVals`` |listi|                vector components in global coordinates

#                                          defining local x-axis (optional),

#                                          vector components in global coordinates defining

#                                          local y-axis (optional)

#    ``shearDist`` |float|                 shear distance from iNode as a fraction

#                                          of the element length (optional, default = 0.5)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the

#                                          bearing (optional, default = no Rayleigh damping

#                                          contribution)

#    ``mass`` |float|                      element mass (optional, default = 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastomeric_Bearing_(Bouc-Wen)_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if orientVals:
#         uniqueArgs.append('-orient')
#         uniqueArgs.append(*orientVals)
#     if shearDist:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(shearDist)
#         uniqueArgs.append(doRayleigh)
#     if mass:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(mass)
#     ops.element('ElastomericBearingBoucWen', eleTag, *eleNodes, kInit, qd, alpha1, alpha2, mu, eta, beta, gamma, *uniqueArgs)

# def flatSliderBearing(eleTag, eleNodes, frnMdlTag, kInit, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None, maxIter=None, tol=None):


#    For a three-dimensional problem



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``frnMdlTag`` |float|                 tag associated with previously-defined FrictionModel

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``PMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial in axial direction

#    ``TMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial in torsional direction

#    ``MyMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial in moment direction around local y-axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.0)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``iter`` |int|                        maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20)

#    ``tol`` |float|                       convergence tolerance to satisfy element equilibrium (optional, default = 1E-8)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Flat_Slider_Bearing_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     if maxIter:
#         uniqueArgs.append('-iter')
#         uniqueArgs.append(maxIter)
#         uniqueArgs.append(tol)
#     ops.element('flatSliderBearing', eleTag, *eleNodes, frnMdlTag, kInit, y1, y2, *uniqueArgs)

# def flatSliderBearing(eleTag, eleNodes, frnMdlTag, kInit, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None, maxIter=None, tol=None):


#    For a three-dimensional problem



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``frnMdlTag`` |float|                 tag associated with previously-defined FrictionModel

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``PMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial in axial direction

#    ``TMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial in torsional direction

#    ``MyMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial in moment direction around local y-axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.0)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``iter`` |int|                        maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20)

#    ``tol`` |float|                       convergence tolerance to satisfy element equilibrium (optional, default = 1E-8)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Flat_Slider_Bearing_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     if maxIter:
#         uniqueArgs.append('-iter')
#         uniqueArgs.append(maxIter)
#         uniqueArgs.append(tol)
#     ops.element('flatSliderBearing', eleTag, *eleNodes, frnMdlTag, kInit, y1, y2, *uniqueArgs)

# def singleFPBearing(eleTag, eleNodes, frnMdlTag, Reff, kInit, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None, maxIter=None, tol=None):


#    For a three-dimensional problem



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``frnMdlTag`` |float|                 tag associated with previously-defined FrictionModel

#    ``Reff`` |float|                      effective radius of concave sliding surface

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``PMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial in axial direction

#    ``TMatTag``  |int|                    tag associated with previously-defined UniaxialMaterial in torsional direction

#    ``MyMatTag``  |int|                   tag associated with previously-defined UniaxialMaterial in moment direction around local y axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.0)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``maxIter`` |int|                     maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20)

#    ``tol`` |float|                       convergence tolerance to satisfy element equilibrium (optional, default = 1E-8)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Single_Friction_Pendulum_Bearing_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     if maxIter:
#         uniqueArgs.append('-iter')
#         uniqueArgs.append(maxIter)
#         uniqueArgs.append(tol)
#     ops.element('singleFPBearing', eleTag, *eleNodes, frnMdlTag, Reff, kInit, y1, y2, *uniqueArgs)

# def singleFPBearing(eleTag, eleNodes, frnMdlTag, Reff, kInit, PMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None, maxIter=None, tol=None):


#    For a three-dimensional problem



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``frnMdlTag`` |float|                 tag associated with previously-defined FrictionModel

#    ``Reff`` |float|                      effective radius of concave sliding surface

#    ``kInit`` |float|                     initial elastic stiffness in local shear direction

#    ``PMatTag`` |int|                     tag associated with previously-defined UniaxialMaterial in axial direction

#    ``TMatTag``  |int|                    tag associated with previously-defined UniaxialMaterial in torsional direction

#    ``MyMatTag``  |int|                   tag associated with previously-defined UniaxialMaterial in moment direction around local y axis

#    ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.0)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``maxIter`` |int|                     maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20)

#    ``tol`` |float|                       convergence tolerance to satisfy element equilibrium (optional, default = 1E-8)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Single_Friction_Pendulum_Bearing_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     if maxIter:
#         uniqueArgs.append('-iter')
#         uniqueArgs.append(maxIter)
#         uniqueArgs.append(tol)
#     ops.element('singleFPBearing', eleTag, *eleNodes, frnMdlTag, Reff, kInit, y1, y2, *uniqueArgs)

# def TFP(eleTag, eleNodes, R1, R2, R3, R4, Db1, Db2, Db3, Db4, d1, d2, d3, d4, mu1, mu2, mu3, mu4, h1, h2, h3, h4, H0, colLoad, K=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``R1`` |float|                        Radius of inner bottom sliding surface

#    ``R2`` |float|                        Radius of inner top sliding surface

#    ``R3`` |float|                        Radius of outer bottom sliding surface

#    ``R4`` |float|                        Radius of outer top sliding surface

#    ``Db1`` |float|                       Diameter of inner bottom sliding surface

#    ``Db2`` |float|                       Diameter of inner top sliding surface

#    ``Db3`` |float|                       Diameter of outer bottom sliding surface

#    ``Db4`` |float|                       Diameter of outer top sliding surface

#    ``d1`` |float|                        diameter of inner slider

#    ``d2`` |float|                        diameter of inner slider

#    ``d3`` |float|                        diameter of outer bottom slider

#    ``d4`` |float|                        diameter of outer top slider

#    ``mu1`` |float|                       friction coefficient of inner bottom sliding surface

#    ``mu2`` |float|                       friction coefficient of inner top sliding surface

#    ``mu3`` |float|                       friction coefficient of outer bottom sliding surface

#    ``mu4`` |float|                       friction coefficient of outer top sliding surface

#    ``h1`` |float|                        height from inner bottom sliding surface to center of bearing

#    ``h2`` |float|                        height from inner top sliding surface to center of bearing

#    ``h3`` |float|                        height from outer bottom sliding surface to center of bearing

#    ``h4`` |float|                        height from inner top sliding surface to center of bearing

#    ``H0`` |float|                        total height of bearing

#    ``colLoad`` |float|                   initial axial load on bearing (only used for first time step then load come from model)

#    ``K`` |float|                         optional, stiffness of spring in vertical dirn (dof 2 if ndm= 2, dof 3 if ndm = 3) (default=1.0e15)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Bearing_Element>`_

#     """
#     uniqueArgs = []
#     if K:
#         uniqueArgs.append(K)
#     ops.element('TFP', eleTag, *eleNodes, R1, R2, R3, R4, Db1, Db2, Db3, Db4, d1, d2, d3, d4, mu1, mu2, mu3, mu4, h1, h2, h3, h4, H0, colLoad, *uniqueArgs)

# def TripleFrictionPendulum(eleTag, eleNodes, frnTag1, frnTag2, frnTag3, vertMatTag, rotZMatTag, rotXMatTag, rotYMatTag, L1, L2, L3, d1, d2, d3, W, uy, kvt, minFv, tol):
#     """


#    ===============================================================   ===========================================================================

#    ``eleTag`` |int|                                                  unique element object tag

#    ``eleNodes`` |listi|                                              a list of two element nodes

#    ``frnTag1``, ``frnTag2``  ``frnTag3`` |int|                       = tags associated with previously-defined FrictionModels at the three sliding interfaces

#    ``vertMatTag`` |int|                                              = Pre-defined material tag for COMPRESSION behavior of the bearing

#    ``rotZMatTag``  ``rotXMatTag``  ``rotYMatTag`` |int|              = Pre-defined material tags for rotational behavior about 3-axis, 1-axis and 2-axis, respectively.

#    ``L1``  ``L2``  ``L3`` |float|                                    = effective radii. Li = R_i - h_i (see Figure 1)

#    ``d1``  ``d2``  ``d3`` |float|                                    = displacement limits of pendulums (Figure 1). Displacement limit of the bearing is 2   ``d1`` +   ``d2`` +   ``d3`` +   ``L1``.   ``d3``/   ``L3`` -   ``L1``.   ``d2``/   ``L2``

#    ``W`` |float|                                                     = axial force used for the first trial of the first analysis step.

#    ``uy`` |float|                                                    = lateral displacement where sliding of the bearing starts. Recommended value = 0.25 to 1 mm. A smaller value may cause convergence problem.

#    ``kvt`` |float|                                                   = Tension stiffness k_vt of the bearing.

#    ``minFv (>=0)`` |float|                                           = minimum vertical compression force in the bearing used for computing the horizontal tangent stiffness matrix from the normalized tangent stiffness matrix of the element.    ``minFv`` is substituted for the actual compressive force when it is less than    ``minFv``, and prevents the element from using a negative stiffness matrix in the horizontal direction when uplift occurs. The vertical nodal force returned to nodes is always computed from    ``kvc`` (or    ``kvt``) and vertical deformation, and thus is not affected by    ``minFv``.

#    ``tol`` |float|                                                   = relative tolerance for checking the convergence of the element. Recommended value = 1.e-10 to 1.e-3.

#    ===============================================================   ===========================================================================





# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Element>`_

#     """
#     uniqueArgs = []
#     ops.element('TripleFrictionPendulum', eleTag, *eleNodes, frnTag1, frnTag2, frnTag3, vertMatTag, rotZMatTag, rotXMatTag, rotYMatTag, L1, L2, L3, d1, d2, d3, W, uy, kvt, minFv, tol, *uniqueArgs)

# def multipleShearSpring(eleTag, eleNodes, nSpring, matTag=None, lim=None, x2=None, x3=None, yp1, yp2, yp3=None, mass=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``nSpring`` |int|                     number of springs

#    ``matTag`` |int|                      tag associated with previously-defined UniaxialMaterial object

#    ``lim`` |float|                       minimum deformation to calculate equivalent coefficient (see note 1)

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis

#    ``yp1``  ``yp2``  ``yp3`` |float|     vector components in global coordinates defining vector yp which lies in the local x-y plane for the element

#    ``mass`` |float|                         element mass

#    ===================================   ===========================================================================



# .. note::



#    If ``dsp`` is positive and the shear deformation of MSS exceeds    ``dsp``, this element calculates equivalent coefficient to adjust force and stiffness of MSS. The adjusted MSS force and stiffness reproduce the behavior of the previously defined uniaxial material under monotonic loading in every direction. If    ``dsp`` is zero, the element does not calculate the equivalent coefficient.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/MultipleShearSpring_Element>`_

#     """
#     uniqueArgs = []
#     if matTag:
#         uniqueArgs.append('-mat')
#         uniqueArgs.append(matTag)
#     if lim:
#         uniqueArgs.append('-lim')
#         uniqueArgs.append(lim)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(yp3)
#     if mass:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(mass)
#     ops.element('multipleShearSpring', eleTag, *eleNodes, nSpring, yp1, yp2, *uniqueArgs)

# def KikuchiBearing(eleTag, eleNodes, shape=None, size=None, totalRubber=None, totalHeight=None, nMSS=None, matMSSTag=None, limDisp=None, nMNS=None, matMNSTag=None, lambda=None, x2=None, x3=None, yp1, yp2, yp3=None, m=None, noPDInput=None, noTilt=None, ci=None, cj=None, limFo=None, limFi=None, nIter=None):
#     """


#    ===========================================   ===========================================================================

#    ``eleTag`` |int|                              unique element object tag

#    ``eleNodes`` |listi|                          a list of two element nodes

#    ``shape`` |float|                             following shapes are available: round, square

#    ``size`` |float|                              diameter (round shape), length of edge (square shape)

#    ``totalRubber`` |float|                       total rubber thickness

#    ``totalHeight`` |float|                       total height of the bearing (defaulut: distance between iNode and jNode)

#    ``nMSS`` |int|                                number of springs in MSS = nMSS

#    ``matMSSTag`` |int|                           matTag for MSS

#    ``limDisp`` |float|                           minimum deformation to calculate equivalent coefficient of MSS (see note 1)

#    ``nMNS`` |int|                                number of springs in MNS = nMNS*nMNS (for round and square shape)

#    ``matMNSTag`` |int|                           matTag for MNS

#    ``lambda`` |float|                            parameter to calculate compression modulus distribution on MNS (see note 2)

#    ``x1``  ``x2``  ``x3`` |float|                vector components in global coordinates defining local x-axis

#    ``yp1``  ``yp2``  ``yp3`` |float|             vector components in global coordinates defining vector yp which lies in the local x-y plane for the element

#    ``m`` |float|                                 element mass

#    ``'-noPDInput'`` |str|                        not consider P-Delta moment

#    ``'-noTilt'`` |str|                           not consider tilt of rigid link

#    ``ci``  ``cj`` |float|                        P-Delta moment adjustment for reaction force (default:    ``ci`` =0.5,    ``cj`` =0.5)

#    ``limFo``  ``limFi``  ``nIter`` |float|       tolerance of external unbalanced force (   ``limFo``), tolorance of internal unbalanced force (   ``limFi``), number of iterations to get rid of internal unbalanced force (   ``nIter``)

#    ===========================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/KikuchiBearing_Element>`_

#     """
#     uniqueArgs = []
#     if shape:
#         uniqueArgs.append('-shape')
#         uniqueArgs.append(shape)
#     if size:
#         uniqueArgs.append('-size')
#         uniqueArgs.append(size)
#         uniqueArgs.append(totalRubber)
#     if totalHeight:
#         uniqueArgs.append('-totalHeight')
#         uniqueArgs.append(totalHeight)
#     if nMSS:
#         uniqueArgs.append('-nMSS')
#         uniqueArgs.append(nMSS)
#     if matMSSTag:
#         uniqueArgs.append('-matMSS')
#         uniqueArgs.append(matMSSTag)
#     if limDisp:
#         uniqueArgs.append('-limDisp')
#         uniqueArgs.append(limDisp)
#     if nMNS:
#         uniqueArgs.append('-nMNS')
#         uniqueArgs.append(nMNS)
#     if matMNSTag:
#         uniqueArgs.append('-matMNS')
#         uniqueArgs.append(matMNSTag)
#     if lambda:
#         uniqueArgs.append('-lambda')
#         uniqueArgs.append(lambda)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(yp3)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#         uniqueArgs.append(noPDInput)
#         uniqueArgs.append(noTilt)
#     if ci:
#         uniqueArgs.append('-adjustPDOutput')
#         uniqueArgs.append(ci)
#         uniqueArgs.append(cj)
#     if limFo:
#         uniqueArgs.append('-doBalance')
#         uniqueArgs.append(limFo)
#         uniqueArgs.append(limFi)
#         uniqueArgs.append(nIter)
#     ops.element('KikuchiBearing', eleTag, *eleNodes, yp1, yp2, *uniqueArgs)

# def YamamotoBiaxialHDR(eleTag, eleNodes, Tp, DDo, DDi, Hr, cr=None, cs=None, vecx=None, vecyp=None, m=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``Tp`` |int|                          compound type = 1 : X0.6R manufactured by Bridgestone corporation.

#    ``DDo`` |float|                       outer diameter [m]

#    ``DDi`` |float|                       bore diameter [m]

#    ``Hr`` |float|                        total thickness of rubber layer [m] Optional Data

#    ``cr``  ``cs`` |float|                coefficients for shear stress components of tau_r and tau_s

#    ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)

#    ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element.

#    ``m`` |float|                         element mass [kg]

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/YamamotoBiaxialHDR_Element>`_

#     """
#     uniqueArgs = []
#     if cr:
#         uniqueArgs.append('-coRS`)
#         uniqueArgs.append(cr)
#         uniqueArgs.append(cs)
#     if vecx:
#         uniqueArgs.append('-orient`)
#         uniqueArgs.append(*vecx)
#         uniqueArgs.append(*vecyp)
#     if m:
#         uniqueArgs.append('-mass`)
#         uniqueArgs.append(m)
#     ops.element('YamamotoBiaxialHDR', eleTag, *eleNodes, Tp, DDo, DDi, Hr, *uniqueArgs)

# def ElastomericX(eleTag, eleNodes, Fy, alpha, Gr, Kbulk, D1, D2, ts, tr, n, x2=None, x3=None, y1, y2, y3=None, kc=None, PhiM=None, ac=None, sDratio=None, m=None, cd=None, tc=None, tag1=None, tag2=None, tag3=None, tag4=None):
#     """


#    For 3D problem



#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``Fy`` |float|                        yield strength

#    ``alpha`` |float|                     post-yield stiffness ratio

#    ``Gr`` |float|                        shear modulus of elastomeric bearing

#    ``Kbulk`` |float|                     bulk modulus of rubber

#    ``D1`` |float|                        internal diameter

#    ``D2`` |float|                        outer diameter (excluding cover thickness)

#    ``ts`` |float|                        single steel shim layer thickness

#    ``tr`` |float|                        single  rubber layer thickness

#    ``n`` |int|                           number of rubber layers

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``   ``y2``  ``y3`` |float|       vector components in global coordinates defining local y-axis (optional)

#    ``kc`` |float|                        cavitation parameter (optional, default = 10.0)

#    ``PhiM`` |float|                      damage parameter (optional, default = 0.5)

#    ``ac`` |float|                        strength reduction parameter (optional, default = 1.0)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.5)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``cd`` |float|                        viscous damping parameter (optional, default = 0.0)

#    ``tc`` |float|                        cover thickness (optional, default = 0.0)

#    ``tag1`` |float|                      Tag to include cavitation and post-cavitation (optional, default = 0)

#    ``tag2`` |float|                      Tag to include buckling load variation (optional, default = 0)

#    ``tag3`` |float|                      Tag to include horizontal stiffness variation (optional, default = 0)

#    ``tag4`` |float|                      Tag to include vertical stiffness variation (optional, default = 0)

#    ===================================   ===========================================================================



# .. note::



#    Because default values of heating parameters are in SI units, user must override the default heating parameters values if using Imperial units



#    User should distinguish between yield strength of elastomeric bearing (:math:`F_y`) and characteristic strength (:math:`Q_d`): :math:`Q_d=F_y*(1-alpha)`



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ElastomericX>`_

#     """
#     uniqueArgs = []
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if kc:
#         uniqueArgs.append(kc)
#     if PhiM:
#         uniqueArgs.append(PhiM)
#     if ac:
#         uniqueArgs.append(ac)
#     if sDratio:
#         uniqueArgs.append(sDratio)
#     if m:
#         uniqueArgs.append(m)
#     if cd:
#         uniqueArgs.append(cd)
#     if tc:
#         uniqueArgs.append(tc)
#     if tag1:
#         uniqueArgs.append(tag1)
#     if tag2:
#         uniqueArgs.append(tag2)
#     if tag3:
#         uniqueArgs.append(tag3)
#     if tag4:
#         uniqueArgs.append(tag4)
#     ops.element('ElastomericX', eleTag, *eleNodes, Fy, alpha, Gr, Kbulk, D1, D2, ts, tr, n, y1, y2, *uniqueArgs)

# def LeadRubberX(eleTag, eleNodes, Fy, alpha, Gr, Kbulk, D1, D2, ts, tr, n, x2=None, x3=None, y1, y2, y3=None, kc=None, PhiM=None, ac=None, sDratio=None, m=None, cd=None, tc=None, qL=None, cL=None, kS=None, aS=None, tag1=None, tag2=None, tag3=None, tag4=None, tag5=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``Fy`` |float|                        yield strength

#    ``alpha`` |float|                     post-yield stiffness ratio

#    ``Gr`` |float|                        shear modulus of elastomeric bearing

#    ``Kbulk`` |float|                     bulk modulus of rubber

#    ``D1`` |float|                        internal diameter

#    ``D2`` |float|                        outer diameter (excluding cover thickness)

#    ``ts`` |float|                        single steel shim layer thickness

#    ``tr`` |float|                        single rubber layer thickness

#    ``n`` |int|                           number of rubber layers

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)

#    ``kc`` |float|                        cavitation parameter (optional, default = 10.0)

#    ``PhiM`` |float|                      damage parameter (optional, default = 0.5)

#    ``ac`` |float|                        strength reduction parameter (optional, default = 1.0)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.5)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``cd`` |float|                        viscous damping parameter (optional, default = 0.0)

#    ``tc`` |float|                        cover thickness (optional, default = 0.0)

#    ``qL`` |float|                        density of lead (optional, default = 11200 kg/m3)

#    ``cL`` |float|                        specific heat of lead (optional, default = 130 N-m/kg oC)

#    ``kS`` |float|                        thermal conductivity of steel (optional, default = 50 W/m oC)

#    ``aS`` |float|                        thermal diffusivity of steel (optional, default = 1.41e-05 m2/s)

#    ``tag1`` |int|                        Tag to include cavitation and post-cavitation (optional, default = 0)

#    ``tag2`` |int|                        Tag to include buckling load variation (optional, default = 0)

#    ``tag3`` |int|                        Tag to include horizontal stiffness variation (optional, default = 0)

#    ``tag4`` |int|                        Tag to include vertical stiffness variation (optional, default = 0)

#    ``tag5`` |int|                        Tag to include strength degradation in shear due to heating of lead core (optional, default = 0)

#    ===================================   ===========================================================================



# .. note::



#    Because default values of heating parameters are in SI units, user must override the default heating parameters values if using Imperial units



#    User should distinguish between yield strength of elastomeric bearing (:math:`F_y`) and characteristic strength (:math:`Q_d`): :math:`Q_d=F_y*(1-alpha)`



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/LeadRubberX>`_

#     """
#     uniqueArgs = []
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if kc:
#         uniqueArgs.append(kc)
#     if PhiM:
#         uniqueArgs.append(PhiM)
#     if ac:
#         uniqueArgs.append(ac)
#     if sDratio:
#         uniqueArgs.append(sDratio)
#     if m:
#         uniqueArgs.append(m)
#     if cd:
#         uniqueArgs.append(cd)
#     if tc:
#         uniqueArgs.append(tc)
#     if qL:
#         uniqueArgs.append(qL)
#     if cL:
#         uniqueArgs.append(cL)
#     if kS:
#         uniqueArgs.append(kS)
#     if aS:
#         uniqueArgs.append(aS)
#     if tag1:
#         uniqueArgs.append(tag1)
#     if tag2:
#         uniqueArgs.append(tag2)
#     if tag3:
#         uniqueArgs.append(tag3)
#     if tag4:
#         uniqueArgs.append(tag4)
#     if tag5:
#         uniqueArgs.append(tag5)
#     ops.element('LeadRubberX', eleTag, *eleNodes, Fy, alpha, Gr, Kbulk, D1, D2, ts, tr, n, y1, y2, *uniqueArgs)

# def HDR(eleTag, eleNodes, Gr, Kbulk, D1, D2, ts, tr, n, a1, a2, a3, b1, b2, b3, c1, c2, c3, c4, x2=None, x3=None, y1, y2, y3=None, kc=None, PhiM=None, ac=None, sDratio=None, m=None, tc=None):
#     """


#    For 3D problem



#    =========================================================================================   ===========================================================================

#    ``eleTag`` |int|                                                                            unique element object tag

#    ``eleNodes`` |listi|                                                                        a list of two element nodes

#    ``Gr`` |float|                                                                              shear modulus of elastomeric bearing

#    ``Kbulk`` |float|                                                                           bulk modulus of rubber

#    ``D1`` |float|                                                                              internal diameter

#    ``D2`` |float|                                                                              outer diameter (excluding cover thickness)

#    ``ts`` |float|                                                                              single steel shim layer thickness

#    ``tr`` |float|                                                                              single rubber layer thickness

#    ``n`` |int|                                                                                 number of rubber layers

#    ``a1``  ``a2``  ``a3``  ``b1``  ``b2``  ``b3``  ``c1``  ``c2``  ``c3``  ``c4`` |float|      parameters of the Grant model

#    ``x1``  ``x2``  ``x3`` |float|                                                              vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|                                                              vector components in global coordinates defining local y-axis (optional)

#    ``kc`` |float|                                                                              cavitation parameter (optional, default = 10.0)

#    ``PhiM`` |float|                                                                            damage parameter (optional, default = 0.5)

#    ``ac`` |float|                                                                              strength reduction parameter (optional, default = 1.0)

#    ``sDratio`` |float|                                                                         shear distance from iNode as a fraction of the element length (optional, default = 0.5)

#    ``m`` |float|                                                                               element mass (optional, default = 0.0)

#    ``tc`` |float|                                                                              cover thickness (optional, default = 0.0)

#    =========================================================================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/HDR>`_

#     """
#     uniqueArgs = []
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if kc:
#         uniqueArgs.append(kc)
#     if PhiM:
#         uniqueArgs.append(PhiM)
#     if ac:
#         uniqueArgs.append(ac)
#     if sDratio:
#         uniqueArgs.append(sDratio)
#     if m:
#         uniqueArgs.append(m)
#     if tc:
#         uniqueArgs.append(tc)
#     ops.element('HDR', eleTag, *eleNodes, Gr, Kbulk, D1, D2, ts, tr, n, a1, a2, a3, b1, b2, b3, c1, c2, c3, c4, y1, y2, *uniqueArgs)

# def RJWatsonEqsBearing(eleTag, eleNodes, frnMdlTag, kInit, PMatTag=None, VyMatTag=None, VzMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None, maxIter=None, tol=None):


#    For a three-dimensional problem





#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``frnMdlTag`` |float|                 tag associated with previously-defined FrictionModel

#    ``kInit`` |float|                     initial stiffness of sliding friction component in local shear direction

#    ``'-P'``  ``PMatTag`` |int|            tag associated with previously-defined UniaxialMaterial in axial direction

#    ``'-Vy'``  ``VyMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in shear direction along local y-axis (MER spring behavior not including friction)

#    ``'-Vz'``  ``VzMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in shear direction along local z-axis (MER spring behavior not including friction)

#    ``'-T'``  ``TMatTag`` |int|            tag associated with previously-defined UniaxialMaterial in torsional direction

#    ``'-My'``  ``MyMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in moment direction around local y-axis

#    ``'-Mz'``  ``MzMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.0)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``maxIter`` |int|                     maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20)

#    ``tol`` |float|                       convergence tolerance to satisfy element equilibrium (optional, default = 1E-8)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/RJ-Watson_EQS_Bearing_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if VyMatTag:
#         uniqueArgs.append('-Vy')
#         uniqueArgs.append(VyMatTag)
#     if VzMatTag:
#         uniqueArgs.append('-Vz')
#         uniqueArgs.append(VzMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     if maxIter:
#         uniqueArgs.append('-iter')
#         uniqueArgs.append(maxIter)
#         uniqueArgs.append(tol)
#     ops.element('RJWatsonEqsBearing', eleTag, *eleNodes, frnMdlTag, kInit, y1, y2, *uniqueArgs)

# def RJWatsonEqsBearing(eleTag, eleNodes, frnMdlTag, kInit, PMatTag=None, VyMatTag=None, VzMatTag=None, TMatTag=None, MyMatTag=None, MzMatTag=None, x2=None, x3=None, y1, y2, y3=None, sDratio=None, doRayleigh=None, m=None, maxIter=None, tol=None):


#    For a three-dimensional problem





#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``frnMdlTag`` |float|                 tag associated with previously-defined FrictionModel

#    ``kInit`` |float|                     initial stiffness of sliding friction component in local shear direction

#    ``'-P'``  ``PMatTag`` |int|            tag associated with previously-defined UniaxialMaterial in axial direction

#    ``'-Vy'``  ``VyMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in shear direction along local y-axis (MER spring behavior not including friction)

#    ``'-Vz'``  ``VzMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in shear direction along local z-axis (MER spring behavior not including friction)

#    ``'-T'``  ``TMatTag`` |int|            tag associated with previously-defined UniaxialMaterial in torsional direction

#    ``'-My'``  ``MyMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in moment direction around local y-axis

#    ``'-Mz'``  ``MzMatTag`` |int|           tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis

#    ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)

#    ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)

#    ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.0)

#    ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution)

#    ``m`` |float|                         element mass (optional, default = 0.0)

#    ``maxIter`` |int|                     maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20)

#    ``tol`` |float|                       convergence tolerance to satisfy element equilibrium (optional, default = 1E-8)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/RJ-Watson_EQS_Bearing_Element>`_

#     uniqueArgs = []
#     if PMatTag:
#         uniqueArgs.append('-P')
#         uniqueArgs.append(PMatTag)
#     if VyMatTag:
#         uniqueArgs.append('-Vy')
#         uniqueArgs.append(VyMatTag)
#     if VzMatTag:
#         uniqueArgs.append('-Vz')
#         uniqueArgs.append(VzMatTag)
#     if TMatTag:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(TMatTag)
#     if MyMatTag:
#         uniqueArgs.append('-My')
#         uniqueArgs.append(MyMatTag)
#     if MzMatTag:
#         uniqueArgs.append('-Mz')
#         uniqueArgs.append(MzMatTag)
#     if <x1:
#         uniqueArgs.append('-orient')
#     if x2:
#         uniqueArgs.append(x1)
#         uniqueArgs.append(x2)
#         uniqueArgs.append(x3)
#         uniqueArgs.append(y3)
#     if sDratio:
#         uniqueArgs.append('-shearDist')
#         uniqueArgs.append(sDratio)
#         uniqueArgs.append(doRayleigh)
#     if m:
#         uniqueArgs.append('-mass')
#         uniqueArgs.append(m)
#     if maxIter:
#         uniqueArgs.append('-iter')
#         uniqueArgs.append(maxIter)
#         uniqueArgs.append(tol)
#     ops.element('RJWatsonEqsBearing', eleTag, *eleNodes, frnMdlTag, kInit, y1, y2, *uniqueArgs)

# def FPBearingPTV(eleTag, eleNodes, MuRef, IsPressureDependent, pRef, IsTemperatureDependent, Diffusivity, Conductivity, IsVelocityDependent, rateParameter, ReffectiveFP, Radius_Contact, kInitial, theMaterialA, theMaterialB, theMaterialC, theMaterialD, x1, x2, x3, y1, y2, y3, shearDist, doRayleigh, mass, iter, tol, unit):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of two element nodes

#    ``MuRef`` |float|                     Reference coefficient of friction

#    ``IsPressureDependent`` |int|         1 if the coefficient of friction is a function of instantaneous axial pressure

#    ``pRef`` |float|                      Reference axial pressure (the bearing pressure under static loads)

#    ``IsTemperatureDependent`` |int|      1 if the coefficient of friction is a function of instantaneous temperature at the sliding surface

#    ``Diffusivity`` |float|               Thermal diffusivity of steel

#    ``Conductivity`` |float|              Thermal conductivity of steel

#    ``IsVelocityDependent`` |int|         1 if the coefficient of friction is a function of instantaneous velocity at the sliding surface

#    ``rateParameter`` |float|             The exponent that determines the shape of the coefficient of friction vs. sliding velocity curve

#    ``ReffectiveFP`` |float|              Effective radius of curvature of the sliding surface of the FPbearing

#    ``Radius_Contact`` |float|            Radius of contact area at the sliding surface

#    ``kInitial`` |float|                  Lateral  stiffness of the sliding bearing before sliding begins

#    ``theMaterialA`` |int|                Tag for the uniaxial material in the axial direction

#    ``theMaterialB`` |int|                Tag for the uniaxial material in the torsional direction

#    ``theMaterialC`` |int|                Tag for the uniaxial material for rocking about local Y axis

#    ``theMaterialD`` |int|                Tag for the uniaxial material for rocking about local Z axis

#    ``x1``  ``x2``  ``x3`` |float|        Vector components to define local X axis

#    ``y1``  ``y2``  ``y3`` |float|        Vector components to define local Y axis

#    ``shearDist`` |float|                 Shear distance from iNode as a fraction of the length of the element

#    ``doRayleigh`` |int|                  To include Rayleigh damping from the bearing

#    ``mass`` |float|                      Element mass

#    ``iter`` |int|                        Maximum number of iterations to satisfy the equilibrium of element

#    ``tol`` |float|                       Convergence tolerance to satisfy the equilibrium of the element

#    ``unit`` |int|                        Tag to identify the unit from the list below.



#                                          * ``1``: N, m, s, C

#                                          * ``2``: kN, m, s, C

#                                          * ``3``: N, mm, s, C

#                                          * ``4``: kN, mm, s, C

#                                          * ``5``: lb, in, s, C

#                                          * ``6``: kip, in, s, C

#                                          * ``7``: lb, ft, s, C

#                                          * ``8``: kip, ft, s, C

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/FPBearingPTV>`_

#     """
#     uniqueArgs = []
#     ops.element('FPBearingPTV', eleTag, *eleNodes, MuRef, IsPressureDependent, pRef, IsTemperatureDependent, Diffusivity, Conductivity, IsVelocityDependent, rateParameter, ReffectiveFP, Radius_Contact, kInitial, theMaterialA, theMaterialB, theMaterialC, theMaterialD, x1, x2, x3, y1, y2, y3, shearDist, doRayleigh, mass, iter, tol, unit, *uniqueArgs)

# def quad(eleTag, eleNodes, thick, type, matTag, rho=0.0=None, b1=0.0=None, b2=0.0=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``thick`` |float|                     element thickness

#    ``type`` |str|                        string representing material behavior. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``

#    ``matTag`` |int|                      tag of nDMaterial

#    ``pressure`` |float|                  surface pressure (optional, default = 0.0)

#    ``rho`` |float|                       element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)

#    ``b1``  ``b2`` |float|                constant body forces defined in the isoparametric domain (optional, default=0.0)

#    ===================================   ===========================================================================



# .. note::



#    #. Consistent nodal loads are computed from the pressure and body forces.

#    #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Quad_Element>`_

#     """
#     uniqueArgs = []
#     if rho=0.0:
#         uniqueArgs.append(pressure=0.0)
#         uniqueArgs.append(rho=0.0)
#         uniqueArgs.append(b1=0.0)
#         uniqueArgs.append(b2=0.0)
#     ops.element('quad', eleTag, *eleNodes, thick, type, matTag, *uniqueArgs)

# def ShellMITC4(eleTag, eleNodes, secTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. Currently must be either a ``'PlateFiberSection'``, or ``'ElasticMembranePlateSection'``

#    ===================================   ===========================================================================



# .. note::



#    #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

#    #. It is a 3D element with 6 dofs and CAN NOT be used in 2D domain.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Shell_Element>`_

#     """
#     uniqueArgs = []
#     ops.element('ShellMITC4', eleTag, *eleNodes, secTag, *uniqueArgs)

# def ShellDKGQ(eleTag, eleNodes, secTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. Currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellDKGQ>`_

#     """
#     uniqueArgs = []
#     ops.element('ShellDKGQ', eleTag, *eleNodes, secTag, *uniqueArgs)

# def ShellDKGT(eleTag, eleNodes, secTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of three element nodes in clockwise or counter-clockwise order

#    ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellDKGT>`_

#     """
#     uniqueArgs = []
#     ops.element('ShellDKGT', eleTag, *eleNodes, secTag, *uniqueArgs)

# def ShellNLDKGQ(eleTag, eleNodes, secTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section



#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellNLDKGQ>`_

#     """
#     uniqueArgs = []
#     ops.element('ShellNLDKGQ', eleTag, *eleNodes, secTag, *uniqueArgs)

# def ShellNLDKGT(eleTag, eleNodes, secTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of three element nodes in clockwise or counter-clockwise order around the element

#    ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellNLDKGT>`_

#     """
#     uniqueArgs = []
#     ops.element('ShellNLDKGT', eleTag, *eleNodes, secTag, *uniqueArgs)

# def ShellNL(eleTag, eleNodes, secTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of nine element nodes, input is the typical, firstly four corner nodes counter-clockwise, then mid-side nodes counter-clockwise and finally the central node

#    ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section



#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellNL>`_

#     """
#     uniqueArgs = []
#     ops.element('ShellNL', eleTag, *eleNodes, secTag, *uniqueArgs)

# def bbarQuad(eleTag, eleNodes, thick, matTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``thick`` |float|                     element thickness

#    ``matTag`` |int|                      tag of nDMaterial

#    ===================================   ===========================================================================



# .. note::



#    #. PlainStrain only.

#    #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Bbar_Plane_Strain_Quadrilateral_Element>`_

#     """
#     uniqueArgs = []
#     ops.element('bbarQuad', eleTag, *eleNodes, thick, matTag, *uniqueArgs)

# def enhancedQuad(eleTag, eleNodes, thick, type, matTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``thick`` |float|                     element thickness

#    ``type`` |str|                        string representing material behavior. Valid options depend on the NDMaterial object and its available material formulations. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``

#    ``matTag`` |int|                      tag of nDMaterial

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Enhanced_Strain_Quadrilateral_Element>`_

#     """
#     uniqueArgs = []
#     ops.element('enhancedQuad', eleTag, *eleNodes, thick, type, matTag, *uniqueArgs)

# def SSPquad(eleTag, eleNodes, matTag, type, thick, b2=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``thick`` |float|                     thickness of the element in out-of-plane direction

#    ``type`` |str|                        string to relay material behavior to the element, can be either ``'PlaneStrain'`` or ``'PlaneStress'``

#    ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object

#    ``b1``  ``b2`` |float|                constant body forces in global x- and y-directions, respectively (optional, default = 0.0)

#    ===================================   ===========================================================================



#    The SSPquad element is a four-node quadrilateral element using physically stabilized single-point integration (SSP --> Stabilized Single Point). The stabilization incorporates an assumed strain field in which the volumetric dilation and the shear strain associated with the the hourglass modes are zero, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements. The formulation for this element is identical to the solid phase portion of the SSPquadUP element as described by McGann et al. (2012).



# .. note::



#    #. Valid queries to the SSPquad element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.

#    #. The SSPquad element was designed with intentions of duplicating the functionality of the Quad Element. If an example is found where the SSPquad element cannot do something that works for the Quad Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SSPquad_Element>`_

#     """
#     uniqueArgs = []
#     if b2:
#         uniqueArgs.append(b1)
#         uniqueArgs.append(b2)
#     ops.element('SSPquad', eleTag, *eleNodes, matTag, type, thick, *uniqueArgs)

# def MVLEM_3D(eleTag, eleNodes, m, thick=None, widths=None, rho=None, matConcreteTags=None, matSteelTags=None, matShearTag=None, c=None, tMod=None, Nu=None, Dens=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes defined in the counter-clockwise direction

#    ``m`` |int|                           number of element uniaxial fibers

#    ``thick`` |listf|                     a list of ``m`` macro-fiber thicknesses

#    ``widths`` |listf|                    a list of ``m`` macro-fiber widths

#    ``rho`` |listf|                       a list of m reinforcing ratios corresponding to macro-fibers; for each fiber: :math:`rho_i = A_{s,i}/A_{gross,i} (1 < i < m)`

#    ``matConcreteTags`` |listi|           a list of ``m`` uniaxialMaterial tags for concrete

#    ``matSteelTags`` |listi|              a list of ``m`` uniaxialMaterial tags for steel

#    ``matShearTag`` |int|                 tag of uniaxialMaterial for shear material

   

#    ``c`` |float|                         location of center of rotation from the base (optional; default = 0.4 (recommended))

#    ``tMod`` |float|                      thickness multiplier (optional; default = 0.63 equivalent to 0.25Ig for out-of-plane bending)

#    ``Nu`` |float|                        Poisson ratio for out-of-plane bending (optional; default = 0.25)

#    ``Dens`` |float|                      density (optional; default = 0.0)

#    ===================================   ===========================================================================



# .. seealso::



#    More information available `HERE <https://kkolozvari.github.io/MVLEM-3D/>`_ and in the following reference:

   

#    K. Kolozvari, K. Kalbasi, K. Orakcal & J. W. Wallace, "Three-Dimensional Model for Nonlinear Analysis of Slender Flanged Reinforced Concrete Walls", Engineering Structures, `Volume 236, 1 June 2021, 112105 <https://www.sciencedirect.com/science/article/pii/S0141029621002558>`_.

#     """
#     uniqueArgs = []
#     if thick:
#         uniqueArgs.append('-thick')
#         uniqueArgs.append(thick)
#     if widths:
#         uniqueArgs.append('-width')
#         uniqueArgs.append(widths)
#     if rho:
#         uniqueArgs.append('-rho')
#         uniqueArgs.append(rho)
#     if matConcreteTags:
#         uniqueArgs.append('-matConcrete')
#         uniqueArgs.append(matConcreteTags)
#     if matSteelTags:
#         uniqueArgs.append('-matSteel')
#         uniqueArgs.append(matSteelTags)
#     if matShearTag:
#         uniqueArgs.append('-matShear')
#         uniqueArgs.append(matShearTag)
#     if c:
#         uniqueArgs.append('-CoR')
#         uniqueArgs.append(c)
#     if tMod:
#         uniqueArgs.append('-ThickMod')
#         uniqueArgs.append(tMod)
#     if Nu:
#         uniqueArgs.append('-Poisson')
#         uniqueArgs.append(Nu)
#     if Dens:
#         uniqueArgs.append('-Density')
#         uniqueArgs.append(Dens)
#     ops.element('MVLEM_3D', eleTag, *eleNodes, m, *uniqueArgs)

# def SFI_MVLEM_3D(eleTag, eleNodes, m, thicks=None, widths=None, matTags=None, c=None, tMod=None, Nu=None, Dens=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes defined in the counter-clockwise direction

#    ``m`` |int|                           number of element uniaxial fibers

#    ``thicks`` |listf|                    a list of ``m`` macro-fiber thicknesses

#    ``widths`` |listf|                    a list of ``m`` macro-fiber widths

#    ``matTags`` |listi|                              a list of ``m`` material tags corresponding to nDmaterial FSAM

   

#    ``c`` |float|                         location of center of rotation from the base (optional; default = 0.4 (recommended))

#    ``tMod`` |float|                      thickness multiplier (optional; default = 0.63 equivalent to 0.25Ig for out-of-plane bending)

#    ``Nu`` |float|                        Poisson ratio for out-of-plane bending (optional; default = 0.25)

#    ``Dens`` |float|                      density (optional; default = 0.0)

#    ===================================   ===========================================================================



# .. seealso::



#    More information available `HERE <https://kkolozvari.github.io/SFI-MVLEM-3D/>`_ and in the following reference:

   

#    K. Kolozvari, K. Kalbasi, K. Orakcal & J. W. Wallace, "Three-Dimensional Shear-Flexure Interaction Model for Analysis of Non-Planar Reinforced Concrete Walls", Journal of Building Engineering, `Volume 44, December 2021, 102946 <https://www.sciencedirect.com/science/article/pii/S2352710221008044?via%3Dihub>`_.

#     """
#     uniqueArgs = []
#     if thicks:
#         uniqueArgs.append('-thick')
#         uniqueArgs.append(thicks)
#     if widths:
#         uniqueArgs.append('-width')
#         uniqueArgs.append(widths)
#     if matTags:
#         uniqueArgs.append('-mat')
#         uniqueArgs.append(matTags)
#     if c:
#         uniqueArgs.append('-CoR')
#         uniqueArgs.append(c)
#     if tMod:
#         uniqueArgs.append('-ThickMod')
#         uniqueArgs.append(tMod)
#     if Nu:
#         uniqueArgs.append('-Poisson')
#         uniqueArgs.append(Nu)
#     if Dens:
#         uniqueArgs.append('-Density')
#         uniqueArgs.append(Dens)
#     ops.element('SFI_MVLEM_3D', eleTag, *eleNodes, m, *uniqueArgs)

# def Tri31(eleTag, eleNodes, thick, type, matTag, rho=None, b1=None, b2=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of three element nodes in counter-clockwise order

#    ``thick`` |float|                     element thickness

#    ``type`` |str|                        string representing material behavior. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``

#    ``matTag`` |int|                      tag of nDMaterial

#    ``pressure`` |float|                  surface pressure (optional, default = 0.0)

#    ``rho`` |float|                       element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)

#    ``b1``  ``b2`` |float|                constant body forces defined in the domain (optional, default=0.0)

#    ===================================   ===========================================================================



# .. note::



#    #. Consistent nodal loads are computed from the pressure and body forces.

#    #. The valid queries to a Tri31 element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the domain.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Tri31_Element>`_

#     """
#     uniqueArgs = []
#     if rho:
#         uniqueArgs.append(pressure)
#         uniqueArgs.append(rho)
#         uniqueArgs.append(b1)
#         uniqueArgs.append(b2)
#     ops.element('Tri31', eleTag, *eleNodes, thick, type, matTag, *uniqueArgs)

# def stdBrick(eleTag, eleNodes, matTag, b2=None, b3=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of eight element nodes in bottom and top faces and in counter-clockwise order

#    ``matTag`` |int|                      tag of nDMaterial

#    ``b1``  ``b2``  ``b3`` |float|        body forces in global x,y,z directions

#    ===================================   ===========================================================================



# .. note::



#    #. The valid queries to a Brick element when creating an ElementRecorder object are 'forces', 'stresses,' ('strains' version > 2.2.0) and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

#    #. This element can only be defined in -ndm 3 -ndf 3



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Standard_Brick_Element>`_

#     """
#     uniqueArgs = []
#     if b2:
#         uniqueArgs.append(b1)
#         uniqueArgs.append(b2)
#         uniqueArgs.append(b3)
#     ops.element('stdBrick', eleTag, *eleNodes, matTag, *uniqueArgs)

# def bbarBrick(eleTag, eleNodes, matTag, b2=None, b3=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of eight element nodes in bottom and top faces and in counter-clockwise order

#    ``matTag`` |int|                      tag of nDMaterial

#    ``b1``  ``b2``  ``b3`` |float|        body forces in global x,y,z directions

#    ===================================   ===========================================================================



# .. note::



#    #. Node numbering for this element is different from that for the eight-node brick (Brick8N) element.

#    #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses', 'strains', and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Bbar_Brick_Element>`_

#     """
#     uniqueArgs = []
#     if b2:
#         uniqueArgs.append(b1)
#         uniqueArgs.append(b2)
#         uniqueArgs.append(b3)
#     ops.element('bbarBrick', eleTag, *eleNodes, matTag, *uniqueArgs)

# def 20NodeBrick(eleTag, eleNodes, matTag, bf1, bf2, bf3, massDen):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of twenty element nodes, input order is shown in notes below

#    ``matTag`` |int|                      material tag associated with previsouly-defined NDMaterial object

#    ``bf1``  ``bf2``  ``bf3`` |float|     body force in the direction of global coordinates x, y and z

#    ``massDen`` |float|                   mass density (mass/volume)

#    ===================================   ===========================================================================



# .. note::



#    The valid queries to a 20NodeBrick element when creating an ElementRecorder object are 'force,' 'stiffness,' stress', 'gausspoint' or 'plastic'. The output is given as follows:







#    #. 'stress'



#       the six stress components from each Gauss points are output by the order: sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_xz,sigma_yz



#    #. 'gausspoint'



#       the coordinates of all Gauss points are printed out



#    #. 'plastic'



#       the equivalent deviatoric plastic strain from each Gauss point is output in the same order as the coordinates are printed



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/OpenSees/manuals/usermanual/734.htm>`_

#     """
#     uniqueArgs = []
#     ops.element('20NodeBrick', eleTag, *eleNodes, matTag, bf1, bf2, bf3, massDen, *uniqueArgs)

# def SSPbrick(eleTag, eleNodes, matTag, b2=None, b3=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of eight element nodes in bottom and top faces and in counter-clockwise order

#    ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object

#    ``b1``  ``b2``  ``b3`` |float|        constant body forces in global x-, y-, and z-directions, respectively (optional, default = 0.0)

#    ===================================   ===========================================================================



# The SSPbrick element is an eight-node hexahedral element using physically stabilized single-point integration (SSP --> Stabilized Single Point). The stabilization incorporates an enhanced assumed strain field, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements.



# .. note::



#    #. Valid queries to the SSPbrick element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.

#    #. The SSPbrick element was designed with intentions of duplicating the functionality of the stdBrick Element. If an example is found where the SSPbrick element cannot do something that works for the stdBrick Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SSPbrick_Element>`_

#     """
#     uniqueArgs = []
#     if b2:
#         uniqueArgs.append(b1)
#         uniqueArgs.append(b2)
#         uniqueArgs.append(b3)
#     ops.element('SSPbrick', eleTag, *eleNodes, matTag, *uniqueArgs)

# def FourNodeTetrahedron(eleTag, eleNodes, matTag, b2=None, b3=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes

#    ``matTag`` |int|                      tag of nDMaterial

#    ``b1``  ``b2``  ``b3`` |float|        body forces in global x,y,z directions

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/FourNodeTetrahedron>`_

#     """
#     uniqueArgs = []
#     if b2:
#         uniqueArgs.append(b1)
#         uniqueArgs.append(b2)
#         uniqueArgs.append(b3)
#     ops.element('FourNodeTetrahedron', eleTag, *eleNodes, matTag, *uniqueArgs)

# def quadUP(eleTag, eleNodes, thick, matTag, bulk, fmass, hPerm, vPerm, b2=0=None, t=0=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``thick`` |float|                     Element thickness

#    ``matTag`` |int|                      Tag of an NDMaterial object (previously defined) of which the element is composed

#    ``bulk`` |float|                      Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`



#                                          where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.



#    ``fmass`` |float|                     Fluid mass density

#    ``hPerm``, ``vPerm`` |float|          Permeability coefficient in horizontal and vertical directions respectively.

#    ``b1``,  ``b2`` |float|               Optional gravity acceleration components in horizontal and vertical directions respectively (defaults are 0.0)

#    ``t`` |float|                         Optional uniform element normal traction, positive in tension (default is 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Four_Node_Quad_u-p_Element>`_

#     """
#     uniqueArgs = []
#     if b2=0:
#         uniqueArgs.append(b1=0)
#         uniqueArgs.append(b2=0)
#         uniqueArgs.append(t=0)
#     ops.element('quadUP', eleTag, *eleNodes, thick, matTag, bulk, fmass, hPerm, vPerm, *uniqueArgs)

# def brickUP(eleTag, eleNodes, matTag, bulk, fmass, permX, permY, permZ, bY=0=None, bZ=0=None):
#     """


#    ==========================================   ===========================================================================

#    ``eleTag`` |int|                             unique element object tag

#    ``eleNodes`` |listi|                         a list of eight element nodes

#    ``matTag`` |int|                             Tag of an NDMaterial object (previously defined) of which the element is composed

#    ``bulk`` |float|                             Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`



#                                                 where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.

#    ``fmass`` |float|                            Fluid mass density

#    ``permX``, ``permY``, ``permZ`` |float|      Permeability coefficients in x, y, and z directions respectively.

#    ``bX``, ``bY``, ``bZ`` |float|               Optional gravity acceleration components in x, y, and z directions directions respectively (defaults are 0.0)

#    ==========================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Brick_u-p_Element>`_

#     """
#     uniqueArgs = []
#     if bY=0:
#         uniqueArgs.append(bX=0)
#         uniqueArgs.append(bY=0)
#         uniqueArgs.append(bZ=0)
#     ops.element('brickUP', eleTag, *eleNodes, matTag, bulk, fmass, permX, permY, permZ, *uniqueArgs)

# def bbarQuadUP(eleTag, eleNodes, thick, matTag, bulk, fmass, hPerm, vPerm, b2=0=None, t=0=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``thick`` |float|                     Element thickness

#    ``matTag`` |int|                      Tag of an NDMaterial object (previously defined) of which the element is composed

#    ``bulk`` |float|                      Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`



#                                          where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.

#    ``fmass`` |float|                     Fluid mass density

#    ``hPerm``, ``vPerm`` |float|          Permeability coefficient in horizontal and vertical directions respectively.

#    ``b1``,  ``b2`` |float|               Optional gravity acceleration components in horizontal and vertical directions respectively (defaults are 0.0)

#    ``t`` |float|                         Optional uniform element normal traction, positive in tension (default is 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BbarQuad_u-p_Element>`_

#     """
#     uniqueArgs = []
#     if b2=0:
#         uniqueArgs.append(b1=0)
#         uniqueArgs.append(b2=0)
#         uniqueArgs.append(t=0)
#     ops.element('bbarQuadUP', eleTag, *eleNodes, thick, matTag, bulk, fmass, hPerm, vPerm, *uniqueArgs)

# def bbarBrickUP(eleTag, eleNodes, matTag, bulk, fmass, permX, permY, permZ, bY=0=None, bZ=0=None):
#     """


#    ==========================================   ===========================================================================

#    ``eleTag`` |int|                             unique element object tag

#    ``eleNodes`` |listi|                         a list of eight element nodes

#    ``matTag`` |int|                             Tag of an NDMaterial object (previously defined) of which the element is composed

#    ``bulk`` |float|                             Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`



#                                                 where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.

#    ``fmass`` |float|                            Fluid mass density

#    ``permX``, ``permY``, ``permZ`` |float|      Permeability coefficients in x, y, and z directions respectively.

#    ``bX``, ``bY``, ``bZ`` |float|               Optional gravity acceleration components in x, y, and z directions directions respectively (defaults are 0.0)

#    ==========================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BbarBrick_u-p_Element>`_

#     """
#     uniqueArgs = []
#     if bY=0:
#         uniqueArgs.append(bX=0)
#         uniqueArgs.append(bY=0)
#         uniqueArgs.append(bZ=0)
#     ops.element('bbarBrickUP', eleTag, *eleNodes, matTag, bulk, fmass, permX, permY, permZ, *uniqueArgs)

# def 9_4_QuadUP(eleTag, eleNodes, thick, matTag, bulk, fmass, hPerm, vPerm, b2=0=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of nine element nodes

#    ``thick`` |float|                     Element thickness

#    ``matTag`` |int|                      Tag of an NDMaterial object (previously defined) of which the element is composed

#    ``bulk`` |float|                      Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`



#                                          where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.

#    ``fmass`` |float|                     Fluid mass density

#    ``hPerm``, ``vPerm`` |float|          Permeability coefficient in horizontal and vertical directions respectively.

#    ``b1``,  ``b2`` |float|               Optional gravity acceleration components in horizontal and vertical directions respectively (defaults are 0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Nine_Four_Node_Quad_u-p_Element>`_

#     """
#     uniqueArgs = []
#     if b2=0:
#         uniqueArgs.append(b1=0)
#         uniqueArgs.append(b2=0)
#     ops.element('9_4_QuadUP', eleTag, *eleNodes, thick, matTag, bulk, fmass, hPerm, vPerm, *uniqueArgs)

# def 20_8_BrickUP(eleTag, eleNodes, matTag, bulk, fmass, permX, permY, permZ, bY=0=None, bZ=0=None):
#     """


#    ==========================================   ===========================================================================

#    ``eleTag`` |int|                             unique element object tag

#    ``eleNodes`` |listi|                         a list of twenty element nodes

#    ``matTag`` |int|                             Tag of an NDMaterial object (previously defined) of which the element is composed

#    ``bulk`` |float|                             Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`



#                                                 where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.

#    ``fmass`` |float|                            Fluid mass density

#    ``permX``, ``permY``, ``permZ`` |float|      Permeability coefficients in x, y, and z directions respectively.

#    ``bX``, ``bY``, ``bZ`` |float|               Optional gravity acceleration components in x, y, and z directions directions respectively (defaults are 0.0)

#    ==========================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Twenty_Eight_Node_Brick_u-p_Element>`_

#     """
#     uniqueArgs = []
#     if bY=0:
#         uniqueArgs.append(bX=0)
#         uniqueArgs.append(bY=0)
#         uniqueArgs.append(bZ=0)
#     ops.element('20_8_BrickUP', eleTag, *eleNodes, matTag, bulk, fmass, permX, permY, permZ, *uniqueArgs)

# def SSPquadUP(eleTag, eleNodes, matTag, thick, fBulk, fDen, k1, k2, void, alpha, b2=0.0=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order

#    ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object

#    ``thick`` |float|                     thickness of the element in out-of-plane direction

#    ``fBulk`` |float|                     bulk modulus of the pore fluid

#    ``fDen`` |float|                      mass density of the pore fluid

#    ``k1`` ``k2`` |float|                 permeability coefficients in global x- and y-directions, respectively

#    ``void`` |float|                      voids ratio

#    ``alpha`` |float|                     spatial pressure field stabilization parameter (see discussion below for more information)

#    ``b1``  ``b2`` |float|                constant body forces in global x- and y-directions, respectively (optional, default = 0.0) - See Note 3

#    ===================================   ===========================================================================



#       The SSPquadUP element is an extension of the SSPquad Element for use in dynamic plane strain analysis of fluid saturated porous media. A mixed displacement-pressure (u-p) formulation is used, based upon the work of Biot as extended by Zienkiewicz and Shiomi (1984).



# The physical stabilization necessary to allow for reduced integration incorporates an assumed strain field in which the volumetric dilation and the shear strain associated with the the hourglass modes are zero, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements.



# Equal-order interpolation is used for the displacement and pressure fields, thus, the SSPquadUP element does not inherently pass the inf-sup condition, and is not fully acceptable in the incompressible-impermeable limit (the QuadUP Element has the same issue). A stabilizing parameter is employed to permit the use of equal-order interpolation for the SSPquadUP element. This parameter $alpha can be computed as



# .. math::

#    \alpha = 0.25*(h^2)/(den*c^2)



# where h is the element size, c is the speed of elastic wave propagation in the solid phase, and den is the mass density of the solid phase. The $alpha parameter should be a small number. With a properly defined $alpha parameter, the SSPquadUP element can produce comparable results to a higher-order element such as the 9_4_QuadUP Element at a significantly lower computational cost and with a greater ease in mesh generation.



# The full formulation for the SSPquadUP element can be found in McGann et al. (2012) along with several example applications.



# .. note::



#    #. The SSPquadUP element will only work in dynamic analysis.

#    #. For saturated soils, the mass density input into the associated nDMaterial object should be the saturated mass density.

#    #. When modeling soil, the body forces input into the SSPquadUP element should be the components of the gravitational vector, not the unit weight.

#    #. Fixing the pore pressure degree-of-freedom (dof 3) at a node is a drainage boundary condition at which zero pore pressure will be maintained throughout the analysis. Leaving the third dof free allows pore pressures to build at that node.

#    #. Valid queries to the SSPquadUP element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.

#    #. The SSPquadUP element was designed with intentions of duplicating the functionality of the QuadUP Element. If an example is found where the SSPquadUP element cannot do something that works for the QuadUP Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SSPquadUP_Element>`_

#     """
#     uniqueArgs = []
#     if b2=0.0:
#         uniqueArgs.append(b1=0.0)
#         uniqueArgs.append(b2=0.0)
#     ops.element('SSPquadUP', eleTag, *eleNodes, matTag, thick, fBulk, fDen, k1, k2, void, alpha, *uniqueArgs)

# def SSPbrickUP(eleTag, eleNodes, matTag, fBulk, fDen, k1, k2, k3, void, alpha, b2=None, b3=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  a list of eight element nodes in counter-clockwise order

#    ``matTag`` |float|                    unique integer tag associated with previously-defined nDMaterial object

#    ``fBulk`` |float|                     bulk modulus of the pore fluid

#    ``fDen`` |float|                      mass density of the pore fluid

#    ``k1``  ``k2``  ``k3`` |float|        permeability coefficients in global x-, y-, and z-directions, respectively

#    ``void`` |float|                      voids ratio

#    ``alpha`` |float|                     spatial pressure field stabilization parameter (see discussion below for more information)

#    ``b1``  ``b2``  ``b3`` |float|        constant body forces in global x-, y-, and z-directions, respectively (optional, default = 0.0) - See Note 3

#    ===================================   ===========================================================================



# The SSPbrickUP element is an extension of the SSPbrick Element for use in dynamic 3D analysis of fluid saturated porous media. A mixed displacement-pressure (u-p) formulation is used, based upon the work of Biot as extended by Zienkiewicz and Shiomi (1984).



# The physical stabilization necessary to allow for reduced integration incorporates an enhanced assumed strain field, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements.



# Equal-order interpolation is used for the displacement and pressure fields, thus, the SSPbrickUP element does not inherently pass the inf-sup condition, and is not fully acceptable in the incompressible-impermeable limit (the brickUP Element has the same issue). A stabilizing parameter is employed to permit the use of equal-order interpolation for the SSPbrickUP element. This parameter $alpha can be computed as



# .. math::



#    \alpha = h^2/(4*(K_s + (4/3)*G_s))



# where :math:`h` is the element size, and :math:`K_s` and :math:`G_s` are the bulk and shear moduli for the solid phase. The :math:`\alpha` parameter should be a small number. With a properly defined :math:`\alpha` parameter, the SSPbrickUP element can produce comparable results to a higher-order element such as the 20_8_BrickUP Element at a significantly lower computational cost and with a greater ease in mesh generation.



# .. note::



#    #. The SSPbrickUP element will only work in dynamic analysis.

#    #. For saturated soils, the mass density input into the associated nDMaterial object should be the saturated mass density.

#    #. When modeling soil, the body forces input into the SSPbrickUP element should be the components of the gravitational vector, not the unit weight.

#    #. Fixing the pore pressure degree-of-freedom (dof 4) at a node is a drainage boundary condition at which zero pore pressure will be maintained throughout the analysis. Leaving the fourth dof free allows pore pressures to build at that node.

#    #. Valid queries to the SSPbrickUP element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.

#    #. The SSPbrickUP element was designed with intentions of duplicating the functionality of the brickUP Element. If an example is found where the SSPbrickUP element cannot do something that works for the brickUP Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SSPbrickUP_Element>`_

#     """
#     uniqueArgs = []
#     if b2:
#         uniqueArgs.append(b1)
#         uniqueArgs.append(b2)
#         uniqueArgs.append(b3)
#     ops.element('SSPbrickUP', eleTag, *eleNodes, matTag, fBulk, fDen, k1, k2, k3, void, alpha, *uniqueArgs)

# def SimpleContact2D(eleTag, iNode, jNode, cNode, lNode, matTag, gTol, fTol):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``iNode``  ``jNode`` |int|            retained nodes (-ndm 2 -ndf 2)

#    ``cNode`` |int|                       constrained node (-ndm 2 -ndf 2)

#    ``lNode`` |int|                       Lagrange multiplier node (-ndm 2 -ndf 2)

#    ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object

#    ``gTol`` |float|                      gap tolerance

#    ``fTol`` |float|                      force tolerance

#    ===================================   ===========================================================================



# The SimpleContact2D element is a two-dimensional node-to-segment contact element which defines a frictional contact interface between two separate bodies. The master nodes are the nodes which define the endpoints of a line segment on the first body, and the slave node is a node from the second body. The Lagrange multiplier node is required to enforce the contact condition. This node should not be shared with any other element in the domain. Information on the theory behind this element can be found in, e.g. Wriggers (2002).



# .. note::



#    #. The SimpleContact2D element has been written to work exclusively with the ContactMaterial2D nDMaterial object.

#    #. The valid recorder queries for this element are:



#       #. force - returns the contact force acting on the slave node in vector form.

#       #. frictionforce - returns the frictional force acting on the slave node in vector form.

#       #. forcescalar - returns the scalar magnitudes of the normal and tangential contact forces.

#       #. The SimpleContact2D elements are set to consider frictional behavior as a default, but the frictional state of the SimpleContact2D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below

#    #. The SimpleContact2D element works well in static and pseudo-static analysis situations.

#    #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SimpleContact2D>`_

#     """
#     uniqueArgs = []
#     ops.element('SimpleContact2D', eleTag, iNode, jNode, cNode, lNode, matTag, gTol, fTol, *uniqueArgs)

# def SimpleContact3D(eleTag, iNode, jNode, kNode, lNode, cNode, lagr_node, matTag, gTol, fTol):
#     """


#    ====================================================   ===========================================================================

#    ``eleTag`` |int|                                       unique element object tag

#    ``iNode``  ``jNode``  ``kNode``  ``lNode`` |int|       master nodes (-ndm 3 -ndf 3)

#    ``cNode`` |int|                                        constrained node (-ndm 3 -ndf 3)

#    ``lagr_node`` |int|                                    Lagrange multiplier node (-ndm 3 -ndf 3)

#    ``matTag`` |int|                                       unique integer tag associated with previously-defined nDMaterial object

#    ``gTol`` |float|                                       gap tolerance

#    ``fTol`` |float|                                       force tolerance

#    ====================================================   ===========================================================================





# The SimpleContact3D element is a three-dimensional node-to-surface contact element which defines a frictional contact interface between two separate bodies. The master nodes are the nodes which define a surface of a hexahedral element on the first body, and the slave node is a node from the second body. The Lagrange multiplier node is required to enforce the contact condition. This node should not be shared with any other element in the domain. Information on the theory behind this element can be found in, e.g. Wriggers (2002).



# .. note::



#    #. The SimpleContact3D element has been written to work exclusively with the ContactMaterial3D nDMaterial object.

#    #. The valid recorder queries for this element are:



#       #. force - returns the contact force acting on the slave node in vector form.

#       #. frictionforce - returns the frictional force acting on the slave node in vector form.

#       #. forcescalar - returns the scalar magnitudes of the single normal and two tangential contact forces.

#       #. The SimpleContact3D elements are set to consider frictional behavior as a default, but the frictional state of the SimpleContact3D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below

#    #. The SimpleContact3D element works well in static and pseudo-static analysis situations.

#    #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SimpleContact3D>`_

#     """
#     uniqueArgs = []
#     ops.element('SimpleContact3D', eleTag, iNode, jNode, kNode, lNode, cNode, lagr_node, matTag, gTol, fTol, *uniqueArgs)

# def BeamContact2D(eleTag, iNode, jNode, sNode, lNode, matTag, width, gTol, fTol, cFlag=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``iNode``  ``jNode`` |int|            master nodes (-ndm 2 -ndf 3)

#    ``sNode`` |int|                       slave node (-ndm 2 -ndf 2)

#    ``lNode`` |int|                       Lagrange multiplier node (-ndm 2 -ndf 2)

#    ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object

#    ``width`` |float|                     the width of the wall represented by the beam element in plane strain

#    ``gTol`` |float|                      gap tolerance

#    ``fTol`` |float|                      force  tolerance

#    ``cFlag`` |int|                       optional initial contact flag



#                                          ``cFlag`` = 0 >> contact between bodies is initially assumed (DEFAULT)



#                                          ``cFlag`` = 1 >> no contact between bodies is initially assumed

#    ===================================   ===========================================================================



# The BeamContact2D element is a two-dimensional beam-to-node contact element which defines a frictional contact interface between a beam element and a separate body. The master nodes (3 DOF) are the endpoints of the beam element, and the slave node (2 DOF) is a node from a second body. The Lagrange multiplier node (2 DOF) is required to enforce the contact condition. Each contact element should have a unique Lagrange multiplier node. The Lagrange multiplier node should not be fixed, otherwise the contact condition will not work.



# Under plane strain conditions in 2D, a beam element represents a unit thickness of a wall. The width is the dimension of this wall in the 2D plane. This width should be built-in to the model to ensure proper enforcement of the contact condition. The Excavation Supported by Cantilevered Sheet Pile Wall practical example provides some further examples and discussion on the usage of this element.



# .. note::



#    #. The BeamContact2D element has been written to work exclusively with the ContactMaterial2D nDMaterial object.

#    #. The valid recorder queries for this element are:



#       #. force - returns the contact force acting on the slave node in vector form.

#       #. frictionforce - returns the frictional force acting on the slave node in vector form.

#       #. forcescalar - returns the scalar magnitudes of the normal and tangential contact forces.

#       #. masterforce - returns the reactions (forces and moments) acting on the master nodes.

#       #. The BeamContact2D elements are set to consider frictional behavior as a default, but the frictional state of the BeamContact2D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below

#    #. The BeamContact2D element works well in static and pseudo-static analysis situations.

#    #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamContact2D>`_

#     """
#     uniqueArgs = []
#     if cFlag:
#         uniqueArgs.append(cFlag)
#     ops.element('BeamContact2D', eleTag, iNode, jNode, sNode, lNode, matTag, width, gTol, fTol, *uniqueArgs)

# def BeamContact3D(eleTag, iNode, jNode, cNode, lNode, radius, crdTransf, matTag, gTol, fTol, cFlag=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``iNode``  ``jNode`` |int|            master nodes (-ndm 3 -ndf 6)

#    ``cNode`` |int|                       constrained node (-ndm 3 -ndf 3)

#    ``lNode`` |int|                       Lagrange multiplier node (-ndm 3 -ndf 3)

#    ``radius`` |float|                    constant radius of circular beam associated with beam element

#    ``crdTransf`` |int|                   unique integer tag associated with previously-defined geometricTransf object

#    ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object

#    ``gTol`` |float|                      gap tolerance

#    ``fTol`` |float|                      force tolerance

#    ``cFlag`` |int|                       optional initial contact flag



#                                          ``cFlag`` = 0 >> contact between bodies is initially assumed (DEFAULT)



#                                          ``cFlag`` = 1 >> no contact between bodies is initially assumed

#    ===================================   ===========================================================================



# The BeamContact3D element is a three-dimensional beam-to-node contact element which defines a frictional contact interface between a beam element and a separate body. The master nodes (6 DOF) are the endpoints of the beam element, and the slave node (3 DOF) is a node from a second body. The Lagrange multiplier node (3 DOF) is required to enforce the contact condition. Each contact element should have a unique Lagrange multiplier node. The Lagrange multiplier node should not be fixed, otherwise the contact condition will not work.



# .. note::



#    #. The BeamContact3D element has been written to work exclusively with the ContactMaterial3D nDMaterial object.

#    #. The valid recorder queries for this element are:



#       #. force - returns the contact force acting on the slave node in vector form.

#       #. frictionforce - returns the frictional force acting on the slave node in vector form.

#       #. forcescalar - returns the scalar magnitudes of the single normal and two tangential contact forces.

#       #. masterforce - returns the reactions (forces only) acting on the master nodes.

#       #. mastermoment - returns the reactions (moments only) acting on the master nodes.

#       #. masterreaction - returns the full reactions (forces and moments) acting on the master nodes.

#       #. The BeamContact3D elements are set to consider frictional behavior as a default, but the frictional state of the BeamContact3D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below

#    #. The BeamContact3D element works well in static and pseudo-static analysis situations.

#    #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamContact3D>`_

#     """
#     uniqueArgs = []
#     if cFlag:
#         uniqueArgs.append(cFlag)
#     ops.element('BeamContact3D', eleTag, iNode, jNode, cNode, lNode, radius, crdTransf, matTag, gTol, fTol, *uniqueArgs)

# def BeamEndContact3D(eleTag, iNode, jNode, cNode, lNode, radius, gTol, fTol, cFlag=None):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``iNode`` |int|                       master node from the beam (-ndm 3 -ndf 6)

#    ``jNode`` |int|                       the remaining node on the beam element with ``iNode`` (-ndm 3 -ndf 6)

#    ``cNode`` |int|                       constrained node (-ndm 3 -ndf 3)

#    ``lNode`` |int|                       Lagrange multiplier node (-ndm 3 -ndf 3)

#    ``radius`` |float|                    radius of circular beam associated with beam element

#    ``gTol`` |float|                      gap tolerance

#    ``fTol`` |float|                      force tolerance

#    ``cFlag`` |float|                     optional initial contact flag



#                                          ``cFlag`` = 0 >> contact between bodies is initially assumed (DEFAULT)

#                                          ``cFlag1`` = 1 >> no contact between bodies is initially assumed

#    ===================================   ===========================================================================



# The BeamEndContact3D element is a node-to-surface contact element which defines a normal contact interface between the end of a beam element and a separate body. The first master node ($iNode) is the beam node which is at the end of the beam (i.e. only connected to a single beam element), the second node ($jNode) is the remaining node on the beam element in question. The slave node is a node from a second body. The Lagrange multiplier node is required to enforce the contact condition. This node should not be shared with any other element in the domain, and should be created with the same number of DOF as the slave node.



# The BeamEndContact3D element enforces a contact condition between a fictitious circular plane associated with a beam element and a node from a second body. The normal direction of the contact plane coincides with the endpoint tangent of the beam element at the master beam node ($iNode). The extents of this circular plane are defined by the radius input parameter. The master beam node can only come into contact with a slave node which is within the extents of the contact plane. There is a lag step associated with changing between the 'in contact' and 'not in contact' conditions.



# This element was developed for use in establishing a contact condition for the tip of a pile modeled as using beam elements and the underlying soil elements in three-dimensional analysis.



# .. note::



#    #. The BeamEndContact3D element does not use a material object.

#    #. The valid recorder queries for this element are:



#       #. force - returns the contact force acting on the slave node in vector form.

#       #. masterforce - returns the reactions (forces and moments) acting on the master node.

#       #. The BeamEndContact3D element works well in static and pseudo-static analysis situations.

#    #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamEndContact3D>`_

#     """
#     uniqueArgs = []
#     if cFlag:
#         uniqueArgs.append(cFlag)
#     ops.element('BeamEndContact3D', eleTag, iNode, jNode, cNode, lNode, radius, gTol, fTol, *uniqueArgs)

# def CatenaryCable(eleTag, iNode, jNode, weight, E, A, L0, alpha, temperature_change, rho, errorTol, Nsubsteps, massType):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``iNode``  ``jNode`` |int|            end nodes (3 dof per node)

#    ``weight`` |float|                    undefined

#    ``E`` |float|                         elastic modulus of the cable material

#    ``A`` |float|                         cross-sectional area of element

#    ``L0`` |float|                        unstretched length of the cable

#    ``alpha`` |float|                     coefficient of thermal expansion

#    ``temperature_change`` |float|        temperature change for the element

#    ``rho`` |float|                       mass per unit length

#    ``errorTol`` |float|                  allowed tolerance for within-element equilbrium (Newton-Rhapson iterations)

#    ``Nsubsteps`` |int|                   number of within-element substeps into which equilibrium iterations are subdivided (not number of steps to convergence)

#    ``massType`` |int|                    Mass matrix model to use (``massType`` = 0 lumped mass matrix,    ``massType`` = 1 rigid-body mass matrix (in development))

#    ===================================   ===========================================================================



# This cable is a flexibility-based formulation of the catenary cable. An iterative scheme is used internally to compute equilibrium. At each iteration, node i is considered fixed while node j is free. End-forces are applied at node-j and its displacements computed. Corrections to these forces are applied iteratively using a Newton-Rhapson scheme (with optional sub-stepping via $Nsubsteps) until nodal displacements are within the provided tolerance ($errortol). When convergence is reached, a stiffness matrix is computed by inversion of the flexibility matrix and rigid-body mode injection.





# .. note::



#    #. The stiffness of the cable comes from the large-deformation interaction between loading and cable shape. Therefore, all cables must have distributed forces applied to them. See example. Should not work for only nodal forces.

#    #. Valid queries to the CatenaryCable element when creating an ElementalRecorder object correspond to 'forces', which output the end-forces of the element in global coordinates (3 for each node).

#    #. Only the lumped-mass formulation is currently available.

#    #. The element does up 100 internal iterations. If convergence is not achieved, will result in error and some diagnostic information is printed out.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/CatenaryCableElement>`_

#     """
#     uniqueArgs = []
#     ops.element('CatenaryCable', eleTag, iNode, jNode, weight, E, A, L0, alpha, temperature_change, rho, errorTol, Nsubsteps, massType, *uniqueArgs)

# def PFEMElementBubble(eleTag, eleNodes, rho, mu, b1, b2, b3=None, kappa=None):
#     """


#    Create a PFEM Bubble element, which is a fluid element for FSI analysis.



#    ========================   =============================================================

#    ``eleTag`` |int|           tag of the element

#    ``eleNodes`` |listi|         A list of three or four element nodes, four are required for 3D

#    ``nd4`` |int|              tag of node 4 (required for 3D)

#    ``rho`` |float|            fluid density

#    ``mu`` |float|             fluid viscosity

#    ``b1`` |float|             body body acceleration in x direction

#    ``b2`` |float|             body body acceleration in y direction

#    ``b3`` |float|             body body acceleration in z direction (required for 3D)

#    ``thickness`` |float|      element thickness (required for 2D)

#    ``kappa`` |float|          fluid bulk modulus (optional)

#    ========================   =============================================================



#     """
#     uniqueArgs = []
#     if b3:
#         uniqueArgs.append(b3)
#     if kappa:
#         uniqueArgs.append(thickness)
#         uniqueArgs.append(kappa)
#     ops.element('PFEMElementBubble', eleTag, *eleNodes, rho, mu, b1, b2, *uniqueArgs)

# def PFEMElementCompressible(eleTag, eleNodes, rho, mu, b1, b2, kappa=None):
#     """


#    Create a PFEM compressible element, which is a fluid element for FSI analysis.



#    ========================   =============================================================

#    ``eleTag`` |int|           tag of the element

#    ``eleNodes`` |listi|         A list of four element nodes, last one is middle node

#    ``rho`` |float|            fluid density

#    ``mu`` |float|             fluid viscosity

#    ``b1`` |float|             body body acceleration in x direction

#    ``b2`` |float|             body body acceleration in y direction

#    ``thickness`` |float|      element thickness (optional)

#    ``kappa`` |float|          fluid bulk modulus (optional)

#    ========================   =============================================================



#     """
#     uniqueArgs = []
#     if kappa:
#         uniqueArgs.append(thickness)
#         uniqueArgs.append(kappa)
#     ops.element('PFEMElementCompressible', eleTag, *eleNodes, rho, mu, b1, b2, *uniqueArgs)

# def SurfaceLoad(eleTag, eleNodes, p):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  the four nodes defining the element, input in counterclockwise order (-ndm 3 -ndf 3)

#    ``p`` |float|                         applied pressure loading normal to the surface, outward is positive, inward is negative

#    ===================================   ===========================================================================



# The SurfaceLoad element is a four-node element which can be used to apply surface pressure loading to 3D brick elements. The SurfaceLoad element applies energetically-conjugate forces corresponding to the input scalar pressure to the nodes associated with the element. As these nodes are shared with a 3D brick element, the appropriate nodal loads are therefore applied to the brick.







# .. note::



#    #. There are no valid ElementalRecorder queries for the SurfaceLoad element. Its sole purpose is to apply nodal forces to the adjacent brick element.

#    #. The pressure loading from the SurfaceLoad element can be applied in a load pattern. See the analysis example below.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SurfaceLoad_Element>`_

#     """
#     uniqueArgs = []
#     ops.element('SurfaceLoad', eleTag, *eleNodes, p, *uniqueArgs)

# def VS3D4(eleTag, eleNodes, E, G, rho, R, alphaN, alphaT):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  4 end nodes

#    ``E`` |float|                         Young's Modulus of element material

#    ``G`` |float|                         Shear Modulus of element material

#    ``rho`` |float|                       Mass Density of element material

#    ``R`` |float|                         distance from the scattered wave source to the boundary

#    ``alphaN`` |float|                    correction parameter in the normal direction

#    ``alphaT`` |float|                    correction parameter in the tangential direction

#    ===================================   ===========================================================================



# .. note::



#    Reference: Liu J, Du Y, Du X, et al. 3D viscous-spring artificial boundary in time domain. Earthquake Engineering and Engineering Vibration, 2006, 5(1):93-102







# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/VS3D4>`_

#     """
#     uniqueArgs = []
#     ops.element('VS3D4', eleTag, *eleNodes, E, G, rho, R, alphaN, alphaT, *uniqueArgs)

# def AC3D8(eleTag, eleNodes, matTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  8 end nodes

#    ``matTag`` |int|                      Material Tag of previously defined nD material

#    ===================================   ===========================================================================



# .. note::



#    Reference: ABAQUS theory manual. (2.9.1 Coupled acoustic-structural medium analysis)







# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/AC3D8>`_

#     """
#     uniqueArgs = []
#     ops.element('AC3D8', eleTag, *eleNodes, matTag, *uniqueArgs)

# def ASI3D8(eleTag, eleNodes1, eleNodes2):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``*eleNodes1`` |listi|                four nodes defining structure domain of element boundaries

#    ``*eleNodes2`` |listi|                four nodes defining acoustic domain of element boundaries

#    ===================================   ===========================================================================



# .. note::



#    Reference: ABAQUS theory manual. (2.9.1 Coupled acoustic-structural medium analysis)







# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ASI3D8>`_

#     """
#     uniqueArgs = []
#     ops.element('ASI3D8', eleTag, *eleNodes1, *eleNodes2, *uniqueArgs)

# def AV3D4(eleTag, eleNodes, matTag):
#     """


#    ===================================   ===========================================================================

#    ``eleTag`` |int|                      unique element object tag

#    ``eleNodes`` |listi|                  4 end nodes

#    ``matTag`` |int|                      Material Tag of previously defined nD material

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/AV3D4>`_

#     """
#     uniqueArgs = []
#     ops.element('AV3D4', eleTag, *eleNodes, matTag, *uniqueArgs)

