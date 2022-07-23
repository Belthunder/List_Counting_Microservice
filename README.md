# List_Counting_Microservice
 The server side of a microservice that counts duplicates found in JSON data.
 
This microservice was designed by Christopher Ball for Ashley McLemore's Link-counting program as part of OSU's CS 361
Summer term 2022.

This service must be started before the requesting program can make requests. Once it has been initiated, it will continue
running and accepting requests until the termination message is sent, at which point the socket will be closed and the microservice
will terminate. 

HOW TO REQUEST DATA FROM THE MICROSERVICE:
1) initiate the microservice. It will set up a zmq socket that the client can connect to. The requesting program is responsible for
connecting to the socket.
2) Use socket.send_json to send JSON to the microservice. This JSON must be of the form: {"links" : [the list of links]}.

EXAMPLE CALL: 

request = {"links": ["one", "one", "two", "three", "two", "four"]}
    print("Sending request %s" % request)
    socket.send_json(request)

HOW TO RECIEVE DATA FROM THE MICROSERVICE:
1) The microservice will count the duplicate links and send back JSON of the form 
{"link_here" : int_number_of_occurrences, "link_two_here : int_number_of_occurrences, etc...}
2) This data can be received using a socket.recv_json() call.

EXAMPLE RECV:
counted_list = socket.recv_json()
print(counted_list)

HOW TO TERMINATE THE MICROSERVICE:
When you are finished with the microservice, simply send it the defined termination message:

END_REQUEST = {"links": "complete"}
socket.send_json(END_REQUEST)

HOW TO MODIFY THE PROGRAM TO SUIT YOUR NEEDS:

Defined constants at the top of the program are:
1) FINAL_SOCKET_END = "tcp://*:62243"
2) END_MESSAGE = "complete"
3) LIST_TOPIC = "links"

These can be edited to change:
1) The socket used for communication.
2) The message that will terminate the program.
3) The topic of the request JSON list/terminating message.

FULL EXAMPLE REQUESTING PROGRAM:

# client.py written by Christopher Ball to test
# the microservice for Ashley McLemore's List-Counting project
# for OSU CS 391 Summer Term 2022.

import zmq

FINAL_SOCKET_START = "tcp://localhost:62243"
END_REQUEST = {"links": "complete"}


def main():
    # set up the zmq socket.
    print("Connecting to server...")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(FINAL_SOCKET_START)

    # send a request to the server (a list in JSON form)
    request = {"links": ["one", "one", "two", "three", "two", "four"]}
    print("Sending request %s" % request)
    socket.send_json(request)
    # Get the JSON object back, and turn it back into a python object.
    counted_list = socket.recv_json()
    print(counted_list)

    socket.send_json(END_REQUEST)

UML:
