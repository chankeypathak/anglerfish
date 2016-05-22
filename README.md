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
