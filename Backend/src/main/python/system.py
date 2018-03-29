import commands
import os
import sys
import subprocess

def stop_if_already_running():
    script_name = os.path.basename(__file__)
    l = commands.getstatusoutput("ps aux | grep -e 'aquarium.py' | grep -v grep")
    if l[1]:
        print(l)
        print("Script is already running, attempting to kill existing instance...")
        attempt_to_kill_existing_instance()
        if subprocess.Popen.returncode != 0:
            print("Could not stop previous script execution, exiting")    
            sys.exit(0);
        
def attempt_to_kill_existing_instance():
    proc = subprocess.Popen(["sudo", "pkill", "-f", "aquarium.py"], stdout=subprocess.PIPE)
    proc.wait()