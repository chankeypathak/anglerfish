# anglerfish
Ugly but Enlightening


# Description of functions

`make_logger(name: str, when: str)`

**Description:** Returns a Logger, that has Colored output, logs to STDOUT, logs to Rotating File,
it will try to Log to Unix SysLog Server if any, log file is based on App name,
if the App ends correctly it will automatically ZIP compress the old unused rotated logs,
this should be the first one to use, since others may need a way to log out important info.

**Arguments:** `name` is a unique name of your App, optional will use PID if not provided, string type.
`when` is one of 'midnight', 'S', 'M', 'H', 'D', 'W0'-'W6', optional will use 'midnight' if not provided, string type.

**Keyword Arguments:** None.

**Returns:** logging.logger object.

**Usage Example:**

python
```
from anglerfish import make_logger
log = make_logger("MyAppName")
log.debug("This is a Test.")
```

---


`bytes2human(bites: int, to: str, bsize: int=1024)`

**Description:** Returns a Human Friendly string containing the argument integer bytes expressed as KiloBytes, MegaBytes, GigaBytes (...), 
uses a Byte Size of 1024 by default, is basically a Bytes to KiloBytes, MegaBytes, GigaBytes (...).

**Arguments:** `bites` is the number of bytes, integer type.
`to` is one of 'k', 'm', 'g', 't', 'p', 'e', string type.
`bsize` is the Byte Size, default to 1024, since tipically is the desired byte size, integer type.

**Keyword Arguments:** None.

**Returns:** string.

**Usage Example:**

python
```
from anglerfish import bytes2human
bytes2human(3284902384, "g")
```

---

`check_encoding()`

**Description:** Checks the all the Encodings of the System and Logs the results, to name a few like STDIN, STDERR, STDOUT, FileSystem, PYTHONIOENCODING and Default Encoding, takes no arguments, requires a working Logger, all "UTF-8" should be ideal on Linux/Mac.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Bool, True if everything is Ok.

**Usage Example:**

python
```
from anglerfish import check_encoding
check_encoding()
```

---

`check_folder(folder_to_check: str)`

**Description:** Checks a working folder from `folder_to_check` argument for everything that can go wrong,
including no Read Permissions, that the folder does not exists, and no space left on it, returns Boolean.

**Arguments:** `folder_to_check` path of the folder to check, string type.

**Keyword Arguments:** None.

**Returns:** Bool, True if everything is Ok.

**Usage Example:**

python
```
from anglerfish import check_folder
check_folder("/path/to/my/folder/")
```

---

`get_clipboard()`

**Description:** Cross-platform cross-desktop Clipboard functionality, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Tuple, `clipboard_copy()' and `clipboard_paste()`.

**Usage Example:**

python
```
from anglerfish import get_clipboard
clipboard_copy, clipboard_paste = get_clipboard()
clipboard_copy("This is a Test.")
print(clipboard_paste())
```

---

`get_sanitized_string(stringy: str, repla: str="")`

**Description:** Take string argument and sanitize non-printable weird characters and return a clean string, 
ready to use on ASCII-only if required, optionally you can pass a replacement string to be used.

**Arguments:** `stringy` string to be clean out of weird characters, string type. 
`repla` a replacement string to be used instead of empty string `""` can be a single character.

**Keyword Arguments:** None.

**Returns:** string.

**Usage Example:**

python
```
from anglerfish import get_sanitized_string
get_sanitized_string("╭∩╮_(҂≖̀‿≖́)_╭∩╮")
```

---

`get_temp_folder(appname: str)`

**Description:** Creates and returns a folder on the systems Temporary directory, 
creating it or not if needed, the folder will have the same name as the App passed as argument,
it means to be a liittle more safe than just writing everything to the systems temp folder where simple name collisions can overwrite and loss data.

**Arguments:** `appname` the name of your app.

**Keyword Arguments:** None.

**Returns:** string, full path to the apps temp folder.

**Usage Example:**

python
```
from anglerfish import get_temp_folder
get_temp_folder("test")
```

---

`beep(waveform: tuple)`

**Description:** A "Beep" sound, a Cross-platform sound playing with Standard Lib only, No Sound file is required,
like old days Pc Speaker Buzzer Beep sound, meant for very long running operations and/or headless command line apps,
it works on Linux, Windows and Mac and requires nothing to run.

**Arguments:** `waveform` tuple containing integers, as the sinewave for the beep sound, defaults to `(79, 45, 32, 50, 99, 113, 126, 127)`.

**Keyword Arguments:** None.

**Returns:** Bool, True is sound playing went Ok.

**Usage Example:**

python
```
from anglerfish import beep
beep()
```

---

`json_pretty(json_dict: dict)`

**Description:** Pretty-Printing JSON data from dictionary to string, very human friendly representation, 
similar to YML but still valid JSON, works perfectly with JavaScript too.

**Arguments:** `json_dict` a dict with data that will be converted to JSON and pretty-printed as string.

**Keyword Arguments:** None.

**Returns:** string, the JSON data.

**Usage Example:**

python
```
from anglerfish import json_pretty
json_pretty({"foo": True, "bar": 42, "baz": []})
```

---

`log_exception()`

**Description:** Log Exceptions but pretty printing with a lot more information of whats going on under the hood, 
returns a string printing it via a working logger at the same time, 
works for Exceptions like on `try...except...finally` constructions, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** string, the info about the exception.

**Usage Example:**

python
```
from anglerfish import log_exception
try:
    0 / 0
except Exception:
    log_exception()
```






---

`make_logger()`

**Description:** .

**Arguments:** .

**Keyword Arguments:** None.

**Returns:** None

**Usage Example:**

python
```
from anglerfish import 

```
