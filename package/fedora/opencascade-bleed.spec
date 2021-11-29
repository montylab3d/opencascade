Name:           opencascade
Version:        {{{git_last_tag}}}.bleed^{{{git_last_tag_commits}}}.{{{git_head_short}}}
Release:        1%{?dist}
Summary:        SDK intended for development of applications dealing with 3D CAD data

License:        LGPLv2+ with exception
URL:            https://github.com/montylab3d/opencascade
# Upstream requires a login to download sources. 
# No longer any direct-access download link.
Source0:        {{{git_repo_pack}}}
Source1:        opencascade/package/fedora/DRAWEXE.1
Source2:        opencascade/package/fedora/opencascade-draw.desktop
Source3:        opencascade/package/fedora/occ-256.png
Source4:        opencascade/package/fedora/occ-128.png
Source5:        opencascade/package/fedora/occ-64.png
Source6:        opencascade/package/fedora/occ-48.png

Patch0:         opencascade/package/fedora/opencascade-cmake.patch


# Utilities
BuildRequires:  cmake gcc gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
# Libraries
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXpm-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXres-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXi-devel
BuildRequires:  libXv-devel
BuildRequires:  mesa-libGL-devel mesa-libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  ftgl-devel
BuildRequires:  freeimage-devel
BuildRequires:  gl2ps-devel
BuildRequires:  libgomp
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  tbb-devel
BuildRequires:  vtk-devel


%description
Open CASCADE Technology (OCCT) is a suite for 3D surface and solid
modeling, visualization, data exchange and rapid application development. It
is an excellent platform for development of numerical simulation software
including CAD/CAM/CAE, AEC and GIS, as well as PDM applications.


%package foundation
Summary:        OpenCASCADE CAE platform shared libraries

%description foundation
OpenCASCADE CAE platform shared libraries

This package contains foundation classes which provide a variety of
general-purpose services such as automated management of heap memory,
exception handling, classes for manipulating aggregates of data, basic
math tools.


%package modeling
Summary:        OpenCASCADE CAE platform shared libraries

%description modeling
OpenCASCADE CAE platform shared libraries

This package supplies data structures to represent 2D and 3D geometric models,
as well as topological and geometrical algorithms.


%package ocaf
Summary:        OpenCASCADE CAE platform shared libraries

%description ocaf
OpenCASCADE CAE platform shared libraries

This package provides OpenCASCADE Application Framework services and
support for data exchange.


%package visualization
Summary:        OpenCASCADE CAE platform shared libraries

%description visualization
OpenCASCADE CAE platform shared libraries

This package provides services for displaying 2D and 3D graphics.


%package examples
Summary:        OpenCASCADE CAE platform shared libraries

%description examples
OpenCASCADE CAE platform shared libraries

This package contains example input files for OpenCASCADE in various formats.


%package draw
Summary:        OpenCASCADE CAE platform shared libraries

%description draw
OpenCASCADE CAE DRAW test harness.


%package devel
Summary:        OpenCASCADE CAE platform library development files
Requires:       %{name}-draw%{?_isa} = %{version}-%{release}
Requires:       %{name}-foundation%{?_isa} = %{version}-%{release}
Requires:       %{name}-modeling%{?_isa} = %{version}-%{release}
Requires:       %{name}-ocaf%{?_isa} = %{version}-%{release}
Requires:       %{name}-visualization%{?_isa} = %{version}-%{release}
Requires:       freeimage-devel
Requires:       freetype-devel
Requires:       gl2ps-devel
Requires:       libICE-devel
Requires:       libSM-devel
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libXScrnSaver-devel
Requires:       libXrandr-devel
Requires:       libXpm-devel
Requires:       libxkbfile-devel
Requires:       libXinerama-devel
Requires:       libXres-devel
Requires:       libXtst-devel
Requires:       libXcomposite-devel
Requires:       libXcursor-devel
Requires:       libXdmcp-devel
Requires:       libXi-devel
Requires:       libXv-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       tbb-devel
Requires:       tcl-devel
Requires:       tk-devel

%description devel
OpenCASCADE CAE platform library development files


%prep
%autosetup -p1 -n opencascade

# Sources are marked executable for no good reason...
find ./src -type f -exec chmod -x {} \;

# Fix executable set on text files.
chmod 0644 *.txt


%build
# opencascade does some manual install trickery that does not respect DESTDIR.
# Make DESTDIR an environment variable that can be passed into the CMake config.
export DESTDIR="%{buildroot}"

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_TBB=True \
       -DUSE_VTK=True \
	   -DINSTALL_VTK=False \
	   -D3RDPARTY_VTK_LIBRARY_DIR=%{_libdir} \
	   -D3RDPARTY_VTK_INCLUDE_DIR=%{_includedir} \
       -DINSTALL_DIR_LIB=%{_lib} \
       -DINSTALL_DIR_CMAKE=%{_lib}/cmake/%{name} 

%cmake_build


%install
%cmake_install

# Draw binary should not be versioned.
mv %{buildroot}%{_bindir}/DRAWEXE-7.* \
   %{buildroot}%{_bindir}/DRAWEXE

# Install manpage for DRAWEXE
install -Dm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/DRAWEXE.1

# Install and validate desktop file
desktop-file-install                           \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE2}

# Install icons
for size in 256 128 64 48; do
    icon=%{_sourcedir}/occ-${size}.png
    install -Dm 0644 $icon \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/occ.png
done

# Remove license files so they can be included by %%license.
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE_LGPL_21.txt,OCCT_LGPL_EXCEPTION.txt}

# Fix non-executable shell scripts
chmod 0755 %{buildroot}%{_bindir}/*.sh


%files foundation
%doc README.txt
%license LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt
# Foundation
%{_libdir}/libTKernel.so.*
%{_libdir}/libTKMath.so.*
%{_datadir}/opencascade/

%files modeling
# Modeling Data
%{_libdir}/libTKG2d.so.*
%{_libdir}/libTKG3d.so.*
%{_libdir}/libTKGeomBase.so.*
%{_libdir}/libTKBRep.so.*
# Modeling Algorithms
%{_libdir}/libTKGeomAlgo.so.*
%{_libdir}/libTKTopAlgo.so.*
%{_libdir}/libTKPrim.so.*
%{_libdir}/libTKBO.so.*
%{_libdir}/libTKBool.so.*
%{_libdir}/libTKHLR.so.*
%{_libdir}/libTKFillet.so.*
%{_libdir}/libTKOffset.so.*
%{_libdir}/libTKFeat.so.*
%{_libdir}/libTKMesh.so.*
%{_libdir}/libTKXMesh.so.*
%{_libdir}/libTKShHealing.so.*
# Data exchange
%{_libdir}/libTKXSBase.so.*
%{_libdir}/libTKSTEPBase.so.*
%{_libdir}/libTKSTEPAttr.so.*
%{_libdir}/libTKSTEP209.so.*
%{_libdir}/libTKSTEP.so.*
%{_libdir}/libTKIGES.so.*
%{_libdir}/libTKXCAF.so.*
%{_libdir}/libTKXDEIGES.so.*
%{_libdir}/libTKXDESTEP.so.*
%{_libdir}/libTKSTL.so.*
%{_libdir}/libTKVRML.so.*
%{_libdir}/libTKXmlXCAF.so.*
%{_libdir}/libTKBinXCAF.so.*
%{_libdir}/libTKRWMesh.so.*

%files visualization
# Visualization Dependents
%{_libdir}/libTKService.so.*
%{_libdir}/libTKV3d.so.*
# Visualization
%{_libdir}/libTKOpenGl.so.*
%{_libdir}/libTKOpenGlTest.so.*
%{_libdir}/libTKMeshVS.so.*
%{_libdir}/libTKIVtk.so.*

%files ocaf
# Application framework
%{_libdir}/libTKCDF.so.*
%{_libdir}/libTKLCAF.so.*
%{_libdir}/libTKCAF.so.*
%{_libdir}/libTKBinL.so.*
%{_libdir}/libTKXmlL.so.*
%{_libdir}/libTKBin.so.*
%{_libdir}/libTKXml.so.*
%{_libdir}/libTKStdL.so.*
%{_libdir}/libTKStd.so.*
%{_libdir}/libTKTObj.so.*
%{_libdir}/libTKBinTObj.so.*
%{_libdir}/libTKXmlTObj.so.*
%{_libdir}/libTKVCAF.so.*

%files draw
# Draw Libraries
%{_libdir}/libTKDraw.so.*
%{_libdir}/libTKIVtkDraw.so.*
%{_libdir}/libTKQADraw.so.*
%{_libdir}/libTKTopTest.so.*
%{_libdir}/libTKViewerTest.so.*
%{_libdir}/libTKXSDRAW.so.*
%{_libdir}/libTKDCAF.so.*
%{_libdir}/libTKXDEDRAW.so.*
%{_libdir}/libTKTObjDRAW.so.*
# DRAWEXE application
%{_bindir}/DRAWEXE
%{_mandir}/man1/DRAWEXE.1.gz
%{_datadir}/applications/opencascade-draw.desktop
%{_datadir}/icons/hicolor/*/apps/*

%files devel
%{_bindir}/*.sh
%{_includedir}/opencascade
%{_libdir}/*.so
%{_libdir}/cmake/opencascade/*.cmake


%changelog
* Sun Nov 21 2021 Monty <xiphmont@gmail.com> - 7.6.0-0
- Update to 7.6.0.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 31 2021 Orion Poplawski <orion@nwra.com> - 7.5.0-3
- Rebuild for VTK 9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Richard Shaw <hobbes1069@gmail.com> - 7.5.0-1
- Update to 7.5.0.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Richard Shaw <hobbes1069@gmail.com> - 7.4.0-2
- Update per reviewer requests.

* Mon Oct 21 2019 Richard Shaw <hobbes1069@gmail.com> - 7.4.0-1
- Initial Packaging.
