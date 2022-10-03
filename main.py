'''
todo:
add kwargs to enable quick-adding a doink with params
auto-add time and date
create charts to view usage over days, weeks, months, what have you
'''

from dbHandler import Handler

OPTIONS = '''\
    1. add doink\n\
    2. clear person\n\
    3. view total doinks\n\
    4. add new person\n\
    5. quit'''
INPUT_SYMBOL = "--> "

# database
FILE_NAME = "db.json"

def add_doink(store_func):

    person= ""
    smokes=0.0
    weed=0.0

    print("How many smokes?")
    try: smokes = float(input(INPUT_SYMBOL))
    except: raise Exception("Please specify an integer or a floating-point number (seperated by a .)")
    
    print("How much weed?")
    try: weed = float(input(INPUT_SYMBOL))
    except: raise Exception("Please specify an integer or a floating-point number (seperated by a .)")
    
    print("Who smoked?")
    try: person = input(INPUT_SYMBOL).lower()
    except: raise Exception(f"Unknown person")

    while True:
        print(f"\n----- Doink -----\n{smokes} smokes\n{weed}g weed\n")
        print(f"Are you sure you want to add this to {person}? (y/n)")
        ans = input(INPUT_SYMBOL)
        if ans == "y": break
        elif ans == "n": 
            print("Disregarding doink...")
            return
        else: 
            print(f"[ERROR] '{ans}' is not a valid option")
            continue
    ## CALLBACK
    store_func(person, smokes, weed)
    
def view_total(view_func):
    print("Which person?")
    ans = input(INPUT_SYMBOL)
    view_func(ans)

def clear_doinks(clear_func):
    print("aight who payed up?")
    person = input(INPUT_SYMBOL).lower()
    clear_func(person)

def add_user(add_user_func):
    print("Name of the person to add?")
    userToAdd = input(INPUT_SYMBOL).lower()
    
    add_user_func(userToAdd)

def main():
    handler = Handler(FILE_NAME)
    while True:
        print("\n"+OPTIONS)
        ans = input(INPUT_SYMBOL)

        try:
            if ans == "1": add_doink(handler.saveDoink)
            elif ans=="2": clear_doinks(handler.clearDoinks)
            elif ans=="3": view_total(handler.viewDoinks)
            elif ans=="4": add_user(handler.addPerson)
            elif ans=="5" or ans=="q": exit()
            else: print(f"\n[ERROR] '{ans}' is not a valid option.")
        except Exception as e: print(f"\n[ERROR] {e}")

if __name__=="__main__": main()