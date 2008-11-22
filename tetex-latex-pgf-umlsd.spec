
%define short_name pgf-umlsd
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Some LaTeX macros for UML Sequence Diagrams
Summary(hu.UTF-8):	Néhány LaTeX makró UML diagramok rajzolásához
Name:		tetex-latex-%{short_name}
Version:	0.3
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
URL:		http://code.google.com/p/pgf-umlsd/
Source0:	http://pgf-umlsd.googlecode.com/files/pgf-umlsd-%{version}.tar.gz
# Source0-md5:	4e9102376c12ea27c8b6d253d35b4f8a
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-pgf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some LaTeX macros for UML Sequence Diagrams.

%description -l hu.UTF-8
Néhány LaTeX makró UML diagramok rajzolásához.

%prep
%setup -q -n %{short_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}
install %{short_name}-demo.pdf %{short_name}-demo.tex $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/doc/latex/%{short_name}
