import bottle
import requests
import json

respuesta = []
empresas = []
empresas2 = []

@bottle.route('/')
def home_page():
    return bottle.template('index.tpl')

@bottle.route('/respuesta_trabajo', method='POST')
def respuesta():
    palabraclave = bottle.request.forms.get('palabraclave')
    provincia = bottle.request.forms.get('provincia')
    categoria = bottle.request.forms.get('categoria')
    sector = bottle.request.forms.get('sector')
    estudios = bottle.request.forms.get('estudios')
    respuesta = requests.get("http://api.workmunity.com/1/search_offers?", params={"return":"json",
  "callback":"json_callback","cache":"on","lang":"es","locale":"es","echo":"test","results":"10",
	"keywords":palabraclave,"country":"es","state":provincia,"town":"0","radio":"on","studies":estudios,"level":"0",
	"category":categoria,"subcategory":"0","sector":sector,"salary":"0","contract":"0","workday":"0",
	"only_verified":"off","only_without_experience":"off"})
    json.loads(respuesta.text)

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
	empresas.append(json.loads(respuesta.text)[i][u'company'])

    for empresa in xrange(int(len(empresas))):
        empresas2.append(empresas[empresa])

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
	localidades.append(json.loads(respuesta.text)[i][u'town_str'])

    for localidad in xrange(int(len(localidades))):
        localidades2.append(empresas[localidad])

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
	puesto.append(json.loads(respuesta.text)[i][u'position'])

    for puesto in xrange(int(len(puestos))):
        puestos2.append(empresas[puesto])

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
	vacante.append(json.loads(respuesta.text)[i][u'vacancies'])

    for vacante in xrange(int(len(puestos))):
        vacantes2.append(empresas[vacante])



    return bottle.template('respuesta.tpl',palabraclave=palabraclave,provincia=provincia,categoria=categoria,estudios=estudios,sector=sector)
bottle.debug(True)
bottle.run(host='localhost',port=8080)
