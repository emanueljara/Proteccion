from flask import Flask
import datetime
import email_to
import pytz

app = Flask(__name__)

def generateFibonacci():

    hora = datetime.datetime.now(pytz.timezone('America/Bogota'))
    hora = hora.strftime('%H:%M:%S')
    hour = hora.split(':')

    x = int(hour[1][0])
    y = int(hour[1][1])
    n = int(hour[2])

    fib = str(x) + ", "
    for i in range(n):
        x, y = y, (x + y)
        fib = fib + str(x) + ", "

    x, y = y, (x + y)
    fib = fib + str(x)
    
    return hora, fib

def sendEmail(hora, fibSeries):

    server = email_to.EmailServer('smtp.gmail.com', 587, 'emmanuel.jaramillo@quind.io', '')
    server.quick_email('emmanuel84jg@gmail.com', ' Hora: ' + str(hora) ,
                   ['Fibonacci: ' + fibSeries])
    server.quick_email('correalondon@gmail.com', ' Hora: ' + str(hora) ,
                   ['Fibonacci: ' + fibSeries])
    server.quick_email('chamogomez@gmail.com', ' Hora: ' + str(hora) ,
                   ['Fibonacci: ' + fibSeries])

@app.route('/serieFibonacci')
def Seriefibonacci():
    hora, fibSeries = generateFibonacci()
    sendEmail(hora, fibSeries)
    return "Hora: " + hora + "serie : " + fibSeries

#app.run(host = "0.0.0.0", debug = True)
