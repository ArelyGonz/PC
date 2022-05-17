#pip install mail_parser
import mailparser

eml_file = input("File name: ")
#parse_from_string
mail = mailparser.parse_from_file(eml_file)
print(mail.date)
print(mail.from_)
print(mail.delivered_to)
print(mail.message_id)
print(mail.subject)
print(mail.to)
