# spack-packages for the DAOS stack

Here are a collection of [spack](https://spack.io/) packages to manage
building the DAOS stack.

For more about spack and what you can do with it, spack has lots of
[documentation](https://spack.readthedocs.io/en/latest/) and a good
[tutorial](https://spack.readthedocs.io/en/latest/tutorial_sc16.html).

## Spack Installation

The DAOS stack requires a few changes to the packages that are provided by
spack (mpich, etc). While this may change in the future, you will for now
need to check out the branch named `topic_daos` from this fork of spack:

```
git clone git@github.com:soumagne/spack.git -b topic_daos
```

Once you do that you must add spack to your environment, see this [page](https://spack.readthedocs.io/en/latest/getting_started.html#add-spack-to-the-shell). For instance for BASH
add to your .bashrc:

```
SPACK_ROOT=/path/to/spack
if [ -f $SPACK_ROOT/share/spack/setup-env.sh ]; then
    . $SPACK_ROOT/share/spack/setup-env.sh
    export SPACK_ROOT
fi
```

The next step is to setup compilers, see this [page](https://spack.readthedocs.io/en/latest/getting_started.html#compiler-configuration).

Finally set up modules, see this [page](https://spack.readthedocs.io/en/latest/getting_started.html#environment-modules). Before running the `spack bootstrap`
command, it is advisable to verify which module environment your system is using.
You can specify that in your spack system package file
`~/.spack/<arch>/packages.yaml` (see also this [page](https://spack.readthedocs.io/en/latest/getting_started.html#system-packages)). For example:

```
packages:
    environment-modules:
        paths:
            environment-modules@4.2.4: /usr
        buildable: False
```

## Repo Installation

Once you've set up spack itself, you need to teach it about this collection
 of packages ('repository' in spack lingo). Go to the top-level directory of
this project and execute the following command:

```
cd spack_daos
spack repo add .
```

Did it work?

```
spack repo list
```

## DAOS Installation

Before installing daos, it is wise to check the dependencies that spack will
need to install (there are quite a few), this can be done with:

```
spack spec -I daos
```

You may then tell spack about the system package that you already have installed
(see side note below).
To build the entire DAOS stack with the default configuration,
simply install daos:

```
spack install -v daos
```

## HDF5 Installation

To install HDF5 with MPI support, it is recommended to use the latest MPICH that
also comes with DAOS support in order to compare native HDF5 with the
HDF5 DAOS VOL connector. To build HDF5, do:

```
spack install -v hdf5+map+mpi^mpich@develop+daos
```

### Side note: System packages vs spack packages

The largest dependency for Mercury is the Boost package.  If your system
already has Boost, you can teach spack about it and other
[system packages](https://spack.readthedocs.io/en/latest/getting_started.html#system-packages).

Let's say you installed Boost through your distribution (an RPM or DEB package)
To inform spack about Boost you e.g. installed from an RPM, you would add it to
`~/.spack/<arch>/packages.yaml`

```
packages:
    boost:
        paths:
            boost@system: /usr
        version: [system]
        buildable: False
```

Several other large dependencies are handled just fine by the
operating system.  Here is an example of a `${HOME}/.spack/linux/packages.yaml`:

```
packages:
    openssl:
        paths:
            openssl@1.0.2g: /usr
        buildable: False
    cmake:
        paths:
            cmake@3.9.1: /usr
        buildable: False
    boost:
        paths:
            boost@1.62: /usr
        buildable: False
    autoconf:
        paths:
            autoconf@2.69: /usr
        buildable: False
    automake:
        paths:
            automake@1.15.1: /usr
        buildable: False
```

You can see that several packages are flagged as `buildable: False`,
generaly because they are either large packages or have large dependencies.

These `packages` files live in a platform-specific directory (run `spack arch
-p` to see what platform spack thinks you are on).  Pretty helpful for e.g.
Argonne, where a home file system is shared between a linux cluster, a blue
gene, and a Cray.  You can describe `packages.py` for each platform.

### Side note: using modules

Spack works well with the module command for loading and unloading
particular packages in your environment once they have been built. In theory
you could integrate it with an existing environment-modules or lmod package
on your system.  Alternatively you can have spack set up its own modules
system:

* run ```spack bootstrap```
    * this will make spack build and install its very own
      environment-modules package that is automatically aware of packages
      that have been installed via spack

The remainder of this document assumes that you will use the module command
to load and unload packages once built.

### Further package configuration

Spack has a bit of trouble resolving a dependency if it is not exactly the same
between packages.  For example, the `hdf5` package depends on mpich when using
the variant `+mpi`. If you install `mpich`, then install `hdf5`,
you may end up with two instances of mpich. If you remember to install
`mpich` with the `@develop+daos` variant, you can avoid this duplication,
but it's easy to forget (and kind of a pain) to type `spack install
hdf5+map+mpi^mpich@develop+daos`.

In my `~/.spack/linux/packages.yaml` you can tell spack you'd like to always build particular variants:

```
packages:
    hdf5:
        variants: +map+mpi
```

## Using DAOS

One consequence of the spack design (where packages are installed into a prefix
based on a hash of their configuration and compiler) is that library and header
paths are unwieldy. An environment-management tool such as `modules` helps a
lot here, and is nicely integrated into spack.

The integration can also help you load in all the dependencies:

```
spack load -r daos
```

## Using HDF5

Similary, you can do:

```
spack load -r hdf5
```

