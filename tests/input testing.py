# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:06:21 2022

@author: Christian
"""

import openseespy.opensees as op

op.wipe()
op.model('basic', '-ndm', 2, '-ndf', 3)
# op.model('ndm', 2)


op.geomTransf('Linear', 1)

op.node(1, *[0,0])
op.node(2, *[1,0])
op.node(3, *[0,0])
massDens = 1
# op.element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Avy, transfTag, *optionalArgs)
op.element('ElasticTimoshenkoBeam',     1, *[1,2], 1., 1., 1., 1., 1., 1, '-cMass')


op.wipe()
op.model('basic', '-ndm', 3)

matTag = 1
op.uniaxialMaterial('Elastic', matTag, 10.**9)
op.nDMaterial('ElasticIsotropic', 2, 10.**9,0.2)
op.element('zeroLengthND', 2, *[1,3], 2)
# op.element('zeroLengthND', 2, *[1,3], 2,'-1DTag',1)

