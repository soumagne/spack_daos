# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Hdf5Daos(CMakePackage):
    """The HDF5 DAOS VOL connector is an external VOL connector that interfaces with the DAOS API"""

    homepage = ''
    url = ''
    git = 'https://github.com/HDFGroup/vol-daos.git'

    maintainers = ['soumagne']

    version('master', branch='master', submodules=True)
    version('v1.1.0rc3', tag='v1.1.0rc3', submodules=True)
    version('v1.1.0rc2', tag='v1.1.0rc2', submodules=True)
    version('v1.1.0rc1', tag='v1.1.0rc1', submodules=True)

    depends_on('cmake@2.8.12.2:', type='build')
    depends_on('daos@1.1.0:')
    depends_on('hdf5@1.13.0:+hl+mpi+map')

    def cmake_args(self):
        """Populate cmake arguments for HDF5 DAOS."""
        spec = self.spec
        variant_bool = lambda feature: str(feature in spec)
        parallel_tests = '+mpi' in spec and self.run_tests

        cmake_args = [
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DBUILD_TESTING:BOOL=%s' % str(self.run_tests),
        ]

        return cmake_args

    def setup_run_environment(self, env):
        env.prepend_path('HDF5_PLUGIN_PATH', self.prefix.lib)

    def check(self):
        """Unit tests fail when run in parallel."""

        with working_dir(self.build_directory):
            make('test', parallel=False)
