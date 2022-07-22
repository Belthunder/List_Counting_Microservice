# counter.py written by Christopher Ball as part of the list-counting microservice
# for OSU CS 361 Summer Term 2022, Ashley McLemore's Link-Counter service
# last modified 07/20/2022

import time
import zmq 

def main() :
    
    context = zmq.Context()
    
    # set up the zmq socket to talk to the requester:
    print("setting up socket to connect to link-counting service")
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:56443")
    
    
    while True:
        
        #  Wait for next request from client
        message = socket.recv()
        print(f"Received request: {message}")

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send_string("World")
        
        
        
        
        
        
        
        
        
        
        
        #wait for a request from the link-counting client
       # message = socket.recv_json()
       # print("Recieved request: %s" % message)
        
        # do the work of translating the JSON into a usable list, 
        # counting duplicates, creating a map, and converting that map to a JSON object to send back.
        
      #  links_list = message["links"]
        #create the map to send
       # map = {}
        # count duplicates
      #  for i in links_list:
      #      map[i] = links_list.count(i)
        
        # convert the map to JSON and send the completed map back to the client as a JSON object
      #  socket.send_json(map)