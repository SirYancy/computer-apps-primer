# Database Tools and Queries
A database is only as good as its tools for organizing, searching, and sorting its tables. In 1876, a man named Melvil Dewey built a system for organizing books and cataloguing them in a collection with index cards and codes. Today, this system is called the _Dewey Decimal System_ and it is the basis for all library databases today, digital or otherwise. The reason the Dewey Decimal System was so popular was how easy it was to implement and reference. As long as a librarian keeps books where they belong and stay on top of organization, a library is the ultimate research tool. This remains true today.

A _query_ in Access is sort of like a table, but it picks and chooses data from one or more other tables and queries to build a new set of data that is filtered, customized, and sorted. In fact, in many ways, a query can then be treated like a table and has a lot of the same features.

Over the next tutorials, we will begin constructing a series of queries. At first, we will learn how to query our database as it is now. Then you will add two more tables, populate them with data, and build a couple queries on your own based on those new tables. So, let's build a basic query.

# Building a query
The in-progress start file can be downloaded [here][start].

For our first query, imagine it's springtime and we want to send out a mass e-mail to all of our customers with dogs advertising our flea and tick treatment clinic. To do that, we need a list of email addresses and dog names from our database. So open your database file and follow along.

![start][1]

Before beginning, we should take a moment to consider what information we will want in our Query. We will want the customer's name and e-mail address. We will want the pet's name as well. And, because we are specifically targeting dogs, we will also want the pets' species. So let's begin.

1. Leave all of the tables closed and go the **Create** tab. In the **Queries** group, select the **Query Design** tool.
2. In the **Show Table** dialogue, we must decide which tables to draw our query data from. This example requires data from all three tables, so we will add all three tables to the query. Click on each one in turn and press the **Add** button. They should appear in the work area.<br /> ![2][2].
3. **Close** the **Show Table** dialogue. Take a look around to get a feel for this new screen and its tools. We have a new context tab called **Query Tools: Design**. There are three panes in the work area. The top one shows our table structure, or at least whatever is relevant to this particular query. The bottom will be where we will list the required fields for our query. On the right, the **Property Sheet** lists some meta data that we will look at a little bit, but for now we can close until we need it later.
4. To add the pet owner's name to the query, simply look in the _Customer_ box of our table structure, and double click on `CustomerName`. You will notice that the field information will appear in the first slot in the query structure pane at the bottom of the window.<br /> ![3][3]
5. Since this is an email campaign, also add the customer's email address to the set of fields. <br /> ![4][4]
1. Now, in order, also add the last two fields:
  1. **PetName** from the _Pet_ table
  2. **SpeciesName** from the _Species_ table
3. Now, we need a way to filter out just the dogs. So, in the bottom pane, look at the entry for SpeciesName. Let's take a closer look at what all is here:
    4. **Field**: the name of the field in its original table
    5. **Table**: the name of the table the field is in
    6. **Sort**: allows us to determine a sort order for our query. It can attempt to honor as many sort criteria you wish.
    7. **Show**: determines whether the field will actually show in our query results.
    8. **Criteria**: allows us to filter the query result based on specific values
    9. **or**: has the power to create multple filter **criteria**.
10. Under **SpeciesName**, in the **Criteria** box, type `"Dog"` including the quotation marks. Then, uncheck the **SpeciesName** field's **Show** box.
1. Lastly, under the **CustomerName** field in the query, change the **Sort** property to **Ascending**. Your final query should look like this: <br /> ![5][5]
1. Finally, in the **Query Tools: Design** tab, in the **Results** group, click the **Run** tool. It is signified by a big red exclamation mark. You can't miss it: <br /> ![6][6]
2. The end result is a list of all of the customers, who own dogs, in alphabetical order, including their email addresses and the names of their dogs.<br /> ![7][7]

Using a query like this really shines when using software integrations like the **Mail-Merge** toolset in **Microsoft Word** or **Outlook**. You could write a form letter and have the software automatically drop in the customer's name and the name of his or her pet and then send them out with a few clicks. But that is beyond the scope of this tutorial.

# Build another Query

Let's say we want to send out a birthday card to all of the pets whose birthdays are this month, April 2017. We will need the following information:
* Customer names
* Mailing addresses
* Pet names
* Pet birthdays
* Pet species - so we can customize their birthday cards

Close all active tables and queries and let's give it a shot.

1. Under the **Create** tab, fire up the **Query Design** tool.
2. You're going to need all three tables, so add them and then close the _Show Table_ dialogue.
3. We need the following fields, then:
    4. Customer -> **CustomerName**
    5. Customer -> **StreetAddress**
    6. Customer -> **City**
    7. Customer -> **State**
    8. Customer -> **ZIP**
    9. Pet -> **PetName**
    10. Pet -> **birthday**
    11. Species -> **SpeciesName** <br /> ![8][8]
12. Next, we will want to tweak our filter criteria and our sort ordering. Let's sort the query alphabetically by customer name. So under CustomerName, change the sort to **Ascending**.
13. Now, under Birthday, we want to filter out all of the pets whose birthdays are in April. This is tricky and requires some up-front knowledge.

<!-- Files -->
[start]: res/vet3_start.accdb

<!-- Images -->
[1]: images/5-5/1.png
[2]: images/5-5/2.png
[3]: images/5-5/3.png
[4]: images/5-5/4.png
[5]: images/5-5/5.png
[6]: images/5-5/6.png
[7]: images/5-5/7.png
[8]: images/5-5/8.png
