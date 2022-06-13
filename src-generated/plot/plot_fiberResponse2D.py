import openseespy.opensees as ops

def ModelName(ModelName, LoadCaseName, element, section, LocalAxis =None, InputType =None, tstep =None):
    """


   ========================  ===============================================================================================================================================================================

   ``ModelName``    |str|     Name of the model to read data from output database, created with `createODB()` command.

   ``LoadCaseName`` |str|     Name of the subfolder with load case output data.

   ``element`` |int|          Tag of the element where the section to be plotted is located.

   ``section``  |int|         Tag of the section to be plotted.

   ``LocalAxis``  |str|       Local axis of the section, based on a user defined axes transformation. (optional, default is "Y")

   ``InputType``  |str|       Type of the fiber response to be plotted, ``"stress"`` or ``"strain"``. (optional, default is "stress")

   ``tstep``    |float|       Approximate time of the analysis at which fiber response is to be plotted. The program will find the closed time step to the input value.(optional, default is the last step).

   ========================  ===============================================================================================================================================================================





   

Examples: 

    

   ``plot_fiberResponse2D("TwoSpan_Bridge", "Dynamic_GM1", 101, 2)``

                 Plots the fiber stress (default) distribution of section 2 in element 101 of structure by reading data from `TwoSpan_Bridge_ODB` with a sub-folder `Dynamic_GM1` at the last analysis step (default).



    """
    uniqueArgs = []
    ops.postprocessing.Get_Rendering.plot_fiberResponse2D(ModelName, LoadCaseName, element, section, LocalAxis , InputType , tstep , *uniqueArgs)

