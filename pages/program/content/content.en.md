##Talks##

![russell-keith-magee](http://dropbucket.ru/pyconru/speakers/russell-keith-magee-small)

<div markdown="1">
**[Dr. Russell Keith-Magee](http://cecinestpasun.com)**, president of the [Django Software Foundation](https://www.djangoproject.com/foundation/), member of the Django core team and co-founder of the [TradesCloud](http://tradescloud.com/).   
**Django 1.6 and beyond: The Django Roadmap**

With the impending release of Django 1.5, now is a good time to reflect on the roadmap for Django 1.6 and beyond. In this talk, Django Core Developer Russell Keith-Magee will gaze into his crystal ball and speculate about what the future may hold for Django -- both in the short term, and possibilities for the long term.   
Audience: Existing Django users interested in what the future holds for their web framework of choice.    
**Time:** 1 hour


**Building a development community: Lessons and challenges**

Over the last 7 years, Django has grown from an in-house project in an obscure Kansas newsroom, to a project with global reach, in use on all 7 continents, with contributors and users all over the planet. How has the Django project managed this process of growth? What lessons can other projects learn from Django's successes and failures? And how can Django protect it's long term survival? In this talk, Django Core Developer Russell Keith-Magee will reflect on the history of the Django project, and look at how Django -- and other open source projects -- can build, grow and sustain their communities.   
Audience: Anyone involved in open source.   
**Time:** 40 min
</div>

![armin-ronacher](http://dropbucket.ru/pyconru/speakers/armin-ronacher-small)

<div markdown="1">
**[Armin Ronacher](http://lucumr.pocoo.org)**, one of the founding members of the[Pocoo Team](http://www.pocoo.org/). Widely known like author [Flask](http://flask.pocoo.org/) and [Jinja2](http://www.pocoo.org/projects/jinja2/#jinja2).   
**Advanced Flask patterns**

This talk shows some interesting patterns for large scale Flask applications and how Flask extension should be structured. It also dives into some of the more unknown helpers in the Werkzeug and Jinja2 base libraries. The goal of this talk is to share some of the things that the documentation can’t explain well by itself. Required prerequisites: basic knowledge of how Flask operates.    
**Time:** 1 hour
</div>

![holger-krekel](http://dropbucket.ru/pyconru/speakers/holger-krekel-small)

<div markdown="1">
**[Holger Krekel](http://holgerkrekel.net/)**, founder of the [PyPy Project](http://pypy.org/), author of the [py.test](http://pytest.org/latest/) and [tox](http://codespeak.net/tox/) testing tools.    
**Re-inventing Python packaging and testing**

Python still does not have a built-in installer that can install dependencies.  You have to first install setuptools/distribute and then use easy_install/pip.  Installation of packages is slow and depends on reachability of  pypi.python.org and other servers.  There is no quality control where you could e. g. see on which platforms the package successfully installs, let alone has its automated tests passing.  There is not really a standard way to run tests.  This talk outlines my plans for improving the situation, including a demo of a new (in-development) PyPI server that speeds up installation by an order of magnitude for many packages.    
**Time:** 50 min
</div>

![david-cramer](http://dropbucket.ru/pyconru/speakers/david-cramer-small)

<div markdown="1">
**[David Cramer](http://justcramer.com/)**, highload specialist from [DISQUS](http://disqus.com/), author of [Sentry](https://www.getsentry.com).   
**Scaling for Success: How to build proper scalable web apps**

I'll talk about what I see as a successful scaling strategy for growing companies. Specifically it will focus on things you should avoid early on, and where you can get easy wins. Additionally I'll cover various high level components of an early scaling strategy such as database sharding, CDN caching, and overall architecture to simplify the growing pains.  
- How to approach sharding (architecture)   
- Horizontal vs vertical, which solution is right and when    
- How we sharded the Django ORM   
- Materialized views using Redis    
- Buffered counters using Redis   
**Time:** 1 hour
</div>

![jeff-lindsay](http://dropbucket.ru/pyconru/speakers/jeff-lindsay-small)

<div markdown="1">
**[Jeff Lindsay](http://progrium.com)**, hacker-philosopher, developer, web architect, founder of the largest community center for hackers [Hacker Dojo](http://www.hackerdojo.com).    
**Building Public Infrastructure with Autosustainble Services**

Five years ago, I realized we needed a vehicle other than startups to build sustainable open source services. This need came from my own problem of building lots and lots of simple services (usually in Python) and not having the time or desire to build a business around them. These services include Localtunnel, RequestBin, Airscript, and others. Here I'll show these projects, their place in the ecosystem, and what I plan to do about making them sustainable. 

**Time:** 50 min
</div>

![Amir Salihefendic](http://dropbucket.ru/pyconru/speakers/amir-salihefendic-small)

<div markdown="1">
**[Amir Salihefendic](http://amix.dk/)**, founder of the [Doist Ltd](http://Doist.io/). Lead developer and co-founder one of the largest in the world sites by Python [Plurk.com](http://plurk.com) in the past.  
**Redis, the hacker's database**

- simple_queue: feature set, comparison with Celery and Rq    
- redis_graph: available options, integration with other tools, and the big-O performance   
- bitmapist, idea, archtecture, reports based on cohorts    
- optionally: tagged-logger / ormist (lightweight Object-to-Redis mapper)   
- optionally: scripting possibility of Lua, Lua-jit (almost as fast as C)   
**Time:** 50 min
</div>

![svetlov](http://dropbucket.ru/pyconru/svetlov)

<div markdown="1">
**Andrew Svetlov**, Python Core Developer, Co-organizer UA PyCon.   
**PEP 3156 — Standard of asynchronous IO Support Rebooted in Python.**
  
Python already has a lot of libraries for network programming. The most famous are twisted, tornado, gevent, medusa/asyncore. These systems are not compatible with each other, that does not give a possibility to write cross-platform libraries working in any event loop. PEP 3156 proposes new general standart, that will be able to support all developers.
</div>

![vlasovskii](http://dropbucket.ru/pycon/vlasovskii)

<div markdown="1">
**Andrew Vlasovskih**,IDE PyCharm developer in JetBrains, author of libraries funcparserlib and iterpipes.  
**Static analysis of Python**

Static analysis provides the information of the source code without executing it. We'll consider available means of static analysis code by Python (PyLint, PyFlakes, Pep8, inspection IDE) and will talk about problems that they can find automatically in code. I'll talk about the approaches that are based static analysis in these tools and about the specifics of the analysis of Python as dynamic language.
Report introduces you whith tools of static analysis, using that in daily practice you can reduce quantity of problems in Python code (errors, exceptions, and stylistic differences).
</div>


![korobov](http://dropbucket.ru/pyconru/korobov)

<div markdown="1">
**Mike Korobov**, Python-developer, speaker of different Python-conferences.    
**How to transition to Python 3?**

I'll tell how do matters stand with transition to Python 3, why should it transition and how (on my mind) transition to it. Knowledge can be applied on practice at the same day. We'll be porting several libraries on evening workshop/sprint. I hope that after the report and the workshop everyone's skill of porting code on Python 3 is systematized. This skill will become necessary soon for reading majority popular project's code for example and for benefit of the World Civilization, why not?:-)   
</div>

![imankulov](http://dropbucket.ru/pyconru/imankulov)

<div markdown="1">
**Roman Imankulov**, developer of the [Doist Ltd](http://Doist.io/).  
**Celery for internal API in SOA infrastructure**

The main purpose of Celery is to execute background tasks. As a rule, Celery processes use the same code base as the main application. I suggest to have a look at Celery from the other side and try to use in as a transport for linking the dispersed application components.  The report will show the particular examples of API realization on Celery, take a good look at questions connected with the routing of demands to workers. Also there will be told why exactly Celery is so good for inside API building, in what situations the usage can be excess. The audience will learn how to connect the components of dispersed application in the whole thing  fast and without extra consumptions, get rid of coherence, and possibly to look at your application from the other side. It’s taken that listeners know the queue messengers concept and conceive why Celery or analogous solutions  can be used

</div>

![koshelev](http://dropbucket.ru/pyconru/koshelev)

<div markdown="1">
**Alexander Koshelev**, team-lead, Yandex 
**What happens inside of asynchronous code?**

What happens inside asynchronous code? What to do if logic becomes cpu-bound? Is it possible to create the hybrid synchronous- asynchronous architecture? I will try to answer these questions in terms of Tornado application. I will make the visualization of application and suggest the  ways to solve some problems.

</div>

![lopuhin](http://dropbucket.ru/pycon/kostialopuhin)

<div markdown="1">
**Konstantin Lopukhin**, CHTD  
**An approach to versioning in relational database**

I want to tell about data versioning  in relational database – where this problem comes from, possible ways of statement and solution. Particularly I will tell about interval based approach which allows working with the system at any moment in the past, do the whole system back-off or back-off of its separate parts. This approach realized in a small library “documents” for Django, but the concept is easy movable. I will take the usage of this approach for traditional applications and for versioned EAV database building, showing data like a graph.

</div>



![kolodin](http://dropbucket.ru/pycon/kolodin)

<div markdown="1">
**Denis Kolodin**, programmer-analyst, IK “Forum”  
**Low-latency and soft-realtime на Python**

The report will tell about software developing working on high speeds and having the predictable reaction time. Also there will be presented the Python integration ways with ctypes and cython with the high-speed services of the operation system. It will touch upon the questions  of  memory, processes, streams, fibers and GIL managing\control. The audience will learn how to build systems with the expected reaction time. The knowledge can be used for servers’ development servicing a lot of clients simultaneously or executing high-speed data processing

</div>


![prokofev](http://dropbucket.ru/pycon/prokofev)

<div markdown="1">
**Dmitry Prokofjev** , developer, Yandex

**System of data synchronization between services evolution**

The report will explain why Yandex needed the data synchronization and what we had to meet with in the process: why we synchronize in the application level. Update log vs Insert log. Problems related with DB. Types of data, transactions absence. Problems related with Django. Problems related with the changings below the application level. For instance, mass update.

</div>


![yumatov](http://dropbucket.ru/pycon/yumatov)

<div markdown="1">
**Mihail Yumatov **, senior developer, Trilan

**SaltStack**

SaltStack – is an instrument for parallel commands execution on servers where commands are functions on Python. In my report I will try to explain why you should pay attention to SaltStack even if you are actually using Chef or Puppet, why – how it can be helpful. I will speak about the usage of how we use SaltStack for the projects deployment automation and take into consideration the additional good possibilities like notification system between services, system of users’ rights and some other things.

</div>


![kostuk](http://dropbucket.ru/pycon/kostuk)

<div markdown="1">
**Grisha Kostjuk** , python-developer, Ostrovok.ru

**Test optimization in terms of django and postgres**
Test execution speed is important not only in TDD but also for Continuous Integration. I will tell you how we organized test environment in Ostrovok.ru: how we isolate the base and cash, how solved the problem with of  launching in to several streams, about the advantages of our runner pluses…In general, I will share the experience how we do it and why the report will especially be helpful for projects which have the real base in tests used, because sqlite in the memory doesn’t fit. And for those who think  about tests’ acceleration.

</div>


![budkar](http://dropbucket.ru/pycon/budkar)

<div markdown="1">
**Alexandr Budkar** , Head of infrastructure development Web search, Yandex.    

**Distributed execution Python code on 1000+ servers.**    

I'll talk about created in Yandex infrastructure for administration a lot of servers, about problems which arise in work with many computers and about the used technologies. Report will be interest those, who develop distributed systems, high loaded services, encounter with processing a lot of data in real time. Also system administrators, who exploit 10+ servers.    

</div>


![generalov_shalapin](http://dropbucket.ru/pycon/generalov_shalapin)

<div markdown="1">
**Ilya Shalyapin, Evgeny V. Generalov** , JetStyle    

**Test Driven Development in Python and Django.**    

In books, articles and videos most test examples are simplified to much. So it's very hard to apply these examples to real work. Real projects are not so simple. In real project we depend on internet connection, databases and filesystems. It's not obvious how to test such things. We will show test examples and tools that we use every day in our practice.    

</div>


![biin](http://dropbucket.ru/pycon/biin)

<div markdown="1">
**Ilya Biin** , developer, Ostrovok.ru    

**Construction distributed caching system and messaging**    

One of the methods optimization speed and quality of work your website is caching. Within the framework of presentation I want share practical experience in the creation, setting and tuning of distributed caching system. Emphasis will be paid features of work such system in conditions changeability network environment and instability of hardware. As well it will be about the exchange of messages through such system, its advantages and disadvantages. Presentation aimed on architects and developers of systems, who works with "heavy" data.    

</div>



![matveenko](http://dropbucket.ru/pycon/matveenko)

<div markdown="1">
**Sergey Matveyenko** ,Senior programmer, Positive Technologies 

**MongoEngine: NoORM for NoSQL**  

Nowdays non relational databases become more popular than relational, in particular, MongoDB. However, even experienced developers, who are familiar with relational databases, their experience don't help them and sometimes it interfere. I'll tell about using MongoEngine, which allows you to bring methods of application development by Python with using MongoDB to more traditional approaches. This will be useful all Python developers who have an interest in MongoDB and non relational databases.    

</div>


![ideco](http://dropbucket.ru/pycon/ideco_foto)

<div markdown="1">
**Valentin Sinisyn, Maxim Sukharev**, Ideco

**Tornado – not only web-sites**

In «Ideco» we don’t do web-developing, we create solutions for web infrastructure which make complicated things easier. There is Linux and other system instruments laid in the depths of these solutions and there’s a good web-interface shown on the surface. Tornado takes the middle  and provides the connection between “top” and “bottom”. Why does it go this way and is why web-framework a successful decision for system programming? You will learn all of these issues from the report. Report will be helpful for Python-programmers, who want to learn the possibilities of Tornado, and also for developers of dispersed systems solving the problems of connection organization between components.

</div>


##Workshops##



![lopuhin](http://dropbucket.ru/pycon/kostialopuhin)

<div markdown="1">
**Konstantin Lopuhin**, ChTD    
**Workshop: We will write your interpreter with using RPython**    

On this workshop we will see:    
  - the structure of the bytecode interpreter(almost all of modern interpreters for dynamic languages are such)    
  - what benefits give us using RPython in implementation(using in PyPy)    
  - and how JIT(just-in-time compiler) works    
The practical part will consist of implementing a few small parts - implementation of a new bytecode, adding just-in-time compiler, analyze and improve performance.Participants will learn what parts consist of interpreter and how it works, how the JIT works, why TDD is good, and then be able to write a quick little dynamic language interpreter for the weekend.    

</div>


![svetlov](http://dropbucket.ru/pyconru/svetlov)

<div markdown="1">
**Andrew Svetlov**, Python Core Developer, co-organizer UA PyCon.  
**Workshop on creation network applications from scratch**  
  
Many programmers wrote asynchronous code using off-the-shelf solutions. The goal of the master-class is to show how all of this works inside. It will be interesting to those who have written the network code using off-the-shelf libraries, or those who want to learn how to do it. Participants will gain knowledge about the basic principles of creating asynchronous network libraries from low level constructions to easy-to-use constructions.    

</div>


![korobov](http://dropbucket.ru/pyconru/korobov)

<div markdown="1">
**Mike Korobov**, Python-developer, speaker of different Python-conferences.  
**Porting library from Python 2 to Python 3**    

Knowledge can be applied on practice at the same day. We'll be porting several libraries on evening workshop/sprint. I hope that after the report and the workshop everyone's skill of porting code on Python 3 is systematized. This skill will become necessary soon for reading majority popular project's code for example and for benefit of the World Civilization, why not?:-)    
</div>
