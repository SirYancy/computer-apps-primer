# Working With Tables

The most fundamental object in a database is the table. The table is where all of the data goes. Everything in a database is derived from the data definitions in the table fields and the actual data in records in the table. We will start from the ground up. Follow along with this tutorial starting with an empty database, and you will have gained some experience building, editing, and tweaking tables as well as doing some light, not-too-strenuous data entry.

# Design your Database

We are going to build our veterinarian database from the ground up and enter some data into it. There is no start file. You're starting clean. But there is one important step that we have to complete before we begin, we need to plan our basic database structure. How many tables do we want? What fields should each table possess? What data types should each field possess? There are many, many considerations in database design, but we will look at a simple example. Let's say we just want basic patient information for our veterinary clinic. We will have three tables:
* Customers
* Pets
* Pet Species (this limits the sorts of pets we accept)

Here is a UML diagram of our basic table design ([UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language) is a modeling and design language that software engineers use to visualize the overall design of a system like a database or a complex program):

![tables1](images\5-3-tables-4.png)

These tables could be tweaked a little bit. It's always debatable whether you need separate fields for all of the different parts of a street address. Some people say you should always err on the side of more fields, others say you should always use as few fields as possible. We'll advocate for a middle-of-the-road approach here. Take a moment to examine the chart, see what each field represents, and what datatypes they are. Another big debate is whether *Name* should be split into First and Last name fields or just be one. For a veterinary clinic, we'll just leave it as one name field, though we may come to regret it later.

Look at the connections. We have one field in the **Pet** table called *Owner*. It has a relationship to the *ID* field in the **Customer** table. This is called a one-to-many relationship. Every pet has one owner, but any owner can possess as many pets as he or she likes. This relationship allows for that. There is also a relationship between the *ID* field in the **Species** table and the *Species* field of the **Pet** table. Each pet can only have one species (we would hope), but the clinic can accept as many species as it wants. In this way, we can also limit our clinic to accepting only certain species, or we can query our pet list based on species.

Let's start building our first table.

# Create a Database

The first step is to create a database. Open Microsoft Access and follow along.

1. Create a blank database.<br /> ![tables1](images\5-3-tables-1.png)
2. Call it vet.accdb<br /> ![tables2](images\5-3-tables-2.png)
3. Take a look around. There are two main work areas. The left pane shows a list all of the objects in your database. That is all of your **tables**, **forms**, **queries**, and **reports**. The main panel has your primary interface. It is here that you will work on whatever object you are currently editing. Right now, it's displaying a blank table called **Table1**.<br /> ![tables3](images\5-3-tables-3.png)
4. Your first table already has one field, called **ID**. Let's add a field for the customer name. Click where it says *Click to Add* and select Short Text. Name the field **CustomerName**. Note, you should not simply use the word *Name* for this field as this is a reserved word in Access and can cause strange behavior. <br /> ![tables5](images\5-3-tables-5.png)
5. Add the rest of the fields as they are laid out in our UML diagram. As for the **NumOfPets** field, let's just leave it as a number for now and come back to it. <table><tr><td>ID</td><td>Number</td></tr><tr><td>CustomerName</td><td>Short Text</td></tr><tr><td>PhoneNumber</td><td>Short Text</td></tr><tr><td>StreetAddress</td><td>Short Text</td></tr><tr><td>City</td><td>Short Text</td></tr><tr><td>State</td><td>Short Text</td></tr><tr><td>ZIP</td><td>Short Text</td></tr><tr><td>Email</td><td>Short Text</td></tr><tr><td>NumOfPets</td><td>Number(?)</td></tr></table><br /> **Note:** It is important to note that most of our fields are, in fact, text fields. This highlights the text-centric nature of databases.
6. Hit Ctrl-S to save the table and name it **Customer**.

# Refine the table

1. With the **Customer** table still open, in the **Home** tab, click the **View** button to switch to the **Design** view.<br />![tables6](images\5-3-tables-6.png)<br /> This view gives us a little more granular control over the different features and details that make up our table.
