#
# Conditional build:
%bcond_with	tests		# build without tests
%bcond_without	doc			# don't build ri/rdoc

Summary:	A monitoring system like Monit only awesome
Summary(pl.UTF-8):	System monitorujący podobny do Monita, tylko przerażający
Name:		god
Version:	0.13.3
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	1ccc6c336c9740b99749ffefa0a802b4
Patch0:		%{name}-nogems.patch
URL:		http://godrb.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel
%{?with_doc:BuildRequires: ruby-rdoc}
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-activesupport < 4.0.0
BuildRequires:	ruby-activesupport >= 2.3.10
BuildRequires:	ruby-airbrake < 3.2
BuildRequires:	ruby-airbrake >= 3.1.7
BuildRequires:	ruby-daemons < 2
BuildRequires:	ruby-daemons >= 1.1
BuildRequires:	ruby-dike < 0.1
BuildRequires:	ruby-dike >= 0.0.3
BuildRequires:	ruby-gollum < 1.4
BuildRequires:	ruby-gollum >= 1.3.1
BuildRequires:	ruby-json < 2
BuildRequires:	ruby-json >= 1.6
BuildRequires:	ruby-mocha < 1
BuildRequires:	ruby-mocha >= 0.10
BuildRequires:	ruby-nokogiri < 1.6
BuildRequires:	ruby-nokogiri >= 1.5.0
BuildRequires:	ruby-prowly < 1
BuildRequires:	ruby-prowly >= 0.3
BuildRequires:	ruby-rake
BuildRequires:	ruby-rcov < 1
BuildRequires:	ruby-rcov >= 0.9
BuildRequires:	ruby-rdoc < 4
BuildRequires:	ruby-rdoc >= 3.10
BuildRequires:	ruby-twitter < 5
BuildRequires:	ruby-twitter >= 4.0
BuildRequires:	ruby-xmpp4r < 1
BuildRequires:	ruby-xmpp4r >= 0.5
%endif
Requires:	ruby-daemons < 2
Requires:	ruby-daemons >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
God is an easy to configure, easy to extend monitoring framework
written in Ruby.

Keeping your server processes and tasks running should be a simple
part of your deployment process. God aims to be the simplest, most
powerful monitoring application available.

%description -l pl.UTF-8
God to łatwy w konfiguracji, prosty w rozszerzaniu system monitorujący
napisany w języku Ruby.

Utrzymywanie działania procesów i zadań serwera powinno być prostą
częścią wdrożenia. God ma być najprostszą, najpotężniejszą dostępną
aplikacją monitorującą.

%package rdoc
Summary:	HTML documentation for god
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla god
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for god.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla god.

%package ri
Summary:	ri documentation for god
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla god
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for god.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla god.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm -r ri/ConditionVariable
rm -r ri/Kernel
rm -r ri/Marshmallow
rm -r ri/Module
rm -r ri/MonitorMixin
rm -r ri/Numeric
rm -r ri/Object
rm ri/cache.ri
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc *.txt
%attr(755,root,root) %{_bindir}/god
%{ruby_vendorlibdir}/god.rb
%{ruby_vendorlibdir}/god

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/God
%endif
