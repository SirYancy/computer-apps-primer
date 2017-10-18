# Tables and Data

We need to populate the database and its tables with actual data in order for this to be interesting. So let's start looking into that, but first, we have to make a couple of minor changes to our tables. 

## Fixing Some Problems

We all make mistakes. And we're going to correct them. There is something amiss with how we are formatting our dates. I had wanted us to use the input mask to make our dates look how we want, but there are two main problems with it. First, it is incredibly difficult to find exact release dates for vinyl records, so our data would be incomplete. So we're going to restrict it just to the year. Second, there's something buggy about the input mask and I'm not really sure what it is, so we're going to change the data type to just a number and go with that.

1. Open up your database file from the previous tutorial.
1. First, open the *Albums* table. In the **Home** tab, click the **View** button at the far left of the ribbon. Now you should be in *Design View*.
1. Select the *Data Type* for *Release Date* and change it to **Number**. Clear the **Input Mask** in the in the *Field Properties* section at the bottom of the window. It should look like this: <br> ![1][1]
1. Save and close the *Albums* table and open the *Artists* table.
1. Here, we're going to change the *ArtistID* field to the **Number** Data Type. So go to *Design View* and make the necessary change. The reason for this is it will make it easier to import the data from an external file. After importing the data, you could certainly change it back to AutoNumber. <br> ![2][2]
1. Do the same thing with the Genre's table and then save and close all tables.

## Importing some data

Next, we will import some actual data. First, let's populate the Genre and Artist tables. Download the two data files.

* [artist.csv](http://erickuha.com/primer/access_resources/artist.csv)
* [genre.csv](http://erickuha.com/primer/access_resources/genre.csv)

Copy them all to your working directory so you don't lose them, and then let's get started.

1. First, make sure all of your tables are closed.
1. In the **External Data** tab, in the **Import** group, find the **Data Source** tool. You want to import from a file, and specifically, from a text file. <br> ![3][3]
1. The dialog that opens will have several options. Let's go through them.
    1. Under file name, click **Browse** and find the **artist.csv** file.
    1. Check the radio button next to **Append a copy of the records to the table** and select the **Artists** table.
    1. Click **OK** <br> ![4][4]
1. You should see the data appear in a small window at the bottom of the next dialog. Ensure that the **Delimited** option is selected and press **Next** <br> ![5][5]
1. Once again, ensure that the radio button next to **Comma** is selected. You should see the table split into columns. Also make sure there is a check next to **First Row Contains Field Names**. Press **Next**. <br> ![6][6]
1. In the final table, verify that you are importing to the Artists table and press **Finish**. No need to save the import steps.
1. Open the Artists table and observe the results. <br> ![7][7]
1. We're going to do exactly the same thing with the **Genres** table and the **genre.csv** file. It should look like this when you are done. <br> ![8][8]

## Adding some of the album data

We'll add a album records by hand because it's good to see how it works. So here's five of the albums from my collection in tabular form:

| AlbumName                   | ReleaseDate | ArtistID | GenreID |
|-----------------------------|-------------|----------|---------|
| Buddy Holly Greatest Hits   | 1977        | 1        | 1       |
| West Side Story             | 1963        | 2        | 2       |
| Camelot                     | 1960        | 2        | 2       |
| All Eyez on Me              | 1995        | 3        | 3       |
| Eagles: Their Greatest Hits | 1976        | 4        | 4       |

1. Close the Artists and Genres tables and open the Artists table.
1. Start at the first line, the ID numbers will be automatically generated and all you have to do is type into each field. **NOTE**: Remember to press **Tab** to move from field to field in each row.
1. Make sure you get the ArtistID and GenreID fields correctly marked. They should correspond to the correct artist and genres in the other two tables. <br> ![9][9]

## Importing the rest of the data

To fill out the rest of the Albums table, we'll use another csv file. The process will be similar to the other two tables

1. Close the Albums table. It won't work if the table is open.
1. Download the file: [albums.csv](http://erickuha.com/primer/access_resources/albums.csv)
1. In the **External Data** tab, select **New Data Source** and select **Text File**.
1. Select the albums.csv file and make sure to **append** it to the Albums table. Press **OK** <br> ![10][10]
1. Make sure to select **Delimited** and go to the next dialog.
1. Select **Comma** and check **First Row Contains Field Names**. <br> ![11][11]
1. Click **Next**, and then **Finish**.
1. Open the Albums table and observe the result: <br> ![12][12]

Save everything, repair and compact your database, and then upload it to the class portal.

In the next tutorial, we will begin querying our database.

<!-- Images -->

[1]: images/data/1.png
[2]: images/data/2.png
[3]: images/data/3.png
[4]: images/data/4.png
[5]: images/data/5.png
[6]: images/data/6.png
[7]: images/data/7.png
[8]: images/data/8.png
[9]: images/data/9.png
[10]: images/data/10.png
[11]: images/data/11.png
[12]: images/data/12.png
