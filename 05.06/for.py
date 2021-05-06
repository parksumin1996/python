marks= []

for i in range(5):
        scr = int(input (" %d번 학생의 성적: " % (i+1)))
        marks.append(scr)

print(marks)
hap = 0
number = 0
for makr in marks:
        number = number +1
        hap = hap +mark
        if mark >= 60:
                print("%d번 학생의 성적은 %d이고 합격입니다." % (number, mark))
        else:
                 print("%d번 학생의 성적은 %d이고 불합격입니다." % (number, mark))
print("전체 총합은 %d이고 평균은 %.2f입니다." % (hap, (hap/number)))
