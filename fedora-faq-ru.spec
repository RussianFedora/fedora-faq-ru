Name: fedora-faq-ru
Version: 2018.10.22
Release: 1%{?dist}

License: CC-BY
URL: https://github.com/xvitaly/%{name}
Summary: Fedora FAQ in russian

Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: python3
BuildRequires: python3-sphinx

%description
We decided to find and document answers to the most of the frequently asked
questions from our conferences about Fedora for convenience of end users.

%prep
%autosetup

%build
make html

%install


%files
%license LICENSE
%doc build/html/*

%changelog
* Mon Oct 22 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.10.22-1
- Initial SPEC release.
