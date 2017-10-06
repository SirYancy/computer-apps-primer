# Pivot Tables

A pivot table is a dynamic summary table for analyzing large data sets which are difficult to parse on their own, even if they are well-formatted. Think of it as making a table out of your table. In this tutorial, we will take three months of sales data and compact it into a pivot table that can allow us to analyze the data more intuitively.

## Tutorial

1. Download the [start file](http://erickuha.com/primer/excel_resources/pivot_start.xlsx).
1. Examine the sheet and get a sense of what it's reporting. Each line is an individual sale of some product. Our goal will be to create a pivot table from this raw data.
1. First, we need to format our data as a table. **Click** somewhere inside the data and press **Ctrl-a** on the keyboard to select all of the table data. <br> ![1][1]
1. In the **Home** tab, click **Format as Table** and select a table style that you like. In the dialog, make sure to check *"My table has headers"*.
1. Make sure that at least one cell inside the table is selected. In the **Insert** tab, select **PivotTable** on the far left of the Ribbon. <br> ![2][2]
1. In the dialog, you will likely want to leave everything to its defaults. The options that should be selected are **Select a table or range** and place the table on a **New Worksheet**. Press **OK**. <br> ![3][3]
1. Now, you have a Pivot Table, but it doesn't have any data in it. Look around the new sheet. In the workseet itself, you have your empty pivot table. Whenever you have it selected, there will be a sidebar on the left which you can use to manipulate the structure of the pivot table. <br> ![4][4]
1. In the **Fields** box, put a check in the **Salesperson** and **Order Amount** fields. Observe how the pivot table is now showing the summary sales data for each salesperson. <br> ![5][5]

## Pivoting

Pivoting is the process of adding or reorganizing the data in your table. Let's try a few quick pivot operations.

1. Being able to see the total sales for each salesperson is instantly useful, but we can actually break it down further. Try this. In the Fields box, **click** on *Month* and **drag** it down to the **Columns** box to create a *Months* column in your pivot table. This is called, you can imagine, pivoting. <br> ![6][6] <br> Now, we have a column for each month and a total column for each salesperson.
1. Now, **drag** the month field from the *Columns* box and into the *Rows* box below the Salesperson field. Observe how the table changes. We now have only two columns but the monthly totals for each salesperson is included next to each month. <br> ![7][7]
1. You can even re-order the *Row* fields by clicking and dragging them to see what happens. <br> ![8][8]
1. You can also remove fields from the table. Uncheck the *Salesperson* field in the fields box and the table will now show only the monthly data. <br> ![9][9]
1. One more thing that you can do is change what is displayed in the *Values* box. Right now, we've left the *Sum of Order Amount* value in there. Click on the dropdown arrow next to *Sum of Order Amount* <br> ![10][10]
1. In the dialog that opens, change the type of calculation to *Average* and see how the table changes. It is now displaying the average total for each sale for each month. <br> ![11][11]

## Challenge

Let's do one last thing to finish off the tutorial before submitting it.

1. Pivot the table so that it shows average totals for each month in columns and for each salersperson in rows. The pivot table should look like this: <br> ![12][12]

When you are satisfied, submit your final file to the class portal as normal.

<!-- Images -->

[1]: images/tutorial_pivot/1.png
[2]: images/tutorial_pivot/2.png
[3]: images/tutorial_pivot/3.png
[4]: images/tutorial_pivot/4.png
[5]: images/tutorial_pivot/5.png
[6]: images/tutorial_pivot/6.png
[7]: images/tutorial_pivot/7.png
[8]: images/tutorial_pivot/8.png
[9]: images/tutorial_pivot/9.png
[10]: images/tutorial_pivot/10.png
[11]: images/tutorial_pivot/11.png
[12]: images/tutorial_pivot/12.png
