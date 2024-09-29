#!/bin/sh

echo "======================Propering Postgresql DB.....============================"

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 1
done
echo "============================Postgresql DB has initialized successfully======================================="
fi
chown -R amir:amir /home/amir/code/staticfiles

exec "$@"