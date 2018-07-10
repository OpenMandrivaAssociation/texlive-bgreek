# revision 15878
# category Package
# catalog-ctan /language/greek/bgreek
# catalog-date 2009-02-21 22:05:10 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-bgreek
Version:	0.3
Release:	11
Summary:	Using Beccari's fonts in betacode for classical Greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/bgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bgreek.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a dialect of the Beta Code encoding
(TLG and Perseus Projects) for typesetting classical Greek
using Claudio Beccari's Greek Fonts. The package provides
virtual fonts, to reference Beccari's fonts in bgreek mode, and
support macros for use with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmn2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgmo2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxn2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bgxo2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmn2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqmo2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxn2488.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo0500.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo0600.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo0700.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo0800.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo0900.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo1000.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo1095.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo1200.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo1440.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo1728.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo2074.tfm
%{_texmfdistdir}/fonts/tfm/public/bgreek/bqxo2488.tfm
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmc2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmn2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgmo2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxc2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxn2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bgxo2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmc2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmn2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqmo2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxc2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxn2488.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo0500.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo0600.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo0700.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo0800.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo0900.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo1000.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo1095.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo1200.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo1440.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo1728.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo2074.vf
%{_texmfdistdir}/fonts/vf/public/bgreek/bqxo2488.vf
%{_texmfdistdir}/tex/latex/bgreek/bcgcmr.fd
%{_texmfdistdir}/tex/latex/bgreek/bcgenc.def
%{_texmfdistdir}/tex/latex/bgreek/bcglmr.fd
%{_texmfdistdir}/tex/latex/bgreek/bcqcmr.fd
%{_texmfdistdir}/tex/latex/bgreek/bcqenc.def
%{_texmfdistdir}/tex/latex/bgreek/bcqlmr.fd
%{_texmfdistdir}/tex/latex/bgreek/bgfonts.tex
%{_texmfdistdir}/tex/latex/bgreek/bgreek.ldf
%{_texmfdistdir}/tex/latex/bgreek/bgreek.sty
%{_texmfdistdir}/tex/latex/bgreek/ibygreek.ldf
%doc %{_texmfdistdir}/doc/latex/bgreek/MANIFEST.TXT
%doc %{_texmfdistdir}/doc/latex/bgreek/README
%doc %{_texmfdistdir}/doc/latex/bgreek/bgman.pdf
%doc %{_texmfdistdir}/doc/latex/bgreek/bgman.tex
%doc %{_texmfdistdir}/doc/latex/bgreek/bgreek.etx
%doc %{_texmfdistdir}/doc/latex/bgreek/cbgreek.etx
%doc %{_texmfdistdir}/doc/latex/bgreek/qbgreek.etx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 749599
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 717913
- texlive-bgreek
- texlive-bgreek
- texlive-bgreek
- texlive-bgreek
- texlive-bgreek

