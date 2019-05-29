#!/bin/bash
for i in 10 20
do
scp /home/student/桌面/lnmp_soft.tar.gz  root@192.168.2.$i:/root
ssh -X root@192.168.2.$i
cd /root
tar -xf lnmp_soft.tar.gz
cd  /lnmp_soft
tar -xf  nginx-1.12.2
cd  nginx-1.12.2
./configure --with-http_ssl_module
make && make install
ln -s /usr/local/nginx/sbin/nginx /sbin/nginx
yum -y install mariadb-server mariadb-devel   php php-mysql php-fpm
systemctl start mariadb  && systemctl start php-fpm
done

