PHONE_DIRECTORY = {}  # directing phone number to phone object
class Phone:
    def __init__(self, number, name):
        self.name = name
        self.number = number
        self.contacts = {}
        self.call_history = []
        self.is_calling = False
        self.is_receiving = False
        self.is_in_call=False
        self.call_start_time=0
        self.current_peer = None
        PHONE_DIRECTORY[self.number]=self
        print(f"Created phone for {self.name} ({self.number}).")

    def is_busy(self):
        return self . is_calling or self . is_receiving or self . is_in_call
    
    def add_contact(self,number,name):
        print ( f" Running add_contact ({ number } , { name }) ... " )
        if number==self.number:
            print(f"Your error message {self.name} adding {name} --> [ITS OWNER'S NUMBER!]")
        elif number not in PHONE_DIRECTORY:
            print(f"Your error message {self.name} adding {name} --> [PHONE DOES NOT EXIST!]")
        elif self.contacts.get(number) == name:
            print(f"Your error message {self.name} adding {name} --> [CONTACT ALREADY EXIST!]")
        elif number in self.contacts:
            print(f"Your error message {self.name} adding {name} --> [NUMBER IS ALREADY SAVED WITH SOME OTHER NAME!]")
        elif name in self.contacts.values():
            print(f"Your error message {self.name} adding {name} --> [NAME ALREADY EXIST IN YOUR CONTACT WITH OTHER NUMBER!]")
        else:
            self.contacts[number] = name
            print(f"Your success message {self.name} adding {name} --> ")
        
    def get_contact_name(self,number):
        return self . contacts . get ( number , f" Unknown ({ number }) " )

    def update_contact(self,number,new_name):
        print ( f" Running update_contact ({ number } , { new_name }) ... " )
        if self.contacts.get(number) == new_name:
            print(f"Your error message {self.name} updating {number} --> [CONTACT ALREADY EXIST!]")
        elif number in self.contacts:
            self.contacts[number] = new_name
            print(f"Your success message {self.name} updating ({number}, {new_name})")
        else:
            print(f"Your error message {self.name} updating {number} --> [NUMBER {number} DOES NOT EXIST!]")
    
    def delete_contact(self,number):
        print ( f" Running delete_contact ({ number }) ... " )
        if number in self.contacts:
            print(f" Your success message {self.name} deleting_contact ({ number })")
            self.contacts.pop(number)
        else:
            print(f" Your error message {self.name} deleting_contact ({ number }) --> [THIS NUMBER {number} DOES NOT EXIST!]")
    
    def search_by_number(self,number):
        print ( f" Searching by number : { number }... " )
        if number in self.contacts:
            print(f"Your success message {self.name} searching {number}-->CONTACT'S NAME: {self.contacts[number]}")
        else:
            print(f"Your error message {self.name} searching {number}-->[THIS NUMBER {number} DOES NOT EXIST!]")

    def search_by_name(self,query):
        print ( f" Searching by name : { query }... " )
        item_lst = self.contacts.items()
        my_list = []
        for i in item_lst:
            if query.lower() in i[1].lower():
                my_list.append(i)
        if len(my_list) == 0:
            print(f"Your error message {self.name} searching {query} -->[{query} DOES NOT MATCH IN YOUR CALL LOG!]")
        elif len(my_list) == 1:
            print(f"CONTACT'S NAME: {my_list[0][1]} NUMBER:{my_list[0][0]}")
        else:
            print(f"Your many contact's name have {query}")
            for i in my_list:
                print(f"CONTACT'S NAME: {i[1]} NUMBER:{i[0]}")

    def search_by_keyword(self,query):
        print ( f" Searching by keyword : { query }... " )
        item_lst = self.contacts.items()
        my_list = []
        for i in item_lst:
            flag = True
            for j in query:
                if j.lower() not in i[1].lower():
                    flag = False
            if flag:
                my_list.append(i)
        if len(my_list) == 0:
            print(f"Your error message {self.name} searching {query} -->[THIS TOKEN {query} DOES NOT MATCH!]")
        elif len(my_list) == 1:
            print(f"CONTACT'S NAME: {my_list[0][1]} NUMBER:{my_list[0][0]}")
        else:
            print(f"Your many contact's name have {query}")
            for i in my_list:
                print(f"CONTACT'S NAME: {i[1]} NUMBER:{i[0]}")

    def show_status(self):
        if not self.current_peer:
            print(f"Status for {self.name}: No active call.")
            return
        num=self.current_peer.number
        name=self.contacts.get(num)
        if self.is_calling and not self.is_in_call:
            print(f"Status for {self.name}: Calling {name}...")
        elif self.is_receiving and not self.is_in_call:
            print(f"Status for {self.name}:Incoming call from {name} ({num})")
        elif self.is_in_call:
            print(f"Status for {self.name}:In call with {num}")
        else:
            print(f"Status for {self.name}:NO ACTIVE CALL!")
            print ( f" Status for { self . name }: Idle " )

    def place_call(self, receiver_number,timestamp):
        print ( f"{ self . name } is attempting to call { receiver_number }... ")
        receiver=PHONE_DIRECTORY[receiver_number]
        if(self.is_busy()):
            print(f"{self.name} is busy...")
            return
        if(receiver.is_busy()):
            print(f"{receiver.name} is busy...")
            return
        self.is_calling=True
        self.current_peer=receiver
        receiver.receive_call(self)
        self.call_start_time=timestamp
        self.show_status()

    def receive_call(self,caller_object):
        print ( f"{ self . name } is receiving a call from { caller_object . name }... ")
        self.is_receiving=True
        self.current_peer=caller_object
        self.show_status()

    def accept_call(self,timestamp):
        if(self.is_receiving):
            print ( f"{ self . name } accepted the call .")
            self.is_receiving=False
            self.is_in_call=True
            self.current_peer.is_calling=False
            self.current_peer.is_in_call=True
            self.call_start_time=timestamp
            self . current_peer . call_start_time = self . call_start_time
            self.show_status()

    def end_call(self,timestamp):
        peer=self.current_peer
        if(peer==None):
            print(f"{self.name} has no active call to end!")
            return
        phone1_call_type=None#self
        phone2_call_type=None
        if(self.is_in_call):
            phone1_call_type="dialled"
            phone2_call_type="received"
        if(self.is_receiving):
            phone1_call_type="missed"
            phone2_call_type="rejected"
        if(self.is_calling):
            phone1_call_type="dialled"
            phone2_call_type="missed"
        self._add_to_history(peer,self.call_start_time,timestamp,phone1_call_type)
        peer._add_to_history(self,peer.call_start_time,timestamp,phone2_call_type)
        self.current_peer=None
        peer.current_peer=None
        self.is_in_call=False
        peer.is_in_call=False
        print ( f"{ self . name } is ending the call activity .")

    def _add_to_history(self,peer,start_time,end_time,call_type):
        log = {
        "peer_name": peer.name,
        "peer_number": peer.number,
        "start_time": start_time,
        "end_time": end_time,
        "duration": end_time - start_time,
        "type": call_type
        }
        self.call_history.append(log)
    def print_analysis(self):
        print ( f" \n - - - Call Analysis for { self . name } ({ self . number }) ---" )
        unique=set()
        for i in self.call_history:
            if i["type"]=='dialled':
                unique.add(i["peer_number"])
        print(f"Unique Calls Made(DIALLED):{len(unique)}")
        lst=[]
        for i in self.call_history:
            if(i["type"]=="dialled" or i["type"]=="received") and i["duration"]>0:
                lst.append(i["duration"])
        avg = (sum(lst)/len(lst)) if lst else 0
        print(f"Average Call Duration: {avg:.2f}s")
        dict={}
        m=0
        for i in self.call_history:
            count=0
            for j in self.call_history:
                if i["peer_number"]==j["peer_number"] and j["type"]=="dialled":
                    count+=1
            if(count==m and m!=0):
                dict[i["peer_number"]]=count
            if(count>m):
                dict.clear()
                dict[i["peer_number"]]=count
        print("Most Frequently Called(DIALLED) Number(s):",dict)
def run_simulation(filename):
    print("---Starting Phone Simulation---")
    with open(filename, "r") as f:
        for line in f:
            line=line.strip()
            if(not line or line.startswith("#")):
                continue
            parts=line.split()
            command=parts[0]
            try:
                if command=="CREATE_PHONE":
                    if(parts[2] not in PHONE_DIRECTORY):
                        ob=Phone(parts[2],parts[1])
                        PHONE_DIRECTORY[parts[2]]=ob
                    else:
                        print("Phone already exists!")
                elif command=="ADD_CONTACT":
                    owner_phone=PHONE_DIRECTORY.get(parts[1])
                    if(owner_phone!=None):
                        owner_phone.add_contact(parts[3],parts[2])
                    else:
                        print("Owner Phone does not exist")
                elif command=="CALL":
                    caller=PHONE_DIRECTORY.get(parts[1])
                    receiver=PHONE_DIRECTORY.get(parts[2])
                    if(caller!=None and receiver!=None):
                        if caller.is_busy() or receiver.is_busy():
                            print("Device is busy!")
                        else:
                            caller.place_call(receiver.number,int(parts[3]))
                elif command=="ACCEPT":
                    receiver=PHONE_DIRECTORY.get(parts[1])
                    if(receiver!=None):
                        receiver.accept_call(int(parts[2]))
                    else:
                        print("Wrong phone number!")
                elif command=="END":
                    phone=PHONE_DIRECTORY.get(parts[1])
                    if(phone!=None):
                        phone.end_call(int(parts[2]))
                    else:
                        print("Wrong phone number!")
                elif command =="CONTACT_NAME":
                    phone=PHONE_DIRECTORY.get(parts[1])
                    if(phone!=None):
                        phone.get_contact_name(parts[2])
                    else:
                        print("Wrong phone number!")
                elif command =="UPDATE_CONTACT":
                    phone=PHONE_DIRECTORY.get(parts[1])
                    if(phone!=None):
                        phone.update_contact(parts[2],parts[3])
                    else:
                        print("Wrong phone number!")
                elif command =="DELETE_CONTACT":
                    phone=PHONE_DIRECTORY.get(parts[1])
                    if(phone!=None):
                        phone.delete_contact(parts[2])
                    else:
                        print("Wrong phone number!")
                elif command =="SEARCH_BY_NUMBER":
                    phone=PHONE_DIRECTORY.get(parts[1])
                    if(phone!=None):
                        phone.search_by_number(parts[2])
                    else:
                        print("Wrong phone number!")
                elif command =="SEARCH_BY_NAME":
                    phone=PHONE_DIRECTORY.get(parts[1])
                    if(phone!=None):
                        phone.search_by_name(parts[2])
                    else:
                        print("Wrong phone number!")
                elif command =="SEARCH_BY_KEYWORD":
                    phone=PHONE_DIRECTORY.get(parts[1])
                    lst=[parts[x].lower() for x in range(2,len(parts))]
                    if(phone!=None):
                        phone.search_by_keyword(lst)
                    else:
                        print("Wrong phone number!")
            except Exception as e:
                print(f"ERROR processing line {line} : {e}")
    print("\n--- Simulation Finished ---")
    for phone in PHONE_DIRECTORY.values():
        phone.print_analysis()
run_simulation("COMMAND.txt")
