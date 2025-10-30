# Learning_API_from_scratch
## introductiion_Pyhton_Backend

Python is widely used in backend development to handle server-side logic, manage databases, and build APIs using powerful frameworks like Flask and Django.

🧠 Core Role of Python in Backend
Server-side logic: Python handles requests from the frontend, processes data, and returns responses.

Database management: It connects to databases (like PostgreSQL, MySQL, MongoDB) using ORMs such as SQLAlchemy or Django ORM.

API development: Python is ideal for building RESTful APIs using frameworks like Flask, Django REST Framework, and FastAPI.

Authentication & security: Python libraries help implement user authentication, authorization, and secure data handling.

Background tasks: Tools like Celery allow Python to manage asynchronous jobs like sending emails or processing files.

# Here we lean what is API and how does it works

## What is an API?
API stands for Application Programming Interface. The application can be any software that performs a specific task and the interface is a point where two applications communicate.

One application acts as a client and the other acts as a server. A client asks for some resource, say for example a photo, and the server sends that photo to the client.

The client here can be your mobile phone, desktop or laptop computer, or any device you use to surf the internet. And the server is a bigger computer that stores the data you want (a photo in our case).

Suppose I want a nature photograph to upload to my travel blog. I might go onto the Unsplash website, type "nature: in the search bar, and it would return a large number of nature photographs.

That's an API working behind the scenes to make the conversation between Unsplash and me happen.

## How Do APIs Work?
Computers follow a protocol to communicate with each other. A protocol is nothing but a set of rules that computers follow to communicate. Any computer that doesn't follow the protocol breaks the communication thread.

You might have used Bluetooth to share data back in the day. Bluetooth is nothing but a protocol for mobile devices to communicate with each other at a shorter distance.

When you ask your friend to send you photos of their last trip, your device acts as a client, and your friend's device (the one that sends photos) is the server.

This is just an example of a protocol. We have a large number of protocols in the world of computer science – one for almost anything.

On the web, we use the HTTP protocol (which stands for Hyper Text Transfer Protocol). APIs available on the web use the HTTP protocol for a number of reasons - it's easy to use and it's popular, for example.

Communications that take place over the HTTP protocol are also known as the request-response cycle because this is exactly how the protocol works. The client sends a request to the server and the server responds to the client regarding that request.

Unlike humans, computers have to be rigid to communicate with each other or they break the communication. For this reason, a client (requesting computer/ device) needs a set of information to send with the request so the server responds accordingly. This information includes:

URL – a web address where you want to make a request
Method – whether you want data already stored somewhere or want to save new data in a database
Header – all the relevant information about your request including in what format the client device expects to receive the data
Body – the body contains the actual request data
In our Unsplash example, the URL is https://unsplash.com/s/photos/nature. The method is GET because we want the server to get nature images back. The header includes information like the format our computer expects to get and accept – like language meaning, the language of the device, our operating system, and so on. The body includes the data we need to send to the server, the nature keyword for example.

There are four types of methods for HTTP requests which we will get back to in a moment. For now, just know that a method indicates what you want to do with the data available on the server. For example, whether you want that data as documents or you want to save a new entry in data saved somewhere.

When a client makes a request, the server responds to that request. The response might be the data the client requested or an error.

Just like a response, a request has a structure including a URL, status code, header and body. In a request, we have a method, which has four types. And in the response, we have a status code which indicates whether a request has been accepted or declined.





