#import libraries
import random
import string
from datetime import datetime

#DVLA programme to check and generate license plate

#define my CONSTANTS
CURRENT_YEAR = int(str(datetime.now().year)[-2:])
SEP2FEB_ADD_ON = 50
REQ_CHARS = 7
INVALID_LETTERS = "QIZ"
VALID_FIRST_LETTERS = 'ABCDEFGHKLMNOPRSVWY'
INVALID_FIRST_LETTERS = "QIZJUTX"
INVALID_FINAL_LETTERS = "QIZ"
REGIONS = ["Anglia", "Birmingham", "Cymru(Wales)", "Deeside", "Essex", "Forest & Fens", "Garden of England", "Hampshire & Dorset",
          "No official mnemonic", "London", "Manchester", "North", "Oxford", "Preston", "Reading", "Scotland", "Severn Valley", 
          "West of England", "Yorkshire"]
LIST_OF_DVLA_OFFICES = [["Anglia", "Peterborough", "ABCDEFGHIJKLMN"],
                        ["Anglia", "Norwich", "OPRSTU"],
                        ["Anglia", "Ipswich", "VWXY"],
                        ["Birmingham", "Birmingham", "ABCDEFGHJKLMNOPRSTUVWXY"],
                        ["Cymru(Wales)", "Cardiff", "ABCDEFGHJKLMNO"],
                        ["Cymru(Wales)", "Swansea", "PRSTUV"],
                        ["Cymru(Wales)", "Bangor", "WXY"],
                        ["Deeside", "Chester", "ABCDEFGHJK"],
                        ["Deeside", "Shrewsbury", "LMNOPRSTUVWXY"],
                        ["Essex", "Chelmsford", "ABCDEFGHJKLMNOPRSTUVWXY"],
                        ["Forest & Fens", "Nottingham", "ABCDEFGHJKLMNOP"],
                        ["Forest & Fens", "Lincoln", "RSTUVWXY"],
                        ["Garden of England", "Maidstone", "ABCDEFGHJKLMNO"],
                        ["Garden of England", "Brighton", "PRSTUVWXY"],
                        ["Hampshire & Dorset", "Bournemouth", "ABCDEFGHJ"],
                        ["Hampshire & Dorset", "Pourtsmouth", "KLMNOPRSTUVXY"],
                        ["Hampshire & Dorset", "Portsmouth(Isle of Wight)", "W"],
                        ["No official mnenonmic", "Luton", "ABCDEFGHJKL"],
                        ["No official mnemonic", "Northampton", "MOPRSTUVWXY"],
                        ["London", "Wimbledon", "ABCDEFGHJ"],
                        ["London", "Stanmore", "KLMNOPRST"],
                        ["London", "Sidcup", "UVWXY"],
                        ["Manchester", "Manchester", "ABCDEFGHJKLMNOPRSTUVWXY"],
                        ["North", "Newcastle", "ABCDEFGHJKLMNO"],
                        ["North", "Stockton", "PRSTUVWXY"],
                        ["Oxford", "Oxford", "ABCDEFGHJKLMNOPRSTUVWXY"],
                        ["Preston", "Preston", "ABCDEFGHJKLMNOPRST"],
                        ["Preston", "Carlisle", "UVRSTUVWXY"],
                        ["Reading", "Reading", "ABCDEFGHJKLMNOPRSTUVWXY"],
                        ["Scotland", "Glasgow", "ABCDEFGHJ"],
                        ["Scotland", "Edinburgh", "KLMNO"],
                        ["Scotland", "Dundee", "PRST"],
                        ["Scotland", "Aberdeen", "UVW"],
                        ["Scotland", "Inverness", "XY"],
                        ["Severn Valley", "Worcester", "ABCDEFGHJKLMNOPRSTUVWXY"],
                        ["West of England", "Exeter", "ABCDEFGHIJ"],
                        ["West of England", "Truro", "KL"],
                        ["West of England", "Bristol", "MNOPRSTUVWXY"],
                        ["Yorkshire", "Leeds", "ABCDEFGHJK"],
                        ["Yorkshire", "Sheffield", "LMNOPRSTU"],
                        ["Yorkshire", "Beverley", "VWXY"]]

test_cases = ["Ab 21bTr", "Ab21bTr", "", "AB", "       ", "JA 21 BTR", "!B 21 BTR", "AB26BTR", "AAB21BT", "AA99BTR", "1234567", 
"YA76YYY", "AA2.1TR", "AB02BTR", "AB01BTR", "AB52BTR", "AB51BTR", "AB76BTR", "AB77BTR", "IA21BTR", "QA21BTR", "ZA21BTR", 
"AQ21BTR", "AI21BTR", "AZ21BTR", "AB21BTQ", "AB21BIT", "AB21ZTR", "AB21BT1", "AB21BT@", "YV21BTR"]

region = ""

def automated_testing(f, s, t, f2, f3, s2, s3):
    f = chr(ord(f) + 1)
    return f + s + t + f2 + f3 + s2 + s3
    

#this function takes the string and strips out spaces
def strip_spaces(s):
    s = s.replace(" ", "")
    return s

#checks the final 3 letters are alpahbetical and not in the invalid letters
def valid_end(s):
    for char in s:
        if char in INVALID_LETTERS or not char.isalpha():
            return False
    #for loop ends
    return True

#finds the office amd region that the license plate was registered at
def find_region_office(region_code, second_letter):
    for i in range(len(LIST_OF_DVLA_OFFICES)):
        if LIST_OF_DVLA_OFFICES[i][0] == region_code:
            if second_letter in LIST_OF_DVLA_OFFICES[i][2]:
                return LIST_OF_DVLA_OFFICES[i][0], LIST_OF_DVLA_OFFICES[i][1]

        return "invalid", "invalid"

#generates first 2 letters of a valid license plate
def generate_valid_first2letters():
    random_office = random.choice(LIST_OF_DVLA_OFFICES) #picks a random line from the LIST_OF_DVLA_OFFICES
    random_second_letter = random.choice(random_office[2]) #chooses a second letter from that line
    return random_office[0][0] + random_second_letter

#generates 2 numbers for the generated license plate
def generate_valid2nums(year):
    sep_feb_value_random = random.randint(SEP2FEB_ADD_ON, year + SEP2FEB_ADD_ON)
    mar_aug_value_random = random.randint(1, year)
    value_choice = random.choice([sep_feb_value_random, mar_aug_value_random])
    return value_choice

#generates final 3 letters of the generated license plate
def generate_random_letters(disallowed_letters):
    
    allowed_letters = [char for char in string.ascii_uppercase if char not in disallowed_letters]
    
    return random.choice(allowed_letters) + random.choice(allowed_letters) + random.choice(allowed_letters)

def calc_license_year(i): #calculate the age of the license plate
    if i <= CURRENT_YEAR and i >= 2:
        year = i
        return year
    elif i >= SEP2FEB_ADD_ON and i <= CURRENT_YEAR + SEP2FEB_ADD_ON:
        year = i - SEP2FEB_ADD_ON
        return year

#print(generate_validfirst2letters()) #debug

#this module / code is for the Main Menu of the DVLA program

quit_choice = False

#main program
while not quit_choice:
    print("----------Choices----------")
    print("C)heck whether a given license plate is valid")
    print("G)enerate License plate")
    print("A)utomated testing")
    print("Q)uit")

    #get the users choice
    choice = input("Enter your choice here: ").upper()
    if choice == "Q":
        print("thanks for using this program, quitting program")
        quit_choice = True
    elif choice == "C":

        print("you have chosen to Check whether a given license plate is valid")

        user_license_plate = input("license plate: ")
        user_license_plate = strip_spaces(user_license_plate.upper())

        if len(user_license_plate) != 7:
            print("license plate must be 7 characters long")
        else:
            print("valid license plate length")
            if user_license_plate[0] not in VALID_FIRST_LETTERS or user_license_plate[1] in INVALID_LETTERS:
                print("invalid first 2 letters")

            else: #we get to here if the first 2 letters are valid
                print("valid first 2 letters")
                region = (REGIONS[VALID_FIRST_LETTERS.index(user_license_plate[0])])

                if user_license_plate[2:4].isdigit():
                    if calc_license_year(int(user_license_plate[2:4])) == None:
                        print("invalid license plate registration year")
                    else:
                        print("license plate registration year:", calc_license_year(int(user_license_plate[2:4]))+2000)

#slice out the last 3 character in the license plate
                        final_letters = user_license_plate[-3:]
                        if valid_end(final_letters):
                            print("valid final 3 letters for a license plate")
                            if len(user_license_plate) > 1:
                                region, office = find_region_office(region, user_license_plate[1])
                                print(f"region: {region}, office: {office}")
                        else:
                            print("invalid final 3 letters for a license plate")

    elif choice == "G":
        print("you have chosen to Generate License plate")

        print(f"randomly generated license plate: {generate_valid_first2letters()}{generate_valid2nums(CURRENT_YEAR)}{generate_random_letters(INVALID_FINAL_LETTERS)}")

    elif choice == "A":
        print("automated testing started(for developer)")
        file = open("DVLA_output.txt", "a")
        for i in test_cases:
            user_license_plate = i
            user_license_plate = strip_spaces(user_license_plate.upper())
            print(user_license_plate)
            file.write(user_license_plate + "\n")

            if len(user_license_plate) != 7:
                print("license plate must be 7 characters long")
                file.write("license plate must be 7 characters long" + "\n")
            else:
                print("valid license plate length")
                file.write("valid license plate length" + "\n")
                if user_license_plate[0] not in VALID_FIRST_LETTERS or user_license_plate[1] in INVALID_LETTERS:
                    print("invalid first 2 letters")
                    file.write("invalid first 2 letters" + "\n")

                else: #we get to here if the first 2 letters are valid
                    print("valid first 2 letters")
                    file.write("valid first 2 letters" + "\n")
                    region = (REGIONS[VALID_FIRST_LETTERS.index(user_license_plate[0])])

                    if user_license_plate[2:4].isdigit():
                        if calc_license_year(int(user_license_plate[2:4])) == None:
                            print("invalid license plate registration year")
                            file.write("invalid license plater registration year" + "\n")
                        else:
                            print("license plate registration year:", calc_license_year(int(user_license_plate[2:4]))+2000)
                            file.write("license plate registration year:", calc_license_year(int(user_license_plate[2:4]))+2000 + "\n")

#slice out the last 3 character in the license plate
                            final_letters = user_license_plate[-3:]
                            if valid_end(final_letters):
                                print("valid final 3 letters for a license plate")
                                file.write("valid final 3 letters for a license plate" + "\n")
                                if len(user_license_plate) > 1:
                                    region, office = find_region_office(region, user_license_plate[1])
                                    print(f"region: {region}, office: {office}")
                                    file.write(f"region: {region}, office: {office}" + "\n")
                            else:
                                print("invalid final 3 letters for a license plate")
                                file.write("invalid final 3 letters for a license plate" + "\n")
        file.close()


    else: #error message - wrong choice
        print("you have chosen an invalid option, try again")
    
    #when the user chooses the quit option set quit_choice to True and this will exit the while loop
#end
print("Thanks for using the DVLA license plate checker. Bye!")