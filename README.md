pySQRL
====

Pyhton SQRL (Secure QR Login) Client


What is SQRL?
A newly proposed authentication scheme from Steve Gibson of GRC.com. It allows for user authentication without the need for:

* Username / Password pair
* OTP (One Time Password) 
* Third party 
* Revealing your identity during login
* An in-band authentication exchange

In a normal web authentication system your credentials are stored with the site you are trying to access. If the site were to be compromised the yours and every other users account information may be accessible allowing the intruder to attempt to use you credentials with elsewhere. The best part about SQRL is that the site never has your login credentials. You keep your never send your "password". The site authenticates you using by verifying you are who you are by using a private / public key signatures. This ends up being vastly more secure.

Details can be found here: https://www.grc.com/sqrl/sqrl.htm
