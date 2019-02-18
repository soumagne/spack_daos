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
    version('3.4.1', sha256='88302a8fa56e7871066652495b05faf14b36dca9f1b740e9fb00da0785e60485', preferred=True)

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
