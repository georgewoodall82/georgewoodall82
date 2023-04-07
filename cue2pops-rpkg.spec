%global debug_package %{nil}

Name:           cue2pops
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        cue2pops converts bin/cue files to vcd files

License:        none
URL:            https://github.com/makefu/cue2pops-linux
VCS:            {{{ git_dir_vcs }}}

Source:         {{{ git_dir_pack }}}

BuildRequires:  gcc make

%description
cue2pops converts bin/cue files to vcd files

%prep
{{{ git_dir_setup_macro }}}

%build
make

%install
install -Dm755 README.TXT "$RPM_BUILD_ROOT/usr/share/doc/cue2pops-git/README"
install -Dm755 cue2pops "$RPM_BUILD_ROOT/usr/bin/cue2pops"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/cue2pops

%doc README

%changelog
* Tue Apr 3 2023 - 1.0-1
- Initial RPM release.
