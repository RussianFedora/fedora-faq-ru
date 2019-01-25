Name: fedora-faq-ru
Version: 2019.01.25
Release: 1%{?dist}

License: CC-BY-SA
URL: https://github.com/RussianFedora/FAQ
Summary: Fedora FAQ in russian
BuildArch: noarch

Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
* Fri Jan 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.01.25-1
- Updated to version 2019.01.25.

* Tue Dec 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.12.25-1
- Updated to version 2018.12.25.

* Thu Oct 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.10.25-1
- Updated to version 2018.10.25.

* Mon Oct 22 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.10.22-1
- Initial SPEC release.
