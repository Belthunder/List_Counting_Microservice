# counter.py written by Christopher Ball as part of the list-counting microservice
# for OSU CS 361 Summer Term 2022, Ashley McLemore's Link-Counter service
# last modified 07/20/2022

import zmq

FINAL_SOCKET_END = "tcp://*:62243"
END_MESSAGE = "complete"
LIST_TOPIC = "links"


def main():
    context = zmq.Context()

    # set up the zmq socket to talk to the requester:
    print("setting up socket to connect to link-counting service")
    socket = context.socket(zmq.REP)
    socket.bind(FINAL_SOCKET_END)

    while True:
        # wait for a request from the link-counting client
        message = socket.recv_json()
        print("Received request: %s" % message)

        # check to see if the ending message has been sent
        if message[LIST_TOPIC] == END_MESSAGE:
            break

        # do the work of translating the JSON into a usable list,
        # counting duplicates, creating a map, and converting that map to a JSON object to send back.

        links_list = message[LIST_TOPIC]
        # create the map to send
        counting = {}
        # count duplicates
        for i in links_list:
            counting[i] = links_list.count(i)

        # convert the map to JSON and send the completed map back to the client as a JSON object
        socket.send_json(counting)
