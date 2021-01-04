#import csv
import time
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *

# path = "nodes.csv" #path to nodes test
# try:
# 	list = open(path)
# 	list_all_node = []
# 	for i in list:
# 		list_all_node.append(str(i.split(',')[3]))
# except Exception as e:
# 	print("Read file with error")
# list_all_node.pop(0) #delete first elements

# Connect to database
try:
	engine = create_engine("mysql+pymysql://{user}:{pwd}@{ip_server}:{port}/pf".format(user='root', pwd='611998', ip_server='localhost', port=3306), echo=True)
	Session = sessionmaker(bind=engine)
	session = Session()
except ValueError:
	print("Can not connect to server, please check your connection")

Base = declarative_base()

class Security_event(Base):
	__tablename__ = 'security_event'
	id = Column(Integer, primary_key=True)
	tenant_id = Column(Integer, nullable=False)
	mac = Column(String(17), nullable=False)
	security_event_id = Column(Integer, nullable=False)
	start_date = Column(DateTime, nullable=False)
	release_date = Column(DateTime, default='0000-00-00 00:00:00')
	status = Column(String(10), default='open')
	ticket_ref = Column(String(255), default=None)
	notes = Column(Text)

class Admin_api_audit_log(Base):
	__tablename__ = 'admin_api_audit_log'
	id = Column(Integer, primary_key=True)
	tenant_id = Column(Integer, nullable=False, default='1')
	created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
	user_name = Column(String(255), default=None)
	action = Column(String(255),  default=None)
	object_id = Column(String(255),  default=None)
	url = Column(String(255),  default=None)
	method = Column(String(10), default=None)
	request = Column(Text)
	status = Column(SmallInteger, nullable=False)

class Node(Base):
	__tablename__ = 'node'
	tenant_id = Column(Integer, primary_key=True, default='1')
	mac = Column(String(17), primary_key=True, nullable=False)
	pid = Column(String(255), nullable=False, default='default')
	category_id = Column(Integer, default=None)
	detect_date = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
	regdate = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
	unregdate = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
	lastskip = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
	time_balance = Column(Integer, default=None)
	bandwidth_balance = Column(BigInteger, default=None)
	status = Column(String(15), nullable=False, default='unreg')
	user_agent = Column(String(255), default=None)
	computername = Column(String(255), default=None)
	notes = Column(String(255), default=None)
	last_arp = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
	last_dhcp = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
	dhcp_fingerprint = Column(String(255), default=None)
	dhcp6_fingerprint = Column(String(255), default=None)
	dhcp_vendor = Column(String(255), default=None)
	dhcp6_enterprise = Column(String(255), default=None)
	device_type = Column(String(255), default=None)
	device_class =  Column(String(255), default=None)
	device_version = Column(String(255), default=None)
	device_score = Column(Integer, default=None)
	device_manufacturer = Column(String(255), default=None)
	bypass_vlan = Column(String(50), default=None)
	voip = Column(Enum('no','yes'), nullable=False, default='no')
	autoreg = Column(String(30), default=None)
	sessionid = Column(String(30), default=None)
	machine_account = Column(String(255), default=None)
	bypass_role_id = Column(Integer, default=None)
	last_seen = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')

class Ip4log(Base):
	__tablename__ = 'ip4log'
	tenant_id = Column(Integer, nullable=False, default='1', primary_key=True)
	mac = Column(String(17), nullable=False)
	ip = Column(String(45), nullable=False, primary_key=True)
	start_time = Column(DateTime, nullable=False)
	end_time = Column(DateTime, default='0000-00-00 00:00:00')


#a = time.time()
data_ip4log = session.query(Ip4log.mac).all()
#data_security_event = session.query(Security_event.mac).all()

while True:
	data_security_event = session.query(Security_event.mac).all()
	for i in data_security_event:
		try:
			data_ip4log.index(i)
		except:
			continue
		# 3 action need to execute: 
		#			1. delete admin_api_audit_log
		#			2. delete security_event
		#			3. move status user from unreg to reg
		try:
			session.query(Admin_api_audit_log).filter(Admin_api_audit_log.object_id==i[0]).delete()
			session.query(Security_event).filter(Security_event.mac==i[0]).delete()
			session.query(Node).filter(Node.mac==i[0]).update({Node.status:'reg'}, synchronize_session = False)
			session.commit()
		except:
			session.rollback()
			print("execute security_heal failure")
	time.sleep(10)
	print("done")

session.close()
print("Done")



# for i in data_ip4log:
# 	print(i[0])
# print("time require 1: " ,time.time() - a)
# print("=================================================")
# b = time.time()
# data_ip4log = session.query(Ip4log).all()
# for i in data_ip4log:
# 	print(i.mac)
# print("time require 2: " ,time.time() - b)


#print(data_security_event[0][0])
# list_mac_register_ip = []
# list_mac_security_event = []

# key_word_sort = lambda list_mac: list_mac[0]
# data_ip4log.sort(key=key_word_sort)
# print("==========================================")
# print("After sort")
# for i in data_ip4log:
# 	print(i)

#Get mac as matched security_event
# for i in data_security_event:
# 	list_mac_security_event.append(i.mac)
# print("length of list_mac_security_event : ",len(list_mac_security_event))
#list_mac_register_ip : Catch all mac was registed from ip4log
# for i in data_ip4log:
# 	print("mac : ", i.mac, "ip : ", i.ip)
# 	list_mac_register_ip.append(i.mac)
# print("length of list_mac_register_ip : ", len(list_mac_register_ip))
#end get list_mac_register_ip
# Close session()

# list_mac_register_ip.sort()
# # list_mac_security_event.sort()
# index_register_ip = 0
# index_security_event = 0







# for i in data_security_event:
# 	try:
# 		data_ip4log.index(i)
# 	except:
# 		continue
# 	# 3 action need to execute: 
# 	#			1. delete admin_api_audit_log
# 	#			2. delete security_event
# 	#			3. move status user from unreg to reg
# 	try:
# 		session.query(Admin_api_audit_log).filter(Admin_api_audit_log.object_id==i[0]).delete()
# 		session.query(Security_event).filter(Security_event.mac==i[0]).delete()
# 		session.query(Node).filter(Node.mac==i[0]).update({Node.status:'reg'}, synchronize_session = False)
# 		session.commit()
# 	except:
# 		print("execute security_heal failt")

# print("===========================================================================")












