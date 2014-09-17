# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kparts

# >> macros
# << macros

# >> bcond_with
# << bcond_with

# >> bcond_without
# << bcond_without

Summary:    KDE Frameworks 5 Tier 3 solution for KParts
Version:    5.2.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kparts.yaml
Source101:  kparts-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  knotifications-devel
BuildRequires:  kservice-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel

%description
KDE Frameworks 5 Tier 3 solution for KParts


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kconfig-devel
Requires:   kcoreaddons-devel
Requires:   ki18n-devel
Requires:   kiconthemes-devel
Requires:   kio-devel
Requires:   kjobwidgets-devel
Requires:   knotifications-devel
Requires:   kservice-devel
Requires:   ktextwidgets-devel
Requires:   kwidgetsaddons-devel
Requires:   kxmlgui-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md AUTHORS
%{_kf5_libdir}/libKF5Parts.so.*
%{_kf5_servicetypesdir}/*.desktop
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kparts_version.h
%{_kf5_includedir}/KParts
%{_kf5_libdir}/libKF5Parts.so
%{_kf5_cmakedir}/KF5Parts
%{_kf5_mkspecsdir}/*.pri
# >> files devel
# << files devel
