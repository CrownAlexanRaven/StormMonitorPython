# System Monitor Python
Its a System Stats monitor, but in Python. Why? Because I felt like it.

- [System Monitor Python](#system-monitor-python)
    - [Installation](#Installation)
        - [Darwin, Linux, UNIX Like](#darwin-linux-unix-like)
        - [Windows](#windows)
    - [Future](#future)



## Installation

### Darwin, Linux, UNIX Like
```zsh
git clone --depth=1 https://github.com/CrownAlexanRaven/SystemMontiorPython.git
cd SystemMonitorPython
python3 -m pip install -r prerequisites.txt

# OR 

curl https://github.com/CrownAlexanRaven/SystemMontiorPython/archive/refs/heads/main.zip --output main.zip 
unzip main.zip
rm main.zip
cd SystemMonitorPython
python3 -m pip install -r prerequisites.txt
```

### Windows

> [!NOTE]\
> I haven't checked if it works on Windows, because I don't use Windows.
> It should work, but i'm not sure.

```bash
git clone --depth=1 https://github.com/CrownAlexanRaven/SystemMontiorPython.git
cd SystemMonitorPython
py3 -m pip install -r prerequisites.txt

# OR

curl -L -o main.zip https://github.com/CrownAlexanRaven/SystemMontiorPython/archive/refs/heads/main.zip
Expand-Archive -Path main.zip -DestinationPath .\SystemMonitorPython
del main.zip
cd SystemMonitorPython
py3 -m pip install -r prerequisites.txt
```

Run the index.py file to start it.


## Future
I have no idea why I made this.

I'm thinking of expanding this into a larger project that does more things because why not.

And before you ask, no I'm not making CPU Temp, because that is more platform specific and i can't figure out how to do it. Tell me how if you know.
