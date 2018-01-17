import time
import RPi.GPIO as GPIO
import MFRC522
import os

CARTOES_LIBERADOS = {
    '3D:53:37:52:B': 'Edivaldo'
}

deniedAccessCount = 0

os.system("python servo_garagem_fecha.py")

try:

    LeitorRFID = MFRC522.MFRC522()
    print("Coloque o cartao")

    while True:
        status, tag_type = LeitorRFID.MFRC522_Request(LeitorRFID.PICC_REQIDL)

        if status == LeitorRFID.MI_OK:
            print('Cartao detectado!')

            status, uid = LeitorRFID.MFRC522_Anticoll()

            if status == LeitorRFID.MI_OK:
                uid = ':'.join(['%X' % x for x in uid])
                print('UID do cartao: %s' % uid)

                if uid in CARTOES_LIBERADOS:
                    print('Acesso Liberado!')
                    print('Ola %s.' % CARTOES_LIBERADOS[uid])
		    os.system("python servo_garagem_abre.py")
		    time.sleep(0.5)
		    os.system("python servo_garagem_fecha.py")
		    
                else:
                    print('Acesso Negado!')
		    
                    
                    if deniedAccessCount >= 3 :
		    	os.system("python mail.py")
		    else:
		    	deniedAccessCount += 1

                print('nAproxime seu cartao RFID')

        time.sleep(.25)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('nPrograma encerrado.')
