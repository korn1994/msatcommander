## Using biopython from CVS ##

**As of 3/17/2007, this is not necessary** as the needed changes are in the [biopython 1.43 release](http://biopython.org/wiki/Download).  However, if you want the bleeding edge, here are instructions for checking it out:

Biopython may be checked out of anonymous CVS (password: cvs):
```
cvs -d:pserver:cvs@cvs.open-bio.org:/home/repository/biopython login
cvs -d:pserver:cvs@cvs.open-bio.org:/home/repository/biopython co biopython
```

You will then need to install these files as you would any other module for python:

```
% python setup.py install
```

