Name: fedora-faq-ru
Version: 2020.05.30
Release: 1%{?dist}

License: CC-BY-SA
URL: https://github.com/RussianFedora/FAQ
Summary: Fedora FAQ in russian
BuildArch: noarch

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop

BuildRequires: python3
BuildRequires: python3-sphinx
BuildRequires: desktop-file-utils

BuildRequires: latexmk
BuildRequires: texlive-cmap
BuildRequires: texlive-metafont-bin
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-babel-russian
BuildRequires: texlive-hyphen-russian
BuildRequires: texlive-titling
BuildRequires: texlive-fancyhdr
BuildRequires: texlive-titlesec
BuildRequires: texlive-tabulary
BuildRequires: texlive-framed
BuildRequires: texlive-wrapfig
BuildRequires: texlive-parskip
BuildRequires: texlive-upquote
BuildRequires: texlive-capt-of
BuildRequires: texlive-needspace
BuildRequires: texlive-collection-langcyrillic
BuildRequires: texlive-cyrillic-bin
BuildRequires: texlive-cmcyr
BuildRequires: texlive-cyrillic-bin-bin
BuildRequires: texlive-fncychap
BuildRequires: texlive-xetex
BuildRequires: dejavu-sans-fonts
BuildRequires: dejavu-serif-fonts
BuildRequires: dejavu-sans-mono-fonts
BuildRequires: texlive-polyglossia
BuildRequires: texlive-xindy

%description
We decided to find and document answers to the most of the frequently asked
questions from our conferences about Fedora for convenience of end users.

%prep
%autosetup -n FAQ-%{version}

%build
make html
make latexpdf

%install
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{SOURCE1}

%files
%license LICENSE
%doc build/html/*
%doc build/latex/%{name}.pdf
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat May 30 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.05.30-1
- Updated to version 2020.05.30.

* Thu Apr 30 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.04.30-1
- Updated to version 2020.04.30.

* Mon Mar 30 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.03.30-1
- Updated to version 2020.03.30.

* Sat Feb 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.02.29-1
- Updated to version 2020.02.29.

* Thu Jan 30 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.01.30-1
- Updated to version 2020.01.30.

* Mon Dec 30 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.12.30-1
- Updated to version 2019.12.30.

* Sat Nov 30 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.11.30-1
- Updated to version 2019.11.30.

* Wed Oct 30 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.10.30-1
- Updated to version 2019.10.30.

* Mon Sep 30 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.09.30-1
- Updated to version 2019.09.30.

* Fri Aug 30 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.08.30-1
- Updated to version 2019.08.30.

* Wed Jul 31 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.07.31-1
- Updated to version 2019.07.31.

* Sun Jun 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.06.23-1
- Updated to version 2019.06.23.

* Sat May 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.05.25-1
- Updated to version 2019.05.25.

* Sun May 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.05.12-1
- Updated to version 2019.05.12.

* Thu Apr 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.04.25-1
- Updated to version 2019.04.25.

* Fri Apr 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.04.12-1
- Updated to version 2019.04.12.

* Mon Mar 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.03.25-1
- Updated to version 2019.03.25.

* Sun Mar 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.03.10-1
- Updated to version 2019.03.10.

* Mon Feb 18 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.02.18-1
- Updated to version 2019.02.18.

* Fri Jan 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.01.25-1
- Updated to version 2019.01.25.

* Tue Dec 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.12.25-1
- Updated to version 2018.12.25.

* Thu Oct 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.10.25-1
- Updated to version 2018.10.25.

* Mon Oct 22 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.10.22-1
- Initial SPEC release.
