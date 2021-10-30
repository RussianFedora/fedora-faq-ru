Name: fedora-faq-ru
Version: 2021.10.30
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
BuildRequires: make

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
* Sat Oct 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.10.30-1
- Updated to version 2021.10.30.
