# home-finder
This python file can be used to extract rental home data from Kijiji.ca from your region.

## How to use

**1.** Go to kijiji and search from rental homes in your region.

**2.** Copy the URL, edit page no in url to {} and add it in the URL parameters as shown below in between " " in home_finder.py. Do not remove the ***.format(start)*** at end 
        
        URL= "https://www.kijiji.ca/b-for-rent/mississauga-peel-region/page-{}/c30349001l1700276?radius=9.0&address=2585+Meadowpine+Boulevard%2C+Mississauga%2C+ON&ll=43.602075,-79.779412".format(start)

**3.** The output excel file with header Title,Price, Km distance and Link will be genrated which can be used to find the required rental home.
