# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class ProtobufC(AutotoolsPackage):
    """This is protobuf-c, a C implementation of the Google Protocol Buffers
       data serialization format. It includes libprotobuf-c, a pure C library
       that implements protobuf encoding and decoding, and protoc-c, a code
       generator that converts Protocol Buffer .proto files to C descriptor
       code, based on the original protoc. protobuf-c formerly included an RPC
       implementation; that code has been split out into the protobuf-c-rpc
       project.
    """

    homepage = "https://github.com/protobuf-c/protobuf-c"
    url = "https://github.com/protobuf-c/protobuf-c/releases/download/v1.3.1/protobuf-c-1.3.1.tar.gz"
    git = "https://github.com/protobuf-c/protobuf-c.git"

    version('develop', branch='master')

    # Current
    version('1.3.1', preferred=True, sha256='51472d3a191d6d7b425e32b612e477c06f73fe23e07f6a6a839b11808e9d2267')

    # Previous versions
    # TODO

    depends_on('autoconf', type='build', when='@develop')
    depends_on('automake', type='build', when='@develop')
    depends_on('libtool',  type='build', when='@develop')
    depends_on('m4', type='build', when='@develop')
    depends_on('pkg-config', type='build')
    depends_on('protobuf')

    def configure_args(self):
        spec = self.spec
        config_args = [
            '--enable-shared',
        ]

        return config_args
