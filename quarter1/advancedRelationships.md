# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
I have 2 classes, Footballer and FootballClub. Footballer represents people who plays football, while on the other hand FooballClub represents
the entities who employ Footballers. 

## Inheritance Relationship

Parent: FootballClub
Child:- Footballer
Explanation: FootballClubs need Footballers to play for it while Footballers can only play for one club at a time. 

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation

Relationship: Aggregation
Explanation: A Footballer needs a FootballClub to play but doesn't necessarily need one to exist.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers: Doing this activity helped me understand how OOP concepts work together in a real world scenario like this footballsystem. I learned how to distinguish different processes by mapping the classes out in both UML class and object diagrams. And using inheritance for Person and aggregation for FootballClub made the code much more organized and logically structured.
