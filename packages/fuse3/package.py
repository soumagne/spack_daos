# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fuse3(MesonPackage):
    """FUSE (Filesystem in Userspace) is an interface for userspace programs
       to export a filesystem to the Linux kernel. The FUSE project consists
       of two components: the fuse kernel module (maintained in the regular
       kernel repositories) and the libfuse userspace library (maintained in
       this repository). libfuse provides the reference implementation for
       communicating with the FUSE kernel module.
    """

    homepage = "https://github.com/libfuse/libfuse"
    url = "https://github.com/libfuse/libfuse/releases/download/fuse-3.4.1/fuse-3.4.1.tar.xz"
    git = "https://github.com/libfuse/libfuse.git"

    version('develop', branch='master')

    # Current
    version('3.6.2', sha256='f45869427575e1e59ab743a67deb57addbf2cb8f9ce431199dbd40ddab71f281')
    version('3.6.1', sha256='6dc3b702f2d13187ff4adb8bcbdcb913ca0510ce0020e4d87bdeb4d794173704')
    version('3.6.0', sha256='0eeccc64698c16c9bf7875588112a55a667293915f5d314108e773b3b63e4a01')
    version('3.5.0', sha256='75bfee6b730145483d18238b50daccde4c1b8133fa1703367fbf8088d0666bf0')
    version('3.4.2', sha256='224dd4a598e23e114395a9717bc79638ab2b1e42c82ae8210aed9365aff325a3')
    version('3.4.1', sha256='88302a8fa56e7871066652495b05faf14b36dca9f1b740e9fb00da0785e60485')

    # Previous versions
    # TODO

    depends_on('meson@0.42.0:', type='build')

    def meson_args(self):
        spec = self.spec
        config_args = [
            '-Ddisable-mtab=true',
            '-Dudevrulesdir={0}'.format(spec.prefix) + '/udev',
            '-Dutils=false',
            '-Dexamples=false',
        ]

        return config_args
