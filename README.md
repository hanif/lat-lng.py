# lat-lng.py

Get latitude & longitude form a given location using Google Maps API.

---

Usage:

```bash
chmod a+x lat-lng

# getting help
./lat-lng --help
> usage: lat-lng [-h] -a ADDRESS
>
> Get latitude & longitude of given address/location.
>
> optional arguments:
>   -h, --help            show this help message and exit
>   -a ADDRESS, --address ADDRESS
>                         Address or location to be geolocated
```

```bash
./lat-lng --address "Bantul"
> (-7.8748176, 110.3255365)

./lat-lng --address "Jalan Ringroad Barat, Yogyakarta"
> (-7.782989300000001, 110.3311353)

# shortcut 
./lat-lng -a "Solo, Indonesia"
> (-7.566667, 110.816667)

```
