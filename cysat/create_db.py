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

#--------------FIELD TYPES------------------
datetime_type = 'NUMERIC'
int_type = 'INTEGER'
txt_type = 'TEXT'
real_type = 'REAL'
#--------------END FIELD TYPES------------------

#----------ESTABLISHING A CONNECTION-----------------
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
#----------------FINISHED CONNECTING--------------------

#-----------------CREATING TABLES---------------------

c.execute('CREATE TABLE {tn} ({sf} {sft},{pf} {pft},{azf} {azft}, {elf} {elft}, {dtf} {dtft})'\
	.format(tn = cur_data_table, sf=satalite_col, sft= txt_type, pf= pass_col, pft = int_type, azf = az_col, azft = real_type, elf = el_col, elft = real_type, dtf = datetime_col, dtft = datetime_type ))
c.execute('CREATE TABLE {tn} ({sf} {sft},{pf} {pft},{azf} {azft}, {elf} {elft}, {dtf} {dtft})'\
	.format(tn = hist_data_table, sf=satalite_col, sft= txt_type, pf= pass_col, pft = int_type, azf = az_col, azft = real_type, elf = el_col, elft = real_type, dtf = datetime_col, dtft = datetime_type ))
c.execute('CREATE TABLE {tn} ({pk} {pkt} PRIMARY KEY, {cmd} {cmdt})'\
	.format(tn = router_instruct, pk = pk_col, pkt = int_type, cmd = command_col, cmdt = txt_type))

#------------------FINISHED CREATING TABLES----------------

#------------------COMMIT AND CLOSE CONNECTION------------

conn.commit()
conn.close()

#-------------------CONNECTION HAS CLOSED