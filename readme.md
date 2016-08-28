system-dasboard
==================


A highly customized status dashboard for my home network.

## Create a release

First you need to build the webfrontend checkout the readme 
in the web folder. 

```
tar -zcvf ../system-dashboard-v.0.0.1.tar.gz server.py web/dist
```


## Install a release

```
tar xzv -C system-dashboard -f system-dashboard-v.0.0.1.tar.gz
```

Probably you need to chown it to the right user.