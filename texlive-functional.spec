Name:		texlive-functional
Version:	69929
Release:	1
Summary:	Provide an intuitive functional programming interface for LaTeX2
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/functional
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/functional.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/functional.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an intuitive functional programming
interface for LaTeX2, which is an alternative choice to expl3
or LuaTeX, if you want to do programming in LaTeX. Although
there are functions in LaTeX3 programming layer (expl3), the
evaluation of them is from outside to inside. With this
package, the evaluation of functions is from inside to outside,
which is the same as other programming languages such as Lua.
In this way, it is rather easy to debug code too.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/functional
%doc %{_texmfdistdir}/doc/latex/functional

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
