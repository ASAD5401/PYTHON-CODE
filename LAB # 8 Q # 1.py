family={"name:":"Asad Ali Khan","Father Name:":"Mehfooz Khan","Mother Name:":"Zareen Naz","Brother Name:":"Saad Khan","Sister name:":["Saima Naz","Nmira Naz"],"Brother-in-law:":"Umar Warsi"}
for x,y in family.items():
    print(x,y)
grandfamily={"Maternal":{"Grand Father name:":"Qasim khan","Grand Mother Name:":"Mehmooda Khan","Uncle":["Mehboob Khan","Maqsood Khan","Munawar Khan","Muzafar Khan"],"Aunts":["Farzana Khan"]},"Paternal":{"Grand Father Name:":"Zahoor Ahmed","Grand Mother Name:":"Raeesa Begum","Uncles:":["Tariq Ahmed","Tabish Ahmed","Danish Ahmed"],"Aunts":["Samreen Naz","Shaheen Naz","Ambreen Naz"]}}
family.update(grandfamily)
for x,y in family.items():
    print(x,y)
