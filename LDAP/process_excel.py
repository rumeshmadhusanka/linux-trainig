import pandas as pd

emp = pd.read_excel('EmployeeInformation-210726-172341.xlsx')
books = pd.read_excel('EmployeeInformation-210726-172341.xlsx', sheet_name="Books")

out_file = open("entries.ldif", "w")
for index, row in emp.iterrows():
    fname, sname, mail, mobile, home, em_type, address = row

    template = \
        f"""\
dn: mail={mail},ou=employees,dc=Itacademy,dc=com
cn: {fname}
sn: {sname}
mail: hello@gmail.co{mail}
mobile: {mobile}
homePhone: {home}
employeeType: {em_type}
localityName: {address}
objectClass: inetOrgPerson\n\n"""
    out_file.write(template)

for index, row in books.iterrows():
    name, did, pub = row
    template = \
        f"""
dn: documentIdentifier={did},ou=books,dc=Itacademy,dc=com
documentTitle: {name}
documentIdentifier: {did}
documentPublisher: {pub}
objectClass: document\n"""
    out_file.write(template)
