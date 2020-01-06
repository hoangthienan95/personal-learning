# Reading a file

## use `open`

```python
In [1]: file_path = 'bookofdreams.txt'
In [2]: open_file = open(file_path, 'r')
In [3]: text = open_file.read()
In [4]: len(text)
Out[4]: 476909”
```

## use `with open(file, 'mode') as opened_file`

## use `pathlib`

```python
In [35]: import pathlib

In [36]: path = pathlib.Path(
           "/Users/kbehrman/projects/autoscaler/check_pending.py")

In [37]: path.read_text()

```

## JSON

```python
In [35]: import pathlib

In [36]: path = pathlib.Path(
           "/Users/kbehrman/projects/autoscaler/check_pending.py")

In [37]: path.read_text()
```

## YAML

```python
In [18]: import yaml

In [19]: with open('verify-apache.yml', 'r') as opened_file:
    ...:     verify_apache = yaml.safe_load(opened_file)
    ...:”
    
    ...

    In [22]: with open('verify-apache.yml', 'w') as opened_file:
    ...:     yaml.dump(verify_apache, opened_file)
```

## Read data in chunk

```python
In [27]: with open('bb141548a754113e.jpg', 'rb') as source_file:
    ...:     while True:
    ...:         chunk = source_file.read(1024)
    ...:         if chunk:
    ...:             process_data(chunk)
    ...:         else:
    ...:             break
    ...: 

```

## Hashing

```python
In [62]: import hashlib

In [63]: secret = "This is the password or document text"

In [64]: bsecret = secret.encode() #turns into binary string

In [65]: m = hashlib.md5()

In [66]: m.update(bsecret)

In [67]: m.digest()
Out[67]: b' \xf5\x06\xe6\xfc\x1c\xbe\x86\xddj\x96C\x10\x0f5E 
```

Different operating systems use different escaped characters to represent line endings. Unix systems use `\n` and Windows systems use `\r\n`. **Python converts these to `\n`**


## `os` module

```python
In [1]: os.listdir('.') 
Out[1]: ['__init__.py', 'os_path_example.py']

In [2]: os.rename('_crud_handler', 'crud_handler') 

In [3]: os.chmod('my_script.py', 0o777) 

In [4]: os.mkdir('/tmp/holding') 

In [5]: os.makedirs('/Users/kbehrman/tmp/scripts/devops') 

In [6]: os.remove('my_script.py') 

In [7]: os.rmdir('/tmp/holding') 

In [8]: os.removedirs('/Users/kbehrman/tmp/scripts/devops') 

In [9]: os.stat('crud_handler') 
Out[9]: os.stat_result(st_mode=16877,
                       st_ino=4359290300,
                       st_dev=16777220,
                       st_nlink=18,
                       st_uid=501,
                       st_gid=20,
                       st_size=576,
                       st_atime=1544115987,
```
