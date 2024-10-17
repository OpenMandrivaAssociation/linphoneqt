Name:		linphoneqt
Version:	4.1.1
Release:	2
Summary:	Voice over IP Application
License:	GPLv2+
Group:		Communications
URL:		https://www.linphone.org
Source0:	https://linphone.org/releases/sources/linphoneqt/linphoneqt-%{version}.tar.gz
Source1:	https://linphone.org/releases/sources/linphoneqt/linphoneqt-%{version}.tar.gz.md5
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Linphone)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	bctoolbox-static-devel
BuildRequires:	pkgconfig(bctoolbox)
Requires:	mediastreamer >= 1:2.16.1
Requires:	qt5-qtdeclarative
Requires:	qt5-qtquickcontrols2
Requires:	qt5-qtquickcontrols
Requires:	qt5-qtgraphicaleffects
Provides:	linphone = %{version}-%{release}
Obsoletes:	linphone < 4.1.1

%description
Linphone is a free VoIP and video softphone based on the SIP protocol.

%prep
%setup -q

# Fix build
sed -i -e 's,LINPHONE_QT_GIT_VERSION,"%{version}",' src/app/AppController.cpp

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc README.md CHANGELOG.md LICENSE
%{_bindir}/linphone
%{_bindir}/linphone-tester
%{_datadir}/applications/linphone.desktop
%{_iconsdir}/hicolor/scalable/apps/linphone.svg
%{_datadir}/linphone/
