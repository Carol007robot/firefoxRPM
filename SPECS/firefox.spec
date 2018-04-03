Name:	firefox	
Version: 59.0.2	
Release: 1%{?dist}
Summary: Firefox 59.0.2 build

Group:	Applications/Internet	
License: MPL/LGPL
URL:	http://www.mozilla.org/products/firefox/

BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Source0: firefox-59.0.2.tar.bz2
Source1: firefox.png
Source2: firefox.desktop

AutoReqProv     : No

#BuildRequires:	
#Requires:	

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%prep
rm -rf %{buildroot}
%setup -c -q

%install
#make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_libdir}
cp -a %{name} %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
cp -a %{SOURCE2} %{buildroot}%{_datadir}/applications
cp -a %{SOURCE1} %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/%{name}/firefox %{buildroot}%{_bindir}/firefox
ln -s %{_libdir}/%{name}/firefox-bin %{buildroot}%{_bindir}/firefox-bin

%files
%defattr(-, root, root)
%{_libdir}/%{name}
%{_datadir}/applications/firefox.desktop
%{_datadir}/pixmaps/firefox.png
%{_bindir}/firefox
%{_bindir}/firefox-bin

%clean
rm -rf %{buildroot}


%changelog
