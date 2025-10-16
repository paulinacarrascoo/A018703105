#Excercise1

temperatures= [30, 22, 30, 21, 26, 2, 31, 36]

avgTemp= sum(temperatures) / len(temperatures)

print("The average temperature is" , avgTemp)


for temperature  in temperatures:
    if temperature >= avgTemp:
        print(temperature, "is above average")
    else:
        print (temperature, "is below average")




#Excercise2

studentsNames=['Pauli', 'Sharon', 'Hannon', 'Ana Lucy', 'Piojo']
studentsGrades=[100, 95, 78, 63, 59]

#Group Average
avgGrade=sum(studentsGrades) / len(studentsGrades)
print(avgGrade, "is the average grade")

failedStudents=0
passedStudentsCount=0

#Percentage of Failed
for studentGrade in studentsGrades:
    if studentGrade < 70:
        print(studentGrade, "that is your grade")
        failedStudents= failedStudents + 1

        failedStudents.append(studentsNames[studentsNames.index])
        print("Percentage of students that failed")
        print(failedStudents /len(studentsNames))

print(failedStudents)

print("Percentage of students that failed")
print(failedStudents /len(studentsNames))
    





