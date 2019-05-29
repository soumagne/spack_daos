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


class Cart(SConsPackage):
    """Collective and RPC Transport (CaRT)"""

    homepage = 'https://github.com/daos-stack/cart'
    git      = 'https://github.com/daos-stack/cart.git'

    version('develop', branch='master', submodules=True)
    version('2019-05-25', commit='99fd1cad76ad026f278f5a04ab1c5f33e8fde284', submodules=True)
    version('2019-03-04', commit='430cbb4071f4d0afd99d73602e338c807aac673c', submodules=True)

    depends_on('boost', type='build')
    depends_on('cmocka', type='build')
    depends_on('mercury@1.0.0:+boostsys')
    depends_on('openmpi+pmix')
    depends_on('openssl')
    depends_on('libuuid')
    depends_on('libyaml')

    patch('cart_include.patch')

    def build_args(self, spec, prefix):
        args = [
            'PREFIX={0}'.format(prefix),
            'BOOST_PREBUILT={0}'.format(spec['boost'].prefix),
            'CMOCKA_PREBUILT={0}'.format(spec['cmocka'].prefix),
            'CRYPTO_PREBUILT={0}'.format(spec['openssl'].prefix),
            'MERCURY_PREBUILT={0}'.format(spec['mercury'].prefix),
            'OMPI_PREBUILT={0}'.format(spec['openmpi'].prefix),
            'PMIX_PREBUILT={0}'.format(spec['pmix'].prefix),
            'UUID_PREBUILT={0}'.format(spec['libuuid'].prefix),
        ]

        return args 
