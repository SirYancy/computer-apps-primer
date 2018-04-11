# Reports

The final object that Access has in its core toolset is the **Report**.

<dl>
    <dt>Report</dt>
    <dd>In Access, a report is a formatted document containing information pulled from a table or query that is printable and readable. The purpose of a report is for printing and exporting to other document formats, such as a PDF.</dd>
</dl>

## Tutorial

### Full Report

Let's create a report that outputs a formatted list of every record in the collection. Open your copy of the database. If you have not completed the other tutorials, you must do this now or you will not be able to continue.

1. Go to the **Create** tab and click on **Report Wizard** tool. <br> ![1][1]
1. In the first page of the wizard, select the ArtistQuery and add all of the fields. <br> ![2][2]
1. Next, ensure that the data is grouped *by Artists*. This will ensure that the table will list each album underneath the name of the artist, which is a good way to organize this information.<br> ![3][3]
1. We don't really need any further grouping levels, however, observe that it is possible to do so. You might, for example, create a report using *genre* as the top level grouping and then *artist* as next level grouping. But we'll leave it as it is for this report. <br> ![4][4]
1. The next page asks us how we want our data sorted. Let's sort the records by release date. In the first drop down, select *ReleaseDate* and hit **Next**. <br> ![5][5]
1. You can lay out the report in several different ways, and I encourage you to re-do this report a couple times so that you can see how they all look. But for now, we'll just use the default **Stepped** layout. <br> ![6][6]
1. Name it "Artists Report" and **Finish**. Observe the results: <br> ![7][7]

### Fixing Any Problems

It looks pretty good, but, you may have to do a little cleaning up. For example, see how part of the *RealeaseDate* heading is cut off in this one. If you have such issues, here's how to fix them.
 
1. First, click **Close Print Preview**. You'll end up in **Design** view which shows you all of the elements of the report. This is a powerful tool, but it is tricky to use. For our purposes, we just want to tweak things just a little bit. First, the **ArtistName** header box can be shrunk a bit. Select it, and click and drag on the right edge to make it a little smaller. And then drag the left edge of the *ReleaseDate* header box to make it large enough to accomodate all of its text. <br> ![8][8]
1. Next, switch to **Report View** and observe the result. ![9][9]
1. In lieu of printing this assignment and keeping with the course's almost all digital policy, we will export the report to a pdf for submission. Click on the **View** tool and switch to **Print Preview**.<br> ![10][10]
1. In **Print Preview**, in the **Data** group, click the **PDF or XPS** tool. This will allow you to publish the report as a document. <br> ![11][11]
1. Choose a suitable place to save the document and then open it to see what it looks like. <br> ![12][12]
1. You will submit this pdf as part of the assignment, so hang on to it.

### One More Report

1. On your own, create one more report from the data in this database. It can be structured any way you like. Export it to a pdf.

### Submission

For this tutorial, you should submit your compacted database file and both pdf files to the class portal. All three files are required. Because it's good practice.

<!-- IMAGES -->

[1]: images/reports/1.png
[2]: images/reports/2.png
[3]: images/reports/3.png
[4]: images/reports/4.png
[5]: images/reports/5.png
[6]: images/reports/6.png
[7]: images/reports/7.png
[8]: images/reports/8.png
[9]: images/reports/9.png
[10]: images/reports/10.png
[11]: images/reports/11.png
[12]: images/reports/12.png

