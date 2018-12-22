from platform import system as system_name
import subprocess
import os
import yaml
from host import Host
import time
import sys
from threading import Thread

class ServiceWatcher:

	def run(self):
		self.import_host_names_as_objects()
		for i in range(0, len(self.hosts)):
			thread = Thread(target=self.watch, args=(i, 5))
			thread.start()

	def watch(self, host_number, interval):
		while True:
			current_status = self.check_host_status(self.hosts[host_number], "3")
			if current_status != self.hosts[host_number].get_last_status():
				self.hosts[host_number].set_last_status(current_status)
				slack.send_message(host)
				sys.stdout.flush()
			time.sleep(interval)

	def import_host_names_as_objects(self):
		path_to_yml = os.path.join(os.path.dirname(os.path.abspath(__file__)), "host_names.yml")
		with open(path_to_yml, 'r') as stream:
			host_names = yaml.load(stream)["hosts"]
		self.hosts = []
		for name in host_names:
			new_host = Host(name)
			self.hosts.append(new_host)

	def check_host_status(self, host, attempts):
		attempt_flag = '-n' if system_name().lower()=='windows' else '-c'
		command = ['ping', attempt_flag, attempts, host.get_name()]
		FNULL = open(os.devnull, 'w')
		return subprocess.call(command, stdout=FNULL, stderr=subprocess.STDOUT) == 0

if __name__ == '__main__':
	sw = ServiceWatcher()
	sw.run()