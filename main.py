import eel
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = OWM("e2fbcdf8aba30271b78027a62c0c2c3f")

@eel.expose
def get_weather(city):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	w = observation.weather
	temp = w.temperature('celsius')['temp']
	
	return "В городе " + city + " сейчас " + str(temp) + " градусов!"
	
	
# Вызов места хранения директории
eel.init("web ")

#Запуск библиотеки eel + указываем откуда и ставим размер окна.
eel.start("main.html", size=(700, 700))