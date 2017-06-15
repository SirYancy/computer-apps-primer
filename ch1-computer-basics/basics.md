# Computer Basics

<dl>
    <dt>Computer</dt>
    <dd>A device which can be instructed to perform arbitrary sets of arithmetic and logical operations.</dd>
</dl>

## The Story so far

In 1949, *Popular Mechanics* boasted that “Computers of the future may weight no more than 1.5 tons.” Technically, they were correct. Computers of today don't, typically, weight much more than that. So what is a computer, really?

In today,s digital world, when we talk about digital computing, we are talking about general purpose computing machines. These are incredibly complex machines that can be programmed to solve (in theory) any mathematical problem. At its core, a computer is a machine that just solves math problems. Very clever mathematicians and computer scientists have found ways to use these math problems to represent just about every conceivable thing in the world. Everything from a text file, to a picture, to a piece of music. And we can do this with amazing accuracy. And so increasingly, computers are taking over more and more of the work that humans used to do. And now we embed them in everything from coffee machines, to robots, to self-driving cars. We carry them around in our pockets. We operate them at our jobs. They are in our entertainment devices. They even have [internet connected toilets](http://www.wired.com/insights/2014/04/toilet-role-internet-things/). It is estimated that could be around [50 billion](http://www.statista.com/statistics/471264/iot-number-of-connected-devices-worldwide/) devices connected to the internet by 2020.

![desktop]<br>
**A desktop computer**

Today's smartphone is 58,000 times more powerful than the Apollo Lander that went to the moon. There is more knowledge and information at our fingertips that at any time in human history. With all of that power and complexity, comes some very real dangers. For one, they are actually hard to use. If you are a computer expert, perhaps you don’t fully understand just how much knowledge you take for granted. For many people, they are very intimidating. Let's attempt to de-mystify them.


![hierarchy]<br>
**Computer Hierarchy**
**Source: By Golftheman (Own work) [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0), via [Wikimedia Commons](https://commons%20.wikimedia.org/wiki/File%3AOperating_system_placement.svg)**

A computer is a shockingly complex machine. Even the simplest computer has millions of components. Some of the most advanced CPUSs in the world today sport billions of transistors, each measuring only about 20 nanometers, many times smaller than the width of a human hair. It is impossible for a human to even hold that mental concept in his or her mind. So how do we deal with that kind of complexity? Let’s talk about **interfaces**.

## Parts of a Computer

There are four main components that a computer needs to operate and they are all separated by interfaces. An interface in computer science is the place where two systems interact with each other. For example, the interface between the user and the application that the user is working on might consist of a keyboard, a mouse, and a display.

<dl>
    <dt>The User</dt>
    <dd>The User is you. If you are reading this text, you are already a computer user and are likely interfacing with it. The interface that you see is probably a web browser window, and the text has been downloaded to that web browser from a web server somewhere in the world.</dd>
    <dt>The Application layer</dt>
    <dd>Most often, when using a computer, you will use some sort of application, or app. This might be a web browser, a word processor, a photo editor, or a video game. Applications are self-contained programs which are designed to assist the user in completing some specific task.</dd>
    <dt>The Operating System Layer</dt>
    <dd>The Operating System is the main software of the computer. It is usually installed immediately after the machine is manufactured or assembled, and it governs almost all of the computer’s operations. It creates a layer of abstraction between the user, the apps, and the hardware. If you are taking my class, the operating system you are most likely using is called Microsoft Windows 7, though many of the same principles and conventions are followed in most modern operating systems.</dd>
    <dt>The Hardware</dt>
    <dd>At the very bottom of the computer hierarchy is the hardware, the bare metal. This text is not designed to go into a great amount of detail about the hardware, as it is primarily geared toward a computer applications class, however, it is probably a good idea to understand what at least some of the hardware components of a computer are, such as the CPU and memory, and a little bit about what those things mean. Especially if you are planning on purchasing a computer yourself. And so, below, you can see a brief overview of the modern computer hardware architecture, otherwise known as the Von Neumann architecture.</dd>
</dl>

## How a computer works

![Von Neumann Architecture]<br>
**Von Neumann Architecture**
**By Kapooht (Own work) [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File%3AVon_Neumann_Architecture.svg)**

The modern concept of a computer follows what’s known as the Von Neumann architecture. What this means is actually pretty simple at its most fundamental. There are three basic components: The computer itself, input devices, and output devices. Let’s look at all three of these in turn.

### THE COMPUTER

![motherboard]<br>
**A Motherboard**

John von Neumann conceived of a very simple architecture which we still use today. At its core, a computer has two main components, the Central Processing Unit (the CPU), and a Memory Unit which today we typically call RAM. A computer stores a “program” in memory (RAM), and then the CPU asks the memory unit for the first step of the program (known as an “instruction” and then executes it. It returns any result to memory and then asks for the next step. Over and over until the program ends. Each of these components can be broken further up into sub-components until we get all the way down to the most fundamental parts of the CPU, the transistors, which can be so small that more than four million of them could fit in the period at the end of this sentence. Despite all of this, the basic idea is really quite simple.

### INPUT/OUTPUT

![mouse and keyboard]<br>
**Common Interface Devices**

It is a pretty poor computer that can’t do anything with the result of some operation or computation. And so, almost all computers have some way for a user or other agent to interact with it. The modern home computer might have dozens of input/output devices attached to it. These allow the user to interact with whatever program (or programs) are running on the computer. Some are obvious, but others are a bit more subtle.

**Input Devices**

* Mouse
* Keyboard
* Scanner
* Game Controller
* Fingerprint Reader
* Touchscreen
* Microphone
* GPS antenna
* Bluetooth Chip

**Output Devices**

* Monitor
* Touchscreen
* Speakers
* Haptic feedback (rumble feature on game controller)
* Printer
* Hard drive
* Jumpdrive

Of course, this list could go on and on. Altogether, these devices are known as Input/Output devices, or I/O devices. Some home computers will have variations on these basic parts. For instance, a gamer might have a high-performance mouse and keyboard, or an XBox 360 controller. An artist might have a digital drawing tablet. A photographer might have a camera set up to transfer photos directly to the computer. Also, your car most likely has many small computers in it which monitor conditions in the car, such as engine temperature. That temperature sensor is an I/O device, and the fan that it it turns on when the temperature gets too high is also an I/O device. Anything that a computer uses to interact with a user or the outside world is a I/O device.

<!-- Images -->
[desktop]: images/desktop_example.jpg
[hierarchy]: https://upload.wikimedia.org/wikipedia/commons/e/e1/Operating_system_placement.svg
[Von Neumann Architecture]: https://upload.wikimedia.org/wikipedia/commons/e/e5/Von_Neumann_Architecture.svg
[motherboard]: images/motherboard.png
[mouse and keyboard]: images/mouse-keyboard.jpg
