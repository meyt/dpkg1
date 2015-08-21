# DPKG One

*ver0.3.0 dev*

Collect debian packages with all dependencies (Debian, Ubuntu, LinuxMint, Elementary Os, Bodhi ...)
this tool help you to backup own already installed packages with all dependencies, 
and reinstall them again.
Prefered to collect & install on the same distro (and version) with the same architecture.


### Requirements

- python 2.7+
- perl
- fakeroot
- dpkg-dev (for making repository catalog)

### Usage

Extract archive and move into directory with `cd` command

#### Collect:

e.g: collecting `vlc` and `cheese` packages.

	./dpkg1 -c vlc cheese


#### Create repository catalog:

	./dpkg1 -r

Now you can add packages path as offline repository, modify path and add this line in the end of `/etc/apt/sources.list` or create new file at `/etc/apt/sources.list.d/myrepository`
    
	deb file:/home/user/dpkg1/pkgs ./


then update repository list and install:

	sudo apt-get update
	sudo apt-get install vlc cheese 

