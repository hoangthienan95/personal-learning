https://realpython.com/absolute-vs-relative-python-imports/

1. Look in `sys.modules` (cache)
2. Standard lib
3. Current directory
4. Search sys.path


 Importing a package essentially imports the package’s `__init__.py` file as a module

 ## Example

### Directory structure
```

└── project
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── package2
        ├── __init__.py
        ├── module3.py
        ├── module4.py
        └── subpackage1
            └── module5.py
 
```

- package1/module2.py contains a function, function1.
- package2/__init__.py contains a class, class1.
- package2/subpackage1/module5.py contains a function, function2.

### Absolute import

```python
from package1 import module1
from package1.module2 import function1
from package2 import class1
from package2.subpackage1.module5 import function2
```

### Relative import

```python

# package1/module1.py

from .module2 import function1
```


```python

# package2/module3.py

from . import class1
from .subpackage1.module5 import function2

```
