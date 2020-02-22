import os
import csv
#import us_states as us_states

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employee_csv = os.path.join("Resources", "employee_data.csv")
employee_dictionary = {
    "Emp_ID": [],
    "First Name": [],
    "Last Name": [],
    "DOB": [],
    "SSN": [],
    "State": []
}
firstnames = []
lastnames = []
names = []
states = []
short = []
first3 = []

#def statesconvert(state):
    #for x in range(len(us_state_abbrev)):
        #f"{us_state_abbrev[states[x]]}"


blinkout = "xxx-xx-"

with open(employee_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        employee_dictionary["Emp_ID"].append(row[0])
        #names.append(row[1].split(" "))[0]
        #for x in range(len(names)):
        employee_dictionary["First Name"].append(row[1].split(" ")[0])
        employee_dictionary["Last Name"].append(row[1].split(" ")[1])
        year = row[2].split("-")[0]
        month = row[2].split("-")[1]
        date = row[2].split("-")[2]
        employee_dictionary["DOB"].append(f"{month}/{date}/{year}")
        last4 = row[3].split("-")[2]
        employee_dictionary["SSN"].append(f"{blinkout}{last4}")
        #states.append(row[4])
    #for y in range(len(states)):
        employee_dictionary["State"].append(f"{us_state_abbrev[row[4]]}")

#print(employee_dictionary["SSN"][2])
#firnum = employee_dictionary["SSN"][2][0]
#firnum = str(firnum)
#firnum = "x"
#print(firnum)
#print(employee_dictionary["SSN"][2][1])
#print(employee_dictionary["SSN"][2][2])
#print(employee_dictionary["SSN"][2][4])
#print(employee_dictionary["SSN"][2][5])



#for x in range(len(employee_dictionary["First Name"])):
    #firstnames.append(employee_dictionary["First Name"][x])
    #lastnames.append(employee_dictionary["Last Name"][x])

#print(len(states))
#print(us_state_abbrev["Ohio"])

#for y in range(len(states)):
    #short.append(f"{us_state_abbrev[states[y]]}")
    #print(f"{us_state_abbrev[states[y]]}")
clean_csv = zip(employee_dictionary["Emp_ID"], employee_dictionary["First Name"], employee_dictionary["Last Name"], employee_dictionary["DOB"], employee_dictionary["SSN"], employee_dictionary["State"])

#print(len(employee_dictionary["SSN"]))
#for i in range(len(employee_dictionary["SSN"])):
    #first3.append(employee_dictionary["SSN"])


#print(us_states)

output_csv = os.path.join("bossoutput.csv")
with open(output_csv, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerows(firstnames)
    #csvwriter.writerows(lastnames)
    #csvwriter.writerows(first3)
    csvwriter.writerow(["Emp_ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    csvwriter.writerows(clean_csv)












