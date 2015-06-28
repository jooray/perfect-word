Perfect Word: Generative Lexicography
=====================================

This piece of software is not production quality -- it is a fun project of ours. We have written it when starting the company and searching for our new name.

It is also unique because it is written in three different programming languages (Ruby, C and Python), which you'll probably hate.

We wanted to find a good name by means of genetic algorithms. It is very difficult to find a good new name for a company these days (especially if a free .com domain is high on your list or priorities). It basically contains three parts: 

Python wikipedia parser
=======================
 

This component parses wiki.xml of Wikipedia and generates list of words. It is then converted by sort -u to list of unique names and converted to FANN training file.

 

C Trainer and tester
====================
 
We train the neural network by using open-source FANN library. We use list of words (divided into sequences of three characters, so "digmia" would become "dig", "igm", "gmi", "mia"), convert it into FANN training file and then train the neural network (using standard backpropagation). A binary called "test" will produce a number between 0 and 1. For example:

    sleeper 0.921576
    world 0.666372
    digmia 0.278822
    poseidon 0.827688
    brzdaozq 0.000000
    plamion 0.959918
    murdamongofondozol 0.089395
    heavy 0.901540


The more the better. (Digmia having such a low score is another story...).

Trained neural network for English is included in the package, no need to do this, if you just want to try it. Just compile test.c and copy it to main perfectword directory.


Genetic Algorithm
=================

Genetic algorithm is written in Ruby and uses SQLite and test binary from the last step. You need to configure the first population. There's also a free domain checker in ```resolve.rb```. 

You can examine the results by using sqlite

    select from words.db table.

Get it
======

As this is a fun project, we provide no support for this, but we will be happy to hear your response. We can not help with installing Ruby, Python and required extensions.

To our knowledge, another company used this to create its name.

Requirements
============

SQLite (with ruby bindings), FANN

Source code overview
====================

 * ```chrumaj.py``` - produces training data from file
 * ```wikipedia-parser.py``` - produces learning data from Wikipedia
 * ```c-train``` - neural network trainer and tester (which is used for ga evaluation). Do a ```make``` and copy the resulting binary to root of the project. The network is trained, you need only test binary
 * ```ga.rb``` - genetic algorithm for creating new words and trying to resolve (to see if .com domain is free)
