from smartcard.System import readers
from smartcard.util import toHexString

  
class RfidACR122U: 
	#return uid in hexa str 
	def read_uid(self): 
		#retorna la llista de readers en grups
		r = readers() 
		#si len(r)==0 es que no hi ha cap reader conectat                   
		if len(r) < 1:
			return "No reader connected!"            
		else:
			#nomes tenim 1 reader conectat, per tant ocupa la posicio 0
			reader = r[0]  
			#ens connectem amb pcsc al reader
			connection = reader.createConnection()
		    #ens connectem a la card
			connection.connect()
			#definim el APDU que necessitem transmitir a card per que ens retorni la UID, comentat a la memoria
			cmdMap = {
					"getuid":[0xFF, 0xCA, 0x00, 0x00, 0x00],
					}
			COMMAND = cmdMap.get("getuid", "getuid")
			#transmitim el COMMAND a la card, la card ens retorna data
			data, sw1, sw2 = connection.transmit(COMMAND)
			#retornem data en forma de string Hexadecimal
			return toHexString(data)
		  
if __name__ == "__main__": 
	rf = RfidACR122U() 
	uid = rf.read_uid() 
	print(uid)
 
