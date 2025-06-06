# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

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

    version('master',  branch='master', submodules=True)
    version('22.01.2', tag='v22.01.2',  submodules=True)
    version('22.01.1', tag='v22.01.1',  submodules=True)

    variant('crypto', default=False, description='Build vbdev crypto module')
    variant('fio', default=False, description='Build fio plugin')
    variant('vhost', default=False, description='Build vhost target')
    variant('virtio', default=False, description='Build vhost initiator and virtio-pci bdev modules')
    variant('pmdk', default=False, description='Build persistent memory bdev')
    variant('reduce', default=False, description='Build vbdev compression module')
    variant('rbd', default=False, description='Build Ceph RBD bdev module')
    variant('rdma', default=False, description='Build RDMA transport for NVMf target and initiator')
    variant('shared', default=False, description='Build spdk shared libraries')
    variant('iscsi-initiator', default=False, description='Build with iscsi bdev module')
    variant('vtune', default=False, description='Required to profile I/O under Intel VTune Amplifier XE')
    variant('ocf', default=False, description='Build OCF library and bdev module')
    variant('isal', default=False, description='Build with ISA-L')
    variant('uring', default=False, description='Build I/O uring bdev')

    mods = ('crypto',
            'vhost',
            'virtio',
            'pmdk',
            'reduce',
            'rbd',
            'rdma',
            'shared',
            'iscsi-initiator',
            'vtune',
            'ocf',
            'isal',
            'uring',
           )

    depends_on('nasm@2.12.02:', type='build')
    depends_on('fio@3.3', when='+fio')
    depends_on('numactl')
    depends_on('libaio')

    patch('https://github.com/spdk/spdk/commit/445a4c808badbad3942696ecf16fa60e8129a747.diff', when='@22.01', sha256='2e412e218517eed2707b874c76faae7f2debf3e755ef198287d3766aa9c7fab4')
    patch('https://github.com/spdk/spdk/commit/b0aba3fcd5aceceea530a702922153bc75664978.diff', when='@22.01', sha256='fe04d364928575397e7ca474ee1dfa32c1ff535b1f31b2deee8748e2a1b3355c')

    def configure_args(self):
        spec = self.spec
        config_args = [
            '--disable-tests',
            '--disable-unit-tests',
            '--disable-apps'
        ]

        if '+fio' in spec:
            config_args.append(
                '--with-fio={0}'.format(spec['fio'].prefix)
            )

        for mod in self.mods:
            if '+' + mod in spec:
                config_args.append('--with-{0}'.format(mod))
            else:
                config_args.append('--without-{0}'.format(mod))

        return config_args

    @run_after('install')
    def install_additional_files(self):
        spec = self.spec
        prefix = self.prefix

        if spec.satisfies('@21.07:'):
            dpdk_build_dir = join_path(self.stage.source_path, 'dpdk', 'build', 'lib')
            install_tree(join_path(dpdk_build_dir, 'pkgconfig'), join_path(prefix.lib, 'pkgconfig'))
            for file in os.listdir(dpdk_build_dir):
                if os.path.isfile(join_path('dpdk', 'build', 'lib', file)):
                    install(join_path('dpdk', 'build', 'lib', file), prefix.lib)
            mkdir(join_path(prefix.include, 'dpdk'))
            install_tree('dpdk/build/include', join_path(prefix.include, 'dpdk'))

        # Copy the config.h file, as some packages might require it
        mkdir(prefix.share)
        mkdir(join_path(prefix.share, 'spdk'))
        install_tree('examples/nvme/fio_plugin', join_path(prefix.share, 'spdk', 'fio_plugin'))
        install_tree('include', join_path(prefix.share, 'spdk', 'include'))
        install_tree('scripts', join_path(prefix.share, 'spdk', 'scripts'))

