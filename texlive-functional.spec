%global tl_name functional
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2024C
Release:	%{tl_revision}.1
Summary:	An intuitive functional programming interface for LaTeX2
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/functional
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/functional.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/functional.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an intuitive functional programming interface for
LaTeX2, which is an alternative choice to expl3 or LuaTeX, if you want
to do programming in LaTeX. Although there are functions in LaTeX3
programming layer (expl3), the evaluation of them is from outside to
inside. With this package, the evaluation of functions is from inside to
outside, which is the same as other programming languages such as Lua.
In this way, it is rather easy to debug code too.

