#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Reform
Summary:	Text::Reform - manual text wrapping and reformating
Summary(pl):	Text::Reform - ręczne wcinanie i przeformatowywanie tekstu
Name:		perl-Text-Reform
Version:	1.10
Release:	2
License:	Artistic  
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	07608172aed9c4a5158a8184b8107029
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module supplies a re-entrant, highly configurable replacement for
the built-in Perl format() mechanism.

%description -l pl
Moduł udostępnia umożliwiający zrównoleglanie, wysoce konfigurowalny
mechanizm zastępujący wbudowany mechanizm format() Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
find -type f | xargs perl -pi -e 's,/usr/local,/usr,g'
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install demo*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/Reform.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
