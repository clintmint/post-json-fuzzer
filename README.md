# post-json-fuzzer

Python script for fuzzing 2 parameters simultaneously in a JSON POST request. Similar to Burp Intruder Pitchfork attack type without the Community Edition limitations.

## Proxy Setup 

Proxying can be done using environment variables.

### Powershell

```pwsh
$env:REQUESTS_CA_BUNDLE="Z:\PATH\TO\burpCert.pem"
$env:HTTP_PROXY="http://127.0.0.1:8080"
$env:HTTPS_PROXY="http://127.0.0.1:8080"
```
### Bash

```sh
export REQUESTS_CA_BUNDLE="/PATH/TO/burpCert.pem"
export HTTP_PROXY="http://127.0.0.1:8080"
export HTTPS_PROXY="http://127.0.0.1:8080"
```

## Testing 

Use a self-hosted vulnerable API such as https://github.com/roottusk/vapi
