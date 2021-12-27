## CodeForces Problems Fetcher!
### Introduction
This is a python script that uses Selenium to help you
download your solutions of the problems you solved on CodeForces.

### What you need to  run the script
1. Firstly, You need to know your 
[chrome version](https://help.zenplanner.com/hc/en-us/articles/204253654-How-to-Find-Your-Internet-Browser-Version-Number-Google-Chrome)
2. Secondly, Install the appropriate Chrome Driver [Link](https://chromedriver.chromium.org/downloads).
3. After you clone or download this repo, you have to install the dependencies  ```  pip install -r requirements.txt ```
4. You have to modify the data in ```PARAMETERS.py``` . You will find e-mail and password varialbes 
that you better modify them to your e-mail(or handle) and your password
5. Now you can run  ```main.py``` and your solutions will be stored in a directory ```/problems``` 
that will be created.

## FAQ
**Why the heck you need my password?**  
There are some problems to which you can't see the submission unless you solved them.
Entering your password will guarantee that most of the problems will be retreived.  
In other words, we know that there are several contests in the GYM, like [this](https://codeforces.com/gym/103202/), to which you can't see their users' 
submissions unless you solve the problems yourself. If you are solving a lot of those contests, the script will
not be able to retrieve their solutions.  
Finally, If most of your submissions are visible to everyone or you suspect that this script will 
steal your password and sell them in the black market, you don't need to enter your password. 

**Does entering my password guarantee that all problems will be retrieved?**

**Some problems are stored with extension .cpp but They aren't C++ ?**

## Issues
There is a little probability that you face those problems when you use the script, but I will list them here and mark them whenever 
I solve them
- [ ] Entering the password correctly but login fails
- [ ] Some problems aren't retreived with no reasonable reason

## Tasks
Those are the tasks remaining in order to say that this script is human-usable :D 
- [ ] Testing the script on Linux.
- [ ] Providing the user with the appropirate feedback whenever login fails. 

