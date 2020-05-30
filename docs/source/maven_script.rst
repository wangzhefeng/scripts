.. _header-n0:

Maven 
======

.. _header-n3:

1.
--

.. code:: shell

   cd ~/project/java_proj/
   mvn archetype:generate -DgroupId=com.mycompany.helloworld -DartifactId=helloworld -Dpackage=com.mycompany.helloworld -Dversion=1.0-SNAPSHOT

-  ``archetype:``

-  ``-DgroupId``

-  ``-DartifactId``

-  ``-Dpackage``

-  ``-Dversion=``

.. code:: 

   .
   ├── pom.xml
   └── src
       ├── main
       │   └── java
       │       └── com
       │           └── mycompany
       │               └── helloworld
       │                   └── App.java
       └── test
           └── java
               └── com
                   └── mycompany
                       └── helloworld
                           └── AppTest.java

   11 directories, 3 files

.. _header-n19:

2.
--

.. code:: shell

   cd helloworld
   mvn package

-  Linux: ``~/.m2/repository/``

-  Win7: ``%USER_HOME%\.m2\repository``

.. code:: 

   .
   ├── pom.xml
   ├── src
   │   ├── main
   │   │   └── java
   │   │       └── com
   │   │           └── mycompany
   │   │               └── helloworld
   │   │                   └── App.java
   │   └── test
   │       └── java
   │           └── com
   │               └── mycompany
   │                   └── helloworld
   │                       └── AppTest.java
   └── target
       ├── classes
       │   └── com
       │       └── mycompany
       │           └── helloworld
       │               └── App.class
       ├── helloworld-1.0-SNAPSHOT.jar
       ├── maven-archiver
       │   └── pom.properties
       ├── maven-status
       │   └── maven-compiler-plugin
       │       ├── compile
       │       │   └── default-compile
       │       │       ├── createdFiles.lst
       │       │       └── inputFiles.lst
       │       └── testCompile
       │           └── default-testCompile
       │               ├── createdFiles.lst
       │               └── inputFiles.lst
       ├── surefire-reports
       │   ├── com.mycompany.helloworld.AppTest.txt
       │   └── TEST-com.mycompany.helloworld.AppTest.xml
       └── test-classes
           └── com
               └── mycompany
                   └── helloworld
                       └── AppTest.class

   28 directories, 13 files

.. _header-n28:

3. 
---

.. code:: shell

   java -cp target/helloworld-1.0-SNAPSHOT.jar com.mycompany.helloworld.App
