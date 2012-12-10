Name:           fslint
Version:        2.42
Release:	%mkrel 1
Summary:       	An utility to find and clean "lint" on a filesystem
Group:          File tools 
License:        GPLv2+
URL:            http://www.pixelbeat.org/fslint/
Source0:        http://www.pixelbeat.org/fslint/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildArch:      noarch
BuildRequires:  gettext, desktop-file-utils
Requires:       python >= 0:2.0, pygtk2.0, pygtk2.0-libglade, cpio

%description
FSlint is a toolkit to find all redundant disk usage (duplicate files
for e.g.). It includes a GUI as well as a command line interface.


%prep
%setup -q 
%{__perl} -pi -e 's|^liblocation=.*$|liblocation="%{_datadir}/%{name}" #RPM edit|' fslint-gui
%{__perl} -pi -e 's|^locale_base=.*$|locale_base=None #RPM edit|' fslint-gui


%build
# Not.


%install
rm -rf %buildroot
install -Dpm 755 fslint-gui %buildroot%{_bindir}/fslint-gui
install -dm 755 %buildroot%{_datadir}/%{name}/%{name}/{fstool,supprt}
install -dm 755 %buildroot%{_datadir}/%{name}/%{name}/supprt/rmlint
install -dm 755 %buildroot%{_mandir}/man1
install -pm 644 fslint.glade fslint_icon.png \
  %buildroot%{_datadir}/%{name}
install -dm 755 %buildroot%{_datadir}/pixmaps
ln -s %{_datadir}/%{name}/fslint_icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -pm 755 fslint/{find*,fslint,zipdir} \
  %buildroot%{_datadir}/%{name}/fslint
install -pm 755 fslint/fstool/* \
  %buildroot%{_datadir}/%{name}/fslint/fstool
install -pm 644 fslint/supprt/fslver \
  %buildroot%{_datadir}/%{name}/fslint/supprt
install -pm 755 fslint/supprt/get* \
  %buildroot%{_datadir}/%{name}/fslint/supprt
install -pm 755 fslint/supprt/rmlint/* \
  %buildroot%{_datadir}/%{name}/fslint/supprt/rmlint

cp -a man/* \
  %buildroot%{_mandir}/man1/

make -C po DESTDIR=%buildroot LOCALEDIR=%{_datadir}/locale install

desktop-file-install \
  --vendor author \
  --dir %buildroot%{_datadir}/applications \
  --mode 644 \
  %{name}.desktop

%find_lang %{name}


%clean
rm -rf %buildroot


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc doc/*
%{_mandir}/man1/fslint*
%{_bindir}/fslint-gui
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/fslint_icon.png



%changelog
* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 2.42-1mdv2011.0
+ Revision: 645174
- update to new version 2.42

* Mon Sep 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.16-2mdv2011.0
+ Revision: 576367
- Fix summary

* Mon Sep 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.16-1mdv2011.0
+ Revision: 576337
- fix group
- import fslint

