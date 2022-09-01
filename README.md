# SW

## Table of Contents

- [About](#about)
- [screenshots](#screenshots)
- [Getting Started](#getting_started)
- [Usage](#usage)


## About <a name = "about"></a>

This tool highlights with colors the console output by applying regular expressions on Hostname, Domain, Ip, Mac, Emails, Success and Error.

## Screenshots <a name = "screenshots"></a>

![alt text](https://raw.githubusercontent.com/sistemasnegros/sw/master/img/1.png)

![alt text](https://raw.githubusercontent.com/sistemasnegros/sw/master/img/2.png)



## Getting Started <a name = "getting_started"></a>

git clone https://github.com/sistemasnegros/sw

### Prerequisites



```
python 3  
```

### Installing

Converting the script into an executable.

```
cd sw/src
chmod +x sw.py
ln -sf sw.py /usr/bin/sw
```

Or Installing from setup.py
```
python setup install
```


## Usage <a name = "usage"></a>

To highlight colors of a file.

```
sw logfile.log
```

To highlight colors of a pipe output.
```
tail -f logfile.log | sw
```



