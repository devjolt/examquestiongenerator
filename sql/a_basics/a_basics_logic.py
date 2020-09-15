from django.shortcuts import render
from random import randint
from sql import sql_classes_and_functions as cf

def list_callable_functions():
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    return entireModuleList

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def previousNext(qtype = None, low = 0, high = None, name='', module_path=''):#uses list of all functions to return previous and next modules in list
    modList = cf.moduleListGen(list_callable_functions(), qtype, low, high)
    modDict = {}
    count = -1
    for thing in modList:
        count+=1
        modDict.update({str(thing):count})
    print(modDict)
    place = modDict[name]
    current = modList[place]
    try:
        next_q = modList[place+1]
    except IndexError:
        next_q = modList[0]
    try:
        previous_q = modList[place-1]
    except IndexError:
        previous_q = modList[-1]
    return f"/sql/basics/{previous_q}", f"/sql/basics/{next_q}"

def module_path():
    return "/sql/basics/"
'''
def e4_at_the_fairground_random():
    modList = moduleListGen("e4q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")
'''

# Just me making sure everything works...
def test():
    test_inst = question()
    return test_inst.returnAll()

def a1qa_what_is_sql():
    true = [
        'SQL stands for structured query language',
        'SQL is used to manage data in relational database management systems',
        'SQL is a domain specific programming language',
        'SQL is not a general purpose programming language'
        'RDBMS stands for relational database management system',
        'SQL arguably consists of a data query language (DQL), a data definition language (DDL), a data control language (DCL) and a data manipulation language (DML)',
        'SQL is a declarative language with proceedural elements',
        'SQL includes a data query language (DQL)',
        'SQL includes a data definition language (DDL)',
        'SQL includes a data control language (DCL)',
        'SQL includes a data manipulation language (DML)',
    ]
    false = [
        'SQL stands for standard query language',
        'SQL stands for structured query literal',
        'SQL stands for structured question language',
        'SQL is a general purpose programming language', 
        'SQL is an functional language',
        'SQL is an object oriented language',
        'SQL does not include a data query language',
        'SQL does not include a data definition language (DDL)',
        'SQL does not include a data control language (DCL)',
        'SQL does not include a data manipulation language (DML)',
        ]
    a1qa = cf.trueFalse(true, false)
    a1qa.previousQ, a1qa.nextQ = previousNext("a1q", 0, 3, cf.currentFuncName(), module_path())
    a1qa.questionBase = f'Which of the following statements about SQL is {a1qa.tf}:'
    a1qa.weblink = 'https://en.wikipedia.org/wiki/SQL'
    a1qa.workOn = 'What Structured Query Language is'
    return a1qa.returnAll()

def a1qb_what_sql_does():
    true = [
        'SQL can execute queries against a database',
        'SQL can retrieve data from a database',
        'SQL can insert records in a database',
        'SQL can update records in a database',
        'SQL can delete records from a database',
        'SQL can create new databases',
        'SQL can create new tables in a database',
        'SQL can create stored procedures in a database',
        'SQL can create views in a database',
        'SQL can set permissions on tables, procedures, and views',
    ]
    false = [
        'SQL can be used to propogate database information to a web page',
        'SQL can take data from a list in another language and insert it into a database',
        'SQL cannot execute queries against a database',
        'SQL cannot retrieve data from a database',
        'SQL cannot insert records in a database',
        'SQL cannot update records in a database',
        'SQL cannot delete records from a database',
        'SQL cannot create new databases',
        'SQL cannot create new tables in a database',
        'SQL cannot create stored procedures in a database',
        'SQL cannot create views in a database',
        'SQL cannot set permissions on tables, procedures, and views',        ]
    q = cf.trueFalse(true, false)
    q.previousQ, q.nextQ = previousNext("a1q", 0, 3, cf.currentFuncName(), module_path())
    q.getAnswersAndIndicators()
    q.questionBase = f'Which of the following statements about SQL is {q.tf}:'
    q.weblink = 'https://www.w3schools.com/sql/sql_intro.asp'
    q.workOn = "What SQL can do"
    return q.returnAll()

def a1qc_database_brands():
    true = [
        'MySQL',
        'Microsoft / Sybase',
        'MonetDB',
        'Oracle',
        'PostgreSQL',
        'SAP HANA',
        'MongoDB',
        'IBM DB2'
    ]
    false = [
        'PythonDB',
        'JavaDB',
        'JavaScriptDB',
        'CythonDB',
        'PythonDB',
        'GoDB',
        'FortranDB'
        ]
    q = cf.trueFalse(true, false)
    q.previousQ, q.nextQ = previousNext("a1q", 0, 3, cf.currentFuncName())
    q.getAnswersAndIndicators()
    areNot = "is" if q.tf == "true" else "is not"
    q.questionBase = f'Which of the following {areNot} a relational database which uses SQL:'
    q.weblink = 'https://www.trustradius.com/relational-databases'
    q.workOn = "Popular relational databases"
    return q.returnAll()

def a1qd_database_entities():
    true = [
        'a database can contain one or many tables',
        'a table can contain one or more records or rows',
        'a table can contain one or more fields or columns',
        'a record is a horizontal entity',
        'a field is a vertical entitiy',
        'each field in a table is represented by a column',
        'each record in a table is represented by a row', 
        'each field in a table has a name',
        'each table in a database has a name',
        'a record is a group of related fields',
        'fields contain defined types of data '
    ]
    false = [
        'a table can contain one or more databases',
        'a row can contain one or more tables',
        'a field can contain one or more tables',
        'a field can contain one or more records',
        'a record is a vertical entity',
        'a field is a horizontal entitiy',
        'each field in a table is represented by a row',
        'each record in a table is represented by a column', 
        'each record in a table has a name',
        'tables in a database are never named',
        'a field is a group of related tables',
        'field data type is never specified'
        ]
    q = cf.trueFalse(true, false)
    q.previousQ, q.nextQ = previousNext("a1q", 0, 3, cf.currentFuncName())
    q.getAnswersAndIndicators()
    q.questionBase = f'Which of the following statements are {q.tf}:'
    q.weblink = 'https://www.cengage.com/school/corpview/RegularFeatures/DatabaseTutorial/db_elements/db_elements2.htm'
    q.workOn = "Database entities"
    return q.returnAll()

def a2qa_statements():
    true = [
        'not all database systems require a semicolon at the end of each SQL statement',
        'semicolons are commonly used to show the end of an SQL statement',
        'SQL keywords are not case sensitive',
        'SQL keywords are commonly written in upper-case',
        'SQL is not a case sensitive language',
        'table and field names are commonly written in lower-case',
        'two or more SQL statements can be executed in the same call to the server if seperated by semicolons in systems that allow it',
        'most actions performed on databases are done with SQL statements',
        'SQL is case insensitive, but case is used to make it more readable',
        ]
    false = [
        'all database systems require a semicolon at the end of each SQL statement',
        'SQL keywords are case sensitive',
        'SQL keywords are never written in upper-case',
        'SQL keywords are written in lower-case',
        'SQL is a case sensitive language',
        'table and field names are commonly written in upper-case',
        'table and field names are never written in lower-case',
        'two or more SQL statements can be never be executed in the same call to the server',
        'full stops are commonly used to show the end of an SQL statement',
        'parenthesis are commonly used to show the end of an SQL statement',
        'commas are commonly used to show the end of an SQL statement',
        'dollar signs are commonly used to show the end of an SQL statement'
        'most actions performed on databases are done using python',
        ]
    q = cf.trueFalse(true, false)
    q.previousQ, q.nextQ = previousNext("a2q", 0, 3, cf.currentFuncName())
    q.getAnswersAndIndicators()
    q.questionBase = f'Which of the following statements are {q.tf}:'
    q.weblink = 'https://www.w3schools.com/sql/sql_syntax.asp'
    q.workOn = "General rules for SQL statements"
    return q.returnAll()

def a2qb_commands_starting_statements():
    true = ['SELECT','UPDATE','DELETE','INSERT','CREATE','ALTER ','DROP',]
    false = ['WHERE','BETWEEN','AND','ALL','BETWEEN','CHECK','CONSTRAINT','DISTINCT','EXISTS','FROM','LIKE','NOT','OR','TABLE','VALUES','WHERE']
    q = cf.trueFalseCode(true, false)
    q.previousQ, q.nextQ = previousNext("a2q", 0, 3, cf.currentFuncName())
    q.getAnswersAndIndicators()
    areNot = "can" if q.tf == "true" else "can't"
    q.questionBase = f'Which of the following commands {areNot} be used at the start of an SQL statement:'
    q.weblink = 'https://www.w3schools.com/SQl/sql_ref_keywords.asp'
    q.workOn = "Commands which start SQL statements"
    return q.returnAll()

'''
def a2qb_commands_starting_statements():
    previousQ, nextQ = previousNext("a2q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = ['SELECT','UPDATE','DELETE','INSERT','CREATE','ALTER ','DROP',]
    false = ['WHERE','BETWEEN','AND','ALL','BETWEEN','CHECK','CONSTRAINT','DISTINCT','EXISTS','FROM','LIKE','NOT','OR','TABLE','VALUES','WHERE']
    code, hint = None, None
    answercode, a1code, a2code, a3code, a4code, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    areNot = "can" if q == "true" else "can't"
    questionBase = f'Which of the following commands {areNot} be used at the start of an SQL statement:'
    answer, a1, a2, a3, a4 = None, None, None, None, None
    help, weblink, video = None, 'https://www.w3schools.com/SQl/sql_ref_keywords.asp', None
    workOn = "Commands which start SQL statements"
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci, workOn)
'''

def a2qc_create_statements():
    names = ['duck', 'stool', 'door','cup', 'tennis', 'pool','monkey','chair','orange','fruit','trampoline','beef','employees','customers','shoes','pants','troopers','rioters','clocks']
    data_types = ['INT','TEXT','DATE','TIME',f'CHAR({randint(1,20)})','REAL','DEC', 'BOOLEAN', f'BINARY({randint(1,16)})']
    entities = ['DATABASE', 'TABLE',]
    choice = randint(0, len(entities)-1)
    entity = entities[choice]
    name = names[randint(0, len(names)-1)]
    answer = f'CREATE {entity} {name}'
    data = '('
    for i in range(randint(1,4)):
        data += f"{names[randint(0, len(names)-1)]} {data_types[randint(0, len(data_types)-1)]}, "
    data = data[:-2] + ')'
    if choice == 0:
        a,b,c = f'CREATE {name} {entity};', f'CREATE {entity} {name} {data};', f'CREATE {entity};'
        answer += ';'
    else:
        answer += data + ';'
        a,b,c = f'CREATE {name} {entity};', f'CREATE {entity} {data} {name};', f'CREATE {entity} {data};'
    q = cf.selectCorrectCode(answer, [a,b,c])
    q.previousQ, q.nextQ = previousNext("a2q", 0, 3, cf.currentFuncName())
    q.getAnswersAndIndicators()
    q.questionBase = f'Which of the following statements for creating a {entity} named {name} is valid:'
    q.weblink = 'https://www.w3schools.com/SQL/sql_ref_create.asp'
    q.workOn = "statements using CREATE"
    return q.returnAll()




"""
Common commands
    CREATE TABLE - creates a new table  
    CREATE DATABASE - creates a new database
    CREATE INDEX - creates an index (search key)

    SELECT - extracts data from a database

    UPDATE - updates data in a database
    INSERT INTO - inserts new data into a database
    ALTER DATABASE - modifies a database
    ALTER TABLE - modifies a table

    DELETE - deletes data from a database
    DROP TABLE - deletes a table
    DROP INDEX - deletes an index

Syntax
    statements
    patterns
    examples of each keywords
    create
    read
    update
    delete
"""