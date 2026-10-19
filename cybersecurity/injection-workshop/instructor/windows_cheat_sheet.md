## Windows Command Prompt Quick Reference ##

### System — Discover your environment ###
```bash
  whoami & hostname & cd      & :: Username *and* computer name *and* current directory
  tasklist                    & :: Running processes
```

### Navigation — Explore directories ###
```bash
  dir                         & :: List files and directories
  cd C:\Windows               & :: Change directory
  cd ..                       & :: Move up one directory
```

### Files — Read and manipulate ###
```bash
  type C:\Windows\win.ini     & :: Display file contents
  more file.txt               & :: Display file one screen at a time
  findstr "root" file.txt     & :: Search for text
  dir C:\Users\*secret* /s /b & :: Search for files by name
  copy file.txt copy.txt      & :: Copy file
  move file.txt new.txt       & :: Move/rename file
  del file.txt                & :: Delete file
```

### Networking — Basic diagnostics ###
```bash
  ipconfig                    & :: Network interfaces
  ping -n 3 127.0.0.1         & :: Test connectivity
  curl https://www.nfl.com/scores > scores.txt
```

**::ember:** Commands execute within the context of the **current user** and **working directory**.
