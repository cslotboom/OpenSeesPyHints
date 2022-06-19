import openseespy.opensees as ops

def BandGen():
    """

    This command is used to construct a BandGeneralSOE linear system of equation
    object. As the name implies, this class is used for matrix systems which 
    have a banded profile. The matrix is stored as shown below in a 1dimensional
    array of size equal to the bandwidth times the number of unknowns.
    When a solution is required, the Lapack routines DGBSV and SGBTRS are used.

    Hints:
        untested

    """
    
    ops.system('BandGen')

def BandSPD():
    """


    This command is used to construct a BandSPDSOE linear system of equation 
    object. As the name implies, this class is used for symmetric positive 
    definite matrix systems which have a banded profile. The matrix is stored 
    as shown below in a 1 dimensional array of size equal to the (bandwidth/2) 
    times the number of unknowns. When a solution is required, the Lapack 
    routines DPBSV and DPBTRS are used.

    Hints:
        untested

    """
    
    ops.system('BandSPD')

def ProfileSPD():
    """


    This command is used to construct a profileSPDSOE linear system of equation 
    object. As the name implies, this class is used for symmetric positive 
    definite matrix systems. The matrix is stored as shown below in a 1 
    dimensional array with only those values below the first non-zero row in 
    any column being stored. This is sometimes also referred to as a skyline 
    storage scheme.

    Hints:
        untested

    """
    
    ops.system('ProfileSPD')

def SuperLU():
    """

    This command is used to construct a SparseGEN linear system of equation 
    object. As the name implies, this class is used for sparse matrix systems. 
    The solution of the sparse matrix is carried out using `SuperLU`_.

    Hints:
        untested

    """
    
    ops.system('SuperLU')

def UmfPack():
    """


    This command is used to construct a sparse system of equations which
    uses the `UmfPack`_ solver.

    Hints:
        untested

    """
    ops.system('UmfPack')

def FullGeneral():
    """

    This command is used to construct a Full General linear system of equation 
    object. As the name implies, the class utilizes NO space saving techniques 
    to cut down on the amount of memory used. If the matrix is of size, nxn, 
    then storage for an nxn array is sought from memory when the program runs. 
    When a solution is required, the Lapack routines DGESV and DGETRS are used.

    .. note::

        This type of system should almost never be used! This is because it requires a lot more memory than every other solver and takes more time in the actal solving operation than any other solver. It is required if the user is interested in looking at the global system matrix.

    Hints:
        untested

    """
    
    ops.system('FullGeneral')

def SparseSYM():
    """

    This command is used to construct a sparse symmetric system of equations which uses a row-oriented solution method in the solution phase.

    Hints:
        untested

    """    
    ops.system('SparseSYM')

def Mumps(icntl14=20., icntl7=7):
    """
    Create a system of equations using the Mumps solver
    
    ========================   ===========================================================================
    ``icntl14``                controls the percentage increase in the estimated working space (optional)
    ``icntl7``                 computes a symmetric permutation (ordering) to determine the pivot order to
                               be used for the factorization in case of sequential analysis (optional)
    
                               * 0: AMD
                               * 1: set by user
                               * 2: AMF
                               * 3: SCOTCH
                               * 4: PORD
                               * 5: Metis
                               * 6: AMD with QADM
                               * 7: automatic
    
    ========================   ===========================================================================

    Use this command only for parallel model.

    .. warning::
    
       Don't use this command if model is not parallel, for example,
       parametric study.

    Hints:
        untested

    """
    uniqueArgs = []
    if icntl14:
        uniqueArgs.append('-ICNTL14')
        uniqueArgs.append(icntl14)
    if icntl7:
        uniqueArgs.append('-ICNTL7')
        uniqueArgs.append(icntl7)
    ops.system('Mumps',     *uniqueArgs)

