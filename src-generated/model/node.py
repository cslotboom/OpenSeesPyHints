import openseespy.opensees as ops

def nodeTag(nodeTag, crds, ndf=None, mass=None, disp=None, vel=None, accel=None):
    """
   Create a OpenSees node.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``crds`` |listf|           nodal coordinates.

   ``ndf`` |float|            nodal ndf. (optional)

   ``mass`` |listf|           nodal mass. (optional)

   ``vel`` |listf|            nodal velocities. (optional)

   ``accel`` |listf|          nodal accelerations. (optional)

   ========================   ===========================================================================







    """
    uniqueArgs = []
    if ndf:
        uniqueArgs.append('-ndf')
        uniqueArgs.append(ndf)
    if mass:
        uniqueArgs.append('-mass')
        uniqueArgs.append(mass)
    if disp:
        uniqueArgs.append('-disp')
        uniqueArgs.append(disp)
    if vel:
        uniqueArgs.append('-vel')
        uniqueArgs.append(vel)
    if accel:
        uniqueArgs.append('-accel')
        uniqueArgs.append(accel)
    ops.node(nodeTag, *crds, *uniqueArgs)

