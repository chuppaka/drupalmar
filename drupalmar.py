from urllib.request import urlopen, Request
from  urllib.error import HTTPError, URLError

#test best practices for DRUPAL :

#list of directory 
test = ['install.php', 'README.txt','LICENSE.txt','CHANGELOG.txt','authorize.php']
print('''
_____  _____  _    _ _____        _      __  __           
|  __ \|  __ \| |  | |  __ \ /\   | |    |  \/  |   /\   |  __ \      
| |  | | |__) | |  | | |__) /  \  | |    | \  / |  /  \  | |__) |
| |  | |  _  /| |  | |  ___/ /\ \ | |    | |\/| | / /\ \ |  _  /
| |__| | | \ \| |__| | |  / ____ \| |____| |  | |/ ____ \| | \ \          
|_____/|_|  \_\\____/|_| /_/    \_\______|_|  |_/_/    \_\_|  \_\

''')


dmn = str(input("Please enter url"))

try:
    for LinkT in test:
        Link= dmn + LinkT
        try:
            req = Request(Link, headers={'User-Agent': 'Mozilla/7.0'})
            try:
                html = urlopen(req)
            except HTTPError as e:
                print("\n",e," for url : ",Link)
        
            except URLError as e:
                print("\n",e," for url : ",Link)
        
            else:
                print("\n access possible to this url : ",Link)

                if LinkT == 'user' :
                    print (" kindly change name of this admin page  !")
            
                if LinkT == 'install.php' :
                    print ("Please restrict access to this page or hide it!")

                if LinkT == 'README.txt' :
                    print ("Please hide this file or change filename!")

                if LinkT == 'LICENSE.txt' :
                    print ("Please hide this file or change filename!")

                if LinkT == 'CHANGELOG.txt' :
                    print ("Please hide this file, restrict acces to this page or change filename!!")

                if LinkT == 'authorize.php' :
                    print ("restrict access to this page!")
                    

        except ValueError:
           print("\nError while the url")
           break
        except KeyboardInterrupt:
           break

except Exception:
   print ("\n")
   

str(input("\nPress any key to exit the program... "))
