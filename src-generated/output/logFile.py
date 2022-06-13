import openseespy.opensees as ops

def filename(filename):
    """
   Log all messages and errors in a file. By default,

   all messages and errors print to terminal or Jupyter Notebook depending on

   how Python was run.



   ===========================   =====================================================================================================================================================

   ``filename`` |str|            name of the log file

   ``'-append'`` |str|           append to the file

   ``'-noEcho'`` |str|           do not print to terminal or Jupyter Notebook

   ===========================   =====================================================================================================================================================

    """
    uniqueArgs = []
    if '-noEcho':
        uniqueArgs.append('-append')
    if '-noEcho':
        uniqueArgs.append('-noEcho')
    ops.logFile(filename, *uniqueArgs)

