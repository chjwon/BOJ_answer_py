semester_num = int(input())
for i_se in range(semester_num):
    subject_num = int(input())
    total_credit = 0
    av_gpa = 0
    for i_su in range(subject_num):
        credit, gpa = input().split(' ')
        credit = int(credit)
        gpa = float(gpa)
        total_credit += credit
        av_gpa += gpa * credit

    av_gpa = av_gpa / total_credit
    av_gpa = int(av_gpa *10)/10
    total_credit = str(total_credit)
    av_gpa = str(av_gpa)
    print(total_credit + ' ' + av_gpa)

