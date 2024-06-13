import argparse,os,sys

class Arguments:
	def __init__(self):
		pass
	def check_args_passlist(self,args):
		passlist = []
		if args.passlist and args.password:
			print("Give only wordlist or password")
			exit()
		if args.passlist:
			with open(args.passlist, "r") as wordlist:
				for word in wordlist:
					passlist.append(word.strip())
		else:passlist.append(args.password)
		return passlist
	def check_args_username(self,args):
		usernames = []
		if args.userlist and args.username:
			print("Give only userlist or username")
			exit()
		if args.userlist:
			with open(args.userlist, "r") as userlist:
				for word in userlist:
					usernames.append(word.strip())
		else:usernames.append(args.username)
		return usernames
	def check_args(self):
		if not (args.username and args.userlist):
			print("You need to give username(s)")
			exit()
		if not (args.password and args.passlist):
			print("You need to give password(s)")
			exit()
	
	def get_arguments(self):
		args = argparse.ArgumentParser()
		
		args.add_argument("-H",'--host', help="Specify ssh server",default="127.0.0.1")
		args.add_argument("-pwd",'--password',help="password")
		args.add_argument("-u",'--username', help="username")
		args.add_argument("-P",'--passlist',help="Passlist")
		args.add_argument("-U",'--userlist', help="Userlist")
		args.add_argument("-p",'--port', help="Port",default=22)
		args.add_argument("-T",'--thread',help="Thread number",default=2)

		args = args.parse_args()
		
		host = args.host
		port = args.port

		userlist = self.check_args_username(args)
		passlist = self.check_args_passlist(args)
		
		thread = args.thread
		
		return (host,port,userlist,passlist,thread)

