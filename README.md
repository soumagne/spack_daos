# spack-packages for the DAOS stack

Here are a collection of [spack](https://spack.io/) packages to manage
building the DAOS stack.

For more about spack and what you can do with it, spack has lots of
[documentation](https://spack.readthedocs.io/en/latest/) and a good
[tutorial](https://spack.readthedocs.io/en/latest/tutorial_sc16.html).

## Repo Installation

Once you've set up spack itself, you need to teach it about this collection
('repository' in spack lingo) of packages. Go to the top-level directory of
this project and execute the following command:

    cd spack_daos
    spack repo add .

Did it work?

    spack repo list

## DAOS Installation

To build the entire DAOS stack with the default configuration,
simply install daos:

    spack install daos

## Using DAOS

One consequence of the spack design (where packages are installed into a prefix
based on a hash of their configuration and compiler) is that library and header
paths are unwieldy. An environment-management tool such as `modules` helps a
lot here, and is nicely integrated into spack.

The integration can also help you load in all the dependencies:

    source <(spack module loads  --dependencies daos)

