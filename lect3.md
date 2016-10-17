#Lecture 3: Security Tactics & Encryption 

##Review


##What are we securing? 
* Network - series of computers that are connected together for the purpose of sharing resources and data 
* Host - individual system on a network 
* Internet - series of interconnected networks that spans the entire world 

##Host Security 
* Operating system - base software on a system that manages the system's resources for the user and programs

##Security Tactics 
* **Least Access Principle** - making sure that someone only has access to what they need and nothing else 
* **Layered Security**
	* Having multiple layers of security 
	* Ex: Bank that has a guard, a safe, and an alarm system 
* **Diversity of defense** 
	* Use different vendors and tactics 
	* Ex: Having 2 firewall vendors 
* **Security through obscurity**
	* Put your important data somewhere other than My Documents 
* **Keep it simple** 
	* Do not have a server perform more than 1 task, keep the tasks of the servers separated 
* **Access Control** - controlling the permissions of an individual 

##Security Mechanisms 
* **Encryption** 
	* ***Symmetric encryption*** - use the same key for encryption and decryption 
		* The key is shared between both parties 
	* ***Asymmetric encryption*** - one key to encrypt and a different key to decrypt 
		* Used for regular encryption and digital signatures 
		* Ex: RSA 
	* ***Public Key Encryption*** 
		* Public key = accessible to everyone and is used to encrypt a message 
		* Private key = secret & only the receiver has the private key that can be used to decrypt the message 
	* Digital signatures - reverse of public key encryption 
		* You sign a message with your private key 
		* People will use your public key to be able to read the message to know that you were the one that sent it.
* **Hashes** - a unique data string that gets produced from an algorithm 
	* This is only 1 way, you cannot get the original word/message using the hash 
	* Hashing the same data will produce the same result every time 
* **Authentication** 
	* Verifying the identity of a user/person 
	* Different from authorization 
		* Authorization = what can/can't be done is a system 
	* Different ways to authenticate 
		* Something you have (usb, smart card) 
		* Something you know (password) 
		* Something you are (retina, fingerprint) 
	* There is two-factor authentication - when you use more than one method of authentication to log someone in 	
* Accounting
* Firewalls
* VPNs
* IDS/ IPS 
* Anti-virus/anti-malware 
* Security Policies 