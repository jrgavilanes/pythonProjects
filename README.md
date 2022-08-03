# Apuntes de Python

## Preparar entorno desarrollo

### BD Postgres Local

    docker-compose -f docker-compose-postgres up


## Python tips

https://codechalleng.es/tips/get-annotations

https://codechalleng.es/tips/dataclasses-and-order

https://codechalleng.es/tips/amazon-affiliation-url

https://codechalleng.es/tips/convert-str-to-datetime-in-pandas

https://codechalleng.es/tips/strip-punctuation

https://codechalleng.es/tips/extract-dictionary-keys-and-values

https://codechalleng.es/tips/create-a-temporary-directory

https://codechalleng.es/tips/sorted-min-max-key-argument

https://codechalleng.es/tips/the-str-isalpha-method

## General tips

Setear prompt minimalista

    export PS1='\u@\h: '

    # con directorio final
    export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]: ../\[\033[01;36m\]\W\[\033[00m\]\$ '
