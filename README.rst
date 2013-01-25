Steam rpm
=========

Get pre-built rpms from `steam.48.io <http://steam.48.io>`_ or get sources from `sources.48.io <http://sources.48.io/steam/>`_ and build using the steps bellow.

You can also download and repack the original .deb package with `fetch_sources` script.

Build instructions
------------------

Fedora
~~~~~~

::

        # install necessary tools
        sudo yum -y install rpm-build rpmdevtools

        # clone this repo
        git clone git://github.com/hackerspace/steamrpm.git && cd steamrpm

        # downloads steam-$version-binary.tar.gz from http://sources.48.io/steam/ (or use fetch_sources to download and repack the original .deb archive)
        spectool -g -s 0 steam.spec

        # move stuff to right directories
        mkdir -p ~/rpmbuild/SOURCES/
        cp *.patch ~/rpmbuild/SOURCES/
        cp STEAM-LICENSE.txt ~/rpmbuild/SOURCES/
        cp steam-*-binary.tar.gz ~/rpmbuild/SOURCES/

        # build the package
        rpmbuild -ba steam.spec

        # install!
        sudo yum -y localinstall ~/rpmbuild/RPMS/x86_64/steam-1*


Authors
-------
See `%changelog` section of the spec file.
