#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fAsianOptions
Version  : 3042.82
Release  : 15
URL      : https://cran.r-project.org/src/contrib/fAsianOptions_3042.82.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fAsianOptions_3042.82.tar.gz
Summary  : Rmetrics - EBM and Asian Option Valuation
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fAsianOptions-lib = %{version}-%{release}
Requires: R-fBasics
Requires: R-fOptions
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-fBasics
BuildRequires : R-fOptions
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R

%description
and valuating Asian Options together with tools for analyzing
    and modeling Exponential Brownian Motion (EBM).

%package lib
Summary: lib components for the R-fAsianOptions package.
Group: Libraries

%description lib
lib components for the R-fAsianOptions package.


%prep
%setup -q -c -n fAsianOptions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569390456

%install
export SOURCE_DATE_EPOCH=1569390456
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fAsianOptions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fAsianOptions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fAsianOptions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fAsianOptions || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fAsianOptions/DESCRIPTION
/usr/lib64/R/library/fAsianOptions/INDEX
/usr/lib64/R/library/fAsianOptions/Meta/Rd.rds
/usr/lib64/R/library/fAsianOptions/Meta/features.rds
/usr/lib64/R/library/fAsianOptions/Meta/hsearch.rds
/usr/lib64/R/library/fAsianOptions/Meta/links.rds
/usr/lib64/R/library/fAsianOptions/Meta/nsInfo.rds
/usr/lib64/R/library/fAsianOptions/Meta/package.rds
/usr/lib64/R/library/fAsianOptions/NAMESPACE
/usr/lib64/R/library/fAsianOptions/R/fAsianOptions
/usr/lib64/R/library/fAsianOptions/R/fAsianOptions.rdb
/usr/lib64/R/library/fAsianOptions/R/fAsianOptions.rdx
/usr/lib64/R/library/fAsianOptions/help/AnIndex
/usr/lib64/R/library/fAsianOptions/help/aliases.rds
/usr/lib64/R/library/fAsianOptions/help/fAsianOptions.rdb
/usr/lib64/R/library/fAsianOptions/help/fAsianOptions.rdx
/usr/lib64/R/library/fAsianOptions/help/paths.rds
/usr/lib64/R/library/fAsianOptions/html/00Index.html
/usr/lib64/R/library/fAsianOptions/html/R.css
/usr/lib64/R/library/fAsianOptions/tests/doRUnit.R
/usr/lib64/R/library/fAsianOptions/unitTests/Makefile
/usr/lib64/R/library/fAsianOptions/unitTests/runTests.R
/usr/lib64/R/library/fAsianOptions/unitTests/runit.BesselFunctions.R
/usr/lib64/R/library/fAsianOptions/unitTests/runit.EBMAsianOptions.R
/usr/lib64/R/library/fAsianOptions/unitTests/runit.EBMDistribution.R
/usr/lib64/R/library/fAsianOptions/unitTests/runit.GammaFunctions.R
/usr/lib64/R/library/fAsianOptions/unitTests/runit.HypergeometricFunctions.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fAsianOptions/libs/fAsianOptions.so
/usr/lib64/R/library/fAsianOptions/libs/fAsianOptions.so.avx2
/usr/lib64/R/library/fAsianOptions/libs/fAsianOptions.so.avx512
