import serial
import pickle

porta = 'COM4'
velocidade = 9600

conexao = serial.Serial(porta, velocidade);

print ('Serial Iniciada...\n')


while True:

    leitura = conexao.readline()

    print(leitura)

    #lista_recuperada = pickle.dumps(leitura)
  #  lista_recuperada1 = pickle.loads(lista_recuperada)
   # print(lista_recuperada1)

   # print(type(leitura))

   # data_sinais = leitura_serial.split("|")
   # print("dado-2" -- data_sinais)


   # if ('GSR' in leitura):
      #  print("G-----"+ leitura)

    #elif('ECG' in leitura):
     #   print("E-----" + leitura)






conexao.close();


#db = MySQLdb.connect(host="mysql.lhost03.w3br.com", user="lhost03", passwd="suasenha", db="seudb")
#con.select_db('banco de dados')

#cursor = db.cursor()

#cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)', (valor1, valor2, valor3))