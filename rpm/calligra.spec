#define karbon 0
#define krita 0
#define freoffice 0
#define kexi 0

Name: calligra
Version: 2.6~gitafae6db30cb24721531c02b6b100e203bd377b77
Release: 1%{?dist}
Group: Applications/Productivity
Source0: calligra-latest.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Summary: Calligra Suite
License: Open
BuildRequires: cmake, automoc4
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: boost-devel
BuildRequires: libkok-devel
BuildRequires: pkgconfig(libgsf-1)
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(eigen2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(QtOpenGL)
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: pkgconfig(QtDBus)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(phonon)
%if 0%{?krita}
BuildRequires: lcms-devel exiv2-devel giflib-devel
%endif
%if 0%{?karbon}
BuildRequires: pkgconfig(poppler-qt4)
BuildRequires: fontconfig-devel
%endif
%if 0%{?kexi}
BuildRequires: sqlite-devel
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

%define kdedatadir %{_datadir}

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%package sheets-core-plugins
Summary: Calligra Sheets core plugins
Group: Development/Libraries

%description sheets-core-plugins
%{summary}.
Plugins that add support for all the default functions in sheets.

%post sheets-core-plugins
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun mobile -p  /sbin/ldconfig
%endif

%package libs
Summary: Shared Calligra libraries
Group: Development/Libraries

%description libs
%{summary}.

%post libs
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun libs -p  /sbin/ldconfig

%package filters
Summary: Calligra input/output filters
Requires: %{name}-words-filters = %{version}-%{release}
Requires: %{name}-sheets-filters = %{version}-%{release}
Requires: %{name}-stage-filters = %{version}-%{release}

%description filters
%{summary}.

%post filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%package filters-libs
Summary: Calligra input/output filters shared libraries

%description filters-libs
%{summary}.

%post filters-libs
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun filters-libs -p  /sbin/ldconfig

%package words-filters
Summary: Calligra Words input/output filters

%description words-filters
%{summary}.

%post words-filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

%postun words-filters -p  /sbin/ldconfig

%package sheets-filters
Summary: Calligra Sheets input/output filters

%description sheets-filters
%{summary}.

%post sheets-filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

#%postun sheets-filters -p  /sbin/ldconfig

%package stage-filters
Summary: Calligra Stage input/output filters

%description stage-filters
%{summary}.

%post stage-filters
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

#%postun stage-filters -p  /sbin/ldconfig

%package plugins
Summary: Calligra plugins

%description plugins
%{summary}.

%post plugins
/sbin/ldconfig
KDESYCOCA=/usr/share/kde4/services/ksycoca4 /usr/bin/kbuildsycoca4 2> /dev/null > /dev/null ||:

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
Requires: libkok-devel

%description devel
%{summary}.

%files
%defattr(-,root,root,-)

# %files words
# %defattr(-,root,root,-)
# %{_libdir}/libkdeinit4_words.so
# %{_bindir}/words

# %{_datadir}/applications/kde4/words.desktop
# %{kdedatadir}/config/wordsrc
# %{kdedatadir}/apps/words/styles/defaultstyles.xml
# %{kdedatadir}/apps/words/words.rc
# %{kdedatadir}/apps/words/words_readonly.rc

%files words-core
%defattr(-,root,root,-)
%{_datadir}/kde4/services/wordspart.desktop
%{_libdir}/libwordsprivate.so.*
%{_libdir}/kde4/wordspart.so
%{kdedatadir}/config/wordsrc
%{kdedatadir}/apps/words/styles/defaultstyles.xml
%{kdedatadir}/apps/words/words.rc
%{kdedatadir}/apps/words/words_readonly.rc

%{_datadir}/kde4/services/words_docx_thumbnail.desktop
%{_datadir}/kde4/services/words_msword_thumbnail.desktop
%{_datadir}/kde4/services/words_rtf_thumbnail.desktop

%files words-templates
%defattr(-,root,root,-)
%{kdedatadir}/apps/words/templates
%{kdedatadir}/apps/words/icons/hicolor/48x48/actions/template_*.png
%{kdedatadir}/apps/words/icons/hicolor/128x128/actions/template_*.png
%{kdedatadir}/apps/words/icons/hicolor/scalable/actions/template_*.svgz

#%files words-plugins
#%defattr(-,root,root,-)

# %files sheets
# %defattr(-,root,root,-)
# %{_libdir}/libkdeinit4_calligrasheets.so
# %{_bindir}/calligrasheets

# %{_datadir}/applications/kde4/sheets.desktop
# %{kdedatadir}/config/sheetsrc
# %{kdedatadir}/config.kcfg/sheets.kcfg
# %{kdedatadir}/apps/sheets/sheetstyles
# %{kdedatadir}/apps/sheets/sheets.notifyrc
# %{kdedatadir}/apps/sheets/sheets.rc
# %{kdedatadir}/apps/sheets/sheets_readonly.rc
# %{kdedatadir}/apps/sheets/icons/hicolor/16x16
# %{kdedatadir}/apps/sheets/icons/hicolor/22x22
# %{kdedatadir}/apps/sheets/icons/hicolor/32x32
# %{kdedatadir}/apps/sheets/dtd/kspread.dtd

%files sheets-core
%defattr(-,root,root,-)
%{_datadir}/kde4/services/sheetspart.desktop
%{_libdir}/libcalligrasheetsodf.so.*
%{_libdir}/libcalligrasheetscommon.so.*
%{_libdir}/kde4/calligrasheetspart.so
%{_libdir}/kde4/spreadsheetshape-deferred.so
%{_datadir}/kde4/servicetypes/sheets_plugin.desktop
%{_datadir}/kde4/services/spreadsheetshape-deferred.desktop
%{kdedatadir}/config/sheetsrc
%{kdedatadir}/config.kcfg/sheets.kcfg
%{kdedatadir}/apps/sheets/CellToolOptionWidgets.xml
%{kdedatadir}/apps/sheets/sheetstyles
%{kdedatadir}/apps/sheets/sheets.rc
%{kdedatadir}/apps/sheets/sheets_readonly.rc
%{kdedatadir}/apps/sheets/icons/hicolor/16x16
%{kdedatadir}/apps/sheets/icons/hicolor/22x22
%{kdedatadir}/apps/sheets/icons/hicolor/32x32
%{kdedatadir}/apps/sheets/dtd/kspread.dtd

%files sheets-templates
%defattr(-,root,root,-)
%{kdedatadir}/apps/sheets/templates
%{kdedatadir}/apps/sheets/icons/hicolor/48x48/actions/template_*.png
%{kdedatadir}/apps/sheets/icons/hicolor/scalable/actions/template_*.svgz

%files sheets-core-plugins
%defattr(-,root,root,-)
%{_datadir}/kde4/services/kspreadmathmodule.desktop
%{kdedatadir}/apps/sheets/functions/math.xml
%{_libdir}/kde4/kspreadmathmodule.so

%{_datadir}/kde4/services/kspreadreferencemodule.desktop
%{kdedatadir}/apps/sheets/functions/reference.xml
%{_libdir}/kde4/kspreadreferencemodule.so

%{_datadir}/kde4/services/kspreadstatisticalmodule.desktop
%{kdedatadir}/apps/sheets/functions/statistical.xml
%{_libdir}/kde4/kspreadstatisticalmodule.so

%{_datadir}/kde4/services/kspreadtextmodule.desktop
%{kdedatadir}/apps/sheets/functions/text.xml
%{_libdir}/kde4/kspreadtextmodule.so

%{_datadir}/kde4/services/kspreadtrigonometrymodule.desktop
%{kdedatadir}/apps/sheets/functions/trig.xml
%{_libdir}/kde4/kspreadtrigonometrymodule.so

%{_datadir}/kde4/services/kspreadbitopsmodule.desktop
%{kdedatadir}/apps/sheets/functions/bitops.xml
%{_libdir}/kde4/kspreadbitopsmodule.so

%{_datadir}/kde4/services/kspreadconversionmodule.desktop
%{kdedatadir}/apps/sheets/functions/conversion.xml
%{_libdir}/kde4/kspreadconversionmodule.so

%{_datadir}/kde4/services/kspreaddatabasemodule.desktop
%{kdedatadir}/apps/sheets/functions/database.xml
%{_libdir}/kde4/kspreaddatabasemodule.so

%{_datadir}/kde4/services/kspreaddatetimemodule.desktop
%{kdedatadir}/apps/sheets/functions/datetime.xml
%{_libdir}/kde4/kspreaddatetimemodule.so

%{_datadir}/kde4/services/kspreadengineeringmodule.desktop
%{kdedatadir}/apps/sheets/functions/engineering.xml
%{_libdir}/kde4/kspreadengineeringmodule.so

%{_datadir}/kde4/services/kspreadfinancialmodule.desktop
%{kdedatadir}/apps/sheets/functions/financial.xml
%{_libdir}/kde4/kspreadfinancialmodule.so

%{_datadir}/kde4/services/kspreadinformationmodule.desktop
%{kdedatadir}/apps/sheets/functions/information.xml
%{_libdir}/kde4/kspreadinformationmodule.so

%{_datadir}/kde4/services/kspreadlogicmodule.desktop
%{kdedatadir}/apps/sheets/functions/logic.xml
%{_libdir}/kde4/kspreadlogicmodule.so

%files sheets-plugins
%defattr(-,root,root,-)
%{_datadir}/kde4/services/kspread_plugin_tool_calendar.desktop
%{_libdir}/kde4/kspread_plugin_tool_calendar.so

# %files stage
# %defattr(-,root,root,-)
# %{_libdir}/libkdeinit4_kpresenter.so
# %{_bindir}/kpresenter
# %{_datadir}/applications/kde4/kpresenter.desktop
# %{kdedatadir}/config/kpresenterrc
# %{kdedatadir}/apps/stage/pics
# %{kdedatadir}/apps/stage/styles/defaultstyles.xml
# %{kdedatadir}/apps/stage/stage.rc
# %{kdedatadir}/apps/stage/stage_readonly.rc
# %{kdedatadir}/apps/stage/icons/hicolor/64x64

%files stage-core
%defattr(-,root,root,-)
%{_datadir}/kde4/services/stagepart.desktop
%{_libdir}/kde4/calligrastagepart.so
%{_libdir}/libcalligrastageprivate.so.*
%{_datadir}/kde4/servicetypes/presentationeventaction.desktop
%{_datadir}/kde4/servicetypes/kpr_pageeffect.desktop
%{_datadir}/kde4/servicetypes/kpr_shapeanimation.desktop
%{kdedatadir}/config/stagerc
%{kdedatadir}/apps/stage/animations/animations.xml
%{kdedatadir}/apps/stage/pics
%{kdedatadir}/apps/stage/icons
%{kdedatadir}/apps/stage/styles/defaultstyles.xml
%{kdedatadir}/apps/stage/stage.rc
%{kdedatadir}/apps/stage/stage_readonly.rc
%{kdedatadir}/apps/stage/icons/hicolor/64x64

%{_datadir}/kde4/services/stage_kpr_thumbnail.desktop
%{_datadir}/kde4/services/stage_powerpoint_thumbnail.desktop
%{_datadir}/kde4/services/stage_pptx_thumbnail.desktop

%files stage-templates
%defattr(-,root,root,-)
%{kdedatadir}/apps/stage/templates
%{kdedatadir}/apps/stage/icons/hicolor/48x48/actions/template_*.png
%{kdedatadir}/apps/stage/icons/hicolor/scalable/actions/template_*.svgz

%files stage-plugins
%defattr(-,root,root,-)
%{_datadir}/kde4/services/calligrastagetoolanimation.desktop
%{_datadir}/kde4/services/kprvariables.desktop
%{_datadir}/kde4/services/calligrastageeventactions.desktop
%{_datadir}/kde4/services/kpr_pageeffect_barwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_clockwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_edgewipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_fade.desktop
%{_datadir}/kde4/services/kpr_pageeffect_iriswipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_matrixwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_slidewipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_spacerotation.desktop
%{_datadir}/kde4/services/kpr_pageeffect_swapeffect.desktop
%{_datadir}/kde4/services/kpr_shapeanimation_example.desktop
%{_libdir}/kde4/kpr_pageeffect_barwipe.so
%{_libdir}/kde4/kpr_pageeffect_clockwipe.so
%{_libdir}/kde4/kpr_pageeffect_edgewipe.so
%{_libdir}/kde4/kpr_pageeffect_fade.so
%{_libdir}/kde4/kpr_pageeffect_iriswipe.so
%{_libdir}/kde4/kpr_pageeffect_matrixwipe.so
%{_libdir}/kde4/kpr_pageeffect_slidewipe.so
%{_libdir}/kde4/kpr_pageeffect_spacerotation.so
%{_libdir}/kde4/kpr_pageeffect_swapeffect.so
%{_libdir}/kde4/kpr_shapeanimation_example.so
%{_libdir}/kde4/calligrastageeventactions.so
%{_libdir}/kde4/calligrastagetoolanimation.so
%{_libdir}/kde4/kprvariables.so

%if 0%{?krita}
%files krita
%defattr(-,root,root,-)
%{_bindir}/krita
%{_libdir}/kde4/kritapart.so
%{_libdir}/libkdeinit4_krita.so
%{_libdir}/libkritaimage.so.*
%{_libdir}/libkritalibbrush.so.*
%{_libdir}/libkritalibpaintop.so.*
%{_libdir}/libkritaui.so.*
%{_datadir}/applications/kde4/krita.desktop
%{kdedatadir}/apps/krita/krita.rc
%{kdedatadir}/apps/krita/krita_readonly.rc
%{kdedatadir}/config/krita.knsrc
%{kdedatadir}/config/kritarc

%{_libdir}/kde4/kolcmsengine.so
%{_datadir}/color/icc/pigment/CMY.icm
%{_datadir}/color/icc/pigment/fogra27l.icm
%{_datadir}/kde4/services/kolcmsengine.desktop

%files krita-filters
%defattr(-,root,root,-)
%{_libdir}/kde4/kritabmpexport.so
%{_libdir}/kde4/kritabmpimport.so
%{_libdir}/kde4/kritagifimport.so
%{_libdir}/kde4/kritajpegexport.so
%{_libdir}/kde4/kritajpegimport.so
%{_libdir}/kde4/kritaoraexport.so
%{_libdir}/kde4/kritaoraimport.so
%{_libdir}/kde4/kritapngexport.so
%{_libdir}/kde4/kritapngimport.so
%{_libdir}/kde4/kritappmexport.so
%{_libdir}/kde4/kritappmimport.so
%{_libdir}/kde4/kritaxcfimport.so
%{_libdir}/kde4/kritaodgimport.so
%{_datadir}/applications/kde4/krita_bmp.desktop
%{_datadir}/applications/kde4/krita_gif.desktop
%{_datadir}/applications/kde4/krita_jpeg.desktop
%{_datadir}/applications/kde4/krita_ora.desktop
%{_datadir}/applications/kde4/krita_png.desktop
%{_datadir}/applications/kde4/krita_ppm.desktop
%{_datadir}/applications/kde4/krita_xcf.desktop
%{_datadir}/applications/kde4/krita_odg.desktop
%{_datadir}/kde4/services/krita_bmp_export.desktop
%{_datadir}/kde4/services/krita_bmp_import.desktop
%{_datadir}/kde4/services/krita_gif_import.desktop
%{_datadir}/kde4/services/krita_jpeg_export.desktop
%{_datadir}/kde4/services/krita_jpeg_import.desktop
%{_datadir}/kde4/services/krita_ora_export.desktop
%{_datadir}/kde4/services/krita_ora_import.desktop
%{_datadir}/kde4/services/krita_png_export.desktop
%{_datadir}/kde4/services/krita_png_import.desktop
%{_datadir}/kde4/services/krita_ppm_export.desktop
%{_datadir}/kde4/services/krita_ppm_import.desktop
%{_datadir}/kde4/services/krita_xcf_import.desktop
%{_datadir}/kde4/services/krita_odg_import.desktop

%files krita-plugins
%defattr(-,root,root,-)
%{_datadir}/kde4/servicetypes/krita_brush.desktop
%{_datadir}/kde4/servicetypes/krita_dock.desktop
%{_datadir}/kde4/servicetypes/krita_filter.desktop
%{_datadir}/kde4/servicetypes/krita_generator.desktop
%{_datadir}/kde4/servicetypes/krita_paintop.desktop
%{_datadir}/kde4/servicetypes/krita_plugin.desktop
%{_datadir}/kde4/servicetypes/krita_tool.desktop

%{_libdir}/kde4/krita_colorspaces_extensions.so
%{_libdir}/kde4/kritabackgrounds.so
%{_libdir}/kde4/kritabigbrother.so
%{_libdir}/kde4/kritablurfilter.so
#%{_libdir}/kde4/kritabracketing2hdr.so
%{_libdir}/kde4/kritabumpmap.so
%{_libdir}/kde4/kritachalkpaintop.so
%{_libdir}/kde4/kritacolorgenerator.so
%{_libdir}/kde4/kritacolorrange.so
%{_libdir}/kde4/kritacolorselectorng.so
%{_libdir}/kde4/kritacolorsfilters.so
%{_libdir}/kde4/kritacolorspaceconversion.so
%{_libdir}/kde4/kritacomplexbrush.so
%{_libdir}/kde4/kritaconvolutionfilters.so
%{_libdir}/kde4/kritacurvepaintop.so
%{_libdir}/kde4/kritadefaultdockers.so
%{_libdir}/kde4/kritadefaultpaintops.so
%{_libdir}/kde4/kritadefaulttools.so
%{_libdir}/kde4/kritadeformpaintop.so
%{_libdir}/kde4/kritadigitalmixer.so
%{_libdir}/kde4/kritadodgeburn.so
%{_libdir}/kde4/kritadropshadow.so
%{_libdir}/kde4/kritadynapaintop.so
%{_libdir}/kde4/kritaembossfilter.so
%{_libdir}/kde4/kritaexample.so
%{_libdir}/kde4/kritaextensioncolorsfilters.so
%{_libdir}/kde4/kritaextensionsmanager.so
%{_libdir}/kde4/kritafastcolortransferfilter.so
%{_libdir}/kde4/kritafilterop.so
%{_libdir}/kde4/kritagridpaintop.so
%{_libdir}/kde4/kritahairypaintop.so
%{_libdir}/kde4/kritahatchingpaintop.so
%{_libdir}/kde4/kritahistogram.so
%{_libdir}/kde4/kritaimageenhancement.so
%{_libdir}/kde4/kritaimagesize.so
%{_libdir}/kde4/kritalayercompose.so
%{_libdir}/kde4/kritalevelfilter.so
%{_libdir}/kde4/kritametadataeditor.so
%{_libdir}/kde4/kritamodifyselection.so
%{_libdir}/kde4/kritamypaintpaintop.so
%{_libdir}/kde4/kritanoisefilter.so
%{_libdir}/kde4/kritaoilpaintfilter.so
%{_libdir}/kde4/kritaparticlepaintop.so
%{_libdir}/kde4/kritaphongbumpmap.so
%{_libdir}/kde4/kritapixelizefilter.so
%{_libdir}/kde4/kritapresetdocker.so
%{_libdir}/kde4/kritapsdexport.so
%{_libdir}/kde4/kritapsdimport.so
%{_libdir}/kde4/kritaraindropsfilter.so
%{_libdir}/kde4/kritarandompickfilter.so
%{_libdir}/kde4/kritarotateimage.so
%{_libdir}/kde4/kritaroundcornersfilter.so
%{_libdir}/kde4/kritarulerassistanttool.so
%{_libdir}/kde4/kritaselectiontools.so
%{_libdir}/kde4/kritaseparatechannels.so
%{_libdir}/kde4/kritashearimage.so
%{_libdir}/kde4/kritasketchpaintop.so
%{_libdir}/kde4/kritasmallcolorselector.so
%{_libdir}/kde4/kritasmalltilesfilter.so
%{_libdir}/kde4/kritasobelfilter.so
%{_libdir}/kde4/kritaspecificcolorselector.so
%{_libdir}/kde4/kritaspraypaintop.so
%{_libdir}/kde4/kritatogether.so
%{_libdir}/kde4/kritatonemapping.so
%{_libdir}/kde4/kritatoolcrop.so
%{_libdir}/kde4/kritatooldyna.so
%{_libdir}/kde4/kritatoolgrid.so
%{_libdir}/kde4/kritatoolperspectivegrid.so
%{_libdir}/kde4/kritatoolpolygon.so
%{_libdir}/kde4/kritatoolpolyline.so
%{_libdir}/kde4/kritatoolstar.so
%{_libdir}/kde4/kritatooltransform.so
%{_libdir}/kde4/kritatrianglecolorselector.so
%{_libdir}/kde4/kritaunsharpfilter.so
%{_libdir}/kde4/kritawavefilter.so
%{_datadir}/kde4/services/krita_colorselectorng.desktop
%{_datadir}/kde4/services/krita_colorspaces_extensions_plugin.desktop
%{_datadir}/kde4/services/krita_digitalmixer.desktop
%{_datadir}/kde4/services/krita_presetdocker.desktop
%{_datadir}/kde4/services/krita_smallcolorselector.desktop
%{_datadir}/kde4/services/krita_specificcolorselector.desktop
%{_datadir}/kde4/services/kritabackgrounds.desktop
%{_datadir}/kde4/services/kritabigbrother.desktop
%{_datadir}/kde4/services/kritablurfilter.desktop
#%{_datadir}/kde4/services/kritabracketing2hdr.desktop
%{_datadir}/kde4/services/kritabumpmapfilter.desktop
%{_datadir}/kde4/services/kritachalkpaintop.desktop
%{_datadir}/kde4/services/kritacolorgenerator.desktop
%{_datadir}/kde4/services/kritacolorrange.desktop
%{_datadir}/kde4/services/kritacolorsfilter.desktop
%{_datadir}/kde4/services/kritacolorspaceconversion.desktop
%{_datadir}/kde4/services/kritacomplexbrush.desktop
%{_datadir}/kde4/services/kritaconvolutionfilters.desktop
%{_datadir}/kde4/services/kritacurvepaintop.desktop
%{_datadir}/kde4/services/kritadefaultdockers.desktop
%{_datadir}/kde4/services/kritadefaultpaintops.desktop
%{_datadir}/kde4/services/kritadefaulttools.desktop
%{_datadir}/kde4/services/kritadeformpaintop.desktop
%{_datadir}/kde4/services/kritadodgeburn.desktop
%{_datadir}/kde4/services/kritadropshadow.desktop
%{_datadir}/kde4/services/kritadynapaintop.desktop
%{_datadir}/kde4/services/kritaembossfilter.desktop
%{_datadir}/kde4/services/kritaexample.desktop
%{_datadir}/kde4/services/kritaextensioncolorsfilters.desktop
%{_datadir}/kde4/services/kritaextensionsmanager.desktop
%{_datadir}/kde4/services/kritafastcolortransfer.desktop
%{_datadir}/kde4/services/kritafilterop.desktop
%{_datadir}/kde4/services/kritagridpaintop.desktop
%{_datadir}/kde4/services/kritahairypaintop.desktop
%{_datadir}/kde4/services/kritahatchingpaintop.desktop
%{_datadir}/kde4/services/kritahistogram.desktop
%{_datadir}/kde4/services/kritaimageenhancement.desktop
%{_datadir}/kde4/services/kritaimagesize.desktop
%{_datadir}/kde4/services/kritalayercompose.desktop
%{_datadir}/kde4/services/kritalevelfilter.desktop
%{_datadir}/kde4/services/kritametadataeditor.desktop
%{_datadir}/kde4/services/kritamodifyselection.desktop
%{_datadir}/kde4/services/kritamypaintpaintop.desktop
%{_datadir}/kde4/services/kritanoisefilter.desktop
%{_datadir}/kde4/services/kritaoilpaintfilter.desktop
%{_datadir}/kde4/services/kritapart.desktop
%{_datadir}/kde4/services/kritaparticlepaintop.desktop
%{_datadir}/kde4/services/kritaphongbumpmapfilter.desktop
%{_datadir}/kde4/services/kritapixelizefilter.desktop
%{_datadir}/kde4/services/kritaraindropsfilter.desktop
%{_datadir}/kde4/services/kritarandompickfilter.desktop
%{_datadir}/kde4/services/kritarotateimage.desktop
%{_datadir}/kde4/services/kritaroundcornersfilter.desktop
%{_datadir}/kde4/services/kritarulerassistanttool.desktop
%{_datadir}/kde4/services/kritaselectiontools.desktop
%{_datadir}/kde4/services/kritaseparatechannels.desktop
%{_datadir}/kde4/services/kritashearimage.desktop
%{_datadir}/kde4/services/kritasketchpaintop.desktop
%{_datadir}/kde4/services/kritasmalltilesfilter.desktop
%{_datadir}/kde4/services/kritasobelfilter.desktop
%{_datadir}/kde4/services/kritaspraypaintop.desktop
%{_datadir}/kde4/services/kritatogether.desktop
%{_datadir}/kde4/services/kritatonemapping.desktop
%{_datadir}/kde4/services/kritatoolcrop.desktop
%{_datadir}/kde4/services/kritatooldyna.desktop
%{_datadir}/kde4/services/kritatoolgrid.desktop
%{_datadir}/kde4/services/kritatoolperspectivegrid.desktop
%{_datadir}/kde4/services/kritatoolpolygon.desktop
%{_datadir}/kde4/services/kritatoolpolyline.desktop
%{_datadir}/kde4/services/kritatoolstar.desktop
%{_datadir}/kde4/services/kritatooltransform.desktop
%{_datadir}/kde4/services/kritatrianglecolorselector.desktop
%{_datadir}/kde4/services/kritaunsharpfilter.desktop
%{_datadir}/kde4/services/kritawavefilter.desktop
%{_libdir}/kde4/kritaexperimentpaintop.so
%{_datadir}/kde4/services/kritaexperimentpaintop.desktop
%{_libdir}/kde4/kritachanneldocker.so
%{_datadir}/kde4/services/krita_channeldocker.desktop

%files krita-data
%defattr(-,root,root,-)
%{_datadir}/color/icc/krita
%{kdedatadir}/apps/krita/backgrounds/old_paper.png
%{kdedatadir}/apps/krita/brushes
%{kdedatadir}/apps/krita/brushmodels
%{kdedatadir}/apps/krita/defaultpresets
%{kdedatadir}/apps/krita/gradients
%{kdedatadir}/apps/krita/icons
%{kdedatadir}/apps/krita/images
%{kdedatadir}/apps/krita/metadata
%{kdedatadir}/apps/krita/paintoppresets
%{kdedatadir}/apps/krita/palettes
%{kdedatadir}/apps/krita/patterns
%{kdedatadir}/apps/krita/pics
%{kdedatadir}/apps/krita/shaders
%{kdedatadir}/apps/krita/templates
%{kdedatadir}/apps/kritaplugins
%{kdedatadir}/apps/krita/dtd/krita.dtd
%{_datadir}/mime/packages/krita_ora.xml
%endif

%if 0%{?karbon}
%files karbon
%defattr(-,root,root,-)
%{_bindir}/karbon
%{_libdir}/kde4/karbonpart.so
%{_libdir}/libkarboncommon.so.*
%{_libdir}/libkarbonui.so.*
%{_libdir}/libkdeinit4_karbon.so
%{_datadir}/applications/kde4/karbon.desktop
%{kdedatadir}/apps/karbon/karbon.rc
%{kdedatadir}/apps/karbon/karbon_readonly.rc
%{kdedatadir}/config/karbonrc
%{_datadir}/kde4/services/karbonpart.desktop
%{_datadir}/kde4/servicetypes/karbon_module.desktop

%files karbon-plugins
%defattr(-,root,root,-)
%{_libdir}/kde4/karbon_flattenpathplugin.so
%{_libdir}/kde4/karbon_refinepathplugin.so
%{_libdir}/kde4/karbon_roundcornersplugin.so
%{_libdir}/kde4/karbon_whirlpinchplugin.so
%{_libdir}/kde4/karbonfiltereffects.so
%{_libdir}/kde4/karbontools.so
%{kdedatadir}/apps/karbon/kpartplugins/FlattenPathPlugin.rc
%{kdedatadir}/apps/karbon/kpartplugins/RefinePathPlugin.rc
%{kdedatadir}/apps/karbon/kpartplugins/RoundCornersPlugin.rc
%{kdedatadir}/apps/karbon/kpartplugins/WhirlPinchPlugin.rc
%{_datadir}/kde4/services/karbonfiltereffects.desktop
%{_datadir}/kde4/services/karbontools.desktop

%files karbon-filters
%defattr(-,root,root,-)
%{_libdir}/kde4/karbon1ximport.so
%{_libdir}/kde4/karbonpdfimport.so
%{_libdir}/kde4/karbonpngexport.so
%{_libdir}/kde4/karbonsvgexport.so
%{_libdir}/kde4/karbonsvgimport.so
%{_libdir}/kde4/wmfexport.so
%{_libdir}/kde4/wmfimport.so
%{_datadir}/kde4/services/karbon_1x_import.desktop
%{_datadir}/kde4/services/karbon_pdf_import.desktop
%{_datadir}/kde4/services/karbon_png_export.desktop
%{_datadir}/kde4/services/karbon_svg_export.desktop
%{_datadir}/kde4/services/karbon_svg_import.desktop
%{_datadir}/kde4/services/karbon_svgz_import.desktop
%{_datadir}/kde4/services/karbon_wmf_export.desktop
%{_datadir}/kde4/services/karbon_wmf_import.desktop

%files karbon-data
%defattr(-,root,root,-)
%{kdedatadir}/apps/karbon/gradients/*
%{kdedatadir}/apps/karbon/icons/hicolor/16x16
%{kdedatadir}/apps/karbon/icons/hicolor/22x22
%{kdedatadir}/apps/karbon/icons/oxygen/16x16

%files karbon-templates
%defattr(-,root,root,-)
%{kdedatadir}/apps/karbon/icons/hicolor/48x48/actions/template_empty.png
%{kdedatadir}/apps/karbon/icons/hicolor/scalable/actions/template_empty.svgz
%{kdedatadir}/apps/karbon/templates/Basic/
%endif

%if 0%{?kexi}
%files kexi
%defattr(-,root,root,-)
%endif

# %files kthesaurus
# %defattr(-,root,root,-)
# %{_datadir}/applications/kde4/KThesaurus.desktop
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
%{_libdir}/libpigmentcms.so.*
%{_libdir}/libkowidgets.so.*
%{_libdir}/libkotext.so.*
#%{_libdir}/libkoproperty.so.*
%{_libdir}/libkoplugin.so.*
%{_libdir}/libkopageapp.so.*
%{_libdir}/libkoodf.so.*
%{_libdir}/libkomain.so.*
%{_libdir}/libkochart.so.*
%{_libdir}/libkdchart.so.*
%{_libdir}/libkundo2.so*
%{_libdir}/libtextlayout.so*
%{_libdir}/libvectorimage.so*
%{_libdir}/libflake.so.*
%{_libdir}/libbasicflakes.so*
%{_libdir}/libRtfReader.so*
%{_libdir}/libkowidgetutils.so*

%{_libdir}/kde4/basicflakesplugin.so
%{_datadir}/kde4/services/basicflakesplugin.desktop
%{_libdir}/kde4/calligradocinfopropspage.so
%{_datadir}/kde4/services/calligradocinfopropspage.desktop

%{_datadir}/kde4/services/textdocumentinspection.desktop
%{_datadir}/kde4/servicetypes/calligra_chart.desktop
%{_datadir}/kde4/servicetypes/calligra_deferred_plugin.desktop
%{_datadir}/kde4/servicetypes/calligra_filter.desktop
%{_datadir}/kde4/servicetypes/calligra_part.desktop
%{_datadir}/kde4/servicetypes/calligradocker.desktop

%files filters-libs
%defattr(-,root,root,-)
%{_libdir}/libmsooxml.so.*
%{_datadir}/mime/packages/msooxml-all.xml

%files filters
%defattr(-,root,root,-)
#%{_bindir}/calligraconverter

%files words-filters
%defattr(-,root,root,-)
#%{_libdir}/libkwordexportfilters.so.*
%{_libdir}/libkowv2.so.*

%{_libdir}/kde4/applixwordimport.so
%{_datadir}/kde4/services/words_applixword_import.desktop

#%{_datadir}/kde4/services/kword_ascii_export.desktop
#%{_libdir}/kde4/asciiexport.so

%{_datadir}/kde4/services/words_ascii_import.desktop
%{_libdir}/kde4/asciiimport.so

%{_datadir}/kde4/services/words_docx_import.desktop
%{_libdir}/kde4/docximport.so

%{_datadir}/kde4/services/words_msword-odf_import.desktop
%{_libdir}/kde4/mswordodf_import.so

#%{_datadir}/kde4/services/kword_rtf_export.desktop
#%{_libdir}/kde4/rtfexport.so
%{_datadir}/kde4/services/words_rtf_import.desktop
%{_libdir}/kde4/rtfimport.so

%{_libdir}/kde4/exportMobi.so
%{_datadir}/kde4/services/words_Mobi_export.desktop
%{_libdir}/kde4/exportepub2.so
%{_datadir}/kde4/services/words_epub2_export.desktop
%{_libdir}/kde4/exporthtml.so
%{_datadir}/kde4/services/words_html_export.desktop

%files sheets-filters
%defattr(-,root,root,-)
%{_datadir}/kde4/services/kspread_xlsx_import.desktop
%{_libdir}/kde4/xlsximport.so

%{_datadir}/kde4/services/sheets_excel_thumbnail.desktop
%{_datadir}/kde4/services/sheets_xlsx_thumbnail.desktop
%{_datadir}/

%{_datadir}/kde4/services/kspread_excel_import.desktop
%{_libdir}/kde4/excelimporttodoc.so

%{_libdir}/kde4/applixspreadimport.so
%{_datadir}/kde4/services/kspread_applixspread_import.desktop

%{_libdir}/kde4/csvimport.so
%{_datadir}/kde4/services/kspread_csv_import.desktop

%{_libdir}/kde4/dbaseimport.so
%{_datadir}/kde4/services/kspread_dbase_import.desktop
%{_libdir}/kde4/gnumericexport.so
%{_datadir}/kde4/services/kspread_gnumeric_export.desktop
%{_libdir}/kde4/gnumericimport.so
%{_datadir}/kde4/services/kspread_gnumeric_import.desktop
%{_libdir}/kde4/opencalcexport.so
%{_datadir}/kde4/services/kspread_opencalc_export.desktop
%{_libdir}/kde4/opencalcimport.so
%{_datadir}/kde4/services/kspread_opencalc_import.desktop
%{_libdir}/kde4/qproimport.so
%{_datadir}/kde4/services/kspread_qpro_import.desktop


%files stage-filters
%defattr(-,root,root,-)
%{_datadir}/kde4/services/kpresenter_powerpoint_import.desktop
%{_libdir}/kde4/powerpointimport.so

%{_datadir}/kde4/services/kpresenter_pptx_import.desktop
%{_libdir}/kde4/pptximport.so

%{_datadir}/kde4/services/Filterkpr2odf.desktop
%{_libdir}/kde4/Filterkpr2odf.so

%files plugins
%defattr(-,root,root,-)
%{_datadir}/kde4/servicetypes/pigment.desktop
%{_datadir}/kde4/servicetypes/pigmentextension.desktop
%{_datadir}/kde4/servicetypes/scripteventaction.desktop
%{_datadir}/kde4/servicetypes/texteditingplugin.desktop
%{_datadir}/kde4/servicetypes/textvariableplugin.desktop
#%{_datadir}/kde4/servicetypes/koplugin.desktop

#maybe have the next two in -filters instead?
#%{_datadir}/kde4/servicetypes/kofilter.desktop
#%{_datadir}/kde4/servicetypes/kofilterwrapper.desktop

%{_datadir}/kde4/servicetypes/filtereffect.desktop
%{_datadir}/kde4/servicetypes/flake.desktop
%{_datadir}/kde4/servicetypes/flakedevice.desktop
%{_datadir}/kde4/servicetypes/flakeshape.desktop
%{_datadir}/kde4/servicetypes/flaketool.desktop
%{_datadir}/kde4/servicetypes/inlinetextobject.desktop
#%{_datadir}/kde4/servicetypes/kochart.desktop
#%{_datadir}/kde4/servicetypes/kofficedocker.desktop
#%{_datadir}/kde4/servicetypes/kofficepart.desktop

#%{_datadir}/kde4/services/treeshape.desktop
#%{_libdir}/kde4/treeshape.so

#%{_datadir}/kde4/services/vectorshape.desktop
#%{_libdir}/kde4/vectorshape.so

# %{_datadir}/kde4/services/videoshape.desktop
# %{_libdir}/kde4/videoshape.so

%{_datadir}/kde4/services/textshape.desktop
%{_libdir}/kde4/textshape.so

%{_datadir}/kde4/services/textvariables.desktop
%{_libdir}/kde4/textvariables.so

%{_datadir}/kde4/services/pathshapes.desktop
%{_libdir}/kde4/pathshapes.so

%{_datadir}/kde4/services/pictureshape.desktop
%{_libdir}/kde4/pictureshape.so

%{_datadir}/kde4/services/pluginshape.desktop
%{_libdir}/kde4/pluginshape.so

# maybe needs to be its own package
%{_datadir}/kde4/services/spreadsheetshape.desktop
%{_libdir}/kde4/spreadsheetshape.so

%{_datadir}/kde4/services/chartshape.desktop
%{_libdir}/libchartshapelib.so.*
%{_libdir}/kde4/chartshape.so

%{_datadir}/kde4/services/defaulttools.desktop
%{_libdir}/kde4/defaulttools.so

%{_datadir}/kde4/services/kchartpart.desktop

#%{_datadir}/kde4/services/kodocinfopropspage.desktop
#%{_libdir}/kde4/kodocinfopropspage.so

#%{_datadir}/kde4/services/kofficethumbnail.desktop
#%{_libdir}/kde4/kofficethumbnail.so

%{_datadir}/kde4/services/kopabackgroundtool.desktop
%{_libdir}/kde4/kopabackgroundtool.so

# staging
#%{kdedatadir}/apps/kpresenter/kpartplugins/googledocs-kpresenter.rc
#%{kdedatadir}/apps/kword/kpartplugins/googledocs-kword.rc
#%{_libdir}/kde4/kofficegoogledocs.so

%files data
%defattr(-,root,root,-)
%{_datadir}/kde4/servicetypes/calligra_application.desktop
%{kdedatadir}/apps/calligra/calligra_shell.rc
%{kdedatadir}/apps/calligra/icons
%{kdedatadir}/apps/calligra/palettes
%{kdedatadir}/apps/calligra/styles
%{_datadir}/icons
%if 0%{?freoffice}
%exclude %{_datadir}/icons/hicolor/64x64/apps/freoffice.png
%exclude %{_datadir}/icons/hicolor/178x200/apps/freoffice.png
%exclude %{_datadir}/icons/hicolor/48x48/hildon/Document.png
%exclude %{_datadir}/icons/hicolor/48x48/hildon/Presenter.png
%exclude %{_datadir}/icons/hicolor/48x48/hildon/SpreadSheet.png
%endif
#%{kdedatadir}/apps/koproperty/icons/hicolor/16x16/actions/button_no.png

%files konqi-servicemenus
%defattr(-,root,root,-)
# %{_datadir}/kde4/services/ServiceMenus/karbon_konqi.desktop
# %{_datadir}/kde4/services/ServiceMenus/kchart_konqi.desktop
# %{_datadir}/kde4/services/ServiceMenus/kformula_konqi.desktop
# %{_datadir}/kde4/services/ServiceMenus/kivio_konqi.desktop
# %{_datadir}/kde4/services/ServiceMenus/kpresenter_konqi.desktop
# %{_datadir}/kde4/services/ServiceMenus/krita_konqi.desktop
# %{_datadir}/kde4/services/ServiceMenus/kspread_konqi.desktop
# %{_datadir}/kde4/services/ServiceMenus/kword_konqi.desktop
# konqi-templates
%{_datadir}/templates/TextDocument.desktop
%{_datadir}/templates/.source/TextDocument.odt
%{_datadir}/templates/SpreadSheet.desktop
%{_datadir}/templates/.source/SpreadSheet.ods
%{_datadir}/templates/Presentation.desktop
%{_datadir}/templates/.source/Presentation.odp
%{_datadir}/templates/Illustration.desktop
%{_datadir}/templates/.source/Illustration.odg


%files devel
%defattr(-,root,root,-)
%{kdedatadir}/apps/cmake/modules/FindCalligraLibs.cmake
%{_includedir}/*
%{_libdir}/libchartshapelib.so
%{_libdir}/libflake.so
%{_libdir}/libkdchart.so
%{_libdir}/libkochart.so
%{_libdir}/libkomain.so
%{_libdir}/libkoodf.so
%{_libdir}/libkopageapp.so
%{_libdir}/libkoplugin.so
#%{_libdir}/libkoproperty.so
%{_libdir}/libkotext.so
%{_libdir}/libkowidgets.so
%{_libdir}/libkowv2.so
%{_libdir}/libcalligrastageprivate.so
%{_libdir}/libcalligrasheetscommon.so
%{_libdir}/libcalligrasheetsodf.so
#%{_libdir}/libkwordexportfilters.so
%{_libdir}/libwordsprivate.so
%{_libdir}/libmsooxml.so
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
%setup -q -c -n %{name}-%{version}/calligra

%build
mkdir build && cd build
cmake \
    -DPRODUCTSET=Libraries \
    -DKDE4_BUILD_TESTS=OFF \
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
rm -Rf %{buildroot}
cd build
make install DESTDIR=%{buildroot}

#cp ../debian/defaults/ksycoca4 %{buildroot}%{_datadir}/kde4/services/
mkdir -p %{buildroot}/%{_datadir}/applications

%if 0%{?freoffice}
mv %{buildroot}/%{_datadir}/applications/hildon/freoffice.desktop %{buildroot}/%{_datadir}/applications/
%endif


%clean
rm -Rf %{buildroot}
