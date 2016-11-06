
# anglerfish

![anglerfish](https://raw.githubusercontent.com/juancarlospaco/anglerfish/master/temp.jpg "Ugly but Enlightening")

*Ugly but Enlightening* | https://pypi.python.org/pypi/anglerfish

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg)](http://opensource.org/licenses/GPL-3.0)
[![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg)](http://opensource.org/licenses/LGPL-3.0)
[![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg)](http://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/anglerfish.svg)](https://pypi.python.org/pypi/anglerfish)
[![Build Status](https://img.shields.io/travis/juancarlospaco/anglerfish/master.svg)](https://travis-ci.org/juancarlospaco/anglerfish)

[![Donate BitCoins](https://www.coinbase.com/assets/buttons/donation_large-5cf4f17cc2d2ae2f45b6b021ee498297409c94dcf0ba1bbf76fd5668e80b0d02.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Donate Bitcoins")
[![Subscribe with BitCoins](https://www.coinbase.com/assets/buttons/subscription_large-11d991f628216af05156fae88a48ce25c0cb36447a265421a43a62e572af3853.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Subscribe with BitCoins")
[![Pay with BitCoins](https://www.coinbase.com/assets/buttons/buy_now_large-6f15fa5979d25404827a7329e8a5ec332a42cf4fd73e27a2c3ccda017034e1b0.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Pay with BitCoins")
[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif "Donate with or without Credit Card")](http://goo.gl/cB7PR)


# Description of functions

<details>
<summary>
make_logger
</summary>

## make_logger

`anglerfish.make_logger(name: str, when: str='midnight', single_zip: bool=False, log_file: str=None, backup_count: int=100, emoji: bool=False)`

**Description:** Returns a Logger, that has Colored output, logs to STDOUT, logs to Rotating File,
it will try to Log to Unix SysLog Server if any, log file is based on App name,
if the App ends correctly it will automatically ZIP compress the old unused rotated logs,
Colored output may not be available on MS Windows OS,
this should be the first one to use, since others may need a way to log out important info, you should always have a logger.
Please use a unique and distinctive name for your app, and use the same name every time Anglerfish needs an app name.

**Arguments:**
- `name` is a unique name of your App, like a unique identifier, string type.
- `when` is one of 'midnight', 'S', 'M', 'H', 'D', 'W0'-'W6', optional will use 'midnight' if not provided, string type.
- `single_zip` Unused Old Rotated Logs will be ZIP Compressed automagically, `True` equals 1 ZIP per Log, `False` equals 1 ZIP for *All* Logs, lets the user choose if you want a single ZIP or one per log file.
- `log_file` log filename path or None, optional, defaults to `None`, `os.path.join(gettempdir(), name.lower().strip() + ".log")` will be used if left as `None`, log filename path on use will be printed to stdout automatically, string type.
- `backup_count` number of log backups to keep, optional, defaults to `100`, meaning 100 backups, integer type.
- `emoji` Kitten Emoji on logger *(ala Yarn)*, Optional, defaults to `False`, boolean type.

**Keyword Arguments:** None.

**Returns:** logging.logger object.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/__init__.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import make_logger
log = make_logger("MyAppName")
log.debug("This is a Test.")
log.info("This is a Test.")
log.warning("This is a Test.")
log.critical("This is a Test.")
log.exception("This is a Test.")
```
</details>


<details>
<summary>
get_free_port
</summary>

## get_free_port

`anglerfish.get_free_port(port_range: tuple=(8000, 9000))`

**Description:** Returns a free unused port number integer.
Takes a tuple of 2 integers as argument, being the range of port numbers to scan.

**Arguments:**
- `port_range` is the range of port numbers to scan, starting port and ending port numbers. 2 items only are allowed. Tuple type.

**Keyword Arguments:** None.

**Returns:** Integer, a free unused port number.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_free_port.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import get_free_port
get_free_port()
```
</details>


<details>
<summary>
make_notification
</summary>

## make_notification

`anglerfish.make_notification(title: str, message: str="", name: str="", icon: str="", timeout: int=3000))`

**Description:** Makes a Passive Notification Bubble (Passive Popup), it works cross-desktop, using one of DBus, PyNotify, notify-send, kdialog, zenity or xmessage.
Should degrade nicely on operating systems that dont have any of those.
Best results are with D-Bus.

**Arguments:**
- `title` is the short title of your message, mandatory, string type.
- `message` is body of your message, defaults to empty string, optional, string type.
- `name` is the name of your App, defaults to empty string, optional, string type.
- `icon` is the icon name of your App, defaults to empty string, optional, string type.
- `timeout` is the timeout for your notification bubble, defaults to `3000`, optional, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_notification.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
from anglerfish import make_notification
make_notification("test")
```
</details>


<details>
<summary>
bytes2human
</summary>

## bytes2human

`anglerfish.bytes2human(bites: int, to: str, bsize: int=1024)`

**Description:** Returns a Human Friendly string containing the argument integer bytes expressed as KiloBytes, MegaBytes, GigaBytes (...),
uses a Byte Size of `1024` by default. Its basically a Bytes to KiloBytes, MegaBytes, GigaBytes (...).

**Arguments:**
- `bites` is the number of bytes, integer type.
- `to` is one of 'k', 'm', 'g', 't', 'p', 'e', being KiloBytes, MegaBytes, GigaBytes (...), string type.
- `bsize` is the Byte Size, defaults to `1024`, since tipically is the desired byte size, integer type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/bytes2human.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import bytes2human
bytes2human(3284902384, "g")
```
</details>


<details>
<summary>
check_encoding
</summary>

## check_encoding

`anglerfish.check_encoding(check_root: bool=True)`

**Description:** Checks the all the Encodings of the System and Logs the results, to name a few like `STDIN`, `STDERR`, `STDOUT`, FileSystem, `PYTHONIOENCODING` and Default Encoding, takes no arguments, requires a working Logger, all "UTF-8" should be ideal on Linux/Mac.

**Arguments:**
- `check_root` Check for root/administrator privileges, optional, boolean type.

**Keyword Arguments:** None.

**Returns:** Bool, `True` if everything is Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_encoding.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import check_encoding
check_encoding()
```
</details>


<details>
<summary>
check_folder
</summary>

## check_folder

`anglerfish.check_folder(folder_to_check: str, check_space: int=1)`

**Description:** Checks a working folder from `folder_to_check` argument for everything that can go wrong,
like no Read Permissions, that the folder does not exists, and no space left on it, etc etc. Returns Boolean.

**Arguments:**
- `folder_to_check` path of the folder to check, string type.
- `check_space` Check for a minimum of disk space, Units are GigaBytes, Defaults to at least 1Gb, optional, integer type.

**Keyword Arguments:** None.

**Returns:** Bool, True if everything is Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_folder.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import check_folder
check_folder("/path/to/my/folder/")
```
</details>


<details>
<summary>
get_clipboard
</summary>

## get_clipboard

`anglerfish.get_clipboard()`

**Description:** Cross-platform cross-desktop Clipboard functionality, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** NamedTuple, `clipboard_copy()` and `clipboard_paste()`.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_clipboard.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import get_clipboard
clipboard_copy, clipboard_paste = get_clipboard()
clipboard_copy("This is a Test.")
print(clipboard_paste())

# Or this way:
get_clipboard().copy("This is a Test.")
print(get_clipboard().paste())
```
</details>


<details>
<summary>
get_sanitized_string
</summary>

## get_sanitized_string

`anglerfish.get_sanitized_string(stringy: str, repla: str="")`

**Description:** Take string argument and sanitize non-printable weird characters and return a clean string,
ready to use on ASCII-only if required, optionally you can pass a replacement string to be used.

**Arguments:**
- `stringy` string to be clean out of weird characters, string type.
- `repla` a replacement string to be used instead of empty string `""`, can be a single character.

**Keyword Arguments:** None.

**Returns:** string, the same as input but ASCII-only ready.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_sanitized_string.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import get_sanitized_string
get_sanitized_string("╭∩╮_(҂≖̀‿≖́)_╭∩╮")
```
</details>


<details>
<summary>
get_temp_folder
</summary>

## get_temp_folder

`anglerfish.get_temp_folder(appname: str)`

**Description:** Creates and returns a folder on the systems Temporary directory,
creating it or not if needed, the folder will have the same name as the App passed as argument,
it means to be a liittle more safe than just writing everything to the systems temp folder where simple name collisions can overwrite and loss data.

**Arguments:** `appname` the name of your app.

**Keyword Arguments:** None.

**Returns:** string, full path to the apps temp folder.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_temp_folder.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import get_temp_folder
get_temp_folder("test")
```
</details>


<details>
<summary>
beep
</summary>

## beep

`anglerfish.beep(waveform: tuple)`

**Description:** A "Beep" sound, a Cross-platform sound playing with Standard Lib only, No Sound file is required,
like old days Pc Speaker Buzzer Beep sound, meant for very long running operations and/or headless command line apps,
it works on Linux, Windows and Mac and requires nothing to run.

**Arguments:** `waveform` tuple containing integers, as the sinewave for the beep sound, defaults to `(79, 45, 32, 50, 99, 113, 126, 127)`.

**Keyword Arguments:** None.

**Returns:** Bool, True is sound playing went Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_beep.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :question:         | **Windows** | Untested    |

**Usage Example:**

```python
from anglerfish import beep
beep()
```
</details>


<details>
<summary>
json_pretty
</summary>

## json_pretty

`anglerfish.json_pretty(json_dict: dict)`

**Description:** Pretty-Printing JSON data from dictionary to string, very human friendly representation,
similar to YML but still valid JSON, works perfectly with JavaScript too.

**Arguments:** `json_dict` a dict with data that will be converted to JSON and pretty-printed as string.

**Keyword Arguments:** None.

**Returns:** string, the JSON data.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_json_pretty.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import json_pretty
json_pretty({"foo": True, "bar": 42, "baz": []})
```
</details>


<details>
<summary>
log_exception
</summary>

## log_exception

`anglerfish.log_exception()`

**Description:** Log Exceptions but pretty printing with a lot more information of whats going on under the hood,
returns a string printing it via a working logger at the same time,
works for Exceptions like on `try...except...finally` constructions, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** string, the info about the exception.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_log_exception.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import log_exception
try:
    0 / 0
except Exception:
    log_exception()
```
</details>


<details>
<summary>
ipdb_on_exception
</summary>

## ipdb_on_exception

`anglerfish.ipdb_on_exception(debugger: str="ipdb")`

**Description:** Automatic iPDB Debugger when an Exception happens,
it install a handler to attach a post-mortem ipdb console on an exception on the fly at runtime,
PDB, iPDB can be used as Debugger console.

**Arguments:**
- `debugger` one of `"ipdb"`, `"pdb"`.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_pdb_on_exception.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import ipdb_on_exception
ipdb_on_exception()
try:
    0 / 0
except Exception:
    pass
```
</details>


<details>
<summary>
seconds2human
</summary>

## seconds2human

`anglerfish.seconds2human(time_on_seconds: int, do_year: bool=True, unit_words: dict={"y": " Years ", "d": " Days ",
"h": " Hours ", "m": " Minutes ", "s": " Seconds "})`

**Description:** From Time on seconds to very human friendly string representation,
calculates time with precision from seconds to days, returns the string with representation.

**Arguments:**
- `time_on_seconds` time on seconds, integer type.
- `do_year` True to calculate Years, optional, defaults to `True`, boolean type.
- `unit_words` dictionary with words representing human Time units,
useful for internationalization of the output string, defaults to English, optional, dict type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/seconds2human.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import seconds2human
seconds2human(490890)
```
</details>


<details>
<summary>
deltatime2human
</summary>

## deltatime2human

`anglerfish.deltatime2human(time_delta, do_year: bool=True, unit_words: dict={"y": " Years ", "d": " Days ",
"h": " Hours ", "m": " Minutes ", "s": " Seconds "})`

**Description:** Convert a TimeDelta object to human string representation.
From `deltatime` object to very human friendly string representation,
calculates time with precision from seconds to years, returns the string with representawation.
Internally is just a shortcut to `anglerfish.seconds2human()`.

**Arguments:**
- `time_delta` deltatime object, `datetime.deltatime` type.
- `do_year` True to calculate Years, optional, defaults to `True`, boolean type.
- `unit_words` dictionary with words representing human Time units,
useful for internationalization of the output string, defaults to English, optional, dict type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/seconds2human.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
import datetime
from anglerfish import deltatime2human
deltatime_object = datetime.timedelta(seconds=123.456789)
deltatime2human(deltatime_object)
```
</details>


<details>
<summary>
set_process_name
</summary>

## set_process_name

`anglerfish.set_process_name(name: str, nice: bool=True)`

**Description:** Set the current process name to the argument `name`,
so instead of all your apps listing as `python` on the system monitor they will have proper names,
this helps debug, troubleshooting and system administration in general.

**Arguments:**
- `name` the name of your app.
- `nice` set a soft CPU nice priority, optional, defaults to `True`, boolean type.

**Keyword Arguments:** None.

**Returns:** Boolean, True if it can change the process name.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_process_name.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
from anglerfish import set_process_name
set_process_name("MyApp")
```
</details>


<details>
<summary>
walk2list
</summary>

## walk2list

`anglerfish.walk2list(where: str, target: str, omit: str, links: Bool=False, tuply: Bool=True)`

**Description:** Perform full recursive walk of `where` folder path,
search for `target` like files, ignoring `omit` like files, follow symbolic links if `links` is `True`,
convert the output to `tuple` if `tuply` is `True`, else return the `list` containing the path of all the files.

**Arguments:**
- `where` path to a folder to scan, string type.
- `target` type of files to search for, for example `.py`, string type,
- `omit` type of files to ignote, for example `.pyc`, string type,
- `links` a Boolean, `True` to follow simbolic links,
- `tuply` a Boolean, `True` to convert the output `list` into a `tuple`.

**Keyword Arguments:** None.

**Returns:** `list` or `tuple`

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/walk2list.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import walk2list
walk2list(".")
```
</details>


<details>
<summary>
walk2dict
</summary>

## walk2dict

`anglerfish.walk2dict(folder: str, links: Bool=False, showhidden: Bool=False, strip: Bool=False, jsony: Bool=False)`

**Description:** Return Nested Dictionary that represents the folders and files structure of the folder,


**Arguments:**
- `folder` path to folder to scan, string type,
- `links` a Boolean, `True` to follow simbolic links,
- `showhidden` a Boolean, `True` to show hidden files and folders,
- `strip` a Boolean, `True` to strip the relative folder path,
- `jsony` a Boolean, `True` to convert the `dict` to JSON.

**Keyword Arguments:** None.

**Returns:** `dict` or `str` with JSON.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/walk2dict.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import walk2dict
walk2dict(".")
```
</details>


<details>
<summary>
multiprocessed
</summary>

## multiprocessed

`anglerfish.multiprocessed(function: Callable, arguments: object, cpu_num: int=1, thread_num: int=1, timeout: int=None)`

**Description:** Execute code on multiple CPU Cores and multiple Threads per CPU Core,
with optional Timeout, on a quick and easy way.

**Arguments:**
- `function` a function of Callable type to execute code,
- `arguments` is an object that represent the arguments for the function,
- `cpu_num` how many CPU Cores to use, integer type,
- `thread_num` how many Threads per CPU Core to use, integer type,
- `timeout` a Timeout on Seconds, integer type or None.

**Keyword Arguments:** None.

**Returns:** concurrent.futures object.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_multiprocess.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

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
</details>


<details>
<summary>
threads
</summary>

## threads

`@threads(n: int, timeout=None)`

**Description:** Execute code on multiple Threads, with optional Timeout, on a quick and easy way.

**Arguments:**
- `n` number of Threads to use for the function execution, integer type,
- `timeout` a Timeout on seconds or None.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_multithread.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import threads
import time
@threads(4)
def process_job():  # a simple function for testing only
    return time.sleep(1)
process_job()
```
</details>


<details>
<summary>
ChainableFuture
</summary>

## ChainableFuture

`anglerfish.ChainableFuture.then(on_success: Callable=None, on_fail: Callable=None)`

**Description:** Make a Chainable `concurrent.futures.Future` that has a `.then()` api.
This copies the JavaScript-like promises `.then()` api on Python 3.
For deep technical theory please see https://github.com/promises-aplus/promises-spec
For Python 3 Futures (JS-like promises) please see https://www.python.org/dev/peps/pep-3148
For simple human explanation this chains one Future with another Future.

**Arguments:**
- `on_success` a function to run when this Future success Ok,Callable type,Optional.
- `on_fail` a function to run when this Future fails,Callable type,Optional.

**Keyword Arguments:** None.

**Returns:** concurrent.futures object. A Future chained to current Future.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_chainable_future.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import ChainableFuture

future1 = ChainableFuture()
future2 = future1.then(lambda arg: arg + ' using ChainableFuture.then() !!!.')
future1.set_result('This is an anglerfish.ChainableFuture demo')
print(future1.result())  # Future 1 is Chained to Future 2.
print(future2.result())
```
</details>


<details>
<summary>
retry
</summary>

## retry

`@retry(tries: int=5, delay: int=3, backoff: int=2,
          timeout: int=None, silent: Bool=False, logger=None)`

**Description:** Retry calling the decorated function using an exponential backoff and timeout.

**Arguments:**
- `tries` how many times retry the operation, defaults to 5, integer type.
- `delay` delay between executions, defaults to 3, integer type.
- `backoff` an exponential backoff offset to apply to the `delay`, defaults to 2, integer type.
- `timeout` a timeout for the whole execution or None, defaults to None.
- `silent` a boolean `True` to be Silent when running the reties, defaults to False.
- `logger` a working logger to log into or None to use `print()`.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_retry.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import retry
@retry(4)
def retry_job():  # a simple function for testing only
    return open("").read()  # Will Fail as expected
retry_job()
```
</details>


<details>
<summary>
set_single_instance
</summary>

## set_single_instance

`anglerfish.set_single_instance(name: str, port: int=8888)`

**Description:** Set a single instance Lock based on Sockets and return socket.socket object or None.

**Arguments:**
- `name` the name of your app to be used as Lock name,
- `port` port number to be used when Unix Socket is not available, mostly on MS Windows, defaults to 8888, integer type.

**Keyword Arguments:** None.

**Returns:** socket.socket object or None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_single_instance.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :question:         | **Windows** | Untested    |

**Usage Example:**

```python
from anglerfish import set_single_instance
set_single_instance("MyApp")
```
</details>


<details>
<summary>
env2globals
</summary>

## env2globals

`anglerfish.env2globals(pattern: str)`

**Description:** Auto add ENV environtment variables starting with `PY_` in upper case to python globals dict.

**Arguments:** `pattern` the pattern to select which variables to add, default to `PY_`

**Keyword Arguments:** None.

**Returns:** Boolean, True if everything is Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/env2globals.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :question:         | **Windows** | Untested    |

**Usage Example:**

```python
from anglerfish import env2globals
env2globals()
```
</details>


<details>
<summary>
html2ebook
</summary>

## html2ebook

`anglerfish.html2ebook(files: list, fyle: str=uuid4().hex + ".epub", meta={})`

**Description:** Convert a folder with HTML5/CSS3 to eBook ePub. JavaScript does not Work on ePub.

**Arguments:**
- `files` a tuple with the list of HTML/CSS files to add to the eBook.
- `fyle` an output file path string, defaults to an uuid4 hexadecimal if not provided.

**Keyword Arguments:** `meta` contains a dict with:
- `title` is the eBook Title (Fallbacks to Filename if not provided).
- `author`  is the eBook Author (Fallbacks to Username if not provided).
- `lang` is the eBook Language (Fallbacks to English if not provided).
- `des` is a friendly eBook Description (Fallbacks to Filename if not provided).
- `copi` eBook CopyRights (Fallbacks to Creative Commons 'CC-BY-NC-SA v.4.0' if not provided).
- `pub` the eBook Publisher (Fallbacks to 'Python' if not provided).
- `date` Date and Time ISO format of eBook creation (Fallbacks to Current Date and Time if not provided).

**Returns:** a string with the file path of the new eBook file.

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import html2ebook
html2ebook(("/mybook/html/index.html", "/mybook/html/chapter1.html"))
```
</details>


<details>
<summary>
TemplatePython
</summary>

## TemplatePython

`anglerfish.TemplatePython(template: str)`

**Description:** TemplatePython is a tiny generic Template Engine that Render and Runs native Python code. Template syntax is similar to Django Templates and Mustache. Fastest way to run Python on HTML and Render the results. No Markup enforced, it can work with HTML/CSS/JS or any kind of Markup. Has built-in optional Minification for HTML. Notice this is a Class, not a Function.

**Arguments:**
- `template` a template string with native Python 3 code between tags, or a file-like object that supports `.read()`.

**Keyword Arguments:** None.

**Returns:** a string with the Rendered HTML.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_template_python.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import TemplatePython
demo = """<html><body>
     {%
     def say_hello(arg):
         {{"<tr> hello ", arg, " </tr>"}}
     %}
     <table>
         {% [say_hello(i) for i in range(9) if i % 2] %}
     </table>
     {% {{ testo }} {{ __doc__.title() }} %}
     {% # this is a python comment %}  </body></html>"""
templar_template = TemplatePython(demo)
print(templar_template(testo=9, mini=True))
```
</details>

<details>
<summary>
path2import
</summary>

## path2import

`anglerfish.path2import(pat: str, name: str=None)`

**Description:** Imports a Python module from a file path string.
This is *as best as it can be* way to load a module from a file path string that
I can find from the official Python Docs, for Python 3.5+ or higher.
This has been created after having `ImportError` trying to use a 1 line module,
that only contains `__version__ = "1.0.0"`,
not meant to replace the standard way of importing modules.

**Arguments:**
- `pat` is the file path on disk from where to load a Python module from, mandatory. String type.
- `name` is the Python module name, optional,
will try to get it from the filename on the `pat` argument if omitted. String type.
- `ignore_exceptions` optional, default to `False`. Set to `True` will not raising
any exceptions and return `None` if loading failed.
- `check_namespace` optional, default to `True`, will check if the `name` is already
in `globals()` namespace, if it does, raising a `NamespaceConflictError` exception.

**Keyword Arguments:** None.

**Returns:** object, a *"live"* Python module object ready for use at runtime.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/path2import.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import path2import
my_module = path2import("/path/to/module.py")
```
</details>


<details>
<summary>
make_post_exec_msg
</summary>

## make_post_exec_msg

`anglerfish.make_post_exec_msg(start_time: object=None, comment: str=None)`

**Description:** Simple Post-Execution Message with information about RAM used by your app and execution Time. Can also display an arbitrary string ideal for Donation links, Social, etc.
It will register itself to be executed at exit via `atexit.register()`.
Its basically a *Goodbye* message.

**Arguments:**
- `start_time` a `datetime` object, ideally should be `datetime.now()`.
- `comment` an arbitrary string ideal for Donation links, Social links, Bitcoin, etc. String type.

**Keyword Arguments:** None.

**Returns:** The formatted message, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_postexec_message.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import make_post_exec_msg
make_post_exec_msg()
```
</details>


<details>
<summary>
watch
</summary>

## watch

`anglerfish.watch(file_path: str, callback: Callable=None, interval: int=60, backoff: int=1, timeout: int=None, repetitions: int=-1, silent: bool=False, logger: object=None)`

**Description:** Watch a file path for changes run callback if modified.
A WatchDog.

**Arguments:**
- `file_path` an existent readable file path to watch for changes. String type.
- `callback` a `Callable` callback function to execute when changes are detected. Callable type.
- `interval` an integer number seconds of interval between chacks for changes. Integer type.
- `backoff` an exponential backoff offset to apply to the `interval`, defaults to 1, integer type.
- `timeout` a timeout for the whole execution or None, defaults to None.
- `repetitions` how many times to check or run, -1 or 0 is infinite, defaults to -1, integer type.
- `silent` a boolean `True` to be Silent while running, defaults to False.
- `logger` a working logger to log into or None to use `print()`.

**Keyword Arguments:** None.

**Returns:** `Callable` output if theres a callable, else the file path that changed.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_watch.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import watch
watch("/tmp/file.txt")
```
</details>


<details>
<summary>
set_desktop_launcher
</summary>

## set_desktop_launcher

`anglerfish.set_desktop_launcher(app: str, desktop_file_content: str, autostart: bool=False)`

**Description:** Adds your app to autostart and/or launcher icon on the Desktop.
According to XDG standard. Runs on Linux. Other platforms simply does nothing.
Windows and Os X dont have a desktop launcher standard file.
Windows only have `*.lnk` but thats meant to be an Internet-only shortcut.

**Arguments:**
- `app` the name of your app. String type.
- `desktop_file_content` the content of the launcher file. String type.
- `autostart` a Boolean True or False to choose if your app will be added to auto-start on the desktop.

**Keyword Arguments:** None.

**Returns:** the path of the newly created launcher. string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_desktop_launcher.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | No API      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
from anglerfish import set_desktop_launcher
set_desktop_launcher("mysuperapp", "")
```
</details>


<details>
<summary>
set_terminal_title
</summary>

## set_terminal_title

`anglerfish.set_terminal_title(titlez: str="")`

**Description:** Set or Reset Bash CLI Window Titlebar Title.
According to XDG standard. Runs on Linux. Other platforms simply does nothing.
For Windows, use `title` command to approach that.

**Arguments:**
- `titlez` the title for the terminal emulator window. Optional. String type.

**Keyword Arguments:** None.

**Returns:** `titlez` if the title has been set on the terminal emulator window or None. string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_terminal_title.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import set_terminal_title
set_terminal_title("mysuperapp")
```
</details>


<details>
<summary>
json2xml
</summary>

## json2xml

`anglerfish.json2xml(json_obj: dict, line_padding: str="")`

**Description:** Takes a JSON and returns an XML, optional custom line paddings.

**Arguments:**
- `json_obj` the json data, dict type.
- `line_padding` optional custom line paddings, string type.

**Keyword Arguments:** None.

**Returns:** XML, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/json2xml.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import json2xml
json2xml({"foo": 42, "bar": 666})
```
</details>


<details>
<summary>
make_json_flat
</summary>

## make_json_flat

`anglerfish.make_json_flat(jsony: dict, delimiter: str="__")`

**Description:** Takes a JSON and returns a JSON, but with Flatten out structure, from Nested to Flat, optional custom delimiter.

**Arguments:**
- `jsony` the json data, dict type.
- `delimiter` optional custom delimiter, string type.

**Keyword Arguments:** None.

**Returns:** JSON, a Flat JSON, dict type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_json_flat.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

</details>


<details>
<summary>
set_zip_comment
</summary>

## set_zip_comment

`anglerfish.set_zip_comment(zip_path: str, comment: str="")`

**Description:** Set a comment on a ZIP file, return a Boolean.

**Arguments:**
- `zip_path` ZIP file path string, str type.
- `comment` Comment for the ZIP file, optional, defaults to empty string, string type.

**Keyword Arguments:** None.

**Returns:** True if Ok, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_zip_comment.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import set_zip_comment
set_zip_comment("test.zip", "This is a comment.")
```
</details>


<details>
<summary>
get_zip_comment
</summary>

## get_zip_comment

`anglerfish.get_zip_comment(zip_path: str)`

**Description:** Get a comment metadata from a ZIP file, UTF-8 string type.

**Arguments:**
- `zip_path` ZIP file path string, str type.

**Keyword Arguments:** None.

**Returns:** UTF-8 Comment, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_zip_comment.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
from anglerfish import get_zip_comment
get_zip_comment("test.zip")
```
</details>


<details>
<summary>
has_battery
</summary>

## has_battery

`anglerfish.has_battery()`

**Description:** Check if computer has a Battery, return Boolean.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** True if has Battery, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_hardware.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | No API      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
from anglerfish import has_battery
has_battery()
```
</details>


<details>
<summary>
on_battery
</summary>

## on_battery

`anglerfish.on_battery()`

**Description:** Check if computer is running on Battery, return Boolean.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** True if computer is running Battery, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_hardware.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | No API      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
from anglerfish import on_battery
on_battery()
```
</details>


<details>
<summary>
set_display_off
</summary>

## set_display_off

`anglerfish.set_display_off()`

**Description:** Set Display monitor OFF, will Automatically turn ON when any Key or Mouse movement detected, return Boolean.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** True if Ok, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_display_off.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | No API      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
from anglerfish import set_display_off
set_display_off()
```
</details>



<details>
<summary>
make_test_terminal_color
</summary>

## make_test_terminal_color

`anglerfish.make_test_terminal_color()`

**Description:** Test the Terminal True-Color.
Prints 3 lines corresponding to Red, Green, Blue from darkest to brightest on the Terminal.
Does not Log anything to logger.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_test_terminal_color.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
from anglerfish import make_test_terminal_color
make_test_terminal_color()
```
</details>


# Install permanently on the system:

**PIP:** *(Recommended!)*
```
pip3 install anglerfish
```
- Use `sudo pip3 install anglerfish` for installing System-wide.
- Use `python3 examples/basic.py` to run an example of all the functionalities.
- This project is oriented to Developers, NOT end-users.
- Feel free to contact us if you need help integrating Anglerfish on your project.


# Why?:

- Too much repeated code across my projects, almost all of them doing tha same.
- Look into other alternatives like Boltons but they dont solve or improve anything.
- Other libs try to fix Python2 problems, that has been improved on Python3.
- Anglerfish modules are less than 100 lines while other solutions are over-engineered and bloated.
- Lots of functionalities on Anglerfish are a *"Must Have"* for modern Apps, like a Logger, etc.
- 1 Module = 1 file = 1 feature, less than 100 lines per file, do 1 thing do it well.
- No Dependencies at all, just Python 3 standard library, cross-platform.
- Easy to use, KISS philosophy.


# Requisites:

- [Python 3.x](https://www.python.org "Python Homepage") *(or PyPy 3.x)*


# Config Helper ?

- Anglerfish will NOT provide any kind of Configuration/Settings Helpers.
- We recommend: https://github.com/ssato/python-anyconfig#python-anyconfig
- `python-anyconfig` only requires Python Standard Library. Works with any kind of config file.


# More must have helpers

*All these tiny generic awesome helpers, utilities, etc only require Python standard lib.*

- https://github.com/shazow/unstdlib.py#unstandard-library-for-python
- https://github.com/hynek/attrs#attrs-attributes-without-boilerplate
- https://github.com/ssato/python-anyconfig#python-anyconfig
- https://github.com/dbader/schedule#usage
- https://github.com/msiemens/tinydb#example-code
- https://github.com/jsonpickle/jsonpickle#jsonpickle
- https://github.com/theodox/spelchek#spelchek
- https://docs.python.org/3/library/zipapp.html#zipapp.create_archive


# Coding Style Guide:

- Lint, [PEP-8](https://www.python.org/dev/peps/pep-0008), [PEP-257](https://www.python.org/dev/peps/pep-0257), [PyLama](https://github.com/klen/pylama#-pylama), [iSort](https://github.com/timothycrosley/isort) must Pass Ok. `pip install pep8 pep257 pylama isort`
- If there are any kind of tests, they must pass. No tests is also acceptable, but having tests is better.


# Name convention

- For names we use: `get_*`, `set_*`, `check_*`, `make_*` and `*2*`.


# Contributors:

- **Please Star this Repo on Github !**, it helps to show up faster on searchs.
- **Ad-Hocracy Meritocracy**: 3 Pull Requests Merged on Master you become Repo Admin. *Join us!*
- [Help](https://help.github.com/articles/using-pull-requests) and more [Help](https://help.github.com/articles/fork-a-repo) and Interactive Quick [Git Tutorial](https://try.github.io).


# Licence:

- GNU GPL Latest Version *AND* GNU LGPL Latest Version *AND* any Licence [YOU Request via Bug Report](https://github.com/juancarlospaco/css-html-js-minify/issues/new).


# Ethics and Humanism Policy:
- May this FLOSS be always Pristine and Clean, No AdWare, No Spamm, No BundleWare, No Infomercial, No MalWare.
- This project is [LGBTQQIAAP friendly](http://www.urbandictionary.com/define.php?term=LGBTQQIAAP "Whats LGBTQQIAAP").
