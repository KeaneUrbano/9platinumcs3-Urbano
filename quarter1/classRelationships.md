# Class Relationships: Association and Multiplicity
## Previous Work

[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Footballer
Description: They are people who play football for a variety of reasons, it could be their full time job or a hobby they like to do.
## New Related Class
Class:Football Club
Description: These are professional establishments created for the purpose of participating in football competitions. They vary from level to level with some worth less
than a few thousand dollars to billions of dollars. Some football clubs are businesses and others are passionate. 
## Association
Relationship: Football Club manages Footballers.
Explanation: Football Clubs employs Footballers to play for their club. 
## Multiplicity
Multiplicity: 1....*
Explanation:
Most official competition rules require at least 11 players to participate. Without footballers a club effectively does not exist. 

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationship.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The association between FootballClub and Footballer is an Composition relationship. A FootballClub contains and manages Footballer objects as part of its team. The direction of the association allows the club to store and interact with multiple player objects.

### What multiplicity did you choose and why?
I chose a multiplicity of **1 to 1..**. A football club must have at least 11 registered player to be considered a eligible team under official competition rules. Then, a single player in this relationship belongs to one club at a given time.

### How did you implement the relationship in Python?
The relationship is applied through putting Football objects into FootballClub class methods like `add_player(player)`. Inside the FootballClub constructor a list attribute (self.squad) is activated to record all Footballer instances. 

### Why did you store an object reference instead of copying its data?
Storing an object reference ensures data consistency and memory efficiency.


### If your relationship uses many, why is a list appropriate?
A list is the best Python data structure for managing multiple player objects in a squad:

Lists provide built-in methods (like .append(), .remove(), or list comprehensions) that make it easy to iterate over players to calculate team wide stats, filter by position, or display squad list.
