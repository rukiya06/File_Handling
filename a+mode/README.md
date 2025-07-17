## About A+ Mode

**A+ Mode** in Python refers to opening a file with the mode `"a+"` using the `open()` function.

- Opens the file for **both appending and reading**.
- Creates the file if it does **not exist**.
- Positions the file pointer at the **end of the file** when opened.
- Allows you to **read existing content** and **append new data** without overwriting.
- To read from the file after opening in `"a+"` mode, you typically need to move the file pointer using `seek()`.
- a+ mode is useful when you want to preserve existing file data, add new data at the end, and also read the content.
