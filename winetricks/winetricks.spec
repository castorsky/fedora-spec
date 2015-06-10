Name:           winetricks
Version:        20150416
Release:        2%{?dist}
Summary:        Winetricks is an easy way to work around problems in Wine.
BuildArch:      noarch

Group:          -
License:        -
URL:            https://github.com/Winetricks/winetricks
Source0:        %{name}-%{version}.tar.gz

#BuildRequires: 
Requires:       wine
Requires:       cabextract

%description
It has a menu of supported games/apps for which it can do all the workarounds
automatically. It also lets you install missing DLLs or tweak various Wine
settings individually.


%prep
%setup -q


%build


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/winetricks
%doc %{_mandir}



%changelog
