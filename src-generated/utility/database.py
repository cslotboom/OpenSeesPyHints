import openseespy.opensees as ops

def type(type, dbName):
    """
   Create a database.



   ===========================   =====================================================================================================================================================

   ``type`` |str|                database type:



                                 * ``'File'`` - outputs database into a file

                                 * ``'MySQL'`` - creates a SQL database

                                 * ``'BerkeleyDB'`` - creates a BerkeleyDB database

   ``dbName`` |str|              database name.

   ===========================   =====================================================================================================================================================

    """
    uniqueArgs = []
    ops.database(type, dbName, *uniqueArgs)

