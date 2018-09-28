## PDF Searcher
A very simple tool for searching recursively through a directory for  a certain term.

The tool takes three parameters
```bash
    --directory=<Place to start>
    --term=<Term to search for>
    -i    add to search without case sensitivity
```

### Example:
```bash
    $ python3 PDFSearch.py --directory=/home --term=Alex -i
```

For directories with spaces in the name, make sure to enclose the directory path in quotes.
