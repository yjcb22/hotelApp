#Create Vms with Vagrant
#Vms using Ubuntu 20.04.3 LTS
#app 192.168.60.4
#db 192.168.60.5
1. Go to the AnsibleVagrant folder
2. Run:
vagrant up
vagrant status
3. Run Ansible playbook
ansible-playbook playbook.yml
4. Run app the app: Connect via ssh to the machine as follows
ssh -XY vagrant@192.168.60.4 "python3.10 app/run.py"
5. Stop Vms
vagrant destroy -f