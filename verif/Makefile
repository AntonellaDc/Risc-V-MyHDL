all: sim view

sim:
	python testbench.py

compile:
	iverilog -o localization -c ../../rtl/filelist.f -g 2005
	vvp localization

view:
	gtkwave _testbench.vcd
