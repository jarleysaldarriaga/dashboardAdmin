from datetime import datetime

def createCase(request,mysql):
    applicant = request.form["applicant"]
    ticket_type = request.form["ticket_type"]
    description = request.form["description"]
    area_asignated = request.form["area_asignated"]
    date_created = datetime.now()
    
    
    
    
    query = mysql.connection.cursor()
    consulta = query.execute("INSERT INTO cases(applicant,ticket_type,description,area_asignated,date_created) values(%s,%s,%s,%s,%s)",(applicant,ticket_type,description,area_asignated,date_created))
    
    mysql.connection.commit()
    query.close()
    
    print(consulta)