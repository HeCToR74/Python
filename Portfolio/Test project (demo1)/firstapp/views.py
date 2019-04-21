from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import CourstitlesModel, QuestionsModel, StepsModel, AnswersModel, UsersModel, GradesModel

# constants
COURS_NAME = "WebUI_Python"
COURS_ID = "1"

def login(request):
    '''
    The function to process queries of "login.html"
    '''
    if request.method == 'POST':
        # retrieve data from "login.html"
        user_name = request.POST.get("username")
        user_password = request.POST.get("password")
        # check if the admin has logged in
        if user_name == "ADMIN" and user_password == "admin":
            users = UsersModel.objects.all()
            # transfer dataset to page "admin_page.html"
            return render(request, "admin_page.html", context={"cours_name": COURS_NAME, "users": users})

        # by the user name we get the corresponding object from the database
        users = UsersModel.objects.filter(login=user_name)
        # check how many users are with this name
        if len(users) != 0:
            user = users[0]
        else:
            user = None
        # check the matching of the username with its password
        if user is not None and user_password == user.password:
            # by the cours id we get the corresponding object from the database        
            steps = StepsModel.objects.filter(cours_id_id=COURS_ID)
            data = []
            for step in steps:
                # by the step id we get the corresponding object from the database
                questions = QuestionsModel.objects.filter(step_id_id=step.id)
                # organize a two-dimensional list, each element of which is a list of two elements: 
                # the category name and the list of issues in this category
                data.append([step.step_name, questions])
            # by the user id we get the corresponding object from the database
            answers = AnswersModel.objects.filter(user_id_id=user.id)

            click = 0
            number_step = 0
            prev_number_step = -1
            next_number_step = 1
            step_name = data[number_step][0]
            if prev_number_step >=0:
                prev_step_name = data[prev_number_step][0]
            else:
                prev_step_name = data[0][0]

            next_step_name = data[next_number_step][0]        
            # transfer dataset to page "index.html"
            return render(request, "index.html", context={"click": click, "user_name": user.login, "user_id": user.id, "number_step": number_step, "last_step": len(steps)-1,\
        "prev_number_step": prev_number_step, "next_number_step": next_number_step,\
        "cours_name": COURS_NAME, "step_name": step_name, "prev_step_name": prev_step_name, "next_step_name": next_step_name,\
        "questions": data[number_step][1], "answers": answers})
        else:
            # transfer dataset to page "login.html"
            return render(request, "login.html")
    else:
        # transfer dataset to page "login.html"
        return render(request, "login.html")

def index(request):
    '''
    The function to process queries of "index.html" page
    '''          
#########################################################
    # for the first record of responses to the database (with each question when registering a response entry is created)
    #for step in steps:
    #    answers = []
    #    for question in questions:
    #        answer = AnswersModel()
    #        answer.answer_like = False
    #        answer.reg_date = datetime.now()
    #        answer.grade_id_id = "3"
    #        answer.question_id_id = question.id
    #        answer.user_id_id = USER_ID
    #        answer.save()
    
#########################################################

    if request.method == "POST":
        # retrieve data from "index.html"
        user_name =  request.POST.get("user_name")
        user_id =  int(request.POST.get("user_id"))
        # by the cours id we get the corresponding object from the database
        steps = StepsModel.objects.filter(cours_id_id=COURS_ID)
        data = []
        for step in steps:
            # by the step id we get the corresponding object from the database
            questions = QuestionsModel.objects.filter(step_id_id=step.id)
            # organize a two-dimensional list, each element of which is a list of two elements: 
            # the category name and the list of issues in this category
            data.append([step.step_name, questions])
        # by the user id we get the corresponding object from the database
        answers = AnswersModel.objects.filter(user_id_id=user_id)
        
        click =  int(request.POST.get("click"))
        click += 1
        number_step =  int(request.POST.get("number_step"))
        prev_number_step =  int(request.POST.get("prev_number_step"))
        next_number_step =  int(request.POST.get("next_number_step"))

        # save the received answers
        for question in data[number_step][1]:
            for answer in answers:
                if answer.question_id_id == question.id:
                    answer.answer_like = request.POST.get("L"+str(question.id))
                    answer.grade_id_id = request.POST.get("G"+str(question.id))
                    answer.reg_date = datetime.now()
                    answer.save()

        action =  request.POST.get("button")
        # determine which button was pressed
        if action == "Log out":            
            return render(request, "login.html", context={"user_name": user_name, "test": "end"})
        if action == "Next":
            number_step += 1
            prev_number_step += 1
            next_number_step += 1
        else:
            number_step -= 1
            prev_number_step -= 1
            next_number_step -= 1
            
        step_name = data[number_step][0]
        prev_step_name = data[prev_number_step][0] 
        if next_number_step < len(steps):
            next_step_name = data[next_number_step][0]
        else:
            next_step_name = data[next_number_step-1][0]

    # transfer dataset to page "index.html"
    return render(request, "index.html", context={"click": click, "user_name": user_name, "user_id": user_id, "number_step": number_step, "last_step": len(steps)-1,\
        "prev_number_step": prev_number_step, "next_number_step": next_number_step,\
        "cours_name": COURS_NAME, "step_name": step_name, "prev_step_name": prev_step_name, "next_step_name": next_step_name,\
        "questions": data[number_step][1], "answers": answers})

def admin_page(request):
    '''
    The function to process queries of "admin_page.html" page
    '''  
    if request.method == 'POST':
        # retrieve data from "admin_page.html"
        users = UsersModel.objects.all()
        user1_id =  int(request.POST.get("user1"))
        user2_id =  int(request.POST.get("user2"))
        user1 = UsersModel.objects.filter(id=user1_id)
        user2 = UsersModel.objects.filter(id=user2_id)
        user1 = user1[0]
        user2 = user2[0]
        # by the user id we get the corresponding object from the database
        answer_user1 = AnswersModel.objects.filter(user_id_id=user1.id)
        answer_user2 = AnswersModel.objects.filter(user_id_id=user2.id)
        questions = QuestionsModel.objects.all()
        grade = GradesModel.objects.all()

        # transfer dataset to page "admin_page.html"
        return render(request, "admin_page.html", context={"cours_name": COURS_NAME, "users": users, "user1": user1, "user2" :user2,\
         "answer_user1": answer_user1, "answer_user2": answer_user2, "questions": questions, "grade": grade})