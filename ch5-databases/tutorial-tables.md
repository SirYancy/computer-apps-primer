# Tables

The first Access object we will explore is the table. The basic idea of a table persists across almost all database software and these concepts will transfer easily if you decide to move on to more advanced database tools in the future.

The table is where all of the data goes. Everything in a database is derived from the data definitions in the table fields and the actual data in records in the table. We will start from the ground up. Follow along with this tutorial starting with an empty database and you will have gained some experience building, editing, and tweaking tables as well as doing some light, not-too-strenuous data entry.

## Designing the Database

The first step in building any database is to plan it. We have to decide on our database's basic structure. How many tables do we want? What fields should each table have? What data types would those fields have? There are many, many considerations in database design, but we will look at a simple example.

You have taken to collecting vinyl records (they're making a [comback](http://www.latimes.com/opinion/op-ed/la-oe-sax-analog-nostalgia-20160103-story.html)!). And since most of them are relatively inexpensive, you've acquired a lot of them in a fairly short period of time. You've decided that you want to keep better track of which ones you have. So you decide to build a database.

It's good to have this idea before we get started. There's a lot to cover, so I'll lay out the plan now and we will refer back to it as we move throughout this chapter. So don't worry if you don't know exactly what it means.

We will construct three tables. One for artists, one for genres, and one for albums. The album table is our primary table and will have the most fields. The others are supplementary and serve only to create relationships and organize the data.

The following diagram is what's called a UML diagram and gives us an idea of the structure of our tables:

<figure>
    <img src="images/tables/1.png" alt="uml">
    <figcaption>A <a href="https://en.wikipedia.org/wiki/Unified_Modeling_Language">UML diagram</a> helps us to organize our thoughts.</figcaption>
</figure>

These tables could probably be tweaked a little bit. You might want more or less information. The **Albums** table, for instance, might benefit from a field for the condition of the vinyl record. But these things can be added in later if we so desire. Though, it is possible that we may regret it later because it will be more data entry down the line.

Look at the connections between the three tables. We have one field in the **Genre** table called *ID* and it is connected to another field in the **Albums** table called *GenreID*. Make sense? Likewise, there is an *ID* field in the **Artists** table connected to the *ArtistID* in the **Albums** table.

Let's start building our tables

## Creating a Database

1. Open **Microsoft Access**. <br> ![2][2]  //TODO make this screenshot
