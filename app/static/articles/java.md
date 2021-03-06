# JAVA学习笔记

## I.概述：
> 八月中旬开始正式学习java，到现在学了有一个多月了.学习Java这门语言的主要想多学一门语言，做一些有意思的事情， 同时也在于它不仅任然是目前最为流行的一门编程语言之一，也因为它足够成熟，有强大的技术支持等诸多原因。

> 这一个多月的时间里，前期主要在看机械工业出版社的《Java语言程序设计》，很基础的一本书，也容易懂，后期看完这本基础书后开始看《Java编程思想》，写得更加深入一些，目前还没看完，然后稍微了解了一些JVM的知识，最近又花了几天时间把《Java语言程序设计》再温习了一边，把原来不太懂的地方再思考了一边。

****

## II.简单却容易忘记的知识点
### A. 类成员修饰符
> * public: 在同一类内可访问， 在同一包内可访问， 在子类内可访问， 在不同包可访问（可见性最高）
> * proteced：在同一类内可访问， 在同一包内可访问， 在子类内可访问
> * (default): 在同一类内可访问， 在同一包内可访问
> * private: 在同一类内可访问。(可见性最低)
> 
> 修饰符private和protected只能用于类成员，public修饰符和默认修饰符（即没有修饰符）既可以用于类，又可以用于类成员。
> 
> 关于protected修饰符：子类可以重写它的父类的protected方法，并把他的可见性改为public。但是，子类不能削弱父类中定义的方法的可访问性。即：可以增强，不能削弱。
> ***

### B.异常
> 异常是从方法抛出的。
> RuntimeException, Error以及它们的子类都称为免检异常，所有其他异常都称为必检异常。
> java编译器会强制要求程序员检查并通过try-catch块处理必检异常，或者在方法头中声明这些异常。

****

## III.面向对象思考
	Java作为一种面向对象的编程语言，很好地履行了面向对象思想。面向对象程序设计(OOP)就是使用对象进行程序设计。

>#### Wikipedia:
>面向对象程序设计（英语：Object-oriented programming，缩写：OOP）是种具有对象概念的程序编程范型，同时也是一种程序开发的方法。它可能包含数据、属性、代码与方法。对象则指的是类的实例。它将对象作为程序的基本单元，将程序和数据封装其中，以提高软件的重用性、灵活性和扩展性，对象里的程序可以访问及经常修改对象相关连的数据。在面向对象程序编程里，计算机程序会被设计成彼此相关的对象。

>面向对象程序设计可以看作一种在程序中包含各种独立而又互相调用的对象的思想，这与传统的思想刚好相反：传统的程序设计主张将程序看作一系列函数的集合，或者直接就是一系列对电脑下达的指令。面向对象程序设计中的每一个对象都应该能够接受数据、处理数据并将数据传达给其它对象，因此它们都可以被看作一个小型的“机器”，即对象。目前已经被证实的是，面向对象程序设计推广了程序的灵活性和可维护性，并且在大型项目设计中广为应用。此外，支持者声称面向对象程序设计要比以往的做法更加便于学习，因为它能够让人们更简单地设计并维护程序，使得程序更加便于分析、设计、理解。反对者在某些领域对此予以否认。

>当我们提到面向对象的时候，它不仅指一种程序设计方法。它更多意义上是一种程序开发方式。在这一方面，我们必须了解更多关于面向对象系统分析和面向对象设计（Object Oriented Design，简称OOD）方面的知识。许多流行的编程语言是面向对象的,它们的风格就是会透由对象来创出实例。
> ***

### A.面向对象的三大支柱：封装，继承，多态
> 1.封装：类的抽象是指将类的实现和类的使用分离，实现的细节被封装并且对用户隐藏， 这被成为类的封装。
> * 作用：将功能封装成一个个独立的单元.
> * 意义：减小耦合,避免牵一发而动全身,方便对程序的修改 
>
> 2.继承：从已经存在的类中定义新的类。
> * 作用：代码重用.
> * 意义：减少编码量,间接减少维护成本.
>
>3.多态：父类变量可以指向子类对象。
> * 作用：不同的场合做出不同相应.
> * 意义：封装的一个实现.
>***

### B.动态绑定
> 方法可以沿着继承链的多个类中实现，JVM决定运行时调用哪个方法。
> 调用的方法由变量的实际类型决定。(向上查找方法)

***

## IV.抽象类、接口
### A.抽象类：
> 抽象类被定义为永远不会也不能被实例化为具体的对象。它往往用于定义一种抽象上的概念，在类的继承关系中它往往被定义在较上层的位置。在程序设计的实践活动中，抽象类与接口存在类似的地方，即它更偏重于对共通的方法和属性进行规约。但与接口存在一个非常大的差异则在于，抽象类往往可以规约一个共同的方法和属性时提供一个对他们的实现。
> ***

### B.接口：
> 接口是一种与类相似的结构。接口在很多方面都与类很相似，但是他的目的是指明相关或者不相关类的多个对象的共同行为。
> 在Java中，接口被看作是一种特殊的类。每个接口都会被编译成为独立的字节码文件。与抽象类相似，不能使用new操作符创建接口的实例。
> 接口可以扩展其他接口(一个或多个)而不是类， 一个类可以扩展它的父类同时实现多个接口。
> 实现了Comparable接口的类可以使用通用的java.util.Arrays.sort方法来排序对象
> 
> 接口与抽象类的比较：
> * 变量：抽象类无限制；接口变量必须为public static final
> * 构造方法：抽象类的子类通过构造方法链调用构造方法，抽象类不能用new操作符实例化；接口没有构造方法，不能用new操作符实例化。
> * 方法：抽象类中无限制；接口中所有方法必须是公共的抽象实例方法。

***

## V.结束语
> Java是一门优秀的语言，非常值得我去深入学习。
> 虽然Java有一些缺点，比如长期被人诟病的代码过于冗长，啰嗦，但这丝毫不影响它的魅力，长期保持在编程语言中的领头羊的位置自然有它独特的优点。
