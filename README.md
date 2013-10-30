pySQRL
====

**Pyhton SQRL (Secure QR Login) Client**


What is SQRL?

A newly proposed authentication scheme from Steve Gibson of GRC.com. It allows
for user authentication without the need of:

* Username / Password pair
* OTP (One Time Password)
* Third party Interactions
* Revealing your identity during login
* An in-band authentication exchange

In a normal web authentication system your credentials are stored with the site
you are trying to access. If the site were to be compromised yours and
every other user's account information may be accessible; allowing the intruder
to attempt to use you credentials with elsewhere. The best part about SQRL is
that the site never has your login credentials. With SQRL you **_never_** send your
**_"password"_**. The site authenticates you using by verifying your identity by 
using a private / public key signatures. This ends up being vastly more secure.

Details can be found here: https://www.grc.com/sqrl/sqrl.htm
The SQRL protocol is new and is subject to change. I'll try my best to follow the published implementation found here:
https://www.grc.com/sqrl/details.htm
Install
-------
The this package requires **ed25519**, **docopt** and **pyinotify**

     git clone http://github.com/bushxnyc/sqrl.git
     cd sqrl
     sudo python setup.py install

Usage
-----
    Usage: sqrl [-d] [-n] [--path=<Dir>] [<SQRLURL>]
           sqrl [-l] [-s <AccountID>] [--create="<Name>"]

    Options:
    -d                    Debugging output
    -l                    List Accounts
    -n                    Notify via libnotify (Gnome)
    -s                    Set an account as Default
    --path=<Dir>          Path for config and key storage
    --create=<Your Name>  Create Account

    Example:
        sqrl -l
        sqrl --id 2a9s8x
        sqrl --create="John Doe"
        sqrl -d "sqrl://example.com/login/sqrl?d=6&nut=a95fa8e88dc499758"

You feed the sqrl URL provided by the authentication service to the script and
it uses it to submit and authentication request on your behalf. Based on how
the sight is design, you may automatically be logged in. **It's that simple**.

Features
--------

* **Debug** - Displays the content of the payload for your to veriy
* **Notification** - Displays notifications on successful or fail auth attemps
  (Gnome Only)
* **Account Management** - Create/Delete/Update Individual sqrl accounts

Debug
-----

When the [-d] argument is given the script outputs all the components of the
request.

    Url: localhost:8080/sqrl?nut=1bfe7ef6f9989bd5709d61f7ac28195e&sqrlver=1&sqrlkey=Zl_nrges0MGPRelRoH9SEwwPcARQSA0QmYNx-ZDcOKU
    Domin: "localhost"
    SQRLver: 1
    SQRLkey: Zl_nrges0MGPRelRoH9SEwwPcARQSA0QmYNx-ZDcOKU
    SQRLsig: LtYQU_j5Lwp6c0TrWEGhP0tj5o_PM8yni_tLmrG375aEIkUNdJzWl_XmLUN-dtZHuKWP1pf8iNUVSSyYRq3QDA
    signature is good

