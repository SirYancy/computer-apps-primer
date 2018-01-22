# How does the Internet Work?

The Internet is based on the principle of _packet switching_. This is the idea that we can reliably transmit any digital file over long distances by breaking up larger files into many smaller files at the sending end, and re-assemble them on the other end. It has been through a variety of incarnations over the years, but eventually, the suite of protocols that became the defacto language of the internet was the **TCP/IP** stack.

## The Stack

* Application Layer
* TCP
* IP
* Hardware Layer

Essentially, the stack works like this:

1. An application (a Web browser, for example), decides it needs some resource from the internet. It makes a call to the TCP/IP system library.
1. Next, the Transmission Control Protocol, takes the information the application is going to send and breaks it up into pieces (if necessary) and takes each piece and packages it up with some addressing information and other metadata into a nice neat little bundle called a packet.
1. Next, it sends it on to the next layer, the Internet Protocol library. The IP layer examines the addressing layer and sends the packet to the next leg of its journey. 
1. The system hardware interface talks to your network hardware and encodes the packet into a digital signal which can be sent on a wire. 
1. From there, it winds its way across the Internet looking for its destination. Or rather, it's passed along from stop to stop like a hot potato and at each stop a router decides where to send it on to next. 
1. When it reaches the destination computer, it climbs back up the stack. The network hardware deserializes the signal (puts it back into its packet form), the IP layer verifies that this is where it belongs, the TCP layer collects all of the packets and reassembles them if necessary, 
1. Lastly, and finally, whatever application (possibly some web server sofware) looks at the request and decides how to respond to it. For example, it might serve up a Webpage and send it back down through the stack and across the internet back to your computer to be rendered in your web browser.

Remember that on modern computers, this process happens very, very quickly (on the order of seconds), but in computer time, it's an incredibly slow and laborious process.

## Infrastructure

Briefly, it's useful to understand the Internet in terms of network hardware. There's a sort of hierarchy of hardware on the internet and each level of that hierarchy, a different level of service exists and a different customer, business, peer relationship exists. For example, you may purchase access to the internet from a local **Internet Service Provider**. They might purchase their access to the Internet through a regional ISP, who in tern will be purchasing network access from what's called a **Network Service Provider**. These are massive telecom companies and the huge bundles of fiber-optic cabling that stretch all the way around the world are collectively often referred to as the **Internet Backbone**. Each NSP is legally required to connect to at least three **Network Access Points**, where packets can jump from one network to another, thus ensuring that the network is really a network and that all computers are connected to all other computers, however circuitiously.

## Domain Routing

Routing on the internet relies heavily on the **Domain Name System**, a network of computers that contain DNS look-up tables where they can take a web address also called a **Uniform Resource Locator** or **URL** and resolve it into an IP address.

This page of this book is located at https://itech.erickuha.com/ch6-internet/what-is-internet.html. But what does that mean? Let's take the address apart and examine its parts.

* **https://** - is the protocol. In particular, http is the protocol of the World Wide Web, called hypertext transfer protocol. It's a collection of commands that can be used to retrieve, update, or delete web pages.
* **com** - The top-level domain of a website is where, organizationally, it exists. There used to be only a few of these, but now there are are many. Their main purpose is to make table-lookups faster by only searching part of the table (the part with all of the .com addresses, for example).
* **erickuha** - is my domain, the domain that I registered for through a domain registrar and have exclusive rights to. It is, somewhere along the line, associated with an IP address, but I do not know what it is.
* **itech** - The sub-domain is the specific part of my domain which can be routed differently than the rest. For example, the root erickuha.com is hosted in one location and itech.erickuha.com is routed to a completely different service, server, and part of the internet.
* **/ch6-internet/what-is-internet.html** is the called a path. It leads to the specific file on the server that is requested when someone navigates to this page. It works almost identically to the file hierarchy on your own computer's file system. A system of forward slashes separates folders/directories and file names with file extensions are used to denote final endpoints. 

There are other schemes for locating resources on the internet, but this is the sanest and simplest one and can be used as a model for understanding the rest of it on down the line.

## Other thoughts

There is a lot more to talk about and a lot more to learn. You can look into all of the different protocols that are used on the Internet and the World Wide Web, or you can look deeper into how packet-switching is actually implemented in the TCP/IP stack. This is a jumping-off point to get you started down the road to understanding more about how the largest piece of technology ever created actually works.
