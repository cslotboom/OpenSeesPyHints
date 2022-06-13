import openseespy.opensees as ops

def inputfile(inputfile, outputfile):
    """
   Convert binary file to text file



   ========================   ===========================================================================

   ``inputfile`` |str|        input file name.

   ``outputfile`` |str|       output file name.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.convertBinaryToText(inputfile, outputfile, *uniqueArgs)

