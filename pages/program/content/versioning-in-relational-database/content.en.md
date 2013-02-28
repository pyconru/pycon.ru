**Konstantin Lopukhin**, CHTD  
**An approach to versioning in relational database**

I want to tell about data versioning  in relational database – where this problem comes from, possible ways of statement and solution. Particularly I will tell about interval based approach which allows working with the system at any moment in the past, do the whole system back-off or back-off of its separate parts. This approach realized in a small library “documents” for Django, but the concept is easy movable. I will take the usage of this approach for traditional applications and for versioned EAV database building, showing data like a graph.


