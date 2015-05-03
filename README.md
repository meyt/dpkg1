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

	python ./dpkg1.py -c package1,package2,package3,...
	

	python ./dpkg1.py -c vlc,cheese,gnome-system-monitor


Install:
	
	sudo python ./dpkg1.py -i package1,package2,package3,...


	sudo python ./dpkg1.py -i vlc,cheese,gnome-system-monitor

