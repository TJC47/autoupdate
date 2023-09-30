# How to integrate into your project
To use the autoupdater, you need to import it into your main file, after you downloaded the file.

You just need to fill in the gaps:
```
import autoupdate
autoupdate.check("<the filename>", "<link to the file>")
```
After you filled in the gaps, it should look like this:
```
import autoupdate
autoupdate.check("example.py", "https://raw.githubusercontent.com/TJC47/autoupdate/main/example.py")
```
You can also check multiple files:
```
import autoupdate
autoupdate.check("file1.py", "https://raw.githubusercontent.com/TJC47/autoupdate/main/file1.py")
autoupdate.check("file2.py", "https://raw.githubusercontent.com/TJC47/autoupdate/main/file2.py")
autoupdate.check("file3.py", "https://raw.githubusercontent.com/TJC47/autoupdate/main/file3.py")
```
