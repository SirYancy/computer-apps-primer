# TUTORIAL 3 - Absolute References

**Absolute references** are one of the tricker concepts in learning how to use Excel. So here's another example to help us work through an idea that trips up a lof of newcomers to Excel and spreadsheets.

## A Times Table

We are going to build a "times table". You remember these from elementary school. They were _supposed_ to help you learn how to multiply small numbers (1 through 10 or 12) together. With Excel, we can build a times table really quite quickly.

1. Start with a new worksbook and a blank worksheet.
2. Add the basic structure of a times table. Start with the numbers 1 through 10 in cells `B2` through `K2`. And again 1 through 10 in cells `A3` through `A12`. You can use the **Fill Handle** to expedite this process. Feel free to style the cells as you like. ![1][1]
3. Now, how does a times table work? You multply the number from the column by the number of the row. So in cell `B3` enter the formula `=B2*A3`. ![2][2]
4. Select cell `B3` again and drag the fill handle across through cell `K3`. Immediately, you should notice that something is amiss. Since our original formula used **relative references**, the numbers have not incremented correctly. Double click on cell `K3` and you will see what happened. In fact, if you filled in the entire table this way, you will actually overflow Excel's abillity to represent very large numbers! ![3][3]
5. Let's try to use an absolute reference. Clear out the table. In cell `B3`, enter the formula `=$B$2*$A$3`. Remember, you use the dollar signs to lock in the cell references so that they don't change.![4][4]
6. Now drag the fill handle out and fill in the table. Observe what happened. Fill in the whole table and it will be 1s all the way down.<br> ![5][5] <br> Since we used a pure **absolute reference**, every cell is just multiplying cells `B2` and `A3`. To fix this we'll use what's called a **mixed reference** which is just a mixture of absolute and reltavie references. We are only going to lock in one coordinate from each operand. In order to do this, we need to look carefully at which coordinates need to be constant and which ones need to change.
8. Clear the table again. In cell `B3` input the formula `=B2*$A3`. Notice that the only coordinate we have locked in is the A from the second operand. Think of what that means. It will ensure that when we drag the fill handle the _right_ that each of `B2` through `K2` will be multiplied by the contents of cell `A3`. ![6]
9. Of course, if you drag the fill hand down now, you run into a problem. The column in the second operand sayted in the first column, exactly as we wanted it tod, but the _row_ in the first operand did not. ![7]
10. To fix this, we need to **lock in the row number of the first operand**. So erase everything and again, in cell B3, enter the formula `=B$2*$A3`. Now, drag the fill handle out and see the resulting, perfectly accurate, 10 by 10 times table. <br>![8]

<div class="alert alert-info" markdown="1">
    **Note:**  At this point, you could extend the times table out as far as you like and Excel would automatically fill it in, quickly and accurately.
</div>

## Conclusion

The subtle nuances of relative and absolute refernces is a little tricky to get the hang of. And the best way to get really around it is going to be just practice, patience, and dilligence. Make sure that the results you're getting make sense. Don't just trust Excel because it doesn't know what you're _trying_ to do. It only knows what you _do_. So the rule: _Make sure the output you're getting makes sense!_

Upload this to the portal when you are finished.


[1]: images/abs_ref/times_table_1.png
[2]: images/abs_ref/times_table_2.png
[3]: images/abs_ref/times_table_3.png
[4]: images/abs_ref/times_table_4.png
[5]: images/abs_ref/times_table_5.png
[6]: images/abs_ref/times_table_6.png
[7]: images/abs_ref/times_table_7.png
[8]: images/abs_ref/times_table_8.png
