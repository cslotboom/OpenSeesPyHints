import openseespy.opensees as ops

def inputfile(inputfile, outputfile):
    """
   Convert text file to binary file



   ========================   ===========================================================================

   ``inputfile`` |str|        input file name.

   ``outputfile`` |str|       output file name.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.convertTextToBinary(inputfile, outputfile, *uniqueArgs)

