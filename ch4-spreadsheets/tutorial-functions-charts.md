# Functions and Basic Charts

It's not time to look at how we can visualize data. Let's create some charts!

For this tutorial, we'll look at some basic charting as well as some more statistical functions.

## Charts

First, though, we should think about charts and what they're for. Charts and graphs are for visualizing data, but it can often be tricky to decide just what kind of chart to use. So how do we decide? Here's a basic rundown, then we'll look at a couple of examples:

| Chart Type   | When to use it                                                                                                                                           |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Line Graph   | Line graphs are used to track changes over time. So if there's a time dimension, use a line graph                                                        |
| Pie Chart    | Use a pie chart to compare parts of a whole. Like a pie!                                                                                                 |
| Bar Graph    | Like a line graph, used to compare changes over time, but usually best for large changes. Can also be used to to compare things between different groups |
| Scatter Plot | If you have two variables that relate to each other, you can set one to the X axis and one to the Y axis. It shows the relationship between two things   |

What does each one look like?

### Line Graph

A line graphs are really great for showing changes over time. A very common example would be to show stock prices changes over time. For a fun contemporary look at a line graph, here's the price of BitCoins over the last year.

<figure>
    <img src="images/tutorial_charts/bitcoin.png" alt="Bitcoin">
    <figcaption>The price of a Bitcoin in USD($) over the last year.</figcaption>
</figure>

As you can see, it gives a fantastic visualization of the change in price over the last year for the most famous crypto-currency. By the way, if you're curious, you can get a good overview of Bitcoin on [wikipedia](https://en.wikipedia.org/wiki/Bitcoin). If you're really interested, the original [whitepaper](https://bitcoin.org/bitcoin.pdf) for Bitcoin is only 8 pages long and is a pretty interesting read as well.

### Pie Chart

A pie chart is great to compare parts of a whole. A particularly infamouse example would the United States budget. Here's a comparison of US spending vs US revenue in two pie charts:

<figure>
    <img src="images/tutorial_charts/us-budget.png" alt="US Budget">
    <figcaption>The FY 2016 US federal spending vs revenue. Source: Wikipedia</figcaption>
</figure>

### Bar Graph

Bar graphs are great for comparing different groups of things. For instance, this chart shows the what percent of US households earn what amount of money in $5000 increments. Except for the last couple of bars, which are clearly labeled. The purpose of the chart is to show income inequality in the United States and illustrates the point quite nicely. Though, of course, it only tells part of the story. The whole story is, perhaps, somewhat bleaker even than this. But that's beyond the scope of this tutorial.

<figure>
    <img src="images/tutorial_charts/household-income.png" alt="household income">
    <figcaption>Distribution of Annual Income Source: US Census Bureau</figcaption>
</figure>

### Scatter Plot




## Tutorial

We're going to take another look at the yearly bills worksheet that we saw in a previous tutorial.

1. Download the [start file](http://erickuha.com/primer/excel_resources/charting_start.xlsx)
1. Reacquaint yourself with the data in the table. It has already been formatted for you. Let's add some more data
1. Add a total row and a total column in the way that you wish. Ensure that it looks like this: <br> ![1][1]

Now we're going to add some columns for statistics. In particular, the **AVERAGE()**, **MAX()**, **MIN()** functions and a "percent of total" column. This way we can get some more data to include in our charts. 

| Function  | Purpose                                                    |
|-----------|------------------------------------------------------------|
| AVERAGE() | Adds all cells together and divides by the number of cells |
| MAX()     | Finds the highest number in a range of cells               |
| MIN()     | Finds the lowest number in a range of cells                |

Follow along:

1. In cell **O2**, enter the new column heading *AVERAGE*. Hit **ENTER**.
1. In cell **O3**, enter the average function. Type ``=AVERAGE(``, then highlight the range **B3:M3**. Make sure you do not include the average column. Notice that when you hit enter, the entire column fills with averages. Excel has intelligently predicted what you are trying to do as a consequence of formatting the data as a table. Adjust the number of decimal places shown so it looks nice. <br> ![2][2]
1. Follow the same process for Columns **P** and **Q** and the MAX() and MIN() functions. The result should look like this: <br> ![3][3]
1. In cell **R2**, enter the new heading *Percent of Total*.
1. Select cell **R3**. Enter `=`, click on cell **N3** (the total for the heating bill), press `/` for division, and click on cell **N7** (the total for all bills), finally press **F4** on the keyboard to convert the reference to **N7** into  an absolute reference. The final formula will end up looking like this (note how Excel automatically re-labels some cell references): `=[@Total]/$N$7`. When you hit **Enter**, it should fill in the rest of the column autmoatically!
1. Change the number format of these cells to percentages, resize the column, and you should have something that looks like this: <br> ![4][4]

Now, we want to make some charts. It would be useful to see how various bills fluctuate throughout the year. So we'll want to build a basic line graph.
