import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "C:\\Users\\ASHISH\\Downloads\\dhamu-python-dev-8a7f55b3e94c.json",
    scope)

client = gspread.authorize(creds)
url = "https://docs.google.com/spreadsheets/d/1IawYJI0q5avMEq1Xlsx_ES4og12q_3D-tTm3tqHSesc/edit#gid=0"
sheet = client.open_by_url(url).sheet1

list_all_record = sheet.get_all_records()

class Student:


    def __init__(self, StudentID, StudentName, DateofBirth, Gender, Class, Category, ConcatDetails, Deposit, TotalFee, FatherName, MotherName, Address, SubmissionDate):
        self.id = StudentID
        self.name = StudentName
        self.dob = DateofBirth
        self.gender = Gender
        self.Class = Class
        self.catergory = Category
        self.contact = ConcatDetails
        self.deposit = Deposit
        self.totalFee = TotalFee
        self.father_name = FatherName
        self.mother_name = MotherName
        self.address = Address
        self.submission_date = SubmissionDate

    @classmethod
    def find_by_id(cls, id):
        for record in list_all_record:
            if record.get("StudentID") == id:
                student = Student(**record)
                break
        print(record)
        return record



