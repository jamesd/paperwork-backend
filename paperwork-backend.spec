Name:           paperwork-backend
Version:        1.0.4
Release:        1%{?dist}
Summary:        Backend part of Paperwork (Python API no UI)

License:        gplv3+
URL:            https://github.com/jflesch/paperwork/wiki
Source0:        https://github.com/jflesch/%{name}/archive/%{version}/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pillow-devel
BuildRequires:  python3-setuptools
Requires:  poppler-glib
Requires:  pygobject3
Requires:  python3-termcolor
Requires:  python3-whoosh


%description
The backend part of Paperwork. It manages:

- The work directory / Access to the documents
- Indexing
- Searching
- Suggestions
- Import
- Export


%prep
%autosetup


%build
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


# %check
# %{__python3} setup.py test


%files
%license LICENSE
%doc AUTHORS README.markdown ChangeLog
%{python3_sitelib}/*
%{_bindir}/paperwork-shell

%changelog
* Sat Nov 19 2016 James Davidson <james@greycastle.net> - 1.0.4-1
- Update to 1.0.4

* Fri Nov 18 2016 James Davidson <james@greycastle.net> - 1.0.3-1
- Initial packaging
