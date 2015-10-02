## Credits

Thanks to [Martin Pitt](http://www.piware.de/2011/01/creating-an-https-server-in-python/).

## Generating server.pem

```sh
$ mkdir ~/.ssl && cd ~/.ssl
$ openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```