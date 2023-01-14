# Get rid off download bars and the like


Install packages in [`environment.yml`](environment.yml) into Python environment. The script is desgined
to be executed from the terminal like


```console
$ conda activate cleanpdf
$ python clean_pdf.py path/to/pdf
```

If no arguments are provided the script will ask you if you really want to overwrite
the original file. There are, however, also multiple options and flags that can be
passed to the script:

- `--new-path`
  
  Path to the new file that should be created.
- `--position`
 
  A tuple of four points (x0, y0, x1, y1) defining the top-left and bottom-right corner
  of the rectangle that should be removed.
- `--exclude`
 
  A single string where pages that should be excluded are separated by a comma.
- `--overwrite`
 
  If this flag is set the original file will be overwritten without confirmation.
  

A more advanced command could look like this:

```console
$ python clean_pdf.py path/to/pdf --new-path test.pdf --exclude "0, 45"
```