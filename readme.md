system-dashboard
==================


A highly customized status dashboard for my home network.

## Create a release

First you need to build the webfrontend checkout the readme 
in the web folder. 

```
git tag -a v0.0.X
git push origin --tags
tar -zcvf ../system-dashboard-v.0.0.X.tar.gz server.py web/dist
```


## Install a release

```
tar xzv -C system-dashboard -f system-dashboard-v.0.0.X.tar.gz
```

Probably you need to chown it to the right user.


## Development

### Backend Python

Install with:

```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

Run with:

```
python server.py
```

### Frontend 

Install with:

```
cd web
npm install
node_modules/.bin/bower install
node_modules/.bin/gulp build
```
Run with:

```
node_modules/.bin/gulp watch
```
