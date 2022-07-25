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
    version('22.01.1', tag='v22.01.1',  submodules=True)
    version('21.07',   tag='v21.07',    submodules=True)
    version('20.01.2', tag='v20.01.2',  submodules=True)
    version('20.01.1', tag='v20.01.1',  submodules=True)
    version('19.04.1', tag='v19.04.1',  submodules=True)
    version('19.04',   tag='v19.04',    submodules=True)
    version('19.01.1', tag='v19.01.1',  submodules=True)
    version('19.01',   tag='v19.01',    submodules=True)
    version('18.10.2', tag='v18.10.2',  submodules=True)
    version('18.10.1', tag='v18.10.1',  submodules=True)
    version('18.10',   tag='v18.10',    submodules=True)
    version('18.07.1', tag='v18.07.1',  submodules=True)
    version('18.07',   tag='v18.07',    submodules=True)

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

    patch('https://github.com/spdk/spdk/commit/b0aba3fcd5aceceea530a702922153bc75664978.diff', when='@22.01.1', sha256='fe04d364928575397e7ca474ee1dfa32c1ff535b1f31b2deee8748e2a1b3355c')
    patch('https://github.com/spdk/spdk/commit/690783a3ae82ebe58c00d643520a66103d66d540.diff', when='@21.07', sha256='63c6213c21f21e3bea3620fbd1ab0f46dd04aa0613667a946d79123eedcfb7bb')
    patch('https://github.com/spdk/spdk/commit/65425be69a0882ac283fb489aa151d7df06c52ad.diff', when='@21.07', sha256='1dccaddee0d7864a838edac1a4272ffcb76cdcb96eea78ab39c05c6d03dde694')
    patch('https://raw.githubusercontent.com/daos-stack/spdk/master/0003-blob-chunk-clear-operations-in-IU-aligned-chunks.patch', when='@21.07', sha256='4a976d8b74efc327feba34847f15aa9a39ed2f2fdab07ba805fae8cfcc6709b8')
    patch('https://github.com/spdk/spdk/commit/148a9ab0c06346f9fec109a1df00651c1f5a0499.diff', when='@21.07', sha256='d79143f38c6a4cb57d63d95a3617493e9b5897443186e82733823257f65f8c28')
    patch('https://github.com/spdk/spdk/commit/086223c029389329b7a4f38ec0f9a30be83849bf.diff', when='@21.07', sha256='2a09ab634f53fc5e6e8321bd82db4578e04c307b0014d0bb38306b84fd6a1116')
    patch('https://github.com/spdk/spdk/commit/a827fd7eeca67209d4c0aaad9a3ed55692e7e36e.diff', when='@21.07', sha256='21c1ef3033ad5c9765d402c919991357212585c8797f3424a65ccd3637cd1112')
    patch('https://github.com/spdk/spdk/commit/038f5b2e1b07f840e610ca206902a90661c6a28f.diff', when='@21.07', sha256='63b9a0c40696926a1f98380daeea0a471692f64cbed304201a8ba4351da2b733')
    patch('https://github.com/spdk/spdk/commit/6c3fdade83cdf48182b7c2c3561ca7dd269d5aa9.diff', when='@21.07', sha256='5be3ffcd3d5dbc27bebb9b5ac05cdd5fdbeb5bbeee3a815a8b28f1ba176fdbaf')
    patch('https://github.com/spdk/spdk/commit/b0aba3fcd5aceceea530a702922153bc75664978.diff', when='@21.07', sha256='fe04d364928575397e7ca474ee1dfa32c1ff535b1f31b2deee8748e2a1b3355c')
    patch('https://github.com/spdk/spdk/commit/91aee82d74696bb70284c794db0b2b9aef4bb9ec.diff', when='@21.07', sha256='c65dc4d1e55231190baa57ceacad7f6967a35a81fa40607768f86c415ab0d303')
    patch('dpdk-ar.patch', when='@21.07')

    def configure_args(self):
        spec = self.spec
        config_args = [
            '--disable-tests',
        ]

        if spec.satisfies('@21.07:'):
            config_args.append('--disable-unit-tests')
            config_args.append('--disable-apps')

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

        if spec.satisfies('@19.04:20.01'):
            for file in os.listdir(join_path(self.stage.source_path, 'dpdk', 'build', 'lib')):
                install(join_path('dpdk', 'build', 'lib', file), prefix.lib)

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

