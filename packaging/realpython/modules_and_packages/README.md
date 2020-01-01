https://realpython.com/python-modules-packages/

**Find location of an imported module**
```python
>>> import mod
>>> mod.__file__
'C:\\Users\\john\\mod.py'
```

**Ways to import**

```python
import <module_name>
from <module_name> import <name> as <alt_name>
from <module_name> import <name(s)>
import <module_name> as <alt_name>

```

**Module import vs script**

When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module. However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'. Using this fact, you can discern which is the case at run-time and alter behavior accordingly:

```python
if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)

```
--- 

## `__init.py__`

Example package:

![](https://files.realpython.com/media/pkg1.9af1c7aea48f.png)


Without the `__init__.py` file, can only import modules with:

```python
import pkg.mod1, pkg.mod2
from pkg import mod1
from pkg import mod2 as quux

from pkg.mod1 import foo
from pkg.mod2 import Bar as Qux

```

`import pkg` has **NO** effect without `
__init__.py`


If a file named `__init__.py` is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.

*In `__init__.py`*
```python
print(f'Invoking __init__.py for {__name__}')
import pkg.mod1, pkg.mod2
```

*Automatic import of modules*
```python
>>> import pkg
Invoking __init__.py for pkg
>>> pkg.mod1.foo()
[mod1] foo()
>>> pkg.mod2.bar()
[mod2] bar()
```

> Note: Much of the Python documentation states that an __init__.py file must be present in the package directory when creating a package. This was once true. It used to be that the very presence of __init__.py signified to Python that a package was being defined. The file could contain initialization code or even be empty, but it had to be present.

>Starting with Python 3.3, Implicit Namespace Packages were introduced. These allow for the creation of a package without any __init__.py file. Of course, it can still be present if package initialization is needed. But it is no longer required.


---
## `__all__`


In summary, `__all__` is used by both packages and modules to control what is imported when import * is specified. But the default behavior differs:

For a package, when `__all__` in `__init__.py` is not defined, import * does not import anything.
For a module, when `__all__` is not defined, import * imports everything (except—you guessed it—names starting with an underscore).
