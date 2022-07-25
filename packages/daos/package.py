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
   
    version('2.2.0', branch='release/2.2', submodules=True) 
    version('2.0.3', tag='v2.0.3', submodules=True)
    version('2.0.2', tag='v2.0.2', submodules=True)
    version('2.0.1', tag='v2.0.1', submodules=True)
    version('1.2.0', tag='v1.2.0', submodules=True)
    version('1.1.4', tag='v1.1.4', submodules=True)
    version('1.1.3', tag='v1.1.3', submodules=True)
    version('1.1.2.1', tag='v1.1.2.1', submodules=True)
    version('1.1.2', tag='v1.1.2', submodules=True)
    version('1.1.1', tag='v1.1.1', submodules=True)

    variant('fwd', default=True,
            description='Bypass root setup and privilege helper')
    variant('debug', default=False,
            description='Enable debugging info and strict compile warnings')

    depends_on('argobots')
    depends_on('mercury+boostsys')
    depends_on('boost', type='build')
    depends_on('cmocka', type='build')
    depends_on('libfuse@3.6.1:')
    depends_on('hwloc')
    depends_on('isa-l')
    depends_on('isa-l_crypto')
    depends_on('libuuid')
    depends_on('libyaml')
    depends_on('openssl')
    depends_on('pmdk')
    depends_on('pmdk@1.11.1:', when='@2.0.0:')
    depends_on('protobuf-c')
    depends_on('readline')
    depends_on('spdk@20.01+shared+rdma', when='@1.1.0:1.2.0')
    depends_on('spdk@21.07+shared+rdma', when='@2.0')
    depends_on('spdk@22.01+shared+rdma', when='@2.2')
    depends_on('libfabric')

    depends_on('go', type='build')

    patch('daos_allow_fwd_1_1_1.patch', when='@1.1.1+fwd')
    patch('daos_load_mpi_1_1_1.patch', when='@1.1.1')    
    patch('daos_load_mpi_1_1_2.patch', when='@1.1.2')
    patch('daos_allow_fwd_1_1_2.patch', when='@1.1.2:1.2.0+fwd')
    patch('daos_load_mpi_1_1_3.patch', when='@1.1.3:1.2.0')
    patch('daos_dpdk.patch', when='@2.0')
    patch('daos_allow_fwd_2_0_0.patch', when='@2.0+fwd')

    def build_args(self, spec, prefix):
        args = [
            'PREFIX={0}'.format(prefix),
        ]

        # Construct ALT_PREFIX and make sure '/usr' is last
        alt_prefix = [
            format(spec['pmdk'].prefix),
            format(spec['argobots'].prefix),
            format(spec['boost'].prefix),
            format(spec['cmocka'].prefix),
            format(spec['openssl'].prefix),
            format(spec['libfuse'].prefix),
            format(spec['hwloc'].prefix),
            format(spec['isa-l'].prefix),
            format(spec['isa-l_crypto'].prefix),
            format(spec['mercury'].prefix),
            format(spec['libfabric'].prefix),
            format(spec['protobuf-c'].prefix),
            format(spec['spdk'].prefix),
            format(spec['libuuid'].prefix),
            format(spec['libyaml'].prefix)
        ]
        alt_prefix_clean = []
        for i in alt_prefix:
            if i != "/usr":
                alt_prefix_clean.append(i)
        alt_prefix_clean.append("/usr")

        args.extend([
            'WARNING_LEVEL=warning',
            'ALT_PREFIX=%s' % ':'.join([str(elem) for elem in alt_prefix_clean]),
            'GO_BIN={0}'.format(spec['go'].prefix.bin) + "/go"
        ])

        return args

    def install_args(self, spec, prefix):
        args = [
            'WARNING_LEVEL=warning',
            'PREFIX={0}'.format(prefix),
        ]

        return args

