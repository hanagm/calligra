#define karbon 0
#define krita 0
#define freoffice 0
#define kexi 0

Name: calligra
Version: 2.7.8+afae6db
Release: 1%{?dist}
Group: Applications/Productivity
URL: http://www.calligra.org/
Source0: %{name}-%{version}.tar.gz
Summary: Calligra Suite
License: Open
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: boost-devel
BuildRequires: pkgconfig(libgsf-1)
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(eigen2)
BuildRequires: pkgconfig(openssl)
BuildRequires: calligra-extra-cmake-modules
%if 0%{?krita}
BuildRequires: pkgconfig(lcms)
BuildRequires: exiv2-devel giflib-devel
%endif
%if 0%{?karbon}
BuildRequires: pkgconfig(poppler-qt4)
BuildRequires: pkgconfig(fontconfig)
%endif
%if 0%{?kexi}
BuildRequires: pkgconfig(sqlite3)
%endif

Requires: %{name}-words-core
Requires: %{name}-sheets-core
Requires: %{name}-stage-core
%if 0%{?krita}
Requires: %{name}-krita
%endif
%if 0%{?karbon}
Requires: %{name}-karbon
%endif
%if 0%{?kexi}
Requires: %{name}-kexi
%endif

%define calligra_runtime_requires %{name}-plugins %{name}-data oxygen-icon-theme

#%define datadir %{_datadir}

%description
%{summary}.

# %package words
# Summary: Calligra Words application
# Requires: %{name}-words-core = %{version}-%{release}
# #Requires: %{name}-words-plugins = %{version}-%{release}
# Requires: %{name}-words-templates = %{version}-%{release}
# Requires: %{name}-words-filters = %{version}-%{release}
# Requires: %{calligra_runtime_requires}
#
# %description words
# %{summary}.

%package words-core
Summary: Calligra Words libraries
Group: Development/Libraries
Requires: %{name}-plugins %{name}-data

%description words-core
%{summary}.

%post words-core
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun words-core -p  /sbin/ldconfig

%package words-templates
Summary: Calligra Words templates

%description words-templates
%{summary}.

#%package words-plugins
#Summary: Calligra Words plugins
#Group: Development/Libraries

#%description words-plugins
#%{summary}.

# %package sheets
# Summary: Calligra Sheets application
# Requires: %{name}-sheets-core = %{version}-%{release}
# Requires: %{name}-sheets-plugins = %{version}-%{release}
# Requires: %{name}-sheets-filters = %{version}-%{release}
# Requires: %{name}-sheets-templates = %{version}-%{release}
# Requires: %{calligra_runtime_requires}
#
# %description sheets
# %{summary}.

%package sheets-core
Summary: Calligra Sheets libraries
Group: Development/Libraries
Requires: %{name}-sheets-core-plugins = %{version}-%{release}
Requires: %{name}-plugins %{name}-data

%description sheets-core
%{summary}.

%post sheets-core
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun sheets-core -p  /sbin/ldconfig

%package sheets-templates
Summary: Calligra Sheets templates

%description sheets-templates
%{summary}.

%package sheets-plugins
Summary: Calligra Sheets plugins
Group: Development/Libraries

%description sheets-plugins
%{summary}.
Non-essential sheets specific plugins.

%post sheets-plugins
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%package sheets-core-plugins
Summary: Calligra Sheets core plugins
Group: Development/Libraries

%description sheets-core-plugins
%{summary}.
Plugins that add support for all the default functions in sheets.

%post sheets-core-plugins
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

# %package stage
# Summary: Calligra Stage application
# Requires: %{name}-stage-core = %{version}-%{release}
# Requires: %{name}-stage-plugins = %{version}-%{release}
# Requires: %{name}-stage-filters = %{version}-%{release}
# Requires: %{name}-stage-templates = %{version}-%{release}
# Requires: %{calligra_runtime_requires}
#
# %description stage
# %{summary}.

%package stage-core
Summary: Calligra Stage libraries
Group: Development/Libraries
Requires: %{name}-plugins %{name}-data

%description stage-core
%{summary}.

%post stage-core
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun stage-core -p  /sbin/ldconfig

%package stage-templates
Summary: Calligra Stage templates

%description stage-templates
%{summary}.

%package stage-plugins
Summary: Calligra Stage libraries
Group: Development/Libraries

%description stage-plugins
%{summary}.

%post stage-plugins
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%if 0%{?krita}
%package krita
Summary: Calligra Krita application
Requires: %{name}-krita-data = %{version}-%{release}
Requires: %{name}-krita-plugins = %{version}-%{release}
Requires: %{name}-krita-filters = %{version}-%{release}
Requires: %{calligra_runtime_requires}

%description krita
%{summary}.

%post krita
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun krita -p  /sbin/ldconfig

%package krita-filters
Summary: Calligra Krita import export filters

%description krita-filters
%{summary}.

%package krita-plugins
Summary: Calligra Krita plugins

%description krita-plugins
%{summary}.

%package krita-data
Summary: Calligra Krita data

%description krita-data
%{summary}.
%endif

%if 0%{?karbon}
%package karbon
Summary: Calligra Karbon application
Requires: %{name}-karbon-data = %{version}-%{release}
Requires: %{name}-karbon-plugins = %{version}-%{release}
Requires: %{name}-karbon-filters = %{version}-%{release}
Requires: %{name}-karbon-templates = %{version}-%{release}
Requires: %{calligra_runtime_requires}

%description karbon
%{summary}.

%post karbon
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun karbon -p  /sbin/ldconfig

%package karbon-plugins
Summary: Calligra Karbon application plugins

%description karbon-plugins
%{summary}.

%package karbon-filters
Summary: Calligra Karbon application filters

%description karbon-filters
%{summary}.

%package karbon-data
Summary: Calligra Karbon application data

%description karbon-data
%{summary}.

%package karbon-templates
Summary: Calligra Karbon application templates

%description karbon-templates
%{summary}.
%endif

%if 0%{?kexi}
%package kexi
Summary: Calligra Kexi application

%description kexi
%{summary}.

%post kexi
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun kexi -p  /sbin/ldconfig
%endif

%package kthesaurus
Summary: Calligra thesaurus application

%description kthesaurus
%{summary}.

%if 0%{?freoffice}
%package mobile
Summary: Calligra FreOffice application
Requires: %{name}-words-core = %{version}-%{release}
Requires: %{name}-sheets-core = %{version}-%{release}
Requires: %{name}-stage-core = %{version}-%{release}
Requires: %{name}-words-filters = %{version}-%{release}
Requires: %{name}-sheets-filters = %{version}-%{release}
Requires: %{name}-stage-filters = %{version}-%{release}
Requires: %{name}-plugins = %{version}-%{release}
#Requires: kdelibs-runtime-core

%description mobile
%{summary}.

%post mobile
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun mobile -p  /sbin/ldconfig
%endif

%package libs
Summary: Shared Calligra libraries
Group: Development/Libraries

%description libs
%{summary}.

%post libs
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun libs -p  /sbin/ldconfig

%package components
Summary: Qt Quick components for showing documents using Calligra
Group: Development/Libraries

%description components
%{summary}.

%package filters
Summary: Calligra input/output filters
Requires: %{name}-words-filters = %{version}-%{release}
Requires: %{name}-sheets-filters = %{version}-%{release}
Requires: %{name}-stage-filters = %{version}-%{release}

%description filters
%{summary}.

%post filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%package filters-libs
Summary: Calligra input/output filters shared libraries

%description filters-libs
%{summary}.

%post filters-libs
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun filters-libs -p  /sbin/ldconfig

%package words-filters
Summary: Calligra Words input/output filters

%description words-filters
%{summary}.

%post words-filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun words-filters -p  /sbin/ldconfig

%package sheets-filters
Summary: Calligra Sheets input/output filters

%description sheets-filters
%{summary}.

%post sheets-filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

#%postun sheets-filters -p  /sbin/ldconfig

%package stage-filters
Summary: Calligra Stage input/output filters

%description stage-filters
%{summary}.

%post stage-filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

#%postun stage-filters -p  /sbin/ldconfig

%package plugins
Summary: Calligra plugins

%description plugins
%{summary}.

%post plugins
/sbin/ldconfig
KDESYCOCA=/usr/share/kde5/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun plugins -p  /sbin/ldconfig

%package data
Summary: Calligra shared data

%description data
%{summary}.

%package konqi-servicemenus
Summary: Calligra Konqueror service menus

%description konqi-servicemenus
%{summary}.

%package devel
Summary: Calligra development files
Group: Development/Libraries

%description devel
%{summary}.

%files
%defattr(-,root,root,-)

# %files words
# %defattr(-,root,root,-)
# %{_libdir}/libkdeinit4_words.so
# %{_bindir}/words

# %{_datadir}/applications/kde5/words.desktop
# %{_datadir}/config/wordsrc
# %{_datadir}/words/styles/defaultstyles.xml
# %{_datadir}/words/words.rc
# %{_datadir}/words/words_readonly.rc

%files words-core
%defattr(-,root,root,-)
%{_datadir}/kde5/services/wordspart.desktop
%{_libdir}/libwordsprivate.so.*
%{_libdir}/calligra/wordspart.so
/usr/etc/xdg/wordsrc
%{_datadir}/words/styles/defaultstyles.xml
%{_datadir}/words/words.rc
%{_datadir}/words/words_readonly.rc

#%{_datadir}/kde5/services/words_docx_thumbnail.desktop
#%{_datadir}/kde5/services/words_msword_thumbnail.desktop
#%{_datadir}/kde5/services/words_rtf_thumbnail.desktop

%files words-templates
%defattr(-,root,root,-)
%{_datadir}/words/templates
%{_datadir}/words/icons/hicolor/48x48/actions/template_*.png
%{_datadir}/words/icons/hicolor/128x128/actions/template_*.png
%{_datadir}/words/icons/hicolor/scalable/actions/template_*.svgz

#%files words-plugins
#%defattr(-,root,root,-)

# %files sheets
# %defattr(-,root,root,-)
# %{_libdir}/libkdeinit4_calligrasheets.so
# %{_bindir}/calligrasheets

# %{_datadir}/applications/kde5/sheets.desktop
# %{_datadir}/config/sheetsrc
# %{_datadir}/config.kcfg/sheets.kcfg
# %{_datadir}/sheets/sheetstyles
# %{_datadir}/sheets/sheets.notifyrc
# %{_datadir}/sheets/sheets.rc
# %{_datadir}/sheets/sheets_readonly.rc
# %{_datadir}/sheets/icons/hicolor/16x16
# %{_datadir}/sheets/icons/hicolor/22x22
# %{_datadir}/sheets/icons/hicolor/32x32
# %{_datadir}/sheets/dtd/kspread.dtd

%files sheets-core
%defattr(-,root,root,-)
%{_datadir}/kde5/services/sheetspart.desktop
%{_libdir}/calligra/calligrasheetspart.so
%{_libdir}/libcalligrasheetsodf.so.*
%{_libdir}/libcalligrasheetscommon.so.*
%{_libdir}/calligra/calligra_shape_spreadsheet.so
%{_libdir}/calligra/calligra_shape_spreadsheet-deferred.so
%{_datadir}/kde5/servicetypes/sheets_plugin.desktop
%{_datadir}/kde5/servicetypes/sheets_viewplugin.desktop
%{_datadir}/kde5/services/calligra_shape_spreadsheet-deferred.desktop
/usr/etc/xdg/sheetsrc
%{_datadir}/config.kcfg/sheets.kcfg
%{_datadir}/sheets/CellToolOptionWidgets.xml
%{_datadir}/sheets/sheetstyles
%{_datadir}/sheets/sheets.rc
%{_datadir}/sheets/sheets_readonly.rc
%{_datadir}/sheets/icons/hicolor/16x16
%{_datadir}/sheets/icons/hicolor/22x22
%{_datadir}/sheets/icons/hicolor/32x32
%{_datadir}/sheets/dtd/kspread.dtd

%files sheets-templates
%defattr(-,root,root,-)
%{_datadir}/sheets/templates
%{_datadir}/sheets/icons/hicolor/48x48/actions/template_*.png
%{_datadir}/sheets/icons/hicolor/scalable/actions/template_*.svgz

%files sheets-core-plugins
%defattr(-,root,root,-)
#%{_libdir}/calligra/sheetssolver.so
#%{_datadir}/kde5/services/sheetssolver.desktop
#%{_datadir}/sheets/viewplugins/solver.rc

# %{_datadir}/kde5/services/kspreadmathmodule.desktop
# %{_datadir}/sheets/functions/math.xml
# %{_libdir}/kde5/kspreadmathmodule.so
#
# %{_datadir}/kde5/services/kspreadreferencemodule.desktop
# %{_datadir}/sheets/functions/reference.xml
# %{_libdir}/kde5/kspreadreferencemodule.so
#
# %{_datadir}/kde5/services/kspreadstatisticalmodule.desktop
# %{_datadir}/sheets/functions/statistical.xml
# %{_libdir}/kde5/kspreadstatisticalmodule.so
#
# %{_datadir}/kde5/services/kspreadtextmodule.desktop
# %{_datadir}/sheets/functions/text.xml
# %{_libdir}/kde5/kspreadtextmodule.so
#
# %{_datadir}/kde5/services/kspreadtrigonometrymodule.desktop
# %{_datadir}/sheets/functions/trig.xml
# %{_libdir}/kde5/kspreadtrigonometrymodule.so
#
# %{_datadir}/kde5/services/kspreadbitopsmodule.desktop
# %{_datadir}/sheets/functions/bitops.xml
# %{_libdir}/kde5/kspreadbitopsmodule.so
#
# %{_datadir}/kde5/services/kspreadconversionmodule.desktop
# %{_datadir}/sheets/functions/conversion.xml
# %{_libdir}/kde5/kspreadconversionmodule.so
#
# %{_datadir}/kde5/services/kspreaddatabasemodule.desktop
# %{_datadir}/sheets/functions/database.xml
# %{_libdir}/kde5/kspreaddatabasemodule.so
#
# %{_datadir}/kde5/services/kspreaddatetimemodule.desktop
# %{_datadir}/sheets/functions/datetime.xml
# %{_libdir}/kde5/kspreaddatetimemodule.so
#
# %{_datadir}/kde5/services/kspreadengineeringmodule.desktop
# %{_datadir}/sheets/functions/engineering.xml
# %{_libdir}/kde5/kspreadengineeringmodule.so
#
# %{_datadir}/kde5/services/kspreadfinancialmodule.desktop
# %{_datadir}/sheets/functions/financial.xml
# %{_libdir}/kde5/kspreadfinancialmodule.so
#
# %{_datadir}/kde5/services/kspreadinformationmodule.desktop
# %{_datadir}/sheets/functions/information.xml
# %{_libdir}/kde5/kspreadinformationmodule.so
#
# %{_datadir}/kde5/services/kspreadlogicmodule.desktop
# %{_datadir}/sheets/functions/logic.xml
# %{_libdir}/kde5/kspreadlogicmodule.so

%files sheets-plugins
%defattr(-,root,root,-)
#%{_datadir}/kde5/services/kspread_plugin_tool_calendar.desktop
#%{_libdir}/kde5/kspread_plugin_tool_calendar.so

# %files stage
# %defattr(-,root,root,-)
# %{_libdir}/libkdeinit4_kpresenter.so
# %{_bindir}/kpresenter
# %{_datadir}/applications/kde5/kpresenter.desktop
# %{_datadir}/config/kpresenterrc
# %{_datadir}/stage/pics
# %{_datadir}/stage/styles/defaultstyles.xml
# %{_datadir}/stage/stage.rc
# %{_datadir}/stage/stage_readonly.rc
# %{_datadir}/stage/icons/hicolor/64x64

%files stage-core
%defattr(-,root,root,-)
%{_datadir}/kde5/services/stagepart.desktop
%{_libdir}/calligra/calligrastagepart.so
%{_libdir}/libcalligrastageprivate.so.*
%{_datadir}/kde5/servicetypes/presentationeventaction.desktop
%{_datadir}/kde5/servicetypes/kpr_pageeffect.desktop
%{_datadir}/kde5/servicetypes/kpr_shapeanimation.desktop
/usr/etc/xdg/stagerc
%{_datadir}/stage/animations/animations.xml
%{_datadir}/stage/pics
%{_datadir}/stage/icons
%{_datadir}/stage/styles/defaultstyles.xml
%{_datadir}/stage/stage.rc
%{_datadir}/stage/stage_readonly.rc

#%{_datadir}/kde5/services/stage_kpr_thumbnail.desktop
#%{_datadir}/kde5/services/stage_powerpoint_thumbnail.desktop
#%{_datadir}/kde5/services/stage_pptx_thumbnail.desktop

%files stage-templates
%defattr(-,root,root,-)
%{_datadir}/stage/templates
%{_datadir}/stage/icons/hicolor/48x48/actions/template_*.png
%{_datadir}/stage/icons/hicolor/scalable/actions/template_*.svgz

%files stage-plugins
%defattr(-,root,root,-)
%{_datadir}/kde5/services/calligrastagetoolanimation.desktop
%{_datadir}/kde5/services/kprvariables.desktop
%{_datadir}/kde5/services/calligrastageeventactions.desktop
%{_datadir}/kde5/services/kpr_pageeffect_barwipe.desktop
%{_datadir}/kde5/services/kpr_pageeffect_clockwipe.desktop
%{_datadir}/kde5/services/kpr_pageeffect_edgewipe.desktop
%{_datadir}/kde5/services/kpr_pageeffect_fade.desktop
%{_datadir}/kde5/services/kpr_pageeffect_iriswipe.desktop
%{_datadir}/kde5/services/kpr_pageeffect_matrixwipe.desktop
%{_datadir}/kde5/services/kpr_pageeffect_slidewipe.desktop
%{_datadir}/kde5/services/kpr_pageeffect_spacerotation.desktop
%{_datadir}/kde5/services/kpr_pageeffect_swapeffect.desktop
%{_datadir}/kde5/services/kpr_shapeanimation_example.desktop
%{_libdir}/calligra/kpr_pageeffect_barwipe.so
%{_libdir}/calligra/kpr_pageeffect_clockwipe.so
%{_libdir}/calligra/kpr_pageeffect_edgewipe.so
%{_libdir}/calligra/kpr_pageeffect_fade.so
%{_libdir}/calligra/kpr_pageeffect_iriswipe.so
%{_libdir}/calligra/kpr_pageeffect_matrixwipe.so
%{_libdir}/calligra/kpr_pageeffect_slidewipe.so
%{_libdir}/calligra/kpr_pageeffect_spacerotation.so
%{_libdir}/calligra/kpr_pageeffect_swapeffect.so
%{_libdir}/calligra/kpr_shapeanimation_example.so
%{_libdir}/calligra/calligrastageeventactions.so
%{_libdir}/calligra/calligrastagetoolanimation.so
%{_libdir}/calligra/kprvariables.so

%if 0%{?krita}
%files krita
%defattr(-,root,root,-)
%{_bindir}/krita
%{_libdir}/kde5/kritapart.so
%{_libdir}/libkdeinit4_krita.so
%{_libdir}/libkritaimage.so.*
%{_libdir}/libkritalibbrush.so.*
%{_libdir}/libkritalibpaintop.so.*
%{_libdir}/libkritaui.so.*
%{_datadir}/applications/kde5/krita.desktop
%{_datadir}/krita/krita.rc
%{_datadir}/krita/krita_readonly.rc
%{_datadir}/config/krita.knsrc
%{_datadir}/config/kritarc

%{_libdir}/kde5/kolcmsengine.so
%{_datadir}/color/icc/pigment/CMY.icm
%{_datadir}/color/icc/pigment/fogra27l.icm
%{_datadir}/kde5/services/kolcmsengine.desktop

%files krita-filters
%defattr(-,root,root,-)
%{_libdir}/kde5/kritabmpexport.so
%{_libdir}/kde5/kritabmpimport.so
%{_libdir}/kde5/kritagifimport.so
%{_libdir}/kde5/kritajpegexport.so
%{_libdir}/kde5/kritajpegimport.so
%{_libdir}/kde5/kritaoraexport.so
%{_libdir}/kde5/kritaoraimport.so
%{_libdir}/kde5/kritapngexport.so
%{_libdir}/kde5/kritapngimport.so
%{_libdir}/kde5/kritappmexport.so
%{_libdir}/kde5/kritappmimport.so
%{_libdir}/kde5/kritaxcfimport.so
%{_libdir}/kde5/kritaodgimport.so
%{_datadir}/applications/kde5/krita_bmp.desktop
%{_datadir}/applications/kde5/krita_gif.desktop
%{_datadir}/applications/kde5/krita_jpeg.desktop
%{_datadir}/applications/kde5/krita_ora.desktop
%{_datadir}/applications/kde5/krita_png.desktop
%{_datadir}/applications/kde5/krita_ppm.desktop
%{_datadir}/applications/kde5/krita_xcf.desktop
%{_datadir}/applications/kde5/krita_odg.desktop
%{_datadir}/kde5/services/krita_bmp_export.desktop
%{_datadir}/kde5/services/krita_bmp_import.desktop
%{_datadir}/kde5/services/krita_gif_import.desktop
%{_datadir}/kde5/services/krita_jpeg_export.desktop
%{_datadir}/kde5/services/krita_jpeg_import.desktop
%{_datadir}/kde5/services/krita_ora_export.desktop
%{_datadir}/kde5/services/krita_ora_import.desktop
%{_datadir}/kde5/services/krita_png_export.desktop
%{_datadir}/kde5/services/krita_png_import.desktop
%{_datadir}/kde5/services/krita_ppm_export.desktop
%{_datadir}/kde5/services/krita_ppm_import.desktop
%{_datadir}/kde5/services/krita_xcf_import.desktop
%{_datadir}/kde5/services/krita_odg_import.desktop

%files krita-plugins
%defattr(-,root,root,-)
%{_datadir}/kde5/servicetypes/krita_brush.desktop
%{_datadir}/kde5/servicetypes/krita_dock.desktop
%{_datadir}/kde5/servicetypes/krita_filter.desktop
%{_datadir}/kde5/servicetypes/krita_generator.desktop
%{_datadir}/kde5/servicetypes/krita_paintop.desktop
%{_datadir}/kde5/servicetypes/krita_plugin.desktop
%{_datadir}/kde5/servicetypes/krita_tool.desktop

%{_libdir}/kde5/krita_colorspaces_extensions.so
%{_libdir}/kde5/kritabackgrounds.so
%{_libdir}/kde5/kritabigbrother.so
%{_libdir}/kde5/kritablurfilter.so
#%{_libdir}/kde5/kritabracketing2hdr.so
%{_libdir}/kde5/kritabumpmap.so
%{_libdir}/kde5/kritachalkpaintop.so
%{_libdir}/kde5/kritacolorgenerator.so
%{_libdir}/kde5/kritacolorrange.so
%{_libdir}/kde5/kritacolorselectorng.so
%{_libdir}/kde5/kritacolorsfilters.so
%{_libdir}/kde5/kritacolorspaceconversion.so
%{_libdir}/kde5/kritacomplexbrush.so
%{_libdir}/kde5/kritaconvolutionfilters.so
%{_libdir}/kde5/kritacurvepaintop.so
%{_libdir}/kde5/kritadefaultdockers.so
%{_libdir}/kde5/kritadefaultpaintops.so
%{_libdir}/kde5/kritadefaulttools.so
%{_libdir}/kde5/kritadeformpaintop.so
%{_libdir}/kde5/kritadigitalmixer.so
%{_libdir}/kde5/kritadodgeburn.so
%{_libdir}/kde5/kritadropshadow.so
%{_libdir}/kde5/kritadynapaintop.so
%{_libdir}/kde5/kritaembossfilter.so
%{_libdir}/kde5/kritaexample.so
%{_libdir}/kde5/kritaextensioncolorsfilters.so
%{_libdir}/kde5/kritaextensionsmanager.so
%{_libdir}/kde5/kritafastcolortransferfilter.so
%{_libdir}/kde5/kritafilterop.so
%{_libdir}/kde5/kritagridpaintop.so
%{_libdir}/kde5/kritahairypaintop.so
%{_libdir}/kde5/kritahatchingpaintop.so
%{_libdir}/kde5/kritahistogram.so
%{_libdir}/kde5/kritaimageenhancement.so
%{_libdir}/kde5/kritaimagesize.so
%{_libdir}/kde5/kritalayercompose.so
%{_libdir}/kde5/kritalevelfilter.so
%{_libdir}/kde5/kritametadataeditor.so
%{_libdir}/kde5/kritamodifyselection.so
%{_libdir}/kde5/kritamypaintpaintop.so
%{_libdir}/kde5/kritanoisefilter.so
%{_libdir}/kde5/kritaoilpaintfilter.so
%{_libdir}/kde5/kritaparticlepaintop.so
%{_libdir}/kde5/kritaphongbumpmap.so
%{_libdir}/kde5/kritapixelizefilter.so
%{_libdir}/kde5/kritapresetdocker.so
%{_libdir}/kde5/kritapsdexport.so
%{_libdir}/kde5/kritapsdimport.so
%{_libdir}/kde5/kritaraindropsfilter.so
%{_libdir}/kde5/kritarandompickfilter.so
%{_libdir}/kde5/kritarotateimage.so
%{_libdir}/kde5/kritaroundcornersfilter.so
%{_libdir}/kde5/kritarulerassistanttool.so
%{_libdir}/kde5/kritaselectiontools.so
%{_libdir}/kde5/kritaseparatechannels.so
%{_libdir}/kde5/kritashearimage.so
%{_libdir}/kde5/kritasketchpaintop.so
%{_libdir}/kde5/kritasmallcolorselector.so
%{_libdir}/kde5/kritasmalltilesfilter.so
%{_libdir}/kde5/kritasobelfilter.so
%{_libdir}/kde5/kritaspecificcolorselector.so
%{_libdir}/kde5/kritaspraypaintop.so
%{_libdir}/kde5/kritatogether.so
%{_libdir}/kde5/kritatonemapping.so
%{_libdir}/kde5/kritatoolcrop.so
%{_libdir}/kde5/kritatooldyna.so
%{_libdir}/kde5/kritatoolgrid.so
%{_libdir}/kde5/kritatoolperspectivegrid.so
%{_libdir}/kde5/kritatoolpolygon.so
%{_libdir}/kde5/kritatoolpolyline.so
%{_libdir}/kde5/kritatoolstar.so
%{_libdir}/kde5/kritatooltransform.so
%{_libdir}/kde5/kritatrianglecolorselector.so
%{_libdir}/kde5/kritaunsharpfilter.so
%{_libdir}/kde5/kritawavefilter.so
%{_datadir}/kde5/services/krita_colorselectorng.desktop
%{_datadir}/kde5/services/krita_colorspaces_extensions_plugin.desktop
%{_datadir}/kde5/services/krita_digitalmixer.desktop
%{_datadir}/kde5/services/krita_presetdocker.desktop
%{_datadir}/kde5/services/krita_smallcolorselector.desktop
%{_datadir}/kde5/services/krita_specificcolorselector.desktop
%{_datadir}/kde5/services/kritabackgrounds.desktop
%{_datadir}/kde5/services/kritabigbrother.desktop
%{_datadir}/kde5/services/kritablurfilter.desktop
#%{_datadir}/kde5/services/kritabracketing2hdr.desktop
%{_datadir}/kde5/services/kritabumpmapfilter.desktop
%{_datadir}/kde5/services/kritachalkpaintop.desktop
%{_datadir}/kde5/services/kritacolorgenerator.desktop
%{_datadir}/kde5/services/kritacolorrange.desktop
%{_datadir}/kde5/services/kritacolorsfilter.desktop
%{_datadir}/kde5/services/kritacolorspaceconversion.desktop
%{_datadir}/kde5/services/kritacomplexbrush.desktop
%{_datadir}/kde5/services/kritaconvolutionfilters.desktop
%{_datadir}/kde5/services/kritacurvepaintop.desktop
%{_datadir}/kde5/services/kritadefaultdockers.desktop
%{_datadir}/kde5/services/kritadefaultpaintops.desktop
%{_datadir}/kde5/services/kritadefaulttools.desktop
%{_datadir}/kde5/services/kritadeformpaintop.desktop
%{_datadir}/kde5/services/kritadodgeburn.desktop
%{_datadir}/kde5/services/kritadropshadow.desktop
%{_datadir}/kde5/services/kritadynapaintop.desktop
%{_datadir}/kde5/services/kritaembossfilter.desktop
%{_datadir}/kde5/services/kritaexample.desktop
%{_datadir}/kde5/services/kritaextensioncolorsfilters.desktop
%{_datadir}/kde5/services/kritaextensionsmanager.desktop
%{_datadir}/kde5/services/kritafastcolortransfer.desktop
%{_datadir}/kde5/services/kritafilterop.desktop
%{_datadir}/kde5/services/kritagridpaintop.desktop
%{_datadir}/kde5/services/kritahairypaintop.desktop
%{_datadir}/kde5/services/kritahatchingpaintop.desktop
%{_datadir}/kde5/services/kritahistogram.desktop
%{_datadir}/kde5/services/kritaimageenhancement.desktop
%{_datadir}/kde5/services/kritaimagesize.desktop
%{_datadir}/kde5/services/kritalayercompose.desktop
%{_datadir}/kde5/services/kritalevelfilter.desktop
%{_datadir}/kde5/services/kritametadataeditor.desktop
%{_datadir}/kde5/services/kritamodifyselection.desktop
%{_datadir}/kde5/services/kritamypaintpaintop.desktop
%{_datadir}/kde5/services/kritanoisefilter.desktop
%{_datadir}/kde5/services/kritaoilpaintfilter.desktop
%{_datadir}/kde5/services/kritapart.desktop
%{_datadir}/kde5/services/kritaparticlepaintop.desktop
%{_datadir}/kde5/services/kritaphongbumpmapfilter.desktop
%{_datadir}/kde5/services/kritapixelizefilter.desktop
%{_datadir}/kde5/services/kritaraindropsfilter.desktop
%{_datadir}/kde5/services/kritarandompickfilter.desktop
%{_datadir}/kde5/services/kritarotateimage.desktop
%{_datadir}/kde5/services/kritaroundcornersfilter.desktop
%{_datadir}/kde5/services/kritarulerassistanttool.desktop
%{_datadir}/kde5/services/kritaselectiontools.desktop
%{_datadir}/kde5/services/kritaseparatechannels.desktop
%{_datadir}/kde5/services/kritashearimage.desktop
%{_datadir}/kde5/services/kritasketchpaintop.desktop
%{_datadir}/kde5/services/kritasmalltilesfilter.desktop
%{_datadir}/kde5/services/kritasobelfilter.desktop
%{_datadir}/kde5/services/kritaspraypaintop.desktop
%{_datadir}/kde5/services/kritatogether.desktop
%{_datadir}/kde5/services/kritatonemapping.desktop
%{_datadir}/kde5/services/kritatoolcrop.desktop
%{_datadir}/kde5/services/kritatooldyna.desktop
%{_datadir}/kde5/services/kritatoolgrid.desktop
%{_datadir}/kde5/services/kritatoolperspectivegrid.desktop
%{_datadir}/kde5/services/kritatoolpolygon.desktop
%{_datadir}/kde5/services/kritatoolpolyline.desktop
%{_datadir}/kde5/services/kritatoolstar.desktop
%{_datadir}/kde5/services/kritatooltransform.desktop
%{_datadir}/kde5/services/kritatrianglecolorselector.desktop
%{_datadir}/kde5/services/kritaunsharpfilter.desktop
%{_datadir}/kde5/services/kritawavefilter.desktop
%{_libdir}/kde5/kritaexperimentpaintop.so
%{_datadir}/kde5/services/kritaexperimentpaintop.desktop
%{_libdir}/kde5/kritachanneldocker.so
%{_datadir}/kde5/services/krita_channeldocker.desktop

%files krita-data
%defattr(-,root,root,-)
%{_datadir}/color/icc/krita
%{_datadir}/krita/backgrounds/old_paper.png
%{_datadir}/krita/brushes
%{_datadir}/krita/brushmodels
%{_datadir}/krita/defaultpresets
%{_datadir}/krita/gradients
%{_datadir}/krita/icons
%{_datadir}/krita/images
%{_datadir}/krita/metadata
%{_datadir}/krita/paintoppresets
%{_datadir}/krita/palettes
%{_datadir}/krita/patterns
%{_datadir}/krita/pics
%{_datadir}/krita/shaders
%{_datadir}/krita/templates
%{_datadir}/kritaplugins
%{_datadir}/krita/dtd/krita.dtd
%{_datadir}/mime/packages/krita_ora.xml
%endif

%if 0%{?karbon}
%files karbon
%defattr(-,root,root,-)
%{_bindir}/karbon
%{_libdir}/kde5/karbonpart.so
%{_libdir}/libkarboncommon.so.*
%{_libdir}/libkarbonui.so.*
%{_libdir}/libkdeinit4_karbon.so
%{_datadir}/applications/kde5/karbon.desktop
%{_datadir}/karbon/karbon.rc
%{_datadir}/karbon/karbon_readonly.rc
%{_datadir}/config/karbonrc
%{_datadir}/kde5/services/karbonpart.desktop
%{_datadir}/kde5/servicetypes/karbon_module.desktop

%files karbon-plugins
%defattr(-,root,root,-)
%{_libdir}/kde5/karbon_flattenpathplugin.so
%{_libdir}/kde5/karbon_refinepathplugin.so
%{_libdir}/kde5/karbon_roundcornersplugin.so
%{_libdir}/kde5/karbon_whirlpinchplugin.so
%{_libdir}/kde5/karbonfiltereffects.so
%{_libdir}/kde5/karbontools.so
%{_datadir}/karbon/kpartplugins/FlattenPathPlugin.rc
%{_datadir}/karbon/kpartplugins/RefinePathPlugin.rc
%{_datadir}/karbon/kpartplugins/RoundCornersPlugin.rc
%{_datadir}/karbon/kpartplugins/WhirlPinchPlugin.rc
%{_datadir}/kde5/services/karbonfiltereffects.desktop
%{_datadir}/kde5/services/karbontools.desktop

%files karbon-filters
%defattr(-,root,root,-)
%{_libdir}/kde5/karbon1ximport.so
%{_libdir}/kde5/karbonpdfimport.so
%{_libdir}/kde5/karbonpngexport.so
%{_libdir}/kde5/karbonsvgexport.so
%{_libdir}/kde5/karbonsvgimport.so
%{_libdir}/kde5/wmfexport.so
%{_libdir}/kde5/wmfimport.so
%{_datadir}/kde5/services/karbon_1x_import.desktop
%{_datadir}/kde5/services/karbon_pdf_import.desktop
%{_datadir}/kde5/services/karbon_png_export.desktop
%{_datadir}/kde5/services/karbon_svg_export.desktop
%{_datadir}/kde5/services/karbon_svg_import.desktop
%{_datadir}/kde5/services/karbon_svgz_import.desktop
%{_datadir}/kde5/services/karbon_wmf_export.desktop
%{_datadir}/kde5/services/karbon_wmf_import.desktop

%files karbon-data
%defattr(-,root,root,-)
%{_datadir}/karbon/gradients/*
%{_datadir}/karbon/icons/hicolor/16x16
%{_datadir}/karbon/icons/hicolor/22x22
%{_datadir}/karbon/icons/oxygen/16x16

%files karbon-templates
%defattr(-,root,root,-)
%{_datadir}/karbon/icons/hicolor/48x48/actions/template_empty.png
%{_datadir}/karbon/icons/hicolor/scalable/actions/template_empty.svgz
%{_datadir}/karbon/templates/Basic/
%endif

%if 0%{?kexi}
%files kexi
%defattr(-,root,root,-)
%endif

# %files kthesaurus
# %defattr(-,root,root,-)
# %{_datadir}/applications/kde5/KThesaurus.desktop
# %{_libdir}/libkdeinit4_kthesaurus.so
# %{_bindir}/kthesaurus

%if 0%{?freoffice}
%files mobile
%defattr(-,root,root,-)
%{_datadir}/freoffice-templates
%{_datadir}/dbus-1/services/com.nokia.FreOffice.service
%{_datadir}/applications/freoffice.desktop
%{_bindir}/FreOffice
%{_datadir}/icons/hicolor/64x64/apps/freoffice.png
%{_datadir}/icons/hicolor/178x200/apps/freoffice.png
%{_datadir}/icons/hicolor/48x48/hildon/Document.png
%{_datadir}/icons/hicolor/48x48/hildon/Presenter.png
%{_datadir}/icons/hicolor/48x48/hildon/SpreadSheet.png
%{_libdir}/libkoabstraction.so.*
%endif

%files libs
%defattr(-,root,root,-)
%{_bindir}/preparetips
%{_libdir}/libKConfigCore.so*
%{_libdir}/libKService.so*
%{_libdir}/libItemViews.so*
%{_libdir}/libKCodecs.so*
%{_libdir}/libKConfigGui.so*
%{_libdir}/libKConfigWidgets.so*
%{_libdir}/libKCoreAddons.so*
%{_libdir}/libKI18n.so*
%{_libdir}/libKWidgetsAddons.so*
%{_libdir}/libXmlGui.so*
%{_libdir}/libkofake.so*
%{_datadir}/kde5/servicetypes/kplugininfo.desktop
%{_datadir}/dbus-1/interfaces/org.kde.KGlobalAccel.xml
%{_datadir}/dbus-1/interfaces/org.kde.kglobalaccel.Component.xml
%{_datadir}/kconfigwidgets/pics/ktip-bulb.png
%{_datadir}/xmlgui/pics/*.png
/usr/etc/xdg/ui/ui_standards.rc

%{_libdir}/libpigmentcms.so.*
%{_libdir}/libkowidgets.so.*
%{_libdir}/libkotext.so.*
#%{_libdir}/libkoproperty.so.*
%{_libdir}/libkoplugin.so.*
%{_libdir}/libkopageapp.so.*
%{_libdir}/libkoodf.so.*
%{_libdir}/libkomain.so.*
#%{_libdir}/libkochart.so.*
%{_libdir}/libcalligrakdchart.so.*
%{_libdir}/libkundo2.so*
%{_libdir}/libkotextlayout.so*
#%{_libdir}/libvectorimage.so*
%{_libdir}/libflake.so.*
%{_libdir}/libbasicflakes.so*
#%{_libdir}/libRtfReader.so*
%{_libdir}/libkowidgetutils.so*

%{_libdir}/calligra/calligra_tool_basicflakes.so
%{_datadir}/kde5/services/calligra_tool_basicflakes.desktop
#%{_libdir}/kde5/calligradocinfopropspage.so
#%{_datadir}/kde5/services/calligradocinfopropspage.desktop

#%{_datadir}/kde5/services/textdocumentinspection.desktop
#%{_datadir}/kde5/servicetypes/calligra_chart.desktop
%{_datadir}/kde5/servicetypes/calligra_deferred_plugin.desktop
%{_datadir}/kde5/servicetypes/calligra_filter.desktop
%{_datadir}/kde5/servicetypes/calligra_part.desktop
%{_datadir}/kde5/servicetypes/calligradocker.desktop

%files components
%defattr(-,root,root,-)
%{_libdir}/calligra/org/kde/calligra

%files filters-libs
%defattr(-,root,root,-)
#%{_libdir}/libmsooxml.so.*
#%{_datadir}/mime/packages/msooxml-all.xml

%files filters
%defattr(-,root,root,-)
#%{_bindir}/calligraconverter

%files words-filters
%defattr(-,root,root,-)
#%{_libdir}/libkwordexportfilters.so.*
#%{_libdir}/libkowv2.so.*

#%{_libdir}/kde5/applixwordimport.so
#%{_datadir}/kde5/services/words_applixword_import.desktop

#%{_datadir}/kde5/services/kword_ascii_export.desktop
#%{_libdir}/kde5/asciiexport.so

#%{_datadir}/kde5/services/words_ascii_import.desktop
#%{_libdir}/kde5/asciiimport.so

#%{_datadir}/kde5/services/words_docx_import.desktop
#%{_libdir}/kde5/docximport.so

#%{_datadir}/kde5/services/words_msword-odf_import.desktop
#%{_libdir}/kde5/mswordodf_import.so

#%{_datadir}/kde5/services/kword_rtf_export.desktop
#%{_libdir}/kde5/rtfexport.so
#%{_datadir}/kde5/services/words_rtf_import.desktop
#%{_libdir}/kde5/rtfimport.so

#%{_libdir}/kde5/exportMobi.so
#%{_datadir}/kde5/services/words_Mobi_export.desktop
#%{_libdir}/kde5/exportepub2.so
#%{_datadir}/kde5/services/words_epub2_export.desktop
#%{_libdir}/kde5/exporthtml.so
#%{_datadir}/kde5/services/words_html_export.desktop

%files sheets-filters
%defattr(-,root,root,-)
# %{_datadir}/kde5/services/kspread_xlsx_import.desktop
# %{_libdir}/kde5/xlsximport.so
#
# %{_datadir}/kde5/services/sheets_excel_thumbnail.desktop
# %{_datadir}/kde5/services/sheets_xlsx_thumbnail.desktop
#
# %{_datadir}/kde5/services/kspread_excel_import.desktop
# %{_libdir}/kde5/excelimporttodoc.so
#
# %{_libdir}/kde5/applixspreadimport.so
# %{_datadir}/kde5/services/kspread_applixspread_import.desktop
#
# %{_libdir}/kde5/csvimport.so
# %{_datadir}/kde5/services/kspread_csv_import.desktop
#
# %{_libdir}/kde5/dbaseimport.so
# %{_datadir}/kde5/services/kspread_dbase_import.desktop
# %{_libdir}/kde5/gnumericexport.so
# %{_datadir}/kde5/services/kspread_gnumeric_export.desktop
# %{_libdir}/kde5/gnumericimport.so
# %{_datadir}/kde5/services/kspread_gnumeric_import.desktop
# %{_libdir}/kde5/opencalcexport.so
# %{_datadir}/kde5/services/kspread_opencalc_export.desktop
# %{_libdir}/kde5/opencalcimport.so
# %{_datadir}/kde5/services/kspread_opencalc_import.desktop
# %{_libdir}/kde5/qproimport.so
# %{_datadir}/kde5/services/kspread_qpro_import.desktop


%files stage-filters
%defattr(-,root,root,-)
# %{_datadir}/kde5/services/kpresenter_powerpoint_import.desktop
# %{_libdir}/kde5/powerpointimport.so
#
# %{_datadir}/kde5/services/kpresenter_pptx_import.desktop
# %{_libdir}/kde5/pptximport.so
#
# %{_datadir}/kde5/services/Filterkpr2odf.desktop
# %{_libdir}/kde5/Filterkpr2odf.so

%files plugins
%defattr(-,root,root,-)
%{_datadir}/kde5/servicetypes/pigment.desktop
%{_datadir}/kde5/servicetypes/pigmentextension.desktop
%{_datadir}/kde5/servicetypes/scripteventaction.desktop
%{_datadir}/kde5/servicetypes/texteditingplugin.desktop
#%{_datadir}/kde5/servicetypes/textvariableplugin.desktop
#%{_datadir}/kde5/servicetypes/koplugin.desktop

#maybe have the next two in -filters instead?
#%{_datadir}/kde5/servicetypes/kofilter.desktop
#%{_datadir}/kde5/servicetypes/kofilterwrapper.desktop

%{_datadir}/kde5/servicetypes/filtereffect.desktop
%{_datadir}/kde5/servicetypes/flake.desktop
%{_datadir}/kde5/servicetypes/flakedevice.desktop
%{_datadir}/kde5/servicetypes/flakeshape.desktop
%{_datadir}/kde5/servicetypes/flaketool.desktop
%{_datadir}/kde5/servicetypes/inlinetextobject.desktop
#%{_datadir}/kde5/servicetypes/kochart.desktop
#%{_datadir}/kde5/servicetypes/kofficedocker.desktop
#%{_datadir}/kde5/servicetypes/kofficepart.desktop

#%{_datadir}/kde5/services/treeshape.desktop
#%{_libdir}/kde5/treeshape.so

#%{_datadir}/kde5/services/vectorshape.desktop
#%{_libdir}/kde5/vectorshape.so

# %{_datadir}/kde5/services/videoshape.desktop
# %{_libdir}/kde5/videoshape.so

%{_datadir}/kde5/services/calligra_shape_text.desktop
%{_libdir}/calligra/calligra_shape_text.so

%{_datadir}/kde5/services/calligra_textinlineobject_variables.desktop
%{_libdir}/calligra/calligra_textinlineobject_variables.so

%{_datadir}/kde5/services/calligra_shape_paths.desktop
%{_libdir}/calligra/calligra_shape_paths.so

%{_datadir}/kde5/services/calligra_shape_picture.desktop
%{_libdir}/calligra/calligra_shape_picture.so

%{_datadir}/kde5/services/calligra_shape_plugin.desktop
%{_libdir}/calligra/calligra_shape_plugin.so

# maybe needs to be its own package
%{_datadir}/kde5/services/calligra_shape_spreadsheet.desktop
%{_libdir}/calligra/calligra_shape_spreadsheet.so

%{_datadir}/kde5/services/calligra_shape_chart.desktop
# %{_libdir}/libchartshapelib.so.*
%{_libdir}/calligra/calligra_shape_chart.so

%{_datadir}/kde5/services/calligra_tool_defaults.desktop
%{_libdir}/calligra/calligra_tool_defaults.so

# %{_datadir}/kde5/services/kchartpart.desktop

#%{_datadir}/kde5/services/kodocinfopropspage.desktop
#%{_libdir}/kde5/kodocinfopropspage.so

#%{_datadir}/kde5/services/kofficethumbnail.desktop
#%{_libdir}/kde5/kofficethumbnail.so

%{_datadir}/kde5/services/kopabackgroundtool.desktop
%{_libdir}/calligra/kopabackgroundtool.so

# staging
#%{_datadir}/kpresenter/kpartplugins/googledocs-kpresenter.rc
#%{_datadir}/kword/kpartplugins/googledocs-kword.rc
#%{_libdir}/kde5/kofficegoogledocs.so

%files data
%defattr(-,root,root,-)
%{_datadir}/kde5/servicetypes/calligra_application.desktop
%{_datadir}/calligra/calligra_shell.rc
%{_datadir}/calligra/icons
%{_datadir}/calligra/palettes
%{_datadir}/calligra/styles
%{_datadir}/icons/*
%if 0%{?freoffice}
%exclude %{_datadir}/icons/hicolor/64x64/apps/freoffice.png
%exclude %{_datadir}/icons/hicolor/178x200/apps/freoffice.png
%exclude %{_datadir}/icons/hicolor/48x48/hildon/Document.png
%exclude %{_datadir}/icons/hicolor/48x48/hildon/Presenter.png
%exclude %{_datadir}/icons/hicolor/48x48/hildon/SpreadSheet.png
%endif
#%{_datadir}/koproperty/icons/hicolor/16x16/actions/button_no.png

%files konqi-servicemenus
%defattr(-,root,root,-)
# %{_datadir}/kde5/services/ServiceMenus/karbon_konqi.desktop
# %{_datadir}/kde5/services/ServiceMenus/kchart_konqi.desktop
# %{_datadir}/kde5/services/ServiceMenus/kformula_konqi.desktop
# %{_datadir}/kde5/services/ServiceMenus/kivio_konqi.desktop
# %{_datadir}/kde5/services/ServiceMenus/kpresenter_konqi.desktop
# %{_datadir}/kde5/services/ServiceMenus/krita_konqi.desktop
# %{_datadir}/kde5/services/ServiceMenus/kspread_konqi.desktop
# %{_datadir}/kde5/services/ServiceMenus/kword_konqi.desktop
# konqi-templates
# %{_datadir}/templates/TextDocument.desktop
# %{_datadir}/templates/.source/TextDocument.odt
# %{_datadir}/templates/SpreadSheet.desktop
# %{_datadir}/templates/.source/SpreadSheet.ods
# %{_datadir}/templates/Presentation.desktop
# %{_datadir}/templates/.source/Presentation.odp
# %{_datadir}/templates/Illustration.desktop
# %{_datadir}/templates/.source/Illustration.odg


%files devel
%defattr(-,root,root,-)
%{_datadir}/cmake/modules/FindCalligraLibs.cmake
%{_libdir}/cmake/*
%{_includedir}/*
# %{_libdir}/libchartshapelib.so
%{_libdir}/libflake.so
%{_libdir}/libcalligrakdchart.so
# %{_libdir}/libkochart.so
%{_libdir}/libkomain.so
%{_libdir}/libkoodf.so
%{_libdir}/libkopageapp.so
%{_libdir}/libkoplugin.so
#%{_libdir}/libkoproperty.so
%{_libdir}/libkotext.so
%{_libdir}/libkowidgets.so
# %{_libdir}/libkowv2.so
%{_libdir}/libcalligrastageprivate.so
%{_libdir}/libcalligrasheetscommon.so
%{_libdir}/libcalligrasheetsodf.so
#%{_libdir}/libkwordexportfilters.so
%{_libdir}/libwordsprivate.so
# %{_libdir}/libmsooxml.so
%{_libdir}/libpigmentcms.so
%if 0%{?karbon}
%{_libdir}/libkarboncommon.so
%{_libdir}/libkarbonui.so
%endif
%if 0%{?krita}
%{_libdir}/libkritaui.so
%{_libdir}/libkritalibpaintop.so
%{_libdir}/libkritalibbrush.so
%{_libdir}/libkritaimage.so
%endif
%if 0%{?kexi}
%endif
#%{_libdir}/libcalligramobile.so
%if 0%{?freoffice}
%{_libdir}/libkoabstraction.so
%endif


%prep
%setup -q -n %{name}-%{version}/calligra

%build
mkdir -p build && cd build
cmake \
    -DPRODUCTSET=Libraries \
    -DKDE4_BUILD_TESTS=OFF \
    -DWITH_KActivities=OFF \
    -DCMAKE_INSTALL_PREFIX=/usr/ \
    -DBUILD_TESTING=ON \
    -DCMAKE_BUILD_TYPE=Release \
    ..
#     -DGHNS=FALSE \
#     -DBUILD_mobile=ON \
#     -DSHOULD_BUILD_ACTIVE=OFF \
#     -DBUILD_artistictextshape=OFF \
#     -DBUILD_colorspaces=OFF \
#     -DBUILD_doc=OFF \
#     -DBUILD_generic_wrapper=OFF \
#     -DBUILD_karbon=%{?karbon:ON}%{!?karbon:OFF} \
#     -DBUILD_kchart=ON \
#     -DBUILD_kformula=ON \
#     -DBUILD_kivio=OFF \
#     -DBUILD_sheets=ON \
#     -DBUILD_musicshape=OFF \
#     -DBUILD_scan=OFF \
#     -DBUILD_f-office=ON \
#     -DBUILD_simpletextedit=OFF \
#     -DBUILD_krita=%{?krita:ON}%{!?krita:OFF} \
#     -DBUILD_koreport=OFF \
#     -DBUILD_reporting=OFF \
#     -DBUILD_colorengines=%{?krita:ON}%{!?krita:OFF} \
#     -DBUILD_kexi=%{?kexi:ON}%{!?kexi:OFF} \
#     %{?kexi:-DKEXI_MOBILE=ON} \
#     -DWITH_Soprano=OFF \
#     -DBUILD_staging=OFF \
#     -DBUILD_f-office=%{?freoffice:ON}%{!?freoffice:OFF} \
#     -DBUILD_koabstraction=%{?freoffice:ON}%{!?freoffice:OFF} \
#     -DBUILD_cstester=OFF \
#     -DBUILD_thumbnail=OFF \
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_datadir}/applications

%if 0%{?freoffice}
mv %{buildroot}/%{_datadir}/applications/hildon/freoffice.desktop %{buildroot}/%{_datadir}/applications/
%endif
