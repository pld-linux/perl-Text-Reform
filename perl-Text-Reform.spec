#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Text
%define		pnam	Reform
Summary:	Text::Reform - manual text wrapping and reformating
Summary(pl.UTF-8):	Text::Reform - ręczne wcinanie i przeformatowywanie tekstu
Name:		perl-Text-Reform
Version:	1.20
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f37f5834f3dc221eacd09bdfcfe40918
URL:		http://search.cpan.org/dist/Text-Reform/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module supplies a re-entrant, highly configurable replacement for
the built-in Perl format() mechanism.

%description -l pl.UTF-8
Moduł udostępnia umożliwiający zrównoleglanie, wysoce konfigurowalny
mechanizm zastępujący wbudowany mechanizm format() Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
find -type f | xargs perl -pi -e 's,/usr/local,/usr,g'
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/Reform.pm
%{_mandir}/man3/Text::Reform.3pm*
