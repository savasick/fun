# crypt data with keys

generate key pair with openssl
```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
```

take from pair public key
```bash
openssl pkey -in private.pem -outform PEM -pubout -out public.pem
```

### encrypt
```bash
python3 encrypt.py
```

### decrypt
```bash
python3 decrypt.py
```

