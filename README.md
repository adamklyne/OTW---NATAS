> Adam Klyne | Jan-21

# OTW - NATAS

## Level 0

Viewing the source code revelead the password
```html
<body>
    <h1>natas0</h1>
    <div id="content">
       You can find the password for the next level on this page.

       <!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
    </div>
</body>
```

## Level 1

Right-clicking on the page was disabled. Source code was viewed using ctrl+shift+i

```html
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">
    <h1>natas1</h1>
    <div id="content">
        You can find the password for the
        next level on this page, but rightclicking has been blocked!

        <!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
    </div>
</body>
```
## Level 2


Inspecting the webpage source code revealed the following:

```html
<body>
    <h1>natas2</h1>
    <div id="content">
        There is nothing on this page
        <img src="files/pixel.png">
    </div>
</body>
```

Inspecting the pixel.png image releaved nothing; however, looking in the ../files 
folder showed there was another file users.txt with the password

## Level 3

Inspecting the webpage source code revealed the following:
```html
<body>
    <h0>natas3</h1>
    <div id="content">
        There is nothing on this page
        <!-- No more information leaks!! Not even Google will find it this time... -->
    </div>
</body>
```
Using this hint, robots.txt was inspected showing:
>    User-agent: *
>   Disallow: /s3cr3t/

Looking in the /s3cr3t folder showed another users.txt file

## Level 4

Inspecting the webpage source code revealed the following:
```html
<body>
    <h1>natas4</h1>
    <div id="content">

    Access disallowed. You are visiting from "" while authorized users should come only 
    from "http://natas5.natas.labs.overthewire.org/"
    <br/>
    <div id="viewsource"><a href="index.php">Refresh page</a></div>
    </div>
</body>
```
With this in mind, I injected the appropriate `Referer` header.

## Level 5


Inspecting the webpage source code revealed the following:
```html
<body>
    <h1>natas4</h1>
    <div id="content">

    <body>
        <h1>natas5</h1>
        <div id="content">
        Access disallowed. You are not logged in</div>
    </body>
</body>
```
With this in mind, I injected the appropriate `loggedin` cookie

## Level 6


## Level 7
Inspecting the webpage source code revealed the following:

```html
<body>
    <h1>natas7</h1>
    <div id="content">

    <a href="index.php?page=home">Home</a>
    <a href="index.php?page=about">About</a>
    <br>
    <br>
    <br />
    <b>Warning</b>:  include(etc/natas_webpass/natas8): failed to open stream: No such file or directory in <b>/var/www/natas/natas7/index.php</b> on line <b>21</b><br />
    <br />
    <b>Warning</b>:  include(): Failed opening 'etc/natas_webpass/natas8' for inclusion (include_path='.:/usr/share/php:/usr/share/pear') in <b>/var/www/natas/natas7/index.php</b> on line <b>21</b><br />

    <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
    </div>
</body>
```

This hint suggests a directory traversal attack.

## Level 8



## Passwords

natas1 | gtVrDuiDfck831PqWsLEZy5gyDz1clto
natas2 | gtVrDuiDfck831PqWsLEZy5gyDz1clto
natas3 | sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
natas4 | Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
natas5 | iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
natas6 | aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
natas7 | 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
natas8 | DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe 
natas9 | W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl