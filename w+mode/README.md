## What is `"w+"` Mode?

In Python, when working with files, the mode `"w+"` is used to open a file for both writing and reading:

- If the file exists, it **truncates** (clears) the file to zero length.
- If the file does not exist, it creates a new file.
- Allows reading and writing to the file.

## Why Use `"w+"`?

You might want to write some data to a file and then immediately read it back without closing and reopening the file. The `"w+"` mode is suitable for such use cases.
