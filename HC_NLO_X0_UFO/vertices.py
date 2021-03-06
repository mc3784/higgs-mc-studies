# This file was automatically created by FeynRules $Revision: 535 $
# Mathematica version: 7.0 for Mac OS X x86 (64-bit) (November 11, 2008)
# Date: Fri 18 Mar 2011 18:40:51

# Modified by F. Demartin in order to include loop Higgs EFT
# Dec 2013


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import couplings as C
import lorentz as L

# ======================================================================
# QCD base vertices
# ======================================================================

V_3 = Vertex(name = 'V_3',
              particles = [ P.G, P.G, P.G ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_4})
              
V_4 = Vertex(name = 'V_4',
              particles = [ P.G, P.G, P.G, P.G ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_6,(0,0):C.GC_6,(2,2):C.GC_6})

V_24 = Vertex(name = 'V_24',
              particles = [ P.d__tilde__, P.d, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_49 = Vertex(name = 'V_49',
               particles = [ P.u__tilde__, P.u, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_25 = Vertex(name = 'V_25',
              particles = [ P.s__tilde__, P.s, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_50 = Vertex(name = 'V_50',
               particles = [ P.c__tilde__, P.c, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.b, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})


V_51 = Vertex(name = 'V_51',
               particles = [ P.t__tilde__, P.t, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

# QCD ghost
V_Ggh = Vertex(name = 'V_Ggh',
               particles = [ P.gh__tilde__, P.gh, P.G ],
               color = [ 'f(2,3,1)' ],
               lorentz = [ L.GHGHG ],
               couplings = {(0,0):C.GC_4})

# ======================================================================
# Non-QCD base vertices
# ======================================================================


V_5 = Vertex(name = 'V_5',
             particles = [ P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_25})

V_8 = Vertex(name = 'V_8',
             particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_27})

V_9 = Vertex(name = 'V_9',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_7})

V_10 = Vertex(name = 'V_10',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_8})

V_11 = Vertex(name = 'V_11',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_26})

V_14 = Vertex(name = 'V_14',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_9})

V_15 = Vertex(name = 'V_15',
              particles = [ P.d__tilde__, P.d, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_16 = Vertex(name = 'V_16',
              particles = [ P.s__tilde__, P.s, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_17 = Vertex(name = 'V_17',
              particles = [ P.b__tilde__, P.b, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_18 = Vertex(name = 'V_18',
              particles = [ P.e__plus__, P.e__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_19 = Vertex(name = 'V_19',
              particles = [ P.m__plus__, P.m__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_20 = Vertex(name = 'V_20',
              particles = [ P.tt__plus__, P.tt__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_21 = Vertex(name = 'V_21',
              particles = [ P.u__tilde__, P.u, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_22 = Vertex(name = 'V_22',
              particles = [ P.c__tilde__, P.c, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_23 = Vertex(name = 'V_23',
              particles = [ P.t__tilde__, P.t, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_28 = Vertex(name = 'V_28',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_23})

V_29 = Vertex(name = 'V_29',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_23})

V_30 = Vertex(name = 'V_30',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_23})

V_31 = Vertex(name = 'V_31',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_12})

V_32 = Vertex(name = 'V_32',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_15})

V_33 = Vertex(name = 'V_33',
              particles = [ P.d__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_18})

V_34 = Vertex(name = 'V_34',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_13})

V_35 = Vertex(name = 'V_35',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_16})

V_36 = Vertex(name = 'V_36',
              particles = [ P.s__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_19})

V_37 = Vertex(name = 'V_37',
              particles = [ P.b__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_14})

V_38 = Vertex(name = 'V_38',
              particles = [ P.b__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_17})

V_39 = Vertex(name = 'V_39',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_20})

V_40 = Vertex(name = 'V_40',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_39})

V_41 = Vertex(name = 'V_41',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_42 = Vertex(name = 'V_42',
              particles = [ P.t__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_45})

V_43 = Vertex(name = 'V_43',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_40})

V_44 = Vertex(name = 'V_44',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_43})

V_45 = Vertex(name = 'V_45',
              particles = [ P.t__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_46})

V_46 = Vertex(name = 'V_46',
              particles = [ P.u__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_41})

V_47 = Vertex(name = 'V_47',
              particles = [ P.c__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_44})

V_48 = Vertex(name = 'V_48',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_47})

V_57 = Vertex(name = 'V_57',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_24})

V_58 = Vertex(name = 'V_58',
              particles = [ P.m__plus__, P.m__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_24})

V_59 = Vertex(name = 'V_59',
              particles = [ P.tt__plus__, P.tt__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_24})

V_60 = Vertex(name = 'V_60',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_61 = Vertex(name = 'V_61',
              particles = [ P.m__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_62 = Vertex(name = 'V_62',
              particles = [ P.tt__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_63 = Vertex(name = 'V_63',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_64 = Vertex(name = 'V_64',
              particles = [ P.vm__tilde__, P.m__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_65 = Vertex(name = 'V_65',
              particles = [ P.vt__tilde__, P.tt__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_66 = Vertex(name = 'V_66',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_23})

V_67 = Vertex(name = 'V_67',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_23})

V_68 = Vertex(name = 'V_68',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_23})

V_69 = Vertex(name = 'V_69',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_28})

V_70 = Vertex(name = 'V_70',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_28})

V_71 = Vertex(name = 'V_71',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_28})









#**********************************************************#
# NEW 
# X0 vertices       
#**********************************************************#

V_3001 = Vertex(name = 'V_3001',
                particles = [ P.A, P.A, P.X0 ],
                color = [ '1' ],
                lorentz = [ L.VVS2, L.VVS10 ],
                couplings = {(0,0):C.GC_3001h,(0,1):C.GC_3001a})

V_3002 = Vertex(name = 'V_3002',
                particles = [ P.G, P.G, P.X0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2, L.VVS10 ],
                couplings = {(0,0):C.GC_3002h,(0,1):C.GC_3002a})

V_3003 = Vertex(name = 'V_3003',
                particles = [ P.G, P.G, P.G, P.X0 ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVVS1, L.VVVS2 ],
                couplings = {(0,0):C.GC_3003h,(0,1):C.GC_3003a})

V_3004 = Vertex(name = 'V_3004',
                particles = [ P.G, P.G, P.G, P.G, P.X0 ],
                color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
                lorentz = [ L.VVVVS1, L.VVVVS2, L.VVVVS3 ],
                couplings = {(0,0):C.GC_3004h,(1,1):C.GC_3004h,(2,2):C.GC_3004h})

V_3005 = Vertex(name = 'V_3005',
                particles = [ P.W__minus__, P.W__plus__, P.X0 ],
                color = [ '1' ],
                lorentz = [ L.VVS10, L.VVS1, L.VVS11, L.VVS2, L.VVS12 ],
                couplings = {(0,0):C.GC_3005a,(0,1):C.GC_3005h1,(0,2):C.GC_3005h2,(0,3):C.GC_3005h3,(0,4):C.GC_3005h4})

V_3006 = Vertex(name = 'V_3006',
                particles = [ P.A, P.Z, P.X0 ],
                color = [ '1' ],
                lorentz = [ L.VVS10, L.VVS11, L.VVS2 ],
                couplings = {(0,0):C.GC_3006a,(0,1):C.GC_3006h1,(0,2):C.GC_3006h2})

V_3007 = Vertex(name = 'V_3007',
                particles = [ P.Z, P.Z, P.X0 ],
                color = [ '1' ],
                lorentz = [ L.VVS10, L.VVS1, L.VVS2, L.VVS13 ],
                couplings = {(0,0):C.GC_3007a,(0,1):C.GC_3007h1,(0,2):C.GC_3007h2,(0,3):C.GC_3007h3})

V_3008 = Vertex(name = 'V_3008',
                particles = [ P.tt__plus__, P.tt__minus__, P.X0 ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS5 ],
                couplings = {(0,0):C.GC_3008h,(0,1):C.GC_3008a})

V_3009 = Vertex(name = 'V_3009',
                particles = [ P.b__tilde__, P.b, P.X0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1, L.FFS5 ],
                couplings = {(0,0):C.GC_3009h,(0,1):C.GC_3009a})

V_3010 = Vertex(name = 'V_3010',
                particles = [ P.t__tilde__, P.t, P.X0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1, L.FFS5 ],
                couplings = {(0,0):C.GC_3010h,(0,1):C.GC_3010a})

V_3011 = Vertex(name = 'V_3011',
                particles = [ P.m__plus__, P.m__minus__, P.X0 ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS5 ],
                couplings = {(0,0):C.GC_3011h,(0,1):C.GC_3011a})

V_3012 = Vertex(name = 'V_3012',
                particles = [ P.c__tilde__, P.c, P.X0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1, L.FFS5 ],
                couplings = {(0,0):C.GC_3012h,(0,1):C.GC_3012a})

