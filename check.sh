#!/bin/bashi
b=192.168.4.100
c=192.168.4.200
d="66ee606d5019d75f83836eeb295c6b6f  -"
f="699d00db64614eb287931b977d5c047f  -"
m=0
    for  i  in  $b  $c
    do
#curl  $i &> /dev/null
md5=`curl -s $i | md5sum`
if   [ "$md5" ==  "$d" -o "$md5" ==  "$f" ];then
        echo "$i内容未被修改"
else
        echo  "$i 已被篡改"
	
fi      
done
