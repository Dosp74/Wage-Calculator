from tkinter import * #tkinter 모듈의 모든 함수 포함

window = Tk() #최상위 윈도우 생성
window.title("Wage Calculator")

hourly_rate = 0 #시급 변수 선언
weekly_rate = 0 #책정 주휴수당 변수 선언
daily_working_hours = 0 #일일 근로시간 변수 선언
number_of_working_days_per_week = 0 #1주 근로일수 변수 선언
monthly_overtime_work_hours = 0 #월 연장 근로시간 변수 선언
monthly_night_work_hours = 0 #월 야간 근로시간 변수 선언

def hourly_rate_button_click():
    global hourly_rate
    hourly_rate = int(e1.get())

def weekly_rate_button_click():
    global weekly_rate
    weekly_rate = int(e2.get())

def daily_working_hours_button_click():
    global daily_working_hours
    daily_working_hours = float(e3.get())

def number_of_working_days_per_week_button_click():
    global number_of_working_days_per_week
    number_of_working_days_per_week = int(e4.get())

def monthly_overtime_work_hours_button_click():
    global monthly_overtime_work_hours
    monthly_overtime_work_hours = float(e5.get())

def monthly_night_work_hours_button_click():
    global monthly_night_work_hours
    monthly_night_work_hours = float(e6.get())

def calculate(): #계산하기 버튼에 대한 계산 및 처리 함수
    global expected_weekly_rate #예상 주휴수당 변수 선언
    if daily_working_hours * number_of_working_days_per_week >= 15 :
        if daily_working_hours * number_of_working_days_per_week <= 40 :
            expected_weekly_rate = (daily_working_hours * number_of_working_days_per_week / 40) * 8 * weekly_rate * (365 / 12 / 7)
        elif daily_working_hours * number_of_working_days_per_week > 40 :
            expected_weekly_rate = 8 * weekly_rate * (365 / 12 / 7)
    else :
        expected_weekly_rate = 0
        
    global expected_overtime_rate #예상 연장수당 변수 선언
    expected_overtime_rate = monthly_overtime_work_hours * hourly_rate * 1.5
    
    global expected_night_rate #예상 야간수당 변수 선언
    expected_night_rate = monthly_night_work_hours * hourly_rate * 1.5
    
    global expected_wage #예상 급여 변수 선언
    expected_wage = (hourly_rate * daily_working_hours * number_of_working_days_per_week * (365 / 12 / 7)) + expected_weekly_rate + expected_overtime_rate + expected_night_rate
    
    global output #실수령액 변수 선언
    output = expected_wage * probation * (1 - tax)
    
    l15.config(text = f"{expected_wage:.2f} 원")
    l16.config(text = f"{expected_weekly_rate:.2f} 원")
    l17.config(text = f"{expected_overtime_rate:.2f} 원")
    l18.config(text = f"{expected_night_rate:.2f} 원")
    l19.config(text = f"{output:.2f} 원")
    


probation = 1.0 #수습기간 관련 변수 선언

check_left = IntVar()
check_right = IntVar()

def probation_check(checked_probation):
    global probation
    if checked_probation == check_left:
        check_right.set(0)
        probation = 0.9
    elif checked_probation == check_right:
        check_left.set(0)
        probation = 1.0

tax = 0.033 #세금 변수 선언

check_var932 = IntVar()
check_var33 = IntVar()

def on_checkbutton_click(selected_var):
    global tax
    if selected_var == check_var932:
        check_var33.set(0)
        tax = 0.0932
    elif selected_var == check_var33:
        check_var932.set(0)
        tax = 0.033



l1=Label(window, text="시급     ➡     월급", font='helvetica 18', bd=5, relief=RIDGE, width=45)
l1["bg"]="orange"
l1.grid(row=0, column=0, columnspan=5)
l2=Label(window, text="시급", font='helvetica 12')
l2.grid(row=1, column=0)
l3=Label(window, text="책정 주휴수당", font='helvetica 12')
l3.grid(row=2, column=0)
l4=Label(window, text="일일 근로시간", font='helvetica 12')
l4.grid(row=3, column=0)
l5=Label(window, text="1주 근로일수", font='helvetica 12')
l5.grid(row=4, column=0)
l6=Label(window, text="월 연장 근로시간", font='helvetica 12')
l6.grid(row=5, column=0)
l7=Label(window, text="월 야간 근로시간", font='helvetica 12')
l7.grid(row=6, column=0)
l8=Label(window, text="수습", font='helvetica 12')
l8.grid(row=7, column=0)
l9=Label(window, text="세금", font='helvetica 12')
l9.grid(row=8, column=0)
l10=Label(window, text="예상 급여", font='helvetica 12')
l10.grid(row=10, column=0)
l11=Label(window, text="예상 주휴수당", font='helvetica 12')
l11.grid(row=11, column=0)
l12=Label(window, text="예상 연장수당", font='helvetica 12')
l12.grid(row=12, column=0)
l13=Label(window, text="예상 야간수당", font='helvetica 12')
l13.grid(row=13, column=0)
l14=Label(window, text="실수령액", font='helvetica 12')
l14.grid(row=14, column=0)

l15=Label(window, text="원", font='helvetica 12')
l15.grid(row=10, column=1)
l16=Label(window, text="원", font='helvetica 12')
l16.grid(row=11, column=1)
l17=Label(window, text="원", font='helvetica 12')
l17.grid(row=12, column=1)
l18=Label(window, text="원", font='helvetica 12')
l18.grid(row=13, column=1)
l19=Label(window, text="원", font='helvetica 12')
l19.grid(row=14, column=1)

e1=Entry(window, bd=5)
e1.grid(row=1, column=1)
e2=Entry(window, bd=5)
e2.grid(row=2, column=1)
e3=Entry(window, bd=5)
e3.grid(row=3, column=1)
e4=Entry(window, bd=5)
e4.grid(row=4, column=1)
e5=Entry(window, bd=5)
e5.grid(row=5, column=1)
e6=Entry(window, bd=5)
e6.grid(row=6, column=1)

b1=Button(window, text="입력", bd=3, command=hourly_rate_button_click)
b1.grid(row=1, column=2)
b2=Button(window, text="입력", bd=3, command=weekly_rate_button_click)
b2.grid(row=2, column=2)
b3=Button(window, text="입력", bd=3, command=daily_working_hours_button_click)
b3.grid(row=3, column=2)
b4=Button(window, text="입력", bd=3, command=number_of_working_days_per_week_button_click)
b4.grid(row=4, column=2)
b5=Button(window, text="입력", bd=3, command=monthly_overtime_work_hours_button_click)
b5.grid(row=5, column=2)
b6=Button(window, text="입력", bd=3, command=monthly_night_work_hours_button_click)
b6.grid(row=6, column=2)
b7=Button(window, text="계산하기", bd=5, width=20, command=calculate)
b7.grid(row=9, column=2)

c1=Checkbutton(window, text="해당", variable=check_left, command=lambda: probation_check(check_left))
c1.grid(row=7, column=1)
c2=Checkbutton(window, text="미해당", variable=check_right, command=lambda: probation_check(check_right))
c2.grid(row=7, column=2)
c3=Checkbutton(window, text="9.32%(4대보험 가입)", variable=check_var932, command=lambda: on_checkbutton_click(check_var932))
c3.grid(row=8, column=1)
c4=Checkbutton(window, text="3.3%(4대보험 미가입)", variable=check_var33, command=lambda: on_checkbutton_click(check_var33))
c4.grid(row=8, column=2)

window.mainloop() #윈도우 이벤트 처리 함수