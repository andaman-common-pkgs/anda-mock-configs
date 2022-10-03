Name:           anda-mock-configs
Version:        2.1
Release:        1%{?dist}
Summary:        Mock configs for Fedora Extras

License:        MIT
URL:            http://fedoraproject.org/wiki/Extras
Source0:        anda.tpl
Source1:        anda-37-x86_64.cfg

BuildRequires:  mock-core-configs
Requires:       mock-core-configs
BuildArch:      noarch


%description
%{summary}

%prep


%build



%install
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates


cp -v %{SOURCE0} %{buildroot}%{_sysconfdir}/mock/templates/
cp -v %{SOURCE1} %{buildroot}%{_sysconfdir}/mock/

%files
%{_sysconfdir}/mock/templates/anda.tpl
%{_sysconfdir}/mock/anda-37-x86_64.cfg

%changelog
* Mon Oct 03 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Intial Release
