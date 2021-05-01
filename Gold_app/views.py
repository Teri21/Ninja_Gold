from django.shortcuts import render, redirect
import random
from datetime import datetime


GOLD_MAP = {
    "farm": (10, 20),
    "cave": (5, 10),
    "house": (2, 5),
    "casino": (0, 50)
}


def index(request):

    if "Gold" not in request.session or "Activities" not in request.session:

        request.session['Gold'] = 0
        request.session['Activities'] = []
    return render(request, 'index.html')


def reset(request):
    request.session.clear()
    return redirect('/')


def process_Gold(request):
    if request.method == 'GET':
        return redirect('/')

    building_name = request.POST['building']

    building = GOLD_MAP[building_name]

    building_name_upper = building_name[0].upper() + building_name[1:]

    curr_gold = random.randint(building[0], building[1])

    now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")

    result = 'earn'

    message = f"Earned {curr_gold} from the {building_name_upper}! ({now_formatted})"

    if building_name == 'casino':

        if random.randint(0, 1) > 0:

            message = f"Entered a {building_name_upper} and lost {curr_gold} golds... Ouch... ({now_formatted})"

            curr_gold = curr_gold * -1
            result = 'lose'

    request.session['Gold'] += curr_gold

    request.session['Activities'].append(
        {"message": message, "result": result})
    return redirect('/')
