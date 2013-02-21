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
**Celery for internal API in Saas infrastructure**

Основная задача Celery состоит в том, чтобы исполнять фоновые задачи. Как правило, процессы celery используют ту же кодовую базу, что и основное приложение.
Я предлагаю взглянуть на Celery с другой стороны и попробовать использовать его в роли транспорта для связи компонентов распределенного приложения.
В докладе будут приведены конкретные примеры реализации API на Celery, рассмотрены возникающие в связи с этим вопросы маршрутизации запросов к воркерам. Также будет упомянуто, чем же Celery так хорош для построения внутреннего API, а в каких ситуациях его использование может показаться излишним.
Слушатели узнают о том, как можно быстро и без лишних накладных расходов связать компоненты распределенного приложения в единое целое, избавиться от сильной связности, и возможно, взглянуть на собственное приложение немного с другой точки зрения. Предполагается, что слушатели знакомы с концепцией очередей сообщений, и представляют, в каких случаях и для чего может использоваться Celery или аналогичные решения.
</div>

![koshelev](http://dropbucket.ru/pyconru/koshelev)

<div markdown="1">
**Alexander Koshelev**, team-lead, Yandex 
**What happens inside of asynchronous code?**

What happens inside asynchronous code? What to do if logic becomes cpu-bound? Is it possible to create the hybrid synchronous- asynchronous architecture? I will try to answer these questions in terms of Tornado application. I will make the visualization of application and suggest the  ways to solve some problems.

</div>

![lopuhin](http://dropbucket.ru/pycon/kostialopuhin)

<div markdown="1">
**Константин Лопухин**, ЧТД  
**Подход к версионированию данных в реляционной БД**

Я хочу рассказать о проблеме версионирования данных в реляционной БД - откуда возникает такая проблема, возможные варианты постановки и решения. Подробнее расскажу о подходе, основанном на интервалах,который позволяет работать в системе в любой момент времени в прошлом, производить откат всей системы или отдельных ее частей. Подход реализован в небольшой библиотеке documents для Django, но сам принцип легко переносим. Рассмотрю применение этого подхода как для традиционных приложений, так и для построения версионированой EAV базы данных, представляющей данные в виде графа.

</div>



![kolodin](http://dropbucket.ru/pycon/kolodin)

<div markdown="1">
**Денис Колодин**,  программист-аналитик, ИК "Форум"  
**Low-latency и soft-realtime на Python**

В докладе будет рассказано о разработках программного обеспечения, работающего на высоких скоростях и имеющего предсказуемое время реакции. Также будут представлены способы интеграции Python с помощью ctypes и cython с высокоскоростными сервисами операционной системы. Затронуты вопросы управления памятью, процессами, потоками, волокнами и GIL. Слушатели поймут, как строить системы с ожидаемым временем реакции. Знания могут быть применены для разработки серверов, обслуживающих множество клиентов одновременно или выполняющих скоростную обработку данных.

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
**Александр Будкарь** , Руководитель службы разработки инфраструктуры веб поиска, Яндекс

**Распределенное исполнение python кода на 10000+ серверах**

Расскажу о созданной в Яндексе инфраструктуре, для управления большим количеством серверов, о проблемах возникающих при работе с большим количеством машин, о используемых технологиях.
Доклад будет интересен тем, кто разрабатывает распределенные системы, высоко нагруженные сервисы, сталкивается с обработкой большого количества данных, в реальном времени. А также администраторам, эксплуатирующим 10+ серверов.

</div>


![generalov_shalapin](http://dropbucket.ru/pycon/generalov_shalapin)

<div markdown="1">
**Илья Шаляпин, Евгений Генералов** , JetStyle

**Разработка через тестирование в Python и Djnago на практике**

Большинство примеров тестов в книгах, семинарах и презентациях упрощены настолько, что их невозможно применить в реальных проектах. Из-за такого упрощения, сначала получаешь заряд мотивации, но столкнувшись с суровой действительностью быстро бросаешь написание тестов. Мы решили исправить этот пробел, показав тестирование на реальных примерах из нашей практики. Мы расскажем о тестировании баз данных, сетевых взаимодействий и веб-форм. Также расскажем об инструментах, которые мы используем для тестирования.

</div>


![biin](http://dropbucket.ru/pycon/biin)

<div markdown="1">
**Илья Биин** , архитектор, Ostrovok.ru

**Построение распределенной системы кеширования и обмена сообщениями**

Одним из способов оптимизации скорости и качества работы вашего сайта является кеширование. В рамках презентации я хочу поделиться практическим опытом по созданию, настройке и тюнингу распределенной системы кеширования. Особое внимание будет уделено особенностям работы такой системы в условиях изменчивости сетевой среды и нестабильности железа. Так же речь пойдет об обмене сообщениями через такую систему. Ее преимуществах и недостатках.
Презентация ориентирована на архитекторов и разработчиков систем, работающих с "тяжелыми" данными.
</div>



![matveenko](http://dropbucket.ru/pycon/matveenko)

<div markdown="1">
**Сергей Матвеенко** ,Старший программист, Positive Technologies

**MongoEngine: NoORM for NoSQL**

Сейчас все большую популярность набирают нереляционные базы данных, в частности, MongoDB. Однако, часто даже опытным разработчикам, хорошо знакомым с реляционными СУБД, их опыт не тольлько не помогает, но даже, иногда, мешает. Я расскажу об использовании MongoEngine, который позволяет приблизить методы разработки приложений на Python с использованием MongoDB к более традиционным подходам.
Будет полезен всем Python разработчикам, кто интересуется MongoDB, нереляционными БД.
</div>


##Workshops##



![lopuhin](http://dropbucket.ru/pycon/kostialopuhin)

<div markdown="1">
**Константин Лопухин**, ЧТД  
**Мастер-класс: пишем свой интерпретатор с использованием RPython**

На этом мастер-классе мы увидим, как устроены байткод интерпретаторы (почти все интерпретаторы для современных динамических языков именно такие), какие преимущества дает использование RPython при реализации (используется в PyPy), и как работает JIT (just-in-time compiler). Практическая часть будет состоять из реализации нескольких небольших частей - реализация нового байт-кода, добавление just-in-time компилятора, анализа и улучшения производительности.
Участники узнают, из каких частей состоит интерпретатор и как они работает, как работает JIT, почему хорош TDD, а после смогут написать быстрый интерпретатор небольшого динамического языка за выходные.
</div>


![svetlov](http://dropbucket.ru/pyconru/svetlov)

<div markdown="1">
**Андрей Светлов**, Python Core Developer, соорганизатор UA PyCon.  
**Мастер класс по созданию сетевых приложений с нуля**
  
Многие программисты писали асинхронный код используя готовые решения. Цель мастер-класса — показать, как это всё работает «под капотом».
Будет интересно тем, кто уже писал сетевой код с использованием готовых библиотек или тем, кто хочет узнать как это делается.
Участники получат знания о базовых принципах создания асинхронных сетевых библиотек начиная с низкого уровня и заканчивая удобными для использования конструкциями

</div>


![korobov](http://dropbucket.ru/pyconru/korobov)

<div markdown="1">
**Mike Korobov**, Python-developer, speaker of different Python-conferences.  
**Porting library from Python 2 to Python 3**    

Knowledge can be applied on practice at the same day. We'll be porting several libraries on evening workshop/sprint. I hope that after the report and the workshop everyone's skill of porting code on Python 3 is systematized. This skill will become necessary soon for reading majority popular project's code for example and for benefit of the World Civilization, why not?:-)    
</div>
