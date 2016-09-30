import time
from ldap3 import Server, Connection, SEARCH_SCOPE_WHOLE_SUBTREE, MODIFY_ADD

s = Server('rzdunski.noip.me:389') #IP address of server where LDAP is listening on default port:389
c = Connection(s, user = 'cn=admin,dc=rzdunski,dc=me', password = 'admin')#this is used for simple autentication  to LDAP server with specified credentials
c.bind()

user = 'cn=test,dc=rzdunski,dc=me'#variable used for add operation request

add_num=int(input('Enter integer number of add operation(s):'))#user gives integer number of add operation request, the int is convertng string to integer type

search_num=int(input('\nEnter integer number of search operation(s):'))#user gives integer number of search operation request     

modify_num=int(input('\nEnter integer number of modify operation(s):'))#user gives integer number of modify operation request


"""below code performs add operation"""

tadd_before=time.time() #retrive current time before add operation, used for calculations of average time for add requets

for add_item in range(add_num): #loop which change the initial variable "user" used to add different entries to LDAP database
	new = user.split(',', 1)
	new[0]=new[0]+str(add_item)
	new_user=','.join(new)
	c.add(new_user, 'organizationalRole', {'cn': 'test-add-operation'}) #the line is adding as many records to LDAP database as user defined in variable "add_num"

tadd_after=time.time()#retrive current time after add operation

diff_add = round(tadd_after-tadd_before, 3)# calculate time of add operation

add_amount = add_item+1

average = round((add_amount/diff_add), 4)#returns average add operations per secound with resolution to four places after comma

print('\nTime to add',add_amount,'entries:',diff_add,'secounds. Average:',average,'add operations per secound.')#display messages


"""below code performs search operation"""

tsearch_before=time.time() #retrive current time before search operation, used for calculations of average time for search requets

for search_item in range(search_num):
        c.search(new[1],'(cn=test*)', SEARCH_SCOPE_WHOLE_SUBTREE, attributes = ['cn', 'objectClass'])#the line perfoms search operation filtered by "cn=test*" as many times as defined in variable "search_num" "add_num"

tsearch_after=time.time() #retrive current time after search operation

diff_search=round((tsearch_after-tsearch_before), 3)# calculate time of search operation

response=c.response #the line assign search results to "response" variable

aver_search=round((len(c.response)/diff_search), 4)# calcualte average of search operation

print('\nSearch time:', diff_search, '. Average:',aver_search,'search operation per secound.')#display message



"""below code performs modify operation"""

tmodify_before=time.time()#retrive current time before modify operation, used for calculations of average time for modify requets

for modify_item in range(modify_num):
        for r in response:
                c.modify(r['dn'], {'cn': (MODIFY_ADD, ['test-modify-operation'])})#the line perfoms modify operation by adding attribute "test-modify-operation" as many times as defined in variable "modify_num"

tmodify_after=time.time()#retrive current time after modify operation

diff_modify=round((tmodify_after-tmodify_before), 3)# calculate time of modify operation

aver_modify=round((len(response)/diff_modify), 4)# calcualte average of modify operation

print('\nModify time:', diff_modify, '. Average:',aver_modify,'modify operation per secound.\n')#display message




"""below code performs delete operation for all added entries"""

del_num = add_num

for del_item in range(del_num):
        new = user.split(',', 1)
        new[0]=new[0]+str(del_item)
        new_user=','.join(new)
        c.delete(new_user)

c.unbind()
