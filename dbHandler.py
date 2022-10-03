from datetime import datetime
import json
import os

from calculatorFunctions import calculate

READ_MODE = "r"
WRITE_MODE = "w"

SEPARATOR = "=" * 45

class Handler:
    def __getFileName__(self): return self.file_name
    def __check_file_exists__(self):
        if not os.path.isfile(self.file_name): 
            with open(self.file_name, "w") as f: f.write(json.dumps({}, indent=4, sort_keys=True))

    def __init__(self, file_path): 
        self.file_name = file_path
        self.__check_file_exists__()

    def saveDoink(self, person: str, smokes: float, weed: float):
        # Variable to hold object once decoded from json file
        db: object = ""

        ## READ AND DECODE CONTENTS OF FILE
        with open("db.json", READ_MODE) as f:
            ## READ
            file_content = f.read()
            if file_content == "" or file_content == None: raise Exception("Empty database")
            ## DECODE
            db = json.loads(file_content)

        ## CHECK IF PERSON EXISTS
        people = []
        for guy in db: people.append(guy)
        if person not in people: raise Exception(f"No person in database called {person}")

        # datetime object containing current date and time
        now = datetime.now()

        # dd/mm/YY H:M:S
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")

        with open("db.json", WRITE_MODE) as f:
            try:
                # Add new entry in person's list of sesh's
                db[person].append(
                    {
                        "date":str(date),
                        "time":str(time),
                        "smokes":float(smokes),
                        "weed":float(weed),
                    }
                )
            except Exception as e: print(f"Couldn't add new entry to list of objects\n{e}")

            ## ENCODE AND WRITE TO FILE
            try:
                ## ENCODE
                newobj = json.dumps(db, indent=4, sort_keys=True)
                ## WRITE
                f.write(newobj)
            except Exception as e: print(f"Couldn't save file\n{e}")
        print("Doink added!")

    def viewDoinks(self, person):
        with open("db.json", READ_MODE) as f:
            ## READ FILE
            obj = json.loads(f.read())

            ## CHECK IF PERSON EXISTS
            people = []
            for guy in obj: people.append(guy)
            if person not in people: raise Exception(f"No person in database called {person}")

            if len(obj[person]) == 0: raise Exception(f"{person} has no doinks saved")

            total_smokes = 0.0
            total_weed = 0.0          

            print(SEPARATOR)
            for sesh in obj[person]:
                print(f"\
{sesh['date']} {sesh['time']} /-/ \
Smokes: {sesh['smokes']} Weed: {sesh['weed']}")
                total_smokes += sesh['smokes']
                total_weed += sesh['weed']

            print(SEPARATOR)
            print(f"Total value: {calculate(total_smokes, total_weed)}")
            print(SEPARATOR)

    def clearDoinks(self, person):
        # Variable to hold decoded json object from file
        db: object 

        ## USER FINAL CONFIRMATION
        if input(f"Are you sure you want to clear {person}s history? ain no way back (Y/n)").lower() != "y": return

        ## READ AND DECODE
        with open("db.json", READ_MODE) as f:
            ## READ
            file_content = f.read()
            if file_content == "" or file_content == None: raise Exception("Empty database")
            ## DECODE
            db = json.loads(file_content)

        ## CHECK IF PERSON EXISTS
        people = []
        for guy in db: people.append(guy)
        if person not in people: raise Exception(f"Person '{person}' doesn't exist")

        cleared_doinks = db[person]
        db[person] = []

        ## WRITE TO FILE
        with open("db.json", WRITE_MODE) as f: 
            ## ENCODE
            newobj = json.dumps(db, indent=4, sort_keys=True)
            ## WRITE
            f.write(newobj)

        ##
        ## SAVE HISTORICAL DATA
        ##
        # variable to hold decoded json object from file
        data: object
        # check file exists and create one if it doesn't
        if not os.path.isfile("historical_data.json"): 
            with open("historical_data.json", "w") as f: f.write(json.dumps({}, indent=4, sort_keys=True))
        # read file and decode json
        with open("historical_data.json", READ_MODE) as f: data = json.loads(f.read())
        ## CHECK IF PERSON EXISTS
        people = []
        for guy in data: people.append(guy)
        if person not in people: data[person] = []
        # add cleared doinks from db
        data[person].append(cleared_doinks)
        # write to file
        with open("historical_data.json", WRITE_MODE) as f: 
            ## ENCODE
            newobj = json.dumps(data, indent=4, sort_keys=True)
            ## WRITE
            f.write(newobj)

        print(f"{person} has been cleared!")

    def addPerson(self, person):
        # Variable to hold object once decoded from json file
        db: object = ""

        ## READ AND DECODE CONTENTS OF FILE
        with open("db.json", READ_MODE) as f:
            ## READ
            file_content = f.read()
            if file_content == "" or file_content == None: raise Exception("Empty database")
            ## DECODE
            db = json.loads(file_content)

        ## CHECK IF PERSON EXISTS
        people = []
        for guy in db: people.append(guy)
        if person in people: raise Exception(f"Person '{person}' already exists")

        db[person] = []

        with open("db.json", WRITE_MODE) as f:
            db[person] = []

            ## ENCODE AND WRITE TO FILE
            try:
                ## ENCODE
                newobj = json.dumps(db, indent=4, sort_keys=True)
                ## WRITE
                f.write(newobj)
            except Exception as e: print(f"Couldn't save file\n{e}")
        print(f"{person} has been added!")


if __name__=="__main__": exit()