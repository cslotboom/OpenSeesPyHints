import openseespy.opensees as ops

def tri(tag, numlines, ltags, id, ndf, meshsize, eleType, *eleArgs):
    """


   Create a triangular mesh object.





   ========================   ===========================================================================

   ``tag`` |int|              mesh tag.

   ``numlines`` |int|         number of lines (:ref:`LineMesh`) for defining a polygon.

   ``ltags`` |listi|          the :ref:`LineMesh` tags

   ``id`` |int|               mesh id. Meshes with same id are considered as same structure

                              of fluid identity.



                              * ``id`` = 0 : not in FSI

                              * ``id`` > 0 : structure

                              * ``id`` < 0 : fluid

   ``ndf`` |int|              ndf for nodes to be created.

   ``meshsize`` |float|       mesh size.

   ``eleType`` |str|          the element type, (optional)



                              * :doc:`PFEMElementBubble`

                              * :doc:`PFEMElementCompressible`

                              * :doc:`tri31`

                              * :doc:`elasticBeamColumn`

                              * :doc:`ForceBeamColumn`

                              * :doc:`dispBeamColumn`



                              if no type is given, only nodes are created.

                              if beam elements are given, beams are created

                              instead of triangular elements.

                              

   ``eleArgs`` |list|         a list of element arguments. The arguments

                              are same as in the element commands, but without

                              element tag, and node tags. (optional)



                              For example,



                              ``eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thickness, kappa]``

   ========================   ===========================================================================



    """
    uniqueArgs = []
    ops.mesh('tri', tag, numlines, *ltags, id, ndf, meshsize, eleType, *eleArgs, *uniqueArgs)

def quad(tag, numlines, ltags, id, ndf, meshsize, eleType, *eleArgs):
    """


   Create a quad mesh object. The number of lines must be 4. These lines are continuous

   to form a loop.





   ========================   ===========================================================================

   ``tag`` |int|              mesh tag.

   ``numlines`` |int|         number of lines (:ref:`LineMesh`) for defining a polygon.

   ``ltags`` |listi|          the :ref:`LineMesh` tags

   ``id`` |int|               mesh id. Meshes with same id are considered as same structure

                              of fluid identity.



                              * ``id`` = 0 : not in FSI

                              * ``id`` > 0 : structure

                              * ``id`` < 0 : fluid

   ``ndf`` |int|              ndf for nodes to be created.

   ``meshsize`` |float|       mesh size.

   ``eleType`` |str|          the element type, (optional)



                              * :doc:`PFEMElementBubble`

                              * :doc:`PFEMElementCompressible`

                              * :doc:`tri31`

                              * :doc:`elasticBeamColumn`

                              * :doc:`ForceBeamColumn`

                              * :doc:`dispBeamColumn`

                              * :doc:`ShellMITC4`



                              if no type is given, only nodes are created.

                              If beam elements are given, beams are created

                              instead of quad elements.

                              If triangular elements are given, they are created

                              by dividing one quad to two triangles.

                              

   ``eleArgs`` |list|         a list of element arguments. The arguments

                              are same as in the element commands, but without

                              element tag, and node tags. (optional)



                              For example,



                              ``eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thickness, kappa]``

   ========================   ===========================================================================



    """
    uniqueArgs = []
    ops.mesh('quad', tag, numlines, *ltags, id, ndf, meshsize, eleType, *eleArgs, *uniqueArgs)

def tet(tag, nummesh, mtags, id, ndf, meshsize, eleType, *eleArgs):
    """


   Create a 3D tetrahedron mesh object.





   ========================   ===========================================================================

   ``tag`` |int|              mesh tag.

   ``nummesh`` |int|          number of 2D mesh for defining a 3D body.

   ``mtags`` |listi|          the mesh tags

   ``id`` |int|               mesh id. Meshes with same id are considered as same structure

                              of fluid identity.



                              * ``id`` = 0 : not in FSI

                              * ``id`` > 0 : structure

                              * ``id`` < 0 : fluid

   ``ndf`` |int|              ndf for nodes to be created.

   ``meshsize`` |float|       mesh size.

   ``eleType`` |str|          the element type, (optional)



                              * :doc:`FourNodeTetrahedron`



                              if no type is given, only nodes are created.



                              

   ``eleArgs`` |list|         a list of element arguments. The arguments

                              are same as in the element commands, but without

                              element tag, and node tags. (optional)



   ========================   ===========================================================================



    """
    uniqueArgs = []
    ops.mesh('tet', tag, nummesh, *mtags, id, ndf, meshsize, eleType, *eleArgs, *uniqueArgs)

def part(tag, type, pArgs, eleType, *eleArgs, vel0=None, p0=None):
    """


   Create or return a group of particles which will be used for background mesh.





   ========================     ==========================================================================================

   ``tag`` |int|                mesh tag.

   ``type`` |str|               type of the mesh

   ``pArgs`` |listf|            coordinates of points defining the mesh region

                                ``nx``, ``ny``, ``nz`` are number of particles in x, y,

                                and z directions

                



                                * ``'quad'`` : [x1, y1, x2, y2, x3, y3, x4, y4, nx, ny]

                                        

                                  Coordinates of four corners in counter-clock wise order.

                                        

                                * ``'cube'`` : [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4,

                                                z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8,

                                                y8, z8, nx, ny, nz]

                                        

                                  Coordinates of four corners at bottom and at top in

                                  counter-clock wise order

                                

                                * ``'tri'`` : [x1, y1, x2, y2, x3, y3, nx, ny]

                                        

                                  Coordinates of three corners in counter-clock wise order



                                * ``'line'`` : [x1, y1, x2, y2, nx]

                              

                                  Coordinates of two ends in counter-clock wise order

                                

                                * ``'pointlist'`` : [x1, y1, <z1>, vx1, vy1, <vz1>,

                                                     ax1, ay1, <az1>, p1, 

                                                     x2, y2, <z2>, vx2, vy2, <vz2>,

                                                     ax2, ay2, <az2>, p2, ..]

                              

                                  input particles' data in a list, in the order of coordinates

                                  of last time step, current coordinates, velocity, acceleration,

                                  and pressure.



                                * ``'pointlist'`` without list



                                  return a list of current particles' data in this mesh



                                  [tag1, x1, y1, <z1>, vx1, vy1, <vz1>,

                                  ax1, ay1, <az1>, p1,

                                  tag2, x2, y2, <z2>, vx2, vy2, <vz2>,

                                  ax2, ay2, <az2>, p2,

                                  ..]



                                  The format is similar to the input list, but with an

                                  additional tag for each particle.



                              

   ``eleType`` |str|            the element type, (optional)



                                * :doc:`PFEMElementBubble`

                                * :doc:`PFEMElementCompressible`

                                * :doc:`tri31`



                                  if no type is given, only nodes are created

                              

   ``eleArgs`` |list|           a list of element arguments.

                                (optional, see :doc:`linemesh` and :doc:`trimesh`)

   ``vel0`` |listf|             a list of initial velocities. (optional)

   ``p0`` |float|               initial pressure. (optional)

   ========================     ==========================================================================================



    """
    uniqueArgs = []
    if vel0:
        uniqueArgs.append('-vel')
        uniqueArgs.append(vel0)
    if p0:
        uniqueArgs.append('-pressure')
        uniqueArgs.append(p0)
    ops.mesh('part', tag, type, *pArgs, eleType, *eleArgs, *uniqueArgs)

def bg(basicsize, lower, upper, tol=None, meshtol=None, wavefilename=None, numl=None, locations=None, numsub=None, id=None, numnodes=None, snodes=None, level=None, llower=None, lupper=None):
    """


   Create a background mesh. 





   ========================   ===========================================================================

   ``basicsize`` |float|      basic mesh size

   ``lower`` |listf|          a list of coordinates of the lower point of the background region.

   ``upper`` |listf|          a list of coordinates of the uuper point of the background region.

   ``tol`` |float|            tolerance for intri check. (optional, default 1e-10)

   ``meshtol`` |float|        tolerance for cell boundary check. (optional, default 0.1)

   ``wavefilename`` |str|     a filename to record wave heights and velocities (optional)

   ``numl`` |int|             number of locations to record wave (optional)

   ``locations`` |listf|      coordinates of the locations (optional)

   ``id`` |int|               structural id > 0, same meaning as :doc:`trimesh` (optional)

   ``numsnodes`` |int|        number of structural nodes (optional)

   ``sNodes`` |listi|         a list of structural nodes (optional)

   ``level`` |int|            some regions can have larger mesh size with larger ``level``.

                              ``level = 1`` means same as basic mesh size.

   ``llower`` |listf|         a list of coordinates of the lower point of the region with

                              larger mesh size (optional)

   ``lupper`` |listf|         a list of coordinates of the upper point of the region with

                              larger mesh size(optional)

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if tol:
        uniqueArgs.append('-tol')
        uniqueArgs.append(tol)
    if meshtol:
        uniqueArgs.append('-meshtol')
        uniqueArgs.append(meshtol)
    if wavefilename:
        uniqueArgs.append('-wave')
        uniqueArgs.append(wavefilename)
        uniqueArgs.append(numl)
        uniqueArgs.append(locations)
    if numsub:
        uniqueArgs.append('-numsub')
        uniqueArgs.append(numsub)
    if id:
        uniqueArgs.append('-structure')
        uniqueArgs.append(id)
        uniqueArgs.append(numnodes)
        uniqueArgs.append(snodes)
    if level:
        uniqueArgs.append('-largeSize')
        uniqueArgs.append(level)
        uniqueArgs.append(llower)
        uniqueArgs.append(lupper)
    ops.mesh('bg', basicsize, *lower, *upper, *uniqueArgs)

