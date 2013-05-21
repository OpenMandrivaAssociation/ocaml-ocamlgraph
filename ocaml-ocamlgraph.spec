%define debug_package          %{nil}

Name:           ocaml-ocamlgraph
Version:        1.8.2
Release:        1
Summary:        OCaml library for arc and node graphs

Group:          Development/Other
License:        LGPLv2 with exceptions

URL:            http://ocamlgraph.lri.fr/
Source0:        http://ocamlgraph.lri.fr/download/ocamlgraph-%{version}.tar.gz
Source1:        ocamlgraph-test.result

ExcludeArch:    sparc64 s390 s390x
BuildRequires:  ocaml >= 3.08 ocaml-findlib-devel ocaml-doc
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  pkgconfig(gtk+-2.0) libgnomecanvas2-devel

%description
Ocamlgraph provides several different implementations of graph data
structures. It also provides implementations for a number of classical
graph algorithms like Kruskal's algorithm for MSTs, topological
ordering of DAGs, Dijkstra's shortest paths algorithm, and
Ford-Fulkerson's maximal-flow algorithm to name a few. The algorithms
and data structures are written functorially for maximal
reusability. Also has input and output capability for Graph Modeling
Language file format and Dot and Neato graphviz (graph visualization)
tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{EVRD}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocamlgraph-%{version}
cp %{SOURCE1} .

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}

make depend
make all OCAMLBEST=opt OCAMLOPT=ocamlopt.opt
make doc

%check
make --no-print-directory check >& test
diff test ocamlgraph-test.result

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
make OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml install-findlib

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}/
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}-devel/examples/
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}-devel/API/
cp -p LICENSE %{buildroot}%{_defaultdocdir}/%{name}-%{version}/
cp -p README %{buildroot}%{_defaultdocdir}/%{name}-%{version}-devel/
cp -p examples/*.ml %{buildroot}%{_defaultdocdir}/%{name}-%{version}-devel/examples/
cp -p doc/* %{buildroot}%{_defaultdocdir}/%{name}-%{version}-devel/API/

%files
%{_libdir}/ocaml/ocamlgraph/
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.mli
%{_defaultdocdir}/%{name}-%{version}/LICENSE

%files devel
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.mli
# Include all code and examples in the doc directory
%{_defaultdocdir}/%{name}-%{version}-devel/



%changelog
* Thu May 10 2012 Crispin Boylan <crisb@mandriva.org> 1.8.1-1
+ Revision: 797971
- New release

* Sun Apr 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.7-2
+ Revision: 652401
- fix buildrequires

* Thu Apr 07 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.7-1
+ Revision: 651775
- imported package ocaml-ocamlgraph

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdv2011.0
+ Revision: 613134
- the mass rebuild of 2010.1 packages

* Mon Aug 10 2009 Florent Monnier <blue_prawn@mandriva.org> 1.1-1mdv2010.0
+ Revision: 413683
- new tarball
- new version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdv2010.0
+ Revision: 390297
- rebuild

* Tue Feb 03 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0-2mdv2010.0
+ Revision: 337142
- The initial RPM release was made from the fedora rpm .spec file (revision 1.4) by Richard W.M. Jones

* Fri Jan 09 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0-1mdv2009.1
+ Revision: 327773
- import ocaml-ocamlgraph

