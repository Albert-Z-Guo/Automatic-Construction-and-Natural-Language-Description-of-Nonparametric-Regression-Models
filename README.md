This repo contains the fixed source code from [Automatic Construction and Natural-Language Description of Nonparametric Regression Models](https://github.com/jamesrobertlloyd/gpss-research).

To install all libraries/dependencies, run:
```bash
pip3 install -r requirement.txt
```

Make sure `config.py` in `./source/cblparallel` has the local paths for [MATLAB](https://www.mathworks.com/products/matlab.html) and GPML. In addition, make sure MATLAB's [Statistics and Machine Learning Toolbox](https://www.mathworks.com/products/statistics.html) and [Signal Processing Toolbox](https://www.mathworks.com/products/signal.html) are installed as well.

To start the program, run:
```bash
./source/demo.py
```

New directories will be generated in `./examples/` which contain all `.tex` files along with MATLAB's `.fig` files. Since LaTeX does not compile with `.fig` files, run `conversion.m` to convert all `.fig` files to `.eps` files. In addition, when compiling using LaTeX, make sure `format` and `include` folders are included.

It is recommended to compile the zipped directory directly via [Overleaf](https://www.overleaf.com).
