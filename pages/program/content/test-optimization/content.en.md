**Grisha Kostjuk** , python-developer, Ostrovok.ru

**Test optimization in terms of django and postgres**
Test execution speed is important not only in TDD but also for Continuous Integration. I will tell you how we organized test environment in Ostrovok.ru: how we isolate the base and cash, how solved the problem with of  launching in to several streams, about the advantages of our runner pluses…In general, I will share the experience how we do it and why the report will especially be helpful for projects which have the real base in tests used, because sqlite in the memory doesn’t fit. And for those who think  about tests’ acceleration.


