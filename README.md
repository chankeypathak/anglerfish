# anglerfish
Ugly but Enlightening


# Description of functions

# make_logger
`make_logger(name: str, when: str)`

**Description:** Returns a Logger, that has Colored output, logs to STDOUT, logs to Rotating File,
it will try to Log to Unix SysLog Server if any, log file is based on App name,
if the App ends correctly it will automatically ZIP compress the old unused rotated logs,
this should be the first one to use, since others may need a way to log out important info, you should always have a logger.

**Arguments:** `name` is a unique name of your App, optional will use PID if not provided, string type.
`when` is one of 'midnight', 'S', 'M', 'H', 'D', 'W0'-'W6', optional will use 'midnight' if not provided, string type.

**Keyword Arguments:** None.

**Returns:** logging.logger object.

**Usage Example:**

```python
from anglerfish import make_logger
log = make_logger("MyAppName")
log.debug("This is a Test.")
```

---

# bytes2human
`bytes2human(bites: int, to: str, bsize: int=1024)`

**Description:** Returns a Human Friendly string containing the argument integer bytes expressed as KiloBytes, MegaBytes, GigaBytes (...), 
uses a Byte Size of 1024 by default. Its basically a Bytes to KiloBytes, MegaBytes, GigaBytes (...).

**Arguments:** `bites` is the number of bytes, integer type.
`to` is one of 'k', 'm', 'g', 't', 'p', 'e', string type.
`bsize` is the Byte Size, default to 1024, since tipically is the desired byte size, integer type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Usage Example:**

```python
from anglerfish import bytes2human
bytes2human(3284902384, "g")
```

---

# check_encoding
`check_encoding()`

**Description:** Checks the all the Encodings of the System and Logs the results, to name a few like STDIN, STDERR, STDOUT, FileSystem, PYTHONIOENCODING and Default Encoding, takes no arguments, requires a working Logger, all "UTF-8" should be ideal on Linux/Mac.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Bool, True if everything is Ok.

**Usage Example:**

```python
from anglerfish import check_encoding
check_encoding()
```

---

# check_folder
`check_folder(folder_to_check: str)`

**Description:** Checks a working folder from `folder_to_check` argument for everything that can go wrong,
like no Read Permissions, that the folder does not exists, and no space left on it, etc etc. Returns Boolean.

**Arguments:** `folder_to_check` path of the folder to check, string type.

**Keyword Arguments:** None.

**Returns:** Bool, True if everything is Ok.

**Usage Example:**

```python
from anglerfish import check_folder
check_folder("/path/to/my/folder/")
```

---

# get_clipboard
`get_clipboard()`

**Description:** Cross-platform cross-desktop Clipboard functionality, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Tuple, `clipboard_copy()` and `clipboard_paste()`.

**Usage Example:**

```python
from anglerfish import get_clipboard
clipboard_copy, clipboard_paste = get_clipboard()
clipboard_copy("This is a Test.")
print(clipboard_paste())
```

---

# get_sanitized_string
`get_sanitized_string(stringy: str, repla: str="")`

**Description:** Take string argument and sanitize non-printable weird characters and return a clean string, 
ready to use on ASCII-only if required, optionally you can pass a replacement string to be used.

**Arguments:** `stringy` string to be clean out of weird characters, string type. 
`repla` a replacement string to be used instead of empty string `""`, can be a single character.

**Keyword Arguments:** None.

**Returns:** string, the same as input but ASCII-only ready.

**Usage Example:**

```python
from anglerfish import get_sanitized_string
get_sanitized_string("╭∩╮_(҂≖̀‿≖́)_╭∩╮")
```

---

# get_temp_folder
`get_temp_folder(appname: str)`

**Description:** Creates and returns a folder on the systems Temporary directory, 
creating it or not if needed, the folder will have the same name as the App passed as argument,
it means to be a liittle more safe than just writing everything to the systems temp folder where simple name collisions can overwrite and loss data.

**Arguments:** `appname` the name of your app.

**Keyword Arguments:** None.

**Returns:** string, full path to the apps temp folder.

**Usage Example:**

```python
from anglerfish import get_temp_folder
get_temp_folder("test")
```

---

# beep
`beep(waveform: tuple)`

**Description:** A "Beep" sound, a Cross-platform sound playing with Standard Lib only, No Sound file is required,
like old days Pc Speaker Buzzer Beep sound, meant for very long running operations and/or headless command line apps,
it works on Linux, Windows and Mac and requires nothing to run.

**Arguments:** `waveform` tuple containing integers, as the sinewave for the beep sound, defaults to `(79, 45, 32, 50, 99, 113, 126, 127)`.

**Keyword Arguments:** None.

**Returns:** Bool, True is sound playing went Ok.

**Usage Example:**

```python
from anglerfish import beep
beep()
```

---

# json_pretty
`json_pretty(json_dict: dict)`

**Description:** Pretty-Printing JSON data from dictionary to string, very human friendly representation, 
similar to YML but still valid JSON, works perfectly with JavaScript too.

**Arguments:** `json_dict` a dict with data that will be converted to JSON and pretty-printed as string.

**Keyword Arguments:** None.

**Returns:** string, the JSON data.

**Usage Example:**

```python
from anglerfish import json_pretty
json_pretty({"foo": True, "bar": 42, "baz": []})
```

---
# log_exception
`log_exception()`

**Description:** Log Exceptions but pretty printing with a lot more information of whats going on under the hood, 
returns a string printing it via a working logger at the same time, 
works for Exceptions like on `try...except...finally` constructions, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** string, the info about the exception.

**Usage Example:**

```python
from anglerfish import log_exception
try:
    0 / 0
except Exception:
    log_exception()
```

---

# ipdb_on_exception
`ipdb_on_exception(debugger: str="ipdb")`

**Description:** Automatic iPDB Debugger when an Exception happens, 
it install a handler to attach a post-mortem ipdb console on an exception on the fly at runtime,
PDB, iPDB can be used as Debugger console.

**Arguments:** `debugger` one of "ipdb", "pdb".

**Keyword Arguments:** None.

**Returns:** None.

**Usage Example:**

```python
from anglerfish import ipdb_on_exception
ipdb_on_exception()
try:
    0 / 0
except Exception:
    pass
```

---

# seconds2human
`seconds2human(time_on_seconds: int)`

**Description:** From Time on seconds to very human friendly string representation,
calculates time with precision from seconds to days, returns the string with representation.

**Arguments:** `time_on_seconds` time on seconds, integer type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Usage Example:**

```python
from anglerfish import seconds2human
seconds2human(490890)
```

---

# set_process_name
`set_process_name(name: str)`

**Description:** Set the current process name to the argument `name`, 
so instead of all your apps listing as `python` on the system monitor they will have proper names,
this helps debug, troubleshooting and system administration in general.

**Arguments:** `name` the name of your app.

**Keyword Arguments:** None.

**Returns:** Boolean, True if it can change the process name.

**Usage Example:**

```python
from anglerfish import set_process_name
set_process_name("MyApp")
```

---

# walk2list
`walk2list(where: str, target: str, omit: str, links: Bool=False, tuply: Bool=True)`

**Description:** Perform full recursive walk of `where` folder path, 
search for `target` like files, ignoring `omit` like files, follow symbolic links if `links` is `True`,
convert the output to `tuple` if `tuply` is `True`, else return the `list` containing the path of all the files.

**Arguments:** `where` path to a folder to scan, string type.
`target` type of files to search for, for example `.py`, string type, 
`omit` type of files to ignote, for example `.pyc`, string type, 
`links` a Boolean, `True` to follow simbolic links, 
`tuply` a Boolean, `True` to convert the output `list` into a `tuple`.

**Keyword Arguments:** None.

**Returns:** `list` or `tuple`

**Usage Example:**

```python
from anglerfish import walk2list
walk2list(".")
```

---

# walk2dict
`walk2dict(folder: str, links: Bool=False, showhidden: Bool=False, strip: Bool=False, jsony: Bool=False)`

**Description:** Return Nested Dictionary that represents the folders and files structure of the folder,


**Arguments:** `folder` path to folder to scan, string type, 
`links` a Boolean, `True` to follow simbolic links,
`showhidden` a Boolean, `True` to show hidden files and folders,
`strip` a Boolean, `True` to strip the relative folder path, 
`jsony` a Boolean, `True` to convert the `dict` to JSON.

**Keyword Arguments:** None.

**Returns:** `dict` or `str` with JSON.

**Usage Example:**

```python
from anglerfish import walk2dict
walk2dict(".")
```

---

# multiprocessed
`multiprocessed(function: Callable, arguments: object, cpu_num: int=1, thread_num: int=1, timeout: int=None)`

**Description:** Execute code on multiple CPU Cores and multiple Threads per CPU Core,
with optional Timeout, on a quick and easy way.

**Arguments:** `function` a function of Callable type to execute code, 
`arguments` is an object that represent the arguments for the function, 
`cpu_num` how many CPU Cores to use, integer type, 
`thread_num` how many Threads per CPU Core to use, integer type, 
`timeout` a Timeout on Seconds, integer type or None.

**Keyword Arguments:** None.

**Returns:** concurrent.futures object.

**Usage Example:**

```python
from anglerfish import multiprocessed
import time

def process_job(job):  # a simple function for testing only
    time.sleep(1)
    count = 100
    while count > 0:
        count -= 1
    return job
jobs = [str(i) for i in range(30)]  # a simple list

print(multiprocessed(process_job, jobs, cpu_num=1, thread_num=4))
print(multiprocessed(process_job, jobs, cpu_num=4, thread_num=1))
```

---

# threads
`@threads(n: int, timeout=None)`

**Description:** Execute code on multiple Threads, with optional Timeout, on a quick and easy way.

**Arguments:** `n` number of Threads to use for the function execution, integer type, 
`timeout` a Timeout on seconds or None.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Usage Example:**

```python
from anglerfish import threads
import time
@threads(4)
def process_job():  # a simple function for testing only
    return time.sleep(1)
process_job()
```

---

# retry
`@retry(tries: int=5, delay: int=3, backoff: int=2,
          timeout: int=None, silent: Bool=False, logger=None)`

**Description:** Retry calling the decorated function using an exponential backoff and timeout.

**Arguments:** `tries` how many times retry the operation, defaults to 5, integer type, 
`delay` delay between executions, defaults to 3, integer type, `backoff` an exponential backoff offset to apply to the `delay`, defaults to 2, integer type, `timeout` a timeout for the whole execution or None, defaults to None, 
`silent` a boolean `True` to be Silent when running the reties, defaults to False, 
`logger` a working logger to log into or None to use `print()`.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Usage Example:**

```python
from anglerfish import retry
@retry(4)
def retry_job():  # a simple function for testing only
    return open("").read()  # Will Fail as expected
retry_job()
```

---

# set_single_instance
`set_single_instance(name: str, port: int=8888)`

**Description:** Set a single instance Lock based on Sockets and return socket.socket object or None.

**Arguments:** `name` the name of your app to be used as Lock name, 
`port` port number to be used when Unix Socket is not available, mostly on MS Windows, defaults to 8888, integer type.

**Keyword Arguments:** None.

**Returns:** socket.socket object or None.

**Usage Example:**

```python
from anglerfish import set_single_instance
set_single_instance("MyApp")
```

---

# env2globals
`env2globals(pattern: str)`

**Description:** Auto add ENV environtment variables starting with `PY_` in upper case to python globals dict.

**Arguments:** `pattern` the pattern to select which variables to add, default to `PY_`

**Keyword Arguments:** None.

**Returns:** Boolean, True if everything is Ok.

**Usage Example:**

```python
from anglerfish import env2globals
env2globals()
```

---

# html2ebook
`html2ebook(files: list, fyle: str=uuid4().hex + ".epub", meta={})`

**Description:** Convert a folder with HTML5/CSS3 to eBook ePub. JavaScript does not Work on ePub.

**Arguments:** `files` a tuple with the list of HTML/CSS files to add to the eBook.
`fyle` an output file path string, defaults to an uuid4 hexadecimal if not provided.

**Keyword Arguments:** `meta` contains a dict with
`title` is the eBook Title (Fallbacks to Filename if not provided).
`author`  is the eBook Author (Fallbacks to Username if not provided).
`lang` is the eBook Language (Fallbacks to English if not provided).
`des` is a friendly eBook Description (Fallbacks to Filename if not provided).
`copi` eBook CopyRights (Fallbacks to Creative Commons 'CC-BY-NC-SA v.4.0' if not provided).
`pub` the eBook Publisher (Fallbacks to 'Python' if not provided).
`date` Date and Time ISO format of eBook creation (Fallbacks to Current Date and Time if not provided).

**Returns:** a string with the file path of the new eBook file.

**Usage Example:**

```python
from anglerfish import html2ebook
html2ebook(("/mybook/html/index.html", "/mybook/html/chapter1.html"))
```
