import csv
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *

path = "nodes.csv"
list = open(path)
data = []
for i in list:
	data.append(str(i.split(',')[3]))

# Connect to database
try:
	engine = create_engine("mysql+pymysql://{user}:{pwd}@localhost/pf".format(user='root', pwd='611998'), echo=True)
except ValueError:
	print("Can not connect to server, please check your connection")
print("Connection successfull!!!")

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
	


Session = sessionmaker(bind=engine)
session = Session()
data_admin_api = session.query(Admin_api_audit_log).all()
for i in data_admin_api:
	print("id :", i.id, " created_at :", i.created_at)
# x = session.query(Security_event).filter(Security_event.mac=="d4:d2:e5:83:68:48")
# for i in x:
# 	print(i.id)
# temp = 0
# for i in data:
# 	try:
# 		x = session.query(Security_event).filter(Security_event.mac==i)
# 		if x:
# 			temp += 1
# 		#session.commit()
# 		#print("delete successfull")
# 	except:
# 		session.rollback()
# 		print("delet error")

# print("So mac tim thay:", temp)
