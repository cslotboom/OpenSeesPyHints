import openseespy.opensees as ops

def ncuts(ncuts, niters=None, ufactor=None):
    """
   In a parallel environment, this command partitions the model. It requires that all processors

   have the exact same model to be partitioned. 



   ========================   ===========================================================================

   ``ncuts`` |int|            Specifies the number of different partitionings that it will compute. 

                              The final partitioning is the one

                              that achieves the best edge cut or communication volume. 

                              (Optional default is 1).

   ``niters`` |int|           Specifies the number of iterations for the refinement algorithms 

                              at each stage of the uncoarsening process. 

                              (Optional default is 10).

   ``ufactor`` |int|          Specifies the maximum allowed load imbalance among the partitions. 

                              (Optional default is 30, indicating a load imbalance of 1.03).

   ``'-info'`` |str|          print information. (optional)

   ========================   ===========================================================================







    """
    uniqueArgs = []
    if niters:
        uniqueArgs.append('-niter')
        uniqueArgs.append(niters)
    if ufactor:
        uniqueArgs.append('-ufactor')
        uniqueArgs.append(ufactor)
    if '-info':
        uniqueArgs.append('-info')
    ops.partition('-ncuts', ncuts, *uniqueArgs)

