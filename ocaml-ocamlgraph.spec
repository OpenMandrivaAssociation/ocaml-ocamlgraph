# Note: rpmlint complains that this package is not marked as
# noarch. This is not really an error as this is current standard
# practice for OCaml libraries even though they do not contain
# architecture dependent files themselves (the devel packages do
# instead).
#
# See https://www.redhat.com/archives/fedora-packaging/2008-August/msg00017.html
# for a discussion and
# https://www.redhat.com/archives/fedora-packaging/2008-August/msg00020.html
# for a potential fix. However, this is probably not the time and
# place to try to change the standard practice, so for now I will
# follow standard practice.
# -- rjones

Name:           ocaml-ocamlgraph
Version:        1.0
Release:        %mkrel 1

Summary:        OCaml library for arc and node graphs
Group:          Development/Other
License:        LGPLv2 with exceptions

URL:            http://ocamlgraph.lri.fr/
Source0:        http://ocamlgraph.lri.fr/download/ocamlgraph-%{version}.tar.bz2
Source1:        ocamlgraph-test.result
Source2:        http://www.lri.fr/~filliatr/ftp/publis/ocamlgraph.ps.bz2
Patch0:         ocamlgraph-1.0-no-view-graph-doc.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml >= 3.08
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libgnomecanvas2-devel

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
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Development/Other

%description    doc
The %{name}-doc package contains the documentation for developing
applications that use %{name}.

%prep
%setup -q -n ocamlgraph-%{version}

%patch0 -p1

cp %{SOURCE1} ./
cp %{SOURCE2} ./


%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
echo ./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir} > /tmp/log

make opt byte viewer editor doc

bunzip2 ocamlgraph.ps.bz2
gzip --best ocamlgraph.ps

%check
make --no-print-directory check >& test
diff test ocamlgraph-test.result


%install
rm -rf %{buildroot}

%define ocaml_destdir %{_libdir}/ocaml

mkdir -p %{buildroot}/%{_usr}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}
mkdir -p %{buildroot}/%{ocaml_destdir}
mkdir -p %{buildroot}/%{ocaml_destdir}/ocamlgraph

make install \
  OCAMLLIB=%{buildroot}/%{ocaml_destdir}/ocamlgraph \
  prefix=%{buildroot}/%{_usr} \
  MANDIR=%{buildroot}/%{_mandir}

mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/examples/
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/API/

cp -p LICENSE  %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/
cp -p README  %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/
cp -p ocamlgraph.ps.gz  %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/
cp -p examples/*.ml  %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/examples/
cp -p doc/*  %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/API/

cp -p src/*.mli %{buildroot}/%{ocaml_destdir}/ocamlgraph/


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{ocaml_destdir}/ocamlgraph/
%exclude %{ocaml_destdir}/ocamlgraph/*.a
%exclude %{ocaml_destdir}/ocamlgraph/*.cmxa
%exclude %{ocaml_destdir}/ocamlgraph/*.cmx
%exclude %{ocaml_destdir}/ocamlgraph/*.mli
%{_defaultdocdir}/%{name}-%{version}/LICENSE

%files devel
%defattr(-,root,root,-)
%{ocaml_destdir}/ocamlgraph/*.a
%{ocaml_destdir}/ocamlgraph/*.cmxa
%{ocaml_destdir}/ocamlgraph/*.cmx
%{ocaml_destdir}/ocamlgraph/*.mli

%files doc
%defattr(-,root,root,-)
%{_defaultdocdir}/%{name}-%{version}/README
%{_defaultdocdir}/%{name}-%{version}/examples/
%{_defaultdocdir}/%{name}-%{version}/API/
%{_defaultdocdir}/%{name}-%{version}/ocamlgraph.ps.gz


