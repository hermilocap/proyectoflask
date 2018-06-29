from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')#wrap o un decorador
def index():
        name='Hermilo'
        return render_template('index.html',name=name) #regresa un string

if __name__=='__main__':
    app.run(debug=True,port=8000)#se encarga de ejecutar el servidor pueto 5000
