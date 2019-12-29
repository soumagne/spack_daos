##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Daos(SConsPackage):
    """The Distributed Asynchronous Object Storage (DAOS) is an open-source
       software-defined object store designed from the ground up for massively
       distributed Non Volatile Memory (NVM)."""

    homepage = 'https://github.com/daos-stack/daos'
    git      = 'https://github.com/daos-stack/daos.git'

    version('master', branch='master', submodules=True)
    version('0.8', tag='v0.8.0', submodules=True)
    version('0.7', tag='v0.7.0', preferred=True, submodules=True)
    version('0.6', tag='v0.6', submodules=True)

    variant('debug', default=False,
            description='Enable debugging info and strict compile warnings')

    depends_on('argobots@1.0rc2:')
    depends_on('cart@master',   when='@master')
    depends_on('cart@daos-0.8', when='@0.8')
    depends_on('cart@daos-0.7', when='@0.7')
    depends_on('cart@daos-0.6', when='@0.6')
    depends_on('cmocka', type='build')
    depends_on('fuse3@3.5.0')
    depends_on('hwloc@:1.999')
    depends_on('isa-l')
    depends_on('libuuid')
    depends_on('libyaml')
    depends_on('openmpi', when='@master')
    depends_on('openmpi+pmix', when='@:0.8')
    depends_on('openssl')
    depends_on('pmdk@:1.6.1')  # Hang with further versions
    depends_on('protobuf-c')
    depends_on('readline')
    depends_on('spdk@18.07.1+fio', when='@0.6')
    depends_on('spdk@19.04.1+fio+shared', when='@0.7:')
    depends_on('libfabric', when='@0.7:')

    depends_on('go', type='build')

    patch('daos_goreq_master.patch', when='@0.8:')
    patch('daos_goreq_0_7.patch',    when='@0.7')
    patch('daos_goreq_0_6.patch',    when='@0.6')
    patch('daos_werror_scons.patch')
    patch('daos_disable_python.patch', when='@0.7:')

    def build_args(self, spec, prefix):
        args = [
            'PREFIX={0}'.format(prefix),
            'ARGOBOTS_PREBUILT={0}'.format(spec['argobots'].prefix),
            'CART_PREBUILT={0}'.format(spec['cart'].prefix),
            'CMOCKA_PREBUILT={0}'.format(spec['cmocka'].prefix),
            'CRYPTO_PREBUILT={0}'.format(spec['openssl'].prefix),
            'FUSE_PREBUILT={0}'.format(spec['fuse3'].prefix),
            'GO_PREBUILT={0}'.format(spec['go'].prefix),
            'HWLOC_PREBUILT={0}'.format(spec['hwloc'].prefix),
            'ISAL_PREBUILT={0}'.format(spec['isa-l'].prefix),
            'OMPI_PREBUILT={0}'.format(spec['openmpi'].prefix),
            'PMDK_PREBUILT={0}'.format(spec['pmdk'].prefix),
            'PROTOBUFC_PREBUILT={0}'.format(spec['protobuf-c'].prefix),
            'SPDK_PREBUILT={0}'.format(spec['spdk'].prefix),
            'UUID_PREBUILT={0}'.format(spec['libuuid'].prefix),
            'YAML_PREBUILT={0}'.format(spec['libyaml'].prefix),
        ]

        if self.spec.satisfies('@0.7:'):
            args.append('OFI_PREBUILT={0}'.format(spec['libfabric'].prefix))

        return args
