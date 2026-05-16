#!/usr/bin/python3
# -*- coding: utf8 -*-
from pythonosc.udp_client import SimpleUDPClient
client = SimpleUDPClient('127.0.0.1', 9000)
print("VRChat added a parameter for avatar scaling.\nIt's between 0.01, and 10000.\n(Use Ctrl+C to exit.)\n")
while True:
	scale = input("Scale: ")
	scale = float(scale)
	client.send_message("/avatar/eyeheight", scale)
