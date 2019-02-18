# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Spdk(AutotoolsPackage):
    """The Storage Performance Development Kit (SPDK) provides a set of tools
       and libraries for writing high performance, scalable, user-mode storage
       applications. It achieves high performance by moving all of the
       necessary drivers into userspace and operating in a polled mode instead
       of relying on interrupts, which avoids kernel context switches and
       eliminates interrupt handling overhead.
    """

    homepage = "https://spdk.io"
    url      = "https://github.com/spdk/spdk/archive/v19.01.tar.gz"
    git      = "https://github.com/spdk/spdk"

    version('develop', branch='master', submodules=True)
    version('19.01', tag='v19.01', submodules=True)
    version('18.10.1', tag='v18.10.1', submodules=True)
    version('18.07.1', tag='v18.07.1', submodules=True, preferred=True)
    version('18.07', tag='v18.07', submodules=True)

    variant('fio', default=False, description='Build fio plugin')

    depends_on('nasm@2.12.02:', type='build')
    depends_on('fio@3.3', when='+fio')

    #patch('spdk_shared.patch')
    #patch('spdk_shared_dpdk.patch')

    def configure_args(self):
        spec = self.spec
        config_args = [
#            '--with-shared',
            '--disable-tests',
        ]

        if '+fio' in spec:
	    config_args.extend([
                '--with-fio={0}'.format(spec['fio'].prefix),
            ])

        return config_args

    @run_after('install')
    def install_additional_files(self):
        spec = self.spec
        prefix = self.prefix

        # Copy the config.h file, as some packages might require it
        mkdir(prefix.share)
        mkdir(join_path(prefix.share, 'spdk'))
        install_tree('examples/nvme/fio_plugin', join_path(prefix.share, 'spdk', 'fio_plugin'))
        install_tree('include', join_path(prefix.share, 'spdk', 'include'))
        install_tree('scripts', join_path(prefix.share, 'spdk', 'scripts'))

