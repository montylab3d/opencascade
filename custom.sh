#!/bin/bash
#
# Mandatory 3rd-parties switches
export HAVE_FREETYPE=true
export HAVE_FTGL=true
export HAVE_TCLTK=true
# Optional 3rd-parties switches
export HAVE_FREEIMAGE=true
export HAVE_GL2PS=true
export HAVE_TBB=true
export HAVE_OPENCL=no
export HAVE_QT=no
export HAVE_VTK=true
#
export CSF_OPT_INC="/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/VTK-6.1.0-new/include/vtk-6.1:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/tbb42_20140416oss/include:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/freeimage-3.17.0/include:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/gl2ps-1.3.8/include:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/freetype-2.5.5/include:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/freetype-2.5.5/include/freetype2:/dn47/SALOME/PRODUCTS/7x/opt/DEBIAN.7.0.64/7.3.0/tcltk-8.6.0/include:/dn47/SALOME/PRODUCTS/7x/opt/DEBIAN.7.0.64/7.3.0/tcltk-8.6.0/include:"
export CSF_OPT_LIB64="/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/VTK-6.1.0-new/lib/:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/tbb42_20140416oss/lib/intel64/gcc4.4:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/freeimage-3.17.0/lib:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/gl2ps-1.3.8/lib:/dn29/PRODUCTS/maintenance/opencascade-6.7.1/Debian80-64/freetype-2.5.5/lib:/dn47/SALOME/PRODUCTS/7x/opt/DEBIAN.7.0.64/7.3.0/tcltk-8.6.0/lib:/dn47/SALOME/PRODUCTS/7x/opt/DEBIAN.7.0.64/7.3.0/tcltk-8.6.0/lib:"
export CSF_OPT_BIN64=""
export CSF_OPT_INC="/dn63/LocalWOK/wok_entities/LOC/dev/IR-2016-03-03-IR-2016-03-03-occt-64/inc:${CSF_OPT_INC}"
export CSF_OPT_LIB64="/dn63/LocalWOK/wok_entities/LOC/dev/IR-2016-03-03-IR-2016-03-03-occt-64/lib:${CSF_OPT_LIB64}"
export CSF_OPT_BIN64="/dn63/LocalWOK/wok_entities/LOC/dev/IR-2016-03-03-IR-2016-03-03-occt-64/bin"
