Name: mythes-de
Summary: German thesaurus
%define upstreamid 20090708
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://www.openthesaurus.de/download/thes_de_DE_v2.zip
Group: Applications/Text
URL: http://www.openthesaurus.de
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: LGPLv2+
BuildArch: noarch

%description
German thesaurus.

%prep
%setup -q -c

%build
for i in README_th_de_DE_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_de_DE_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
de_DE_aliases="de_AT de_BE de_CH de_LI de_LU"
for lang in $de_DE_aliases; do
        ln -s th_de_DE_v2.idx "th_"$lang"_v2.idx"
        ln -s th_de_DE_v2.dat "th_"$lang"_v2.dat"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_de_DE_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090708-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-2
- tidy spec

* Wed Jul 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Mon Jun 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Thu Apr 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090402-1
- latest version

* Mon Mar 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090302-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090202-1
- latest version

* Tue Dec 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081223-1
- latest version

* Sun Nov 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081123-1
- latest version

* Thu Oct 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081016-1
- latest version

* Mon Sep 01 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080901-1
- latest version

* Thu Jul 31 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080731-1
- latest version
