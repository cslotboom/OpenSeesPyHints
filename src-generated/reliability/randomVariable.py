import openseespy.opensees as ops

def tag(tag, dist, mean=None, stdv=None, startPoint=None, params=None):
    """
   Create a random variable with user specified distribution



   ========================   ===========================================================================

   ``tag`` |int|              random variable tag

   ``dist`` |str|             random variable distribution



                              * ``'normal'``

                              * ``'lognormal'``

                              * ``'gamma'``

                              * ``'shiftedExponential'``

                              * ``'shiftedRayleigh'``

                              * ``'exponential'``

                              * ``'rayleigh'``

                              * ``'uniform'``

                              * ``'beta'``

                              * ``'type1LargestValue'``

                              * ``'type1SmallestValue'``

                              * ``'type2LargestValue'``

                              * ``'type3SmallestValue'``

                              * ``'chiSquare'``

                              * ``'gumbel'``

                              * ``'weibull'``

                              * ``'laplace'``

                              * ``'pareto'``

                              

   ``mean`` |float|           mean value

   ``stdv`` |float|           standard deviation

   ``startPoint`` |float|     starting point of the distribution

   ``params`` |listi|         a list of parameter tags

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if mean:
        uniqueArgs.append('-mean')
        uniqueArgs.append(mean)
    if stdv:
        uniqueArgs.append('-stdv')
        uniqueArgs.append(stdv)
    if startPoint:
        uniqueArgs.append('-startPoint')
        uniqueArgs.append(startPoint)
    if params:
        uniqueArgs.append('-parameters')
        uniqueArgs.append(params)
    ops.randomVariable(tag, dist, *uniqueArgs)

