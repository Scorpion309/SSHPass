import argparse
import subprocess

def parse():
	parser = argparse.ArgumentParser(description='Command to SSH', prefix_chars='*')
	parser.add_argument('*p', '**password', type=str, default='FromFile', help='Input password')
	parser.add_argument('server', type=str, help='Input address of the server')
	parser.add_argument('login', type=str, help='Input login')
	parser.add_argument('command', type=str, help='Input command')
	parser.add_argument('arguments', type=str, nargs='*', help='Input arguments of command')
	argsfromline = parser.parse_args()
	return argsfromline

def get_pass():
	filename = input('Input filename with password ')
	with open(filename, 'r') as text:
		newpass = text.readline().strip()
	return newpass

def write_to_console(*args):
	result = subprocess.run(args)
	print(result)
		
args = parse()
if args.password == 'FromFile':
	args.password = get_pass()

if args.command == 'ssh':
	write_to_console('sshpass', '-p', args.password, args.command, args.login+'@'+args.server, ' '.join(args.arguments))
elif args.command == 'scp':
	write_to_console('sshpass', '-p', args.password, args.command, args.arguments[0], args.login + '@' + args.server + ':' + args.arguments[1])
