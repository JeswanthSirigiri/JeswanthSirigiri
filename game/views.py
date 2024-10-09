# # from django.http import request
# # from django.shortcuts import render
# # import random
# # def home(request):
# #     return render(request,'display.html')
# #
# #
# # def is_win(player, opponent):
# #     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
# #             player == 'p' and opponent == 'r'):
# #         return True
# #
# #
# # def score_card(request):
# #     user = 0
# #     comp = 0
# #     for i in range(3):
# #         n1 = (request.POST["txtno1"])
# #         n2 = random.choice(['r', 'p', 's'])
# #         if n1 == n2:
# #             res = 'It\'s a tie'
# #         elif is_win(n1, n2):
# #             res = 'You won!'
# #             user += 1
# #         else:
# #             res = 'You lost!'
# #             comp += 1
# #     if user>=2:
# #         overall_winner = "You won the series"
# #     elif comp>=2:
# #         overall_winner = "Computer won the series!"
# #     else:
# #         overall_winner = "It's a tie series!"
# #     return render(request, 'display.html', {'N1': n1, 'N2': n2, 'res': res, 'total':overall_winner,'score':user,"i":i})
from django.shortcuts import render
import random

def home(request):
    return render(request,'display.html')


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


def score_card(request):
        l2=[]
        user=0
        comp=0
        n1 = (request.POST["txtno1"])
        n3=(request.POST["txtno3"])
        n4=(request.POST["txtno4"])
        l=[n1,n3,n4]
        for i in l:
            n2 = random.choice(['r', 'p', 's'])
            l2.append(n2)
            if i == n2 :
                #res = 'It\'s a tie'
                comp = comp
                user = user
            elif is_win(i, n2):
                #res = 'You won!'
                user =+1
            else:
                #res = 'You lost!'
                comp=+1
        n2,n5,n6=l2
        print(comp,user)
        if user > comp :
            res = "you won"
        elif comp > user:
            res = "you lost!"
        else:
            res = "tie"
        return render(request, 'display.html', {'N1': n1,'N3':n3,'N4':n4,'N2': n2,"N5":n5,"N6":n6,'res': res})
