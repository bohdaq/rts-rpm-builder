%define _topdir    /home/bohdaq/rts-rpm-builder
%define name       rts
%define release    0
%define version    2.0.0
%define buildroot  %{_topdir}/%{name}-%{version}-root

BuildRoot:         %{buildroot}
Summary:           Rust TLS Server
License:           MIT
Name:              %{name}
Version:           %{version}
Release:           %{release}
Source:            %{name}-%{version}.tar.gz
Prefix:            /usr
Group:             Development/Tools

%description
rust-tls-server (rts) is a web server capable of serving static content over https.

%prep
%setup -q

%build
cargo test

%install
rustup override set nightly
cargo build -Zunstable-options --release  --out-dir $RPM_BUILD_ROOT/usr/local/bin

%files
%defattr(-, root, root)
/usr/local/bin/rts

