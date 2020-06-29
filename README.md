# Finding an Office for our Company
In this project we were asked to find an office that satisfied certain requirements. 
The company has the following structure: 
- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President

The requirements are the following: 
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- The CEO is Vegan
- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
- The office dog "Pepe" needs a hairdresser every month. Ensure there's one not too far away.

## Process 
- First I cleaned up the a Dataframe containing the video game companies which included companies from the database provided by Marc
- Then I exported a JSON file to compass to explore this database
- Then I did the same but for design companies
- After examining both databases I realized that the city that had most video game companies and a design company was either SAN FRANCISCO or Brooklyn (New York). 
- I decided to go for San Francisco since the maintenance guy will apreaciate being closer to a better team's stadium (The Golden state warriors)
- Then I used pymongo to extract the coordinates of the design company. 
- With those coordinates I found the closest bar and pub since our company clearly likes to party.
- I found a midpoint between the pub and bar since this was already close to the design company. That satisfies two requirements. 
- Then I created a function to extract data from the FourSquare API to find the closes vegan restaurant, dog hairdresser, airport, starbucks and basketball stadium. 
- Finally I plotted a map