%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from fast_xs-0.8.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname fast_xs
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define __arch_install_post   /usr/lib/rpm/check-rpaths

Summary: fast_xs provides C extensions for escaping text
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 0.8.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://fast-xs.rubyforge.org/
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems

BuildRequires: make
BuildRequires: ruby-enterprise
BuildRequires: %{?ruby_dist_dash}rubygems
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
fast_xs provides C extensions for escaping text.
The original String#fast_xs method is based on the xchar code by Sam Ruby:
* http://intertwingly.net/stories/2005/09/28/xchar.rb
* http://intertwingly.net/blog/2005/09/28/XML-Cleansing
_why also packages an older version with Hpricot (patches submitted).
The version here should be compatible with the latest version of Hpricot
code.
Ruby on Rails will automatically use String#fast_xs from either Hpricot
or this gem version with the bundled Builder package.
String#fast_xs is an almost exact translation of Sam Ruby's original
implementation (String#to_xs), but it does escape "&quot;" (which is an
optional, but all parsers are able ot handle it.  XML::Builder as
packaged in Rails 2.0 will be automatically use String#fast_xs instead
of String#to_xs available.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
                --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/Manifest.txt
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.8.0-1.hhg
- Rebuild for Ruby Enterprise Edition

* Fri Apr 29 2011 Sergio Rubio <rubiojr@frameos.org> - 0.8.0-1
- Initial package
