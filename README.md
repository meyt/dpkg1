# DPKG One

*ver0.2.0 dev*

Collect debian packages with all dependencies (Debian, Ubuntu, LinuxMint, Elementary Os, Bodhi ...)
this tool help you to backup own already installed packages with all dependencies, 
and reinstall them again.
Prefered to collect & install on the same distro (and version) with the same architecture.


### Requirements

- python 2.7+
- perl
- fakeroot


### Usage

Extract archive and move into directory with `cd` command

#### Collect:

	// e.g: collecting vlc and cheese
	./dpkg1 -c vlc cheese


#### Force install (root access):

	// e.g: isntall vlc and cheese
	sudo ./dpkg1 -i vlc cheese



#### Create repository catalog:

	./dpkg1 -r

Now you can add packages path as offline repository, modify and add this line in the end of `/etc/apt/sources.list`
    
	deb file:/home/user/dpkg1/pkgs


then update repository list and install:


	sudo apt-get update
	sudo apt-get install vlc cheese 

