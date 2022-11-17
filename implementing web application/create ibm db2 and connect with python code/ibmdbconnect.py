#STEPS TO CREATE IBM DB2 AND CONNECTION WITH PYTHON  
#STEP 1: Import the ibm_db Python library: 
!pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.7 import ibm_db 

#STEP 2: Identify the database connection credentials: 
dsn_hostname = "fbd88901-ebdb-4a4f-a32e-
9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud" dsn_uid = "wxs77796" 	dsn_pwd = "fv1zsnR7cf2LCSA3" dsn_driver = "{IBM DB2 ODBC DRIVER}" dsn_database = "BLUDB" # e.g. "BLUDB" dsn_port = "32731" 	 dsn_protocol = 
"TCPIP" 	 	# i.e. "TCPIP" dsn_security = "SSL" 
#i.e. "SSL"  
#STEP 3: Create the DB2 database connection: 
dsn = ( 
 
"DRIVER={0};" 
"DATABASE={1};" 
"HOSTNAME={2};" 
"PORT={3};" 
"PROTOCOL={4};" 
"UID={5};" 
"PWD={6};" 
"SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security) print(dsn) Now establish the connection to the database 
try: 
conn = ibm_db.connect(dsn, "", "") 	print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname) 
 
except: 
print ("Unable to connect: ", ibm_db.conn_errormsg() ) 
 
server = ibm_db.server_info(conn) 
 
 
print ("DBMS_NAME: ", server.DBMS_NAME) print ("DBMS_VER: ", 	server.DBMS_VER) print ("DB_NAME: ", server.DB_NAME) 
 
client = ibm_db.client_info(conn) 
 
 
print ("DRIVER_NAME:  ", client.DRIVER_NAME) print ("DRIVER_VER:    ", client.DRIVER_VER) print 
("DATA_SOURCE_NAME: ", client.DATA_SOURCE_NAME) print 
("DRIVER_ODBC_VER: 	", client.DRIVER_ODBC_VER) print 
("ODBC_VER: 	", client.ODBC_VER) print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE) print ("APPL_CODEPAGE:  	", client.APPL_CODEPAGE) print 
("CONN_CODEPAGE: 	", client.CONN_CODEPAGE) 
 
#STEP 4: Close the Connection: 
 
ibm_db.close(conn) 