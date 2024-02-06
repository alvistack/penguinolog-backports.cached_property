# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-backports-cached-property
Epoch: 100
Version: 1.0.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Python 3.8 functools.cached_property backport to python 3.6
License: MIT
URL: https://github.com/penguinolog/backports.cached_property/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python 3.8 adds great descriptor to functools: cached\_property.
Technically all required APIs was available since python 3.6, but it is
what it is. This package is a backport of this functionality for python
3.6 and 3.7.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-backports-cached-property
Summary: Python 3.8 functools.cached_property backport to python 3.6
Requires: python3
Requires: python3-typing-extensions >= 3.6
Provides: python3-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python3dist(backports-cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(backports-cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(backports-cached-property) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-backports-cached-property
Python 3.8 adds great descriptor to functools: cached\_property.
Technically all required APIs was available since python 3.6, but it is
what it is. This package is a backport of this functionality for python
3.6 and 3.7.

%files -n python%{python3_version_nodots}-backports-cached-property
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-backports-cached-property
Summary: Python 3.8 functools.cached_property backport to python 3.6
Requires: python3
Requires: python3-typing-extensions >= 3.6
Provides: python3-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python3dist(backports-cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(backports-cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(backports-cached-property) = %{epoch}:%{version}-%{release}

%description -n python3-backports-cached-property
Python 3.8 adds great descriptor to functools: cached\_property.
Technically all required APIs was available since python 3.6, but it is
what it is. This package is a backport of this functionality for python
3.6 and 3.7.

%files -n python3-backports-cached-property
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-backports-cached-property
Summary: Python 3.8 functools.cached_property backport to python 3.6
Requires: python3
Requires: python3-typing-extensions >= 3.6
Provides: python3-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python3dist(backports-cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(backports-cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-backports-cached-property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(backports-cached-property) = %{epoch}:%{version}-%{release}

%description -n python3-backports-cached-property
Python 3.8 adds great descriptor to functools: cached\_property.
Technically all required APIs was available since python 3.6, but it is
what it is. This package is a backport of this functionality for python
3.6 and 3.7.

%files -n python3-backports-cached-property
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
