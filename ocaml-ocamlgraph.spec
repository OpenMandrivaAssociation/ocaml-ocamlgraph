Name:           ocaml-ocamlgraph
Version:        1.8.1
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
BuildRequires:  gtk2-devel libgnomecanvas2-devel

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

