Name:           nrf-udev
Version:        1.0.1
Release:        1%{?dist}
Summary:        udev rules for nRF (Nordic Semiconductor) development kits
BuildArch:      noarch

License:        None
URL:            https://github.com/NordicSemiconductor/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       udev

%description
udev rules for nRF (Nordic Semiconductor) development kits


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d
cp nrf-udev_1.0.1-all/lib/udev/rules.d/71-nrf.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/
cp nrf-udev_1.0.1-all/lib/udev/rules.d/99-mm-nrf-blacklist.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/


%files
%{_prefix}/lib/udev/rules.d/71-nrf.rules
%{_prefix}/lib/udev/rules.d/99-mm-nrf-blacklist.rules


%changelog
* Fri May 10 2024 Leon Rinkel <leon@rinkel.me> - 1.0.1-1
- initial release
