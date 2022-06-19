# from .beamIntegration import *
from . import beamIntegration

# from .block import *
from . import block


# from .element import *
from . import element

# from .frictionModel import *

from .geomTransf import *
from . import geomTransf


# from .mp_constraint import *
# from .ndMaterial import *

# from .pattern import *
from . import pattern

# from .rayleigh import *

# from .section import *

# from .SP_Constraint import *
from . import SPconstraint

# from .timeSeries import *
from . import timeSeries


# from .uniaxialMaterial import *
from . import uniaxialMaterial


import openseespy.opensees as ops

def basic(ndm, ndf=None):
    """
    Set the default model dimensions and number of dofs.
          
    ========================   ===========================================================================    
    ``ndm`` |int|              number of dimensions (1,2,3)
    ``ndf`` |int|              number of dofs (optional)    
    ========================   ===========================================================================
     
    Hint:
        Checked

    """
    uniqueArgs = []
    if ndm:
        uniqueArgs.append('-ndm')
        uniqueArgs.append(ndm)
    if ndf:
        uniqueArgs.append('-ndf')
        uniqueArgs.append(ndf)
    ops.model('basic', *uniqueArgs)
    

def node(nodeTag, crds, ndf=None, mass=None, disp=None, vel=None, accel=None):
    """
    Create a OpenSees node.
    
    ========================   ===========================================================================
    ``nodeTag`` |int|          node tag.
    
    ``crds`` |listf|           nodal coordinates.
    
    ``ndf`` |float|            nodal ndf. (optional)
    
    ``mass`` |listf|           nodal mass. (optional)
    
    ``disp`` |listf|           nodal disp. (optional)
    
    ``vel`` |listf|            nodal velocities. (optional)
    
    ``accel`` |listf|          nodal accelerations. (optional)
    
    ========================   ===========================================================================

    Hint:
        untested

    """
    uniqueArgs = []
    if ndf:
        uniqueArgs.append('-ndf')
        uniqueArgs.append(ndf)
    if mass:
        uniqueArgs.append('-mass')
        uniqueArgs += mass
    if disp:
        uniqueArgs.append('-disp')
        uniqueArgs += disp
    if vel:
        uniqueArgs.append('-vel')
        uniqueArgs += vel
    if accel:
        uniqueArgs.append('-accel')
        uniqueArgs += accel
    ops.node(nodeTag, *crds, *uniqueArgs)








    
def pressureConstraint(nodeTag, pNodeTag):
    """
    Create a pressure constraint for incompressible flow.
    
    ========================   ===========================================================================
    ``nodeTag`` |int|          tag of node to be constrained
    ``pNodeTag`` |int|         tag of extra pressure node, which
                               must exist before calling this command
    ========================   ===========================================================================

    For example, 
    
    .. code-block:: python
    
       ops.node(1, 0.0, 0.0)
       ops.node(2, 0.0, 0.0, '-ndf', 1)
       ops.pressureConstraint(1, 2)

    Hint:
        untested

    """
    ops. pressureConstraint(nodeTag, pNodeTag)
    
def mass(nodeTag, massValues):
    """
    This command is used to set the mass at a node
    
    ========================   =============================================================
    ``nodeTag`` |int|          integer tag identifying node whose mass is set
    ``massValues`` |listf|     ndf nodal mass values corresponding to each DOF
    ========================   =============================================================

    """
    ops.mass(nodeTag, *massValues)


    

def region(regTag, eles=None, elesOnly=False, startEle=None, endEle=None, 
           elesOnlyRange=False, nodes=None, nodeOnly=False, startNode=None, 
           endNode=None, alphaM=None, betaK=None, betaKinit=None, betaKcomm=None):
    """
    The region command is used to label a group of nodes and elements. 
    This command is also used to assign rayleigh damping parameters to the 
    nodes and elements in this region. The region is specified by either 
    elements or nodes, not both. If elements are defined, the region includes 
    these elements and the all connected nodes, unless the -eleOnly option is 
    used in which case only elements are included. If nodes are specified, the 
    region includes these nodes and all elements of which all nodes are 
    prescribed to be in the region, unless the -nodeOnly option is used in 
    which case only the nodes are included.
    
    ========================   =============================================================
    ``regTag`` |int|           unique integer tag
    ``eles`` |listi|           tags of selected elements in domain to be
                               included in region (optional)
    ``nodes`` |listi|          tags of selected nodes in domain to be
                               included in region (optional)
    ``startEle`` |int|         tag for start element. If included the function will assume that a range is being input. (optional)
    ``endEle`` |int|           tag for end element.  (optional)
    ``startNode`` |int|        tag for start node. If included the function will assume that a range is being input. (optional)
    ``endNode`` |int|          tag for end node. (optional)
    ``alphaM`` |float|         factor applied to elements or nodes mass matrix (optional)
    ``betaK`` |float|          factor applied to elements current stiffness matrix (optional)
    ``betaKinit`` |float|      factor applied to elements initial stiffness matrix (optional)
    ``betaKcomm`` |float|      factor applied to elements committed stiffness matrix (optional)
    ========================   =============================================================

    .. note::

    The user cannot prescribe the region by BOTH elements and nodes.

    Hint:
        untested
        It's being assumed that you can only have '-ele' or '-eleOnly, but
        not both at once. This is not immediately clear in the documentation,
        and the assumption might be incorrect.
    """
    uniqueArgs = []
    if eles and not elesOnly:
        uniqueArgs.append('-ele')
        uniqueArgs += eles
    if eles and elesOnly:
        uniqueArgs.append('-eleOnly')
        uniqueArgs += eles
    if startEle and not elesOnlyRange:
        uniqueArgs.append('-eleRange')
        uniqueArgs.append(startEle)
        uniqueArgs.append(endEle)
    if startEle and elesOnlyRange:
        uniqueArgs.append('-eleOnlyRange')
        uniqueArgs.append(startEle)
        uniqueArgs.append(endEle)
    if nodes and not nodeOnly:
        uniqueArgs.append('-node')
        uniqueArgs += nodes
    if nodes and nodeOnly:
        uniqueArgs.append('-nodeOnly')
        uniqueArgs += nodes
    if startNode:
        uniqueArgs.append('-nodeRange')
        uniqueArgs.append(startNode)
        uniqueArgs.append(endNode)
    if startNode:
        uniqueArgs.append('-nodeOnlyRange')
        uniqueArgs.append(startNode)
        uniqueArgs.append(endNode)
    if alphaM:
        uniqueArgs.append('-rayleigh')
        uniqueArgs.append(alphaM)
        uniqueArgs.append(betaK)
        uniqueArgs.append(betaKinit)
        uniqueArgs.append(betaKcomm)
    ops.region(regTag, *uniqueArgs)



def rayleigh(alphaM, betaK, betaKinit, betaKcomm):
    """
    This command is used to assign damping to all previously-defined elements and nodes. When using rayleigh damping in OpenSees, the damping matrix for an element or node, D is specified as a combination of stiffness and mass-proportional damping matrices:

    .. math::
    
       D = \\alpha_M * M + \\beta_K * K_{curr} + \\beta_{Kinit} * K_{init} + \\beta_{Kcomm} * K_{commit}

    ========================   =============================================================
    ``alphaM`` |float|         factor applied to elements or nodes mass matrix
    ``betaK`` |float|          factor applied to elements current stiffness matrix.
    ``betaKinit`` |float|      factor applied to elements initial stiffness matrix.
    ``betaKcomm`` |float|      factor applied to elements committed stiffness matrix.
    ========================   =============================================================

    Hint:
        untested

    """
    ops.rayleigh(alphaM, betaK, betaKinit, betaKcomm)