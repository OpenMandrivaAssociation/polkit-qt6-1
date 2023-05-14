%define major 1
%define	oname polkit-qt-1
%define git 20230513

Summary:	Library that allows developer to access PolicyKit-1 API
Name:		polkit-qt6-1
Version:	0.114.1
Release:	%{?git:0.%{git}.}1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/libraries/polkit-qt-1
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/polkit-qt-1/-/archive/master/polkit-qt-1-master.tar.bz2#/polkit-qt-1-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/stable/polkit-qt-1/%{oname}-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6)
BuildRequires:	pkgconfig(polkit-agent-1)

%description
Polkit-qt is a library that allows developer to access PolicyKit-1
API with a nice Qt-style API

#-----------------------------------------------------------------------------
%define libpolkit_qt6_core_1 %mklibname polkit-qt6-core-1_ %{major}

%package -n %{libpolkit_qt6_core_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Provides:	polkit-agent

%description -n %{libpolkit_qt6_core_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt6_core_1}
%{_libdir}/libpolkit-qt6-core-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt6_gui_1 %mklibname polkit-qt6-gui-1_ %{major}

%package -n %{libpolkit_qt6_gui_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries

%description -n %{libpolkit_qt6_gui_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt6_gui_1}
%{_libdir}/libpolkit-qt6-gui-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt6_agent_1 %mklibname polkit-qt6-agent-1_ %{major}

%package -n %{libpolkit_qt6_agent_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries

%description -n %{libpolkit_qt6_agent_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt6_agent_1}
%{_libdir}/libpolkit-qt6-agent-1.so.%{major}*

#-----------------------------------------------------------------------------

%package   devel
Summary:	Devel stuff for polkit-Qt
Group:		Development/KDE and Qt
Requires:	%{libpolkit_qt6_core_1} = %{version}-%{release}
Requires:	%{libpolkit_qt6_gui_1} = %{version}-%{release}
Requires:	%{libpolkit_qt6_agent_1} = %{version}-%{release}

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_includedir}/polkit-qt6-1
%{_libdir}/libpolkit-qt6-agent-1.so
%{_libdir}/libpolkit-qt6-core-1.so
%{_libdir}/libpolkit-qt6-gui-1.so
%{_libdir}/pkgconfig/polkit-qt6-1.pc
%{_libdir}/pkgconfig/polkit-qt6-agent-1.pc
%{_libdir}/pkgconfig/polkit-qt6-core-1.pc
%{_libdir}/pkgconfig/polkit-qt6-gui-1.pc
%{_libdir}/cmake/PolkitQt6-1/*.cmake

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{?git:master}%{!?git:%{version}}

%build
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
