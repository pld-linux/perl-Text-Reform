#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Reform
Summary:	Text::Autoformat perl module
Summary(pl):	Modu³ perla Text::Autoformat
Name:		perl-Text-Reform
Version:	1.10
Release:	1
License:	Artistic  
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Autoformat provides intelligent formatting of plaintext without
the need for any kind of embedded mark-up. The module recognizes
Internet quoting conventions, a wide range of bulleting and number
schemes, centred text, and block quotations, and reformats each
appropriately. Other options allow the user to adjust inter-word and
inter-paragraph spacing, justify text, and impose various
capitalization schemes.

%description -l pl
Text::Autoformat udostêpnia inteligentne formatowanie czystego tekstu
bez potrzeby jamkichkolwiek znaczników. Modu³ rozpoznaje internetowe
konwencje cytowania, szeroki zasób wyliczeñ i wiele schematów, tekst
centrowany, cytaty blokowe - i ka¿dy z nich odpowiednio reformatuje.
Inne opcje pozwalaj± u¿ytkownikowi regulowaæ odstêpy miêdzy s³owami
i miêdzy akapitami, justowaæ tekst i stosowaæ ró¿ne schematy wielko¶ci
liter.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
find -type f | xargs perl -pi -e 's,/usr/local,/usr,g'
%{__perl} Makefile.PL
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
%{perl_sitelib}/Text/Reform.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
