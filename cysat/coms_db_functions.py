import sqlite3

#----------------DATABASEs-----------------
sqlite_file = 'coms_db.sqlite'
#------------------END OF DATABASE---------
#---------------TABLES--------------
cur_data_table = 'current_data_table'
hist_data_table = 'hist_data_table'
router_instruct = 'router_instruct'
#--------------------END OF TABLES------------------



#--------------COLUMNS--------------
satalite_col = 'satalite'
pass_col = 'pass_numbr'
az_col = 'az'
el_col = 'el'
datetime_col = 'datetime'
pk_col = "pk"  				#primary key
command_col = "command"
#--------------END COLUMNS------------------

def insert_to_data_table(table_name,sat, pass, az ,el,dt):
	#----------ESTABLISHING A CONNECTION-----------------
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	#----------------FINISHED CONNECTING------------------

	try:
    	c.execute('INSERT INTO {tn} ({sata}, {passa}, {aza}, {ela}, {dta}) VALUES ({sate}, {passe}, {aze}, {ele}, {dte})'\
        	.format(tn=table_name, sata = satalite_col , passa = pass_col, aza = az_col, ela = el_col, dta = datetime_col, sate = sat, passe = pass, aze = az, ele = el, dte = dt))
	except sqlite3.IntegrityError:
    	print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

    #------------------COMMIT AND CLOSE CONNECTION------------
	conn.commit()
	conn.close()
	#-------------------CONNECTION HAS CLOSED

def insert_to_router_table(txt):
	#----------ESTABLISHING A CONNECTION-----------------
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	#----------------FINISHED CONNECTING------------------
	
	max_pk = c.execute('SELECT MAX({pk}) FROM {tn}'.format(pk = pk_col, tn= router_instruct))
	max_pk++ 
	c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES ({pk}, {tt})".\
        format(tn=router_instruct, idf=pk_col, cn=command_col, pk = max_pk, tt= txt))

    #------------------COMMIT AND CLOSE CONNECTION------------
	conn.commit()
	conn.close()
	#-------------------CONNECTION HAS CLOSED




