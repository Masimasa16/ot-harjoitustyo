# Ohjelmomistotekniikka, harjoitustyö

## Dokumentaatio

[Vaatimusmaarittely](documentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](documentaatio/arkkitehtuuri.md)

[Tuntikirjanpito](documentaatio/tuntikirjanpito.md)

[Changelog](documentaatio/changelog.md)

## Asennus

Asenna riippuvuudet komennolla:

    - poetry install


## Komentorivitoiminnot

### Käynistäminen

    poetry run invoke start

### Testaus

    poetry run invoke test

### Testikattavuus

    poetry run invoke coverage-report

### Pylint

    poetry run invoke lint