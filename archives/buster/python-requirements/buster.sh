#!/bin/bash

> buster.txt

for p in $(cat stretch.txt) ; do
    name=${p%==*} ;
    old=${p#*==} ;
    pkg=$(echo "python-$name" | sed -e 's/python-python-/python-/' -e 's/python-py/python-/' -e 's/_/-/g'| tr '[A-Z]' '[a-z]') ;
    case $name in
        cherrypy) pkg=python-cherrypy3;;
        beautifulsoup) pkg=python-bs4;;
        futures) pkg=python-concurrent.futures;;
        websocket-client) pkg=python-websocket;;
    esac
    pkg2=python2-${pkg#python-}
    pkg3=python3-${pkg#python-}
    new=$(grep $pkg apt_list)
    [ -z "$new" ] && new=$(grep $pkg3 apt_list)
    [ -z "$new" ] && new=$(grep $pkg2 apt_list)
    new=$(echo $new | head -1 |awk '{print $2}' | sed -e 's/-.*$//' -e 's/\+.*$//')
    [ -z "$new" ] && new="missing!!!"
    case $name in
        anytree|apns2|asynqp|flask-classful|flask-session|flask-menu|pyfcm|flask-wtf) new="OK WAZO debian package";;
        pygments-style-github) new="used by blog, not needed as debian package";;
    esac
    echo "$name $old -> $new" ;
    echo "$name==$new" >> buster.txt
done
