# TUTORIAL 2 - Formulas 2

In this tutorial, we will look at more complex ways of building formulas and learn some of the tricks of Excel which will allow us to work more quickly and efficiently.

## This tutorial covers

* The fill handle
* Order of operations
* Relative references
* Absolute references

## The Fill handle

1. Open Excel and create a new workbook.
2. In cell **A1**, type _January_. <br /> ![image 1][image1]
3. Click and hold the **Fill Handle** and begin dragging to the right.
4. Watch the **tooltip** as it cycles through the months until you reach December.<br /> ![tooltip][image2]

This method of using the Fill Handle can be used in all sorts of different ways. The Fill Handle will automatically fill and _increment_ abbreviated months, days of the week, Numbers, dates, times, and, as we shall see, cell references. <br /> ![fillhandle][image3]

Let's look at a couple other ways to use the Fill Handle.

1. Download this [start file]. (Right-Click and click _Save target as..._). <br /> ![start file][image4] <br /> This file contains a list of bills for a year in one household.
2. In cell `N2` enter the word _Totals_.
3. In cell `N3`, enter a formula that adds together all of the numbers in the first row of the table:
  1. Press `=`, click on cell `B3`, press `+`, click on cell `C3`, press `+`, and so on, until you reach the end of the row.
  1. The formula should be `=B3+C3+D3+E3+F3+G3+H3+I3+J3+K3+L3+M3`: <br /> ![first formula][image5]<br /> **Note:** There are easier and better ways to do this, but for now, we'll stick to techniques that we know.
2. Press **Enter**. The total should read `1436`.
3. Now for the magic part. Re-select Cell `N3`.
4. Click on the fill handle and drag it down across cells `N4` through `N7`<br />![fill handle][image6]
5. Release the right mouse button and then column will fill in with the totals of each row.<br /> ![totals][image7]
6. Click on each of the cells this totals column and carefully examine the formulas that have been inserted into them. Notice that in each one, the only difference in the formulas is the row number of each cell reference. Excel has automatically incremented these row numbers for each row. And it did this in a way that you can rely on.
7. Let's do a totals row. In cell `A7`, enter the word _Totals_. And then in cell `B7`, enter the formula `=B3+B4+B5+B6`. When you hit **Enter**, the total should read 555.
8. Now, select cell `B7` again and grab the fill handle and drag it to the right across to cell `N7`.
9. Now, notice how each total has automatically incremented the column letter exactly as expected.<br />![final][image8]
10. Feel free to style it however you like.

## Absolute references

Next we'll look at another way to reference cells.

1. In the same workbook, go to the **Payroll** worksheet.<br /> ![payroll1][image9]
2. First, let's calculate gross pay for the first employee. This is a simple multiplication. In cell `D3`, enter the formula `=C3*B3`. Press **Enter**.<br />![payroll2][image10]
3. Drag the fill handle down to fill in the rest.
4. In Cell `A9`, type _Taxes_ and then in cell `B9`, enter _30%_. (This is a very simplified example of a payroll spreadsheet).<br />![payroll3][image11]
5. To calculate Frank Zappa's taxes, you'd multiply the Gross Pay by the taxes. Specifically, in cell `E3`, enter the formula `=D3*B9`. Press **Enter**. The expected result of _160_ will show.
6. Drag the fill handle down to fill in the rest. You should immediately recognize something is amiss.<br />![payroll4][image12]
7. The solution is to use an **absolute reference**. Change the formula in cell `E3` to read `=D3*$B$9`. This makes the reference to cell `B9` absolute. Now, when you drag the fill handle down, the reference to cell B9 will not change, giving us the expected results.<br /> ![payroll5][image13]
8. The final column should be easy.<br />![payroll6][image14]

Upload your resulting file to the portal.
<!-- Files-->
[start file]: res\bills_start.xlsx

<!-- Images -->
[image1]: images/formulas2/2-1.png
[image2]: images/formulas2/2-2.png
[image3]: images/formulas2/2-3.png
[image4]: images/formulas2/2-4.png
[image5]: images/formulas2/2-5.png
[image6]: images/formulas2/2-6.png
[image7]: images/formulas2/2-7.png
[image8]: images/formulas2/2-8.png
[image9]: images/formulas2/2-9.png
[image10]: images/formulas2/2-10.png
[image11]: images/formulas2/2-11.png
[image12]: images/formulas2/2-12.png
[image13]: images/formulas2/2-13.png
[image14]: images/formulas2/2-14.png
