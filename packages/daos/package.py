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

    version('develop', branch='master', submodules=True)
    version('2019-05-29', commit='eac79b423ff83075ec84d2e4e63c7ab67953fb42', submodules=True)
    version('2019-03-05', commit='4a12f52a477ac774672a4131cba7c4ab37fa040f', submodules=True)

    variant('debug', default=False,
            description='Enable debugging info and strict compile warnings')

    depends_on('argobots@develop')
    depends_on('cart@develop', when='@develop')
    depends_on('cart@2019-03-04', when='@2019-03-05')
    depends_on('cart@2019-05-25', when='@2019-05-29')
    depends_on('cmocka', type='build')
    depends_on('fuse3')
    depends_on('hwloc@:1.999')
    depends_on('isa-l')
    depends_on('libuuid')
    depends_on('libyaml')
    depends_on('openmpi+pmix')
    depends_on('openssl')
    depends_on('pmdk')
    depends_on('protobuf-c@1.3:')
    depends_on('readline')
    depends_on('spdk@:18.07.1+fio')

    depends_on('go', type='build')

    patch('prereq.patch')
    patch('werror.patch')

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

        return args
