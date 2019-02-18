# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class IsaL(AutotoolsPackage):
    """ISA-L is a collection of optimized low-level functions targeting
       storage applications. ISA-L includes:

       - Erasure codes - Fast block Reed-Solomon type erasure codes for
         any encode/decode matrix in GF(2^8).
       - CRC - Fast implementations of cyclic redundancy check. Six
         different polynomials supported.
           iscsi32, ieee32, t10dif, ecma64, iso64, jones64.
       - Raid - calculate and operate on XOR and P+Q parity found in
         common RAID implementations.
       - Compression - Fast deflate-compatible data compression.
       - De-compression - Fast inflate-compatible data compression.
    """

    homepage = "https://github.com/01org/isa-l"
    url = "https://github.com/01org/isa-l/archive/v2.25.0.tar.gz"
    git = "https://github.com/01org/isa-l.git"

    version('develop', branch='master')

    # Current
    version('2.25.0', tag='v2.25.0', preferred=True)

    # Previous versions
    # TODO

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',  type='build')
    depends_on('yasm@1.2.0:', type='build')
    depends_on('nasm@2.13:', type='build')

    def configure_args(self):
        spec = self.spec
        config_args = [
            '--enable-shared',
        ]

        return config_args
