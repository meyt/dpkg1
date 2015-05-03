# DPKG One

*ver0.1.2 dev*

Collect debian packages with all dependencies (Debian, Ubuntu, LinuxMint, Elementary Os, Bodhi ...)
this tool help you to backup own already installed packages with all dependencies, 
and reinstall them again.
Prefered to collect & install on the same distro (and version) with the same architecture.


### Requirements

- python 2.7+
- perl
- fakeroot



### Usage

Collect:

	./dpkg1 -c package1 package2 package3,...
	

	./dpkg1 -c vlc cheese gnome-system-monitor


Install:
	
	sudo ./dpkg1 -i package1 package2 package3,...


	sudo ./dpkg1 -i vlc cheese gnome-system-monitor

