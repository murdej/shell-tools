# shell-tools

## dudiff

Compares two outputs command `du`. Displays deleted, new, growed and reduced directories and size change.

Example
<pre>
 du > 20160515.du
 ...
 du > 20160615.du
 dudiff.py 20160515.du 20160615.du
 
 deleted:
                    4 ./d3
 new:
                   16 ./d4
 growed:
                   52 ./d1
                   48 ./d1/1
 reduced:
                   68 ./d2
                    4 .
</pre>

