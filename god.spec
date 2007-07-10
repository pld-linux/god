Summary:	A monitoring system like Monit only awesome
Name:		god
Version:	0.1.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{name}-%{version}.gem
# Source0-md5:	fc71bda162d2d6b5b8a2dea1a21e2b38
Patch0:	%{name}-nogems.patch
URL:		http://god.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-daemons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
God is an easy to configure, easy to extend monitoring framework
written in Ruby.

Keeping your server processes and tasks running should be a simple
part of your deployment process. God aims to be the simplest, most
powerful monitoring application available.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
%patch0 -p1
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc *.txt examples
%attr(755,root,root) %{_bindir}/god
%{ruby_rubylibdir}/god.rb
%{ruby_rubylibdir}/god
%{ruby_ridir}/God
