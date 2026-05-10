from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom

school = School("YASA", "Rajshahi")

# Add Classrooms
eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Add Students
sumi = Student("Sumaiya Islam", eight)
mim = Student("Akhi Aktar Mim", eight)
upsa = Student("Upoma Saha", eight)

ashu = Student("Asmaul Husna", nine)
rija = Student("Rima Jahan", nine)
fate = Student("Fatema", nine)
soak = Student("Soheli Akhi", nine)

fatu = Student("Fatema Tuj Johura", ten)
urmu = Student("Urmila Urmi", ten)
khaj = Student("Khandakar Jahida", ten)

school.student_admission(sumi)
school.student_admission(mim)
school.student_admission(upsa)

school.student_admission(ashu)
school.student_admission(rija)
school.student_admission(fate)
school.student_admission(soak)

school.student_admission(fatu)
school.student_admission(urmu)
school.student_admission(khaj)

# Teacher Objects
nitun = Teacher("Nitun Kumar Poddar")
toukir = Teacher("Toukir Ahmed")
azam = Teacher("Md. Shafiul Azam")
abc = Teacher("Abc")
bcd = Teacher("Bcd")
cde = Teacher("Cde")

# Subjects Objects
spl = Subject('SPL', nitun)
oop = Subject('OOP', toukir)
dm = Subject('DM', azam)
phy = Subject('Phy', abc)
che = Subject('Che', bcd)
math = Subject('Math', cde)

# Add subjects
eight.add_subject(spl)
eight.add_subject(phy)
eight.add_subject(che)

nine.add_subject(oop)
nine.add_subject(che)
nine.add_subject(math)

ten.add_subject(dm)
ten.add_subject(math)
ten.add_subject(phy)

# Add Teachers
school.add_teacher(spl, nitun)
school.add_teacher(oop, toukir)
school.add_teacher(dm, azam)
school.add_teacher(phy, abc)
school.add_teacher(che, bcd)
school.add_teacher(math, cde)

# Take Semester Final
eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()

print(school)