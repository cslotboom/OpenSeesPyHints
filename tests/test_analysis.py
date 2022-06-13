# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:06:21 2022

@author: Christian
"""

import openseespyhint as op
import openseespy.opensees as ops


op.model.model.basic(2, 3)

# ops.wipe()
# ops.node(1, *[0.,0.])

# import numpy as np

# constraints
op.analysis.constraints
op.analysis.constraints.Plain()
op.analysis.constraints.Lagrange(0.2, 0.3)
op.analysis.constraints.Penalty(0.2, 0.3)
op.analysis.constraints.Transformation()

tol = 10.**-6
Niter = 20
op.analysis.test.NormUnbalance(tol, Niter)
op.analysis.test.NormDispIncr(tol, Niter)
op.analysis.test.EnergyIncr(tol, Niter)
op.analysis.test.RelativeNormUnbalance(tol, Niter)
# op.analysis.test.Re

op.analysis.test.NormDispAndUnbalance(tol, tol, Niter)
# ops.test('NormUnbalance',tol, Niter)
# ops.wipe()


# op.analysis.algorithm.Linear()
# op.analysis.algorithm.Newton()
# op.analysis.algorithm.NewtonLineSearch()
# op.analysis.algorithm.ModifiedNewton()
# op.analysis.algorithm.KrylovNewton()
# op.analysis.algorithm.SecantNewton()
# op.analysis.algorithm.RaphsonNewton()
op.analysis.algorithm.PeriodicNewton()
# op.analysis.algorithm.BFGS()
# op.analysis.algorithm.Broyden()

# ops.algorithm('Linear')







# Transformation


# import openseespyhint.analysis as op

# op.analysis.analysis()
# op.model.model
# print(op.model)


# op.analysis.constraints.Plain()
# op.analysis.


# import openseespy.opensees as op

# op.wipe()
# op.model('basic', '-ndm', 2, '-ndf', 3)
# # op.model('ndm', 2)


# op.geomTransf('Linear', 1)

# op.node(1, *[0,0])
# op.node(2, *[1,0])
# op.node(3, *[0,0])
# massDens = 1
# # op.element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Avy, transfTag, *optionalArgs)
# op.element('ElasticTimoshenkoBeam',     1, *[1,2], 1., 1., 1., 1., 1., 1, '-cMass')


# op.wipe()
# op.model('basic', '-ndm', 3)

# matTag = 1
# op.uniaxialMaterial('Elastic', matTag, 10.**9)
# op.nDMaterial('ElasticIsotropic', 2, 10.**9,0.2)
# op.element('zeroLengthND', 2, *[1,3], 2)

