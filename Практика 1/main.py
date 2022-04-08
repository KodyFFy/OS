import psutil
import os
import json
import xml.etree.ElementTree as ET
import zipfile as zip

def indent(elem, level=0):
    try:
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    except:
        print("Произошла ошибка модуля отспупов для XML!")
        menu()

def menu():
	try:
		print("------------------------------")
		print("1. Вывод информации о дисках.")
		print("2. Работа с файлами.")
		print("3. Работа с JSON.")
		print("4. Работа с XML")
		print("5. Работа с ZIP.")
		quest = int(input("Введите номер: "))
		print("------------------------------")
		if quest < 1 or quest > 5:
			print(f"Ошибка. В меню нет функции с номером {quest}!")
			menu()
		elif quest == 1:
			diskInfo()
		elif quest == 2:
			FileSystem()
		elif quest == 3:
			Json()
		elif quest == 4:
			XML()
		elif quest == 5:
			ZIP()
	except:
		print("Произошла ошибка модуля <Menu>")
		menu()

def diskInfo():
	try:
		disks = psutil.disk_partitions()
		for d in disks:
			name = d[0]
			typE = d[2]
			memory_info_all = psutil.disk_usage(d[0])
			size = memory_info_all[0]
			busy = memory_info_all[1]
			free = memory_info_all[2]
			procent = memory_info_all[3]
			print("------------------------------")
			print(f"Информация о дисках:")
			print(f"Имя диска: {name}")
			print(f"Тип файловой системы: {typE}")
			print(f"Всего места: {size}")
			print(f"Занято места: {busy}")
			print(f"Свободно: {free}")
			print(f"Процент занятости: {procent}%")
			print("------------------------------")
		menu()
	except:
		print("Произошла ошибка модуля <diskInfo>")
		diskInfo()

def FileSystem():
		print("------------------------------")
		print("1. Cоздать файл.")
		print("2. Записать строку в файл.")
		print("3. Прочитать файл в консоль.")
		print("4. Удалить файл.")
		print("0. В главное меню.")
		quest = int(input("Введите номер: "))
		print("------------------------------")
		if quest < 0 or quest > 4:
			print(f"Ошибка. В меню нет функции с номером {quest}!")
			FileSystem()
		elif quest == 1:
			name = input("Введите имя файла(без расширения): ")
			file_name = name + ".txt"
			FILE = open(file_name, "w+")
			FILE.close()
			print(f"Файл под названием {file_name} успешно создан!")
			FileSystem()
		elif quest == 2:
			name = input("Введите название файла для редактирования(без расширения): ")
			file_name = name + ".txt"
			isfile = os.path.isfile(file_name)
			if isfile is False:
				print("Файл не существует. Возврат в меню.")
				FileSystem()
			else:
				text = input("Ввести текст тут: ")
				FILE = open(file_name, "a")
				FILE.write(text + "\n")
				FILE.close()
				print("Запись успешно добавлена в файл!")
				FileSystem()
		elif quest == 3:
			name = input("Введите название файла для вывода в консоль(без расширения): ")
			file_name = name + ".txt"
			isfile = os.path.isfile(file_name)
			if isfile is False:
				print("Файл не существует. Возврат в меню.")
				FileSystem()
			else:
				FILE = open(file_name, "r")
				texts = FILE.read()
				FILE.close()
				print("------------------------------")
				print(f"Содержание файла: {texts}")
				print("------------------------------")
				FileSystem()
		elif quest == 4:
			name = input("Введите название файла для вывода в консоль(без расширения): ")
			file_name = name + ".txt"
			isfile = os.path.isfile(file_name)
			if isfile is False:
				print("Файл не существует. Возврат в меню.")
				FileSystem()
			else: 
				os.remove(file_name)
				print(f"Файл с именем {file_name} успешно удален!")
				FileSystem()
		elif quest == 0:
			menu()

def Json():
	print("------------------------------")
	print("Тема работы с JSON президенты мира и мини инфа о них.")
	print("1. Cоздать файл JSON.")
	print("2. Записать новый объект.")
	print("3. Прочитать файл в консоль.")
	print("4. Удалить файл.")
	print("0. В главное меню.")
	quest = int(input("Введите номер: "))
	print("------------------------------")
	if quest < 0 or quest > 4:
		print(f"Ошибка. В меню нет функции с номером {quest}!")
		Json()	
	elif quest == 1:
		name = input("Введите имя файла(без расширения): ")
		file_name = name + ".json"
		FILE = open(file_name, "w+")
		FILE.write("{}")
		FILE.close()
		print(f"Файл под названием {file_name} успешно создан!")
		with open (file_name, "r") as f:
			pres = json.load(f)

		pres["Президенты:"] = {}
		pres["Президенты:"]["Путин В.В."] = {}
		pres["Президенты:"]["Путин В.В."]["ФИО"] = "Владимир Владимирович Путин"
		pres["Президенты:"]["Путин В.В."]["Мини-Инфа"] = {}
		pres["Президенты:"]["Путин В.В."]["Мини-Инфа"]["Страна"] = "Российская Федерация"
		pres["Президенты:"]["Путин В.В."]["Мини-Инфа"]["Возраст"] = 69
		pres["Президенты:"]["Путин В.В."]["Мини-Инфа"]["Цвет глаз"] = "Серый"
		pres["Президенты:"]["Путин В.В."]["Мини-Инфа"]["Рост"] = "170 см"
		with open (file_name, "w") as w:
			pres = json.dump(pres, w, indent = 2, ensure_ascii=False)
		print("------------------------------")


		Json()
	elif quest == 2:
		name = input("Введите название файла для редактирования(без расширения): ")
		file_name = name + ".json"
		isfile = os.path.isfile(file_name)
		if isfile is False:
			print("Файл не существует. Возврат в меню.")
			Json()
		else:
			sub_name = input("Введите фамилию президента и сокрщено имя и отчество(Например: Путин В.В.): ")
			Name = input("Введите полное ФИО президента: ")
			age = int(input("Введите возраст президента: "))
			eye = input("Введите цвет глаз: ")
			height = input("Введите рост: ")
			country = input("Введите название страны: ")

		with open (file_name, "r") as f:
			pres = json.load(f)
		pres["Президенты:"][sub_name] = {}
		pres["Президенты:"][sub_name]["ФИО"] = Name
		pres["Президенты:"][sub_name]["Мини-Инфа"] = {}
		pres["Президенты:"][sub_name]["Мини-Инфа"]["Страна"] = country
		pres["Президенты:"][sub_name]["Мини-Инфа"]["Возраст"] = age
		pres["Президенты:"][sub_name]["Мини-Инфа"]["Цвет глаз"] = eye
		pres["Президенты:"][sub_name]["Мини-Инфа"]["Рост"] = height
		with open (file_name, "w") as w:
			pres = json.dump(pres, w, indent = 2, ensure_ascii=False)
		Json()
	elif quest == 3:
		name = input("Введите название файла для редактирования(без расширения): ")
		file_name = name + ".json"
		isfile = os.path.isfile(file_name)
		if isfile is False:
			print("Файл не существует. Возврат в меню.")
			Json()
		else:
			with open (file_name, "r") as f:
				pres = json.load(f)
				i = 1
			for q in pres["Президенты:"]:
				FIO = pres["Президенты:"][q]["ФИО"]
				cou = pres["Президенты:"][q]["Мини-Инфа"]["Страна"]
				age = pres["Президенты:"][q]["Мини-Инфа"]["Возраст"]
				eye = pres["Президенты:"][q]["Мини-Инфа"]["Цвет глаз"]
				height = pres["Президенты:"][q]["Мини-Инфа"]["Рост"]

				print(f"{i}.Презедент: {FIO};\nЛидер страны: {cou};\nВозраст: {age};\nЦвет глаз: {eye};\nРост: {height}\n")
				i+=1
			Json()
	elif quest == 4:
		name = input("Введите название файла для вывода в консоль(без расширения): ")
		file_name = name + ".json"
		isfile = os.path.isfile(file_name)
		if isfile is False:
			print("Файл не существует. Возврат в меню.")
			Json()
		else: 
			os.remove(file_name)
			print(f"Файл с именем {file_name} успешно удален!")
			Json()
	elif quest == 0:
		menu()

def XML():
	print("------------------------------")
	print("1. Cоздать файл XML.")
	print("2. Записать новый объект.")
	print("3. Прочитать файл в консоль.")
	print("4. Удалить файл.")
	print("0. В главное меню.")
	quest = int(input("Введите номер: "))
	print("------------------------------")
	if quest < 0 or quest > 4:
		print(f"Ошибка. В меню нет функции с номером {quest}!")
		XML()	
	elif quest == 1:
		name = input("Введите имя файла(без расширения): ")
		file_name = name + ".xml"
		
		root = ET.Element("Мир")
		Countrys = ET.Element("Страны")
		root.append(Countrys)

		Country = ET.Element("Государство", name = "Российская Федерация")
		Countrys.append(Country)

		info2 = ET.SubElement(Country, "Площадь")
		info2.text = "17,1 миллионов км^2"

		info3 = ET.SubElement(Country, "Популяция")
		info3.text = "145 478 097"

		info4 = ET.SubElement(Country, "Лидер")
		info4.text = "Владимир Владимирович Путин"

		indent(root)

		tree = ET.ElementTree(root)
		
		

		tree.write(file_name, encoding= 'utf-8')

		

		print(f"Файл под названием {file_name} успешно создан!")
		XML()
	elif quest == 2:
		name = input("Введите название файла для редактирования(без расширения): ")
		file_name = name + ".xml"
		isfile = os.path.isfile(file_name)
		if isfile is False:
			print("Файл не существует. Возврат в меню.")
			XML()
		else:

			tree = ET.parse(file_name)
			root = tree.getroot()
			drevo = root[0]
			state = input("Название страны: ")
			area = input("Площадь страны: ")
			population = input("Число людей в стране: ")
			leader = input("ФИО лидера: ")

			Country = ET.Element("Государство", name = state)
			drevo.append(Country)

			info2 = ET.SubElement(Country, "Площадь")
			info2.text = area

			info3 = ET.SubElement(Country, "Популяция")
			info3.text = population

			info4 = ET.SubElement(Country, "Лидер")
			info4.text = leader

			indent(root)

			tree = ET.ElementTree(root)		
			tree.write(file_name, encoding= 'utf-8')
			print("Запись успешно сохранена!")
			XML()
	elif quest == 3:
		name = input("Введите название файла для редактирования(без расширения): ")
		file_name = name + ".xml"
		isfile = os.path.isfile(file_name)
		if isfile is False:
			print("Файл не существует. Возврат в меню.")
			XML()
		else:
			tree = ET.parse(file_name)
			root = tree.getroot()

			for el in root:
				for s in el:
					name = s.attrib
					name = name['name']
					print(name)
					area = s[0].text + "км^2"
					population = s[1].text
					leader = s[2].text
					print(f"Название государства: {name};\nПлощадь государства: {area};\nПопуляция государства: {population};\nЛидер государства: {leader};")
					print("######################")
			XML()
	elif quest == 4:
		name = input("Введите название файла для вывода в консоль(без расширения): ")
		file_name = name + ".xml"
		isfile = os.path.isfile(file_name)
		if isfile is False:
			print("Файл не существует. Возврат в меню.")
			XML()
		else: 
			os.remove(file_name)
			print(f"Файл с именем {file_name} успешно удален!")
			XML()
	elif quest == 0:
		menu()

def ZIP():
	print("------------------------------")
	print("1. Cоздать файл ZIP.")
	print("2. Добавить файл в архив.")
	print("3. Разархивировать арив.")
	print("4. Удалить файл.")
	print("0. В главное меню.")
	quest = int(input("Введите номер: "))
	global file_name
	global Qfiles
	print("------------------------------")
	if quest < 0 or quest > 4:
		print(f"Ошибка. В меню нет функции с номером {quest}!")
		ZIP()	
	elif quest == 1:
		name = input("Введите имя файла(без расширения): ")
		file_name = name + ".zip"
		FILE = open(file_name, "w+")
		FILE.close()
		print(f"Файл под названием {file_name} успешно создан!")
		ZIP()
	elif quest == 2:
		name = input("Введите название файла для редактирования(без расширения): ")
		file_name = name + ".zip"
		isfile = os.path.isfile(file_name)
		if isfile is False or zip.is_zipfile(False):
			print("Файл не существует. Возврат в меню.")
			ZIP()
		else:
			object_File = input("Введите название файла-объекта (с расширением): ")
			zipfile = zip.ZipFile(file_name, 'w')
			zipfile.write(object_File)
			zipfile.close()
			print(f"Файл {object_File} успешно добавлен в архив файла {file_name}!")
			ZIP()
	elif quest == 3: 
		name = input("Введите название файла для редактирования(без расширения): ")
		file_name = name + ".zip"
		isfile = os.path.isfile(file_name)
		if isfile is False or zip.is_zipfile(False):
			print("Файл не существует. Возврат в меню.")
			ZIP()
		else:
			zipfile = zip.ZipFile(file_name, 'r')
			Qfiles = zipfile.namelist()
			zipfile.extractall()
			for i in Qfiles:
				name = i
				print(f"Имя файла: {name}")
				try:
					filee = open(name, "r")
					info = filee.read()
					filee.close()
					print("Информация в файле: ################## \n")
					print(info)
				except:
					print("Попытка вывести файл в консоль провалилась!")
					ZIP()
			zipfile.close()
			ZIP()
	elif quest == 4:
		if file_name is None or Qfiles is None:
			print("Файлы которые использовала программа не найдены.")
			
			ZIP()
		try:
			os.remove(file_name)
			print(f"Файл с именем {file_name} успешно удален!")
			for  i in Qfiles:
				os.remove(i)
				print(f"Файл с именем {i} успешно удален!")
			ZIP()
		except:
			print("Либо файла нет, либо произошла ошибка.")
			ZIP()
	elif quest == 4:
		menu()

menu()
