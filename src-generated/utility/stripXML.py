import openseespy.opensees as ops

def inputml(inputml, outputdata, outputxml):
    """
   Strip a xml file to a data file and a descriptive file.



   ========================   ===========================================================================

   ``inputxml`` |str|         input xml file name.

   ``outputdata`` |str|       output data file name.

   ``outputxml`` |str|        output xml file name.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.stripXML(inputml, outputdata, outputxml, *uniqueArgs)

