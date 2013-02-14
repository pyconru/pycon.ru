##Доклады##

![russell-keith-magee](http://dropbucket.ru/pyconru/speakers/russell-keith-magee-small)

<div markdown="1">
**[Dr. Russell Keith-Magee](http://cecinestpasun.com)**, президент [Django Software Foundation](https://www.djangoproject.com/foundation/), член Django core team, CTO компании [TradesCloud](http://tradescloud.com/).

**Django 1.6 and beyond: The Django Roadmap**

With the impending release of Django 1.5, now is a good time to reflect on the roadmap for Django 1.6 and beyond. In this talk, Django Core Developer Russell Keith-Magee will gaze into his crystal ball and speculate about what the future may hold for Django -- both in the short term, and possibilities for the long term.   
Audience: Existing Django users interested in what the future holds for their web framework of choice.

**Длительность:** 1 час

**Building a development community: Lessons and challenges**

Over the last 7 years, Django has grown from an in-house project in an obscure Kansas newsroom, to a project with global reach, in use on all 7 continents, with contributors and users all over the planet. How has the Django project managed this process of growth? What lessons can other projects learn from Django's successes and failures? And how can Django protect it's long term survival? In this talk, Django Core Developer Russell Keith-Magee will reflect on the history of the Django project, and look at how Django -- and other open source projects -- can build, grow and sustain their communities.   
Audience: Anyone involved in open source.

**Длительность:** 40 минут
</div>

![armin-ronacher](http://dropbucket.ru/pyconru/speakers/armin-ronacher-small)

<div markdown="1">
**[Armin Ronacher](http://lucumr.pocoo.org)**, один из основателей [Pocoo Team](http://www.pocoo.org/). Широко известен как автор [Flask](http://flask.pocoo.org/) и [Jinja2](http://www.pocoo.org/projects/jinja2/#jinja2).

**Advanced Flask patterns**

This talk shows some interesting patterns for large scale Flask applications and how Flask extension should be structured. It also dives into some of the more unknown helpers in the Werkzeug and Jinja2 base libraries. The goal of this talk is to share some of the things that the documentation can’t explain well by itself. Required prerequisites: basic knowledge of how Flask operates.

**Длительность:** 1 час
</div>

![holger-krekel](http://dropbucket.ru/pyconru/speakers/holger-krekel-small)

<div markdown="1">
**[Holger Krekel](http://holgerkrekel.net/)**, основатель [PyPy Project](http://pypy.org/), автор популярных инстументов [py.test](http://pytest.org/latest/) и [tox](http://codespeak.net/tox/).

**Re-inventing Python packaging and testing**

Python still does not have a built-in installer that can install dependencies.  You have to first install setuptools/distribute and then use easy_install/pip.  Installation of packages is slow and depends on reachability of  pypi.python.org and other servers.  There is no quality control where you could e. g. see on which platforms the package successfully installs, let alone has its automated tests passing.  There is not really a standard way to run tests.  This talk outlines my plans for improving the situation, including a demo of a new (in-development) PyPI server that speeds up installation by an order of magnitude for many packages.

**Длительность:** 50 минут
</div>

![david-cramer](http://dropbucket.ru/pyconru/speakers/david-cramer-small)

<div markdown="1">
**[David Cramer](http://justcramer.com/)**, специалист по высоким нагрузкам из [DISQUS](http://disqus.com/), автор [Sentry](https://www.getsentry.com).

**Scaling for Success: How to build proper scalable web apps**

I'll talk about what I see as a successful scaling strategy for growing companies. Specifically it will focus on things you should avoid early on, and where you can get easy wins. Additionally I'll cover various high level components of an early scaling strategy such as database sharding, CDN caching, and overall architecture to simplify the growing pains.  
- How to approach sharding (architecture)   
- Horizontal vs vertical, which solution is right and when    
- How we sharded the Django ORM   
- Materialized views using Redis    
- Buffered counters using Redis 

**Длительность:** 1 час
</div>

![jeff-lindsay](http://dropbucket.ru/pyconru/speakers/jeff-lindsay-small)

<div markdown="1">
**[Jeff Lindsay](http://progrium.com)**, хакер-философ, разработчик, архитектор, основатель крупнейшего в США коммьюнити-центра для хакеров [Hacker Dojo](http://www.hackerdojo.com).

**Distributed Service Architectures with Python**

The description will come up soon...

**Длительность:** 50 минут
</div>

![Amir Salihefendic](http://dropbucket.ru/pyconru/speakers/amir-salihefendic-small)

<div markdown="1">
**[Amir Salihefendic](http://amix.dk/)**, основатель компании [Doist Ltd](http://Doist.io/).  В прошлом - ведущий разработчик и со-основатель [Plurk.com](http://plurk.com), одного из самых крупных в мире сайтов на Питоне.

**Redis, the hacker's database**    
- simple_queue: feature set, comparison with Celery and Rq    
- redis_graph: available options, integration with other tools, and the big-O performance   
- bitmapist, idea, archtecture, reports based on cohorts    
- optionally: tagged-logger / ormist (lightweight Object-to-Redis mapper)   
- optionally: scripting possibility of Lua, Lua-jit (almost as fast as C)

**Длительность:** 50 минут
</div>

![svetlov](http://dropbucket.ru/pyconru/svetlov)

<div markdown="1">
**Андрей Светлов**, Python Core Developer, соорганизатор UA PyCon.  
**PEP 3156 — стандарт на асинхронные операции в Питоне.**
  
Питон уже имеет немало библиотек для сетевого программирования. Самые известные — twisted, tornado, gevent, medusa/asyncore. Эти системы не совместимы между собой, что не дает возможности писать кроссплатформенные библиотеки работающие в любом event loop. PEP 3156 предлагает новый общий стандарт, который смогут поддерживать все разработчики.
</div>

![vlasovskii](http://dropbucket.ru/pycon/vlasovskii)

<div markdown="1">
**Андрей Власовских**, разработчик IDE PyCharm в JetBrains, автор библиотек funcparserlib и iterpipes.

**Статический анализ языка Python**

Статический анализ позволяет получать информацию из исходного кода программы без её выполнения. Мы рассмотрим доступные средства статического анализа кода на языке Python (PyLint, PyFlakes, Pep8, инспекции в IDE) и поговорим о том, какие проблемы они могут автоматически находить в коде. Я расскажу о подходах, на которых основан статический анализ в этих инструментах, более подробно остановлюсь на специфике анализа Python как динамического языка.
Доклад познакомит с инструментами статического анализа, благодаря использованию которых в повседневной практике можно снизить количество проблем в коде на Python (ошибок, исключений, стилистических расхождений).А еще позволит узнать о теории, стоящей за инструментами статического анализа и познакомиться с особенностями применения статического анализа динамических языков типа Python.
</div>


![korobov](http://dropbucket.ru/pyconru/korobov)

<div markdown="1">
**Михаил Коробов**, Python-разработчик, спикер различных Python-конференций.  
**Как перейти на Python 3?**

Расскажу, как обстоят дела с переходом на 3й питон, зачем на него переходить и как (по моему мнению) на него переходить. Знания можно будет в тот же день применить на практике, совместно портировав библиотеку-другую в рамках вечернего воркшопа/спринта.
Надеюсь, что после доклада и воркшопа у каждого человека появится (или систематизируется) навык портирования кода на Python 3. Этот навык в скором времени станет необходим, например, для того, чтобы читать код большинства популярных проектов (даже если пишете на 2.x). Ну и пользу для мировой цивилизации никто не отменял. 
</div>

![imankulov](http://dropbucket.ru/pyconru/imankulov)

<div markdown="1">
**Роман Иманкулов**, разработчик [Doist Ltd](http://Doist.io/).  
**Celery для внутреннего API в инфраструктуре SaaS**

Основная задача Celery состоит в том, чтобы исполнять фоновые задачи. Как правило, процессы celery используют ту же кодовую базу, что и основное приложение.
Я предлагаю взглянуть на Celery с другой стороны и попробовать использовать его в роли транспорта для связи компонентов распределенного приложения.
В докладе будут приведены конкретные примеры реализации API на Celery, рассмотрены возникающие в связи с этим вопросы маршрутизации запросов к воркерам. Также будет упомянуто, чем же Celery так хорош для построения внутреннего API, а в каких ситуациях его использование может показаться излишним.
Слушатели узнают о том, как можно быстро и без лишних накладных расходов связать компоненты распределенного приложения в единое целое, избавиться от сильной связности, и возможно, взглянуть на собственное приложение немного с другой точки зрения. Предполагается, что слушатели знакомы с концепцией очередей сообщений, и представляют, в каких случаях и для чего может использоваться Celery или аналогичные решения.
</div>

![koshelev](http://dropbucket.ru/pyconru/koshelev)

<div markdown="1">
**Александр Кошелев**, руководитель группы разработки, Яндекс.  
**Препарирование работы асинхронного кода**

Что происходит внутри асинхронного кода? Как быть, когда логика становится cpu-bound? Можно ли сделать гибридную синхронно-асинхронную архитектуру?
Я попробую ответить на эти вопросы на примере приложения на Tornado. Сделаю визуализацию работы приложения и предложу пути решения некоторых проблем.
</div>

![lopuhin](http://dropbucket.ru/pycon/kostialopuhin)

<div markdown="1">
**Константин Лопухин**, ЧТД  
**Подход к версионированию данных в реляционной БД**

Я хочу рассказать о проблеме версионирования данных в реляционной БД - откуда возникает такая проблема, возможные варианты постановки и решения. Подробнее расскажу о подходе, основанном на интервалах,который позволяет работать в системе в любой момент времени в прошлом, производить откат всей системы или отдельных ее частей. Подход реализован в небольшой библиотеке documents для Django, но сам принцип легко переносим. Рассмотрю применение этого подхода как для традиционных приложений, так и для построения версионированой EAV базы данных, представляющей данные в виде графа.

</div>

![shtan](http://dropbucket.ru/pycon/shtan)

<div markdown="1">
**Данила Штань**, руководитель разработки холдинга 66.ru  
**uWSGI как швейцарский нож python-web-разработчика**

uWSGI, который начинался как быстрый контейнер приложений на питоне постепенно эволюционировал в инфраструктурное решение не только для запуска, но и для разработки приложений в целом (причем не только на языке python). К сожалению, недостаток документации зачастую отталкивает разработчиков и сисадминов от использования uWSGI.   Мой доклад нацелен на людей (как разработчиков, так и сисадминов), которые имеют практический опыт разворачивания web-приложений на питоне в production-среде, которые готовы рассматривать альтернативы выбранным решениям. Помимо знакомства с собственно сервером приложений мы посмотрим на дополнительные фичи (например кэширование или выполнение фоновых задач), которые зачастую позволяют (особенно в небольших проектах) уменьшить количество используемых сторонних технологий вроде memcached или celery.
</div>


![kolodin](http://dropbucket.ru/pycon/kolodin)

<div markdown="1">
**Денис Колодин**,  программист-аналитик, ИК "Форум"  
**Low-latency и soft-realtime на Python**

В докладе будет рассказано о разработках программного обеспечения, работающего на высоких скоростях и имеющего предсказуемое время реакции. Также будут представлены способы интеграции Python с помощью ctypes и cython с высокоскоростными сервисами операционной системы. Затронуты вопросы управления памятью, процессами, потоками, волокнами и GIL. Слушатели поймут, как строить системы с ожидаемым временем реакции. Знания могут быть применены для разработки серверов, обслуживающих множество клиентов одновременно или выполняющих скоростную обработку данных.

</div>


![prokofev](http://dropbucket.ru/pycon/prokofev)

<div markdown="1">
**Дмитрий Прокофьев** разработчик, Яндекс

**Эволюция системы синхронизации данных между сервисами**

В докладе будет рассказано о том, зачем Яндексу понадобилась синхронизация данных и с чем пришлось столкнуться в процессе:
Почему синхронизируем на уровне приложения.
Update log против Insert log.
Проблемы связанные с DB. Типы данных, отсутствие транзакций.
Проблемы связанные с Django.
Проблемы связанные c изменениями ниже уровня приложения. Например массовый update.

</div>


![yumatov](http://dropbucket.ru/pycon/yumatov)

<div markdown="1">
**Михаил Юматов** , старший разработчик, Трилан

**SaltStack**

SaltStack — это инструмент для параллельного выполнения команд на серверах, где команды — функции на Python. В докладе я попробую объяснить, почему стоит обратить внимание на SaltStack, даже если вы уже используете Chef или Puppet, чем он может быть полезен. Расскажу, как мы используем SaltStack для автоматизации развертывания проектов и уделю внимание дополнительным приятным возможностям, таким как система уведомлений между серверами, система прав пользователей и некоторым другим.

</div>


![kostuk](http://dropbucket.ru/pycon/kostuk)

<div markdown="1">
**Гриша Костюк** , python-разработчик, Ostrovok.ru

**Оптимизация тестов на примере django и postgres**

Скорость выполнения тестов не только важна при TDD, но также важна для непрерывной интеграции, тем более если сборки идут часто, а при большой команде - это неизбежно. Расскажу как мы организовали тестовую среду в ostrovok.ru: как изолируем базу и кеши, как решили вопрос запуска в несколько потоков, про плюсы своего раннера... В общем поделюсь опытом как мы это делаем и почему
Доклад будет особенно полезен тем проектам, в которых используется реальная база в тестах, т.к. sqlite в памяти не подходит. И тем кто задумывается как ускорить такие тесты.

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


##Мастер-классы##



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
**Михаил Коробов**, Python-разработчик, спикер различных Python-конференций.  
**Портирование библиотеки с python 2 на python 3**

Информацию, полученную из доклада можно будет в тот же день применить на практике, совместно портировав библиотеку-другую в рамках вечернего воркшопа/спринта.
Надеюсь, что после  у каждого человека появится (или систематизируется) навык портирования кода на Python 3. Этот навык в скором времени станет необходим, например, для того, чтобы читать код большинства популярных проектов (даже если пишете на 2.x). Ну и пользу для мировой цивилизации никто не отменял. 
</div>
