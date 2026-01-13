#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	Request-Params
Summary:	Retrieve GET/POST Parameters from HTTP Requests
Summary(pl.UTF-8):	Odczytywanie parametrów GET/POST z zapytań HTTP
Name:		perl-%{pdir}-%{pnam}
Version:	1.01
Release:	3
License:	same as Perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fccd255a2992c77b5c40cb5e1e75b256
URL:		http://search.cpan.org/dist/HTTP-Request-Params/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Email-MIME
BuildRequires:	perl-Email-MIME-ContentType
BuildRequires:	perl-Email-MIME-Modifier >= 1.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software does all the dirty work of parsing HTTP Requests to find
incoming query parameters.

%description -l pl.UTF-8
Biblioteka wykonująca brudną robotę z parsowaniem zapytań HTTP w celu
znalezienia parametrów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/Request/Params.pm
%{_mandir}/man3/*
