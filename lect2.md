#Lecture 2: Operating systems & Command Line 

##Review from Lecture 1: 
1. What is the CIA Triangle and what does it mean?

	* **Confidentiality** - only those that should have access will be able to have access to the information
	* **Integrity** - being whole, complete, or uncorrupted
	* **Authentication** - enables the user to access information without interference

2. What are the 3 Goals of security? 

	* **Prevention** - stop the attack from happening
	* **Detection** - know when the attack is happening
	* **Recovery** - stop, assess, repair, and maintain functionality during the attack

3. What are the differences between internal, civil, and criminal investigations? 
 < TO BE ANSWERED > 
 
##History of Operating Systems 
* Windows 95/98/ME 
	* Network/internet functionality was an afterthought 
	* Usability > Security 
		*  	There was no security (the login screen could be skipped by hitting "cancel" 
*   Windows NT 
	*   Network was built into the OS 
	*   There was still not much security 
*   Windows 2000 
	*   First Windows OS that had security in mind 
	*   Still had issues with usability over security 
*   Windows XP 
	* There were more security mechanisms made, and they were trying to not take away the usability of it    	
* Windows Vista 
* Windows 7 
* Windows 8 
* Windows 10 


##Linux
* **Linux** - open-source operating system 


#BOOT PROCESSES 
##POST 
* POST = Power-on Self Test 
* It is performed by the firmware after the device has been turned on 
* There are LED lights that would indicate if there was a problem while trying to boot up 
* The OS only loads after the POST system and pre-boot sequence has finished 

##Post Functions 
* Verify the integrity of BIOS 
* Verify system memory and size 
* Verify CPU
* Discover, initialize, and catalog all system buses and device
* Identify, organize, and select which devices are available for booting 
* Provide a user interface for the system's configuration 

##BIOS
**BIOS** - Basic Input/Output System 

* BIOS is a type of firmware that happens during the booting process
* Only used by PC's (Mac's use something else) 
* The purpose is to load an operating system from the boot device
* Each BIOs is specifically designed to work with a particular mother model 
* Stored on flash memory chip on motherboard 

##UEFI 
* **UEFI** - Unified Extensible Firmware Interface 
* Specification that describes a software interface between firmware and an operating system 
* Replaces the BIOS  
* This is also used in Macs 
* Advantage of using this over BIOS is the ability to boot from larger disks, it's CPU dependent and it has the ability to support network capabilities 

#Pieces of a computer 
* Motherboard It's the main board that holds all of the pieces together to 
* Central Processing Unit CPU - does the work of the computer, it carries out the little instructions and operations 
* Random Access Memory RAM - volatile storage (the information will be lost when the device shuts off), allows data to be accessed in the same time and location as the memory, and it is fast temporary storage 
* Hard Drive - used for storing data on disks, but there is also the option of using SSD's as an alternative to hard drives 
* Solid State Drive SSD - uses flash memory 

#Operating Systems 
* It is the software that manipulates hardware so that the users do not have to 
* It manages the hardware and software resources 
	* Memory management 
	* CPU & Processor management
	* Input & output 
	* File management 
	* Networking 
	* Command Interpreter 
* Real Time Operating Systems (RTOS) - operating systems that is not based on manual user input & output but pre-programmed behaviors 

#Definitions
* **Program** - executable code 
* **Process** - single instance of a program 
* **Thread** - smallest unit of processing that can be scheduled 

##Kernel 
* Manager of resources 
	* Manages the input/output requests from software and translates them to data processing instructions for the CPU and other hardware 
	* Assigns space to processes 
* Mechanism for inter-process communication 

##Mutli-tasking vs Multi-Processing 
* **Multi-task** - being able to have multiple process running at the same time 
	* The kernel gives each task a certain amount of time  and then switch back and forth between processes
* **Multi-Processing** - Allowing processes to execute on multiple cores 

##Memory Management 
* Each process has its own designated address space for memory 
* Kernel is responsible for allowing processes to use memory in a safe manner, by not overwriting each other 
* **Paging** (virtual memory) 
	* Lets the memory to be swapped if there is NOT enough RAM to hold everything that is trying to be stored 

##Interrupts 
* Helps hardware/software to signal to processor that an event needs immediate attention 
* Executes an interrupt handler to deal with the event 
* **Hardware interrupts:** Devices used to communicate with the processor 
* **Software Interrupt:** used when software needs to interact with hardware 
* 
 	
##Execution Modes