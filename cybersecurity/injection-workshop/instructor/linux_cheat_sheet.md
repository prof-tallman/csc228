## Debian Linux Quick Reference ##

### System — Discover your environment ###
```bash
  whoami; hostname; pwd       # Username *and* computer name *and* current directory
  ps aux                      # Running processes
```

### Navigation — Explore directories ###
```bash
  ls -lh                      # List files and directories
  cd /tmp                     # Change directory
  cd ..                       # Move up one directory
```

### Files — Read and manipulate ###
```bash
  cat /etc/os-release         # Display file contents
  head -n 5 file.txt          # First 5 lines
  tail -n 5 file.txt          # Last 5 lines
  grep "root" /etc/passwd     # Search for text
  find /home -name "*secret*" # Search for files by name
  cp file.txt copy.txt        # Copy file
  mv file.txt new.txt         # Move/rename file
  rm file.txt                 # Delete file
```

### Networking — Basic diagnostics ###
```bash
  ip addr                     # Network interfaces
  ping -c 3 127.0.0.1         # Test connectivity
  curl http://www.nfl.com/scores > scores.txt
```

**Remember:** Commands execute within the context of the **current user** and **working directory.**
