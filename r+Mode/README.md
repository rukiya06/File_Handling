## What is `r+` mode?

- The `r+` mode opens a file for **reading and writing**.
- The file pointer is placed at the **beginning** of the file.
- The file **must exist**; otherwise, Python raises a `FileNotFoundError`.
- You can read from and write to the file without truncating its content.
