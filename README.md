# Risc-V-MyHDL
# **MyHDL**

Hi everybody.

This is the situation: I'm a student with one subject left (and the final project ) to get a dregree in Electronic Engineering at Córdoba, Argentina. This subject is Digital Electronic.

To pass, I must implement a RISC-V pipelined processor.
So, MyHDL was my option.

I'm  doing my final project at **The Laboratory of Circuits and Robust Systems**, "LCSR", which operates in The FCEFyN Electronics Department of the UNC focused on the following main lines of work:

Failure Prevention (FP): Aims to decrease the probability of occurrence of failures, (removal or blocking of failure-causing factors, or desensitization to them). This line of work seeks to increase the reliability
of the system.

Fault Tolerance, (TF): Aims at increasing the probability and speed of detection and recovery (and/or adaptation) in case of failure. This line work seeks to increase the availability of the system.

System Scalability, (ES): Aims to achieve fundamental properties of robust systems, such as "gracefull degradation", "gracefull
upgradation". These properties allow a kind of exchange between performance and availability. These lines of work can be focused on analog electronics, digital electronics, mixed systems (analog and digital), from lower levels of abstraction such as transistors up to the highest levels such as networks. In short, to all types of applications and electronic systems.
As an example, the following are the current lines of research of the LCSR:

- RF Transistor Robotics.

- Multi-core Processor Robotics on NOC based platforms,

- "Network on Chips" and "DTN", "Delay Tolerant Networks".

- Robusting of distributed systems based on DTN networks, "Delay Tolerant Networks".

- Fault injection systems to determine probability distributions and statistics of digital systems under fault conditions.



MyHDL 0.11 
==========

What is MyHDL?
--------------
MyHDL is a free, open-source package for using Python as a hardware
description and verification language.

To find out whether MyHDL can be useful to you, please read:

   - http://www.myhdl.org/start/why.html

Website
-------
The project website is located at http://www.myhdl.org

Documentation
-------------
The manual is available on-line:

   - http://docs.myhdl.org/en/stable/manual


Installation
------------
It is recommended to install MyHDL (and your project's other dependencies) in
a virtualenv.

Installing the latest stable release:

```
pip install myhdl
```

To install the development version from github:
```
pip install -e 'git+https://github.com/myhdl/myhdl#egg=myhdl
```

To install a local clone of the repository:
```
pip install -e path/to/dir
```

To install a specific commit hash, tag or branch from git:
```
pip install -e 'git+https://github.com/myhdl/myhdl@f696b8#egg=myhdl
```

You can test the proper installation as follows:

```
cd myhdl/test/core
py.test
```
Enviroment
------------
Py-RISC-V requires only MyHDL to run. To install you could use pip:

$ git clone https://gitlab.com/leoborgnino/myhdl-playground.git

$ cd myhdl-playground

Documentation
------------
There is a report (in spanish) which was the academic document of this project You can download from here.

Feedback
------------
Would you like to continue this project? May be try it in real hardware ? Or add a GUI and use as user-friendly simulator ?

So, I would like to read from you. Please write me to _antonelladc950(at)gmail.com.






