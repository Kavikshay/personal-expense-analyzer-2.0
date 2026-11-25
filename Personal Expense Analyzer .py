import csv
import os
from pathlib import Path
import json
def to_json():
    try:
        new=[]
        json_file=Path(input('enter json file name:'))
        with open('Personal Expense data.csv','r',newline='',encoding='utf-8')as file:
            read=csv.DictReader(file,restval='N/A',restkey='extra')
            for i in read:
                new.append({'date':i["date"],
                            "month":i['month'],
                            'year':i['year'],
                            'name':i['name'],
                            'description':i['description'],
                            'amount':int(i['amount'])}
                            )
        if json_file.exists()==False:
            print('file dont exist')
        else:
            with open(json_file,'w')as file:
                json.dump(new,file,indent=4)
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
        print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
    except json.JSONDecodeError:
        print('JSON file contains invalid JSON')
    
def get_json():
    try:
        get=Path(input('enter json file to get data form it:'))
        data=[]
        if get.exists()==False:
            print('file dont exists')
        else:
            with open(get,'r')as file:
                data.extend(json.load(file))
                if os.path.getsize(get)==0:
                    print('data is empty')
                else:        
                    with open('Personal Expense data.csv','a',newline='',encoding='utf-8')as file:
                        writer = csv.DictWriter(file, fieldnames=data[0].keys())
                        if os.path.getsize("Personal Expense data.csv") == 0:
                            writer.writeheader()
                            writer.writerows(data)
                        else:
                            writer.writerows(data)
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
        print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
    except json.JSONDecodeError:
        print('JSON file contains invalid JSON')
        

def top():
    try:
        if os.path.getsize("Personal Expense data.csv") == 0:
            print("file is empty fist enter data to see ")
        else:
            item={}
            with open('Personal Expense data.csv','r',newline='',encoding='utf-8')as file:
                reader=csv.DictReader(file,restval='N/a',restkey='extra')
                for an in reader:
                    if an['name'] in item:
                        item[an['name']]+=int(an['amount'])
                    else:
                        item[an['name']]=int(an['amount'])
                sorted_data = sorted(item.items(), key=lambda x: x[1], reverse=True)
                count=1
                for i,j in sorted_data[:5]:
                    print(count,'.',i,';',j)
                    count+=1
                print('\n are the top 5 expense')
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
        print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
    
def report():
    try:
        if os.path.getsize("Personal Expense data.csv") == 0:
            print("file is empty fist enter data to see ")
        else:
            year=int(input('enter year:'))
            month=input('enter month:')
            months = {
                    "01": "January",
                    "02": "February",
                    "03": "March",
                    "04": "April",
                    "05": "May",
                    "06": "June",
                    "07": "July",
                    "08": "August",
                    "09": "September",
                    "10": "October",
                    "11": "November",
                    "12": "December"
                    }
            if int(month)==0 or int(month)>=13:
                print("print month can't me zero or more then 13")
            else:
                total=0
                count=0
                with open('Personal Expense data.csv','r',newline='',encoding='utf-8')as file:
                    reader=csv.DictReader(file,restval='N/a',restkey='extra')
                    for i in reader:
                        if year==int(i['year']) and int(month)==int(i['month']):
                            total+=int(i['amount'])
                            count+=1
                    month_name = months.get(month, "Invalid month")
                    print('----------Generate Monthly Expense Report----------')
                    print('month:',month_name,year)
                    print('Total expenses:','₹',total)
                    print('Total transactions:',count)
                    ex=input('\n do you waht to export in new csv file(yes/no):')
                    if ex.lower()=='yes':
                        p=Path(input('enter new csv file name:'))
                        if p.exists():
                            with open(p,'a',newline='',encoding='utf-8')as file:
                                writer=csv.DictWriter(file,fieldnames=['month','year','total_expenses','total_transactions'],extrasaction='ignore')
                                if os.path.getsize("Personal Expense data.csv") == 0:
                                    writer.writeheader()
                                    writer.writerow({'month': month_name,'year': year,'total_expenses': total,'total_transactions': count})
                                else:
                                    writer.writerow({'month': month_name,'year': year,'total_expenses': total,'total_transactions': count})
                                print('data is exported in your csv file')
                        else:
                            print('file not exists')


    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
            print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
        
def largest():
    try:
        if os.path.getsize("Personal Expense data.csv") == 0:
            print("file is empty fist enter data to see ")
        else:
            with open('Personal Expense data.csv','r',newline='',encoding='utf-8')as file:
                reader=csv.DictReader(file,restval='N/a',restkey='extra')
                larg_name=None
                larg_amount=0
                for l in reader:
                    if int(l['amount']) > larg_amount:
                        larg_amount=int(l['amount'])
                        larg_name=l['name']
                print('\nlargest amount:',larg_amount)
                print('item name:',larg_name)
                print()
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")

def search():
    try:
        if os.path.getsize("Personal Expense data.csv") == 0:
            print("file is empty fist enter data to see ")
        else:
            print('1.search by date\n2.search by month\n3.search by year')
            find=int(input('enter your choice:'))
            with open('Personal Expense data.csv','r',newline='',encoding='utf-8')as file:
                reader=csv.DictReader(file,restval='N/a',restkey='extra')
                if find==3:
                    amount=0
                    found=False
                    y=int(input('enter year to find it:'))
                    for f in reader:
                        if int(f['year'])==y:
                            print('item name:',f['name'])
                            print('item description:',f['description'])
                            print('item amount:',f["amount"])
                            amount+=int(f['amount'])
                            found=True
                    print('tota amount spend this year:',amount)
                    if found == False:
                        print('noting is found')
                if find==2:
                    found=False
                    m=int(input('enter month to find:'))
                    if m==0 or m>=13:
                        print("print month can't me zero or more then 13")
                    else:
                        amount=0
                        for f in reader:
                            if int(f['month'])==m:
                                print('item name:',f['name'])
                                print('item description:',f['description'])
                                print('item amount:',f["amount"])
                                amount+=int(f['amount'])
                                found=True
                        print('total amount sepend this month:',amount)
                        if found==False:
                            print("noting found ")
                if find==1:
                    found=False
                    d=int(input('enter date:'))
                    if d == 0 or d >=32:
                        print("date cant be zero or cant be more then 31")
                    else:
                        amount=0
                        for f in reader:
                            if int(f['date'])==d:
                                print('item name:',f['name'])
                                print('item description:',f['description'])
                                print('item amount:',f["amount"])
                                amount+=int(f['amount'])
                                found=True
                        if found==False:
                            print('nothing found')
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
            print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
        
def analysiser():
    try:
        if os.path.getsize("Personal Expense data.csv") == 0:
            print("file is empty fist enter data to see ")
        else:
            item={}
            total=0
            with open('Personal Expense data.csv','r',newline='',encoding='utf-8')as file:
                reader=csv.DictReader(file,restval='N/a',restkey='extra')
                for an in reader:
                    if an['name'] in item:
                        item[an['name']]+=int(an['amount'])
                    else:
                        item[an['name']]=int(an['amount'])
                    total+=int(an['amount'])
                for v,a in item.items():
                    print(v,':',a)
                print("\ntoatal amount spend:",total)
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
            print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
        
def view():
    try:
        if os.path.getsize("Personal Expense data.csv") == 0:
            print("file is empty fist enter data to see ")
        else:
            with open('Personal Expense data.csv','r',newline='',encoding='utf-8')as file:
                reader=csv.reader(file)
                print()
                for i in reader:
                    print(i)
                print("\n data is printed \n")
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
        print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
        
def add():
    try:
        date=int(input("enter date:"))
        if date <= 0 or date >=32:
            print("date cant be zero or cant be more then 31")
        else:
            month=int(input("enter month:"))
            if month<=0 or month>=13:
                print("print month can't me zero or more then 13")
            else:
                year=int(input("enter year:"))
                name=input('enter item name:')
                description=input('enter item description:')
                amount=int(input('enter item anount:'))
                with open('Personal Expense data.csv','a',newline='',encoding='utf-8')as file:
                    writer=csv.DictWriter(file,fieldnames=["date",'month','year','name','description','amount'],extrasaction='ignore')
                    if os.path.getsize("Personal Expense data.csv") == 0:
                        writer.writeheader()
                        writer.writerow({'date':date,"month":month,'year':year,'name':name,'description':description,'amount':str(amount)})
                    else:
                        writer.writerow({'date':date,"month":month,'year':year,'name':name,'description':description,'amount':str(amount)})
            ask=input('do you want to enter another data(yes/no):')
            if ask.lower()=='yes':
                add()
            elif ask.lower()=='no':
                return
            else:
                print('invalid choice enter')
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except FileNotFoundError:
        print("Expense file not found! Please add an expense first.")
    except PermissionError:
        print("Permission denied! Close the CSV file if it is open in another program.")
    except OSError:
        print("An error occurred while accessing the file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except KeyError:
        print("Required column 'amount' is missing from the CSV file.")
    except csv.Error:
        print("Unable to read the CSV file. Please check its format.")
        
def mane():
    try:
        while True:
            print("========== PERSONAL EXPENSE ANALYZER ==========")
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Category-wise Expense Analysis")
            print("4. Search Expenses by Date Range")
            print("5. Find Highest Expense")
            print("6. Generate Monthly Expense Report")
            print("7. Display Top 5 Expenses")
            print("8. add CSV file data to JSON file data")
            print('9. get data form JSON file and add the data into CSV file')
            print("10. Exit")
            print("===============================================")
            chice=int(input("Enter your choice:"))
            if chice ==10:
                break
            elif chice ==1:
                add()
            elif chice ==2:
                view()
            elif chice==3:
                analysiser()
            elif chice==4:
                search()
            elif chice==5:
                largest()
            elif chice==6:
                report()
            elif chice==7:
                top()
            elif chice==8:
                to_json()
            elif chice==9:
                get_json()
            else:
                print('invalid choice')
    except ValueError:
        print("Invalid input! Please enter a valid number.")

        

mane()       