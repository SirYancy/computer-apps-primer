# Database Tools: Reports
A report is a data-visualization tool. Reports are printable, reader-friendly tabular data. The information in a report can be drawn from any combination of tables or queries. Let's build a simple one first:

## A Simple Reports
If you wish, you can download the in-progress file [here][in progress]

We already have a query the shows all of the bills that are overdue. Let's convert that into a printable report.

1. Go to the **Create** tab. Under **Reports**, click **Report Wizard**. <br> ![2]
2. In the _Tables/Queries_ dropdown, select the _Query: Overdue Invoice Query_.
3. Add all fields except _VisitID_. Hit **Next**<br> ![2]
4. On the next screen, you can choose how the data will be organized. In this case, it will be useful to know which customers are the most delinquent, so we will view our data _by Customer_. Press **Next**. <br> ![3]
5. We don't need any more grouping levels, so hit **Next**
6. Sort by _DueDate_ in _Ascending_ order.<br>![4]
7. On the next screen, keep the _Stepped_ layout and _Portrait_ orientation. Hit **Next**
8. On the final screen of the wizard, name it **Overdue Report**, and make sure the radio is checked to preview the report. Hit **Finish**.<br>![5]
9. Immediately, you'll notice that, while mostly formatted very nicely, some of the dates are hashed out. Next, we'll fix this <br> ![6]
10. At the top of the screen, hit **Close Print Preview** and you should get booted back to the Report Design view. Here, you can adjust the sizing on various elements like, for example, the width of the Due Date box. <br> ![7]
11. Click on the DueDate box and drag its left edge by the handle until it's wide enough that you think it will accomodate just about any length date.<br> ![8]
12. Now, in the top right, change the View to **Print Preview** again and observe the results.<br> ![9]

## Make two more Reports from Queries
We have two more **queries** that might make good printable **reports**. Using the same procedure, build two more reports using the _DogQuery_ and the _AprilBirthdayQuery_. At any step of this process, make decisions that seem reasonable to you. If you don't like how the **Report** turns out, then simply delete it an start again, since this is, in general, a fairly quick process.


## Last Challenge - Add totals to the Overdue Invoices report
This tutorial is forthcoming, but will be demonstrated in class.


<!-- Files -->
[in progress]: res/vet5_reports_start.accdb

<!-- Images -->

[1]: images/5-8/1.png
[2]: images/5-8/2.png
[3]: images/5-8/3.png
[4]: images/5-8/4.png
[5]: images/5-8/5.png
[6]: images/5-8/6.png
[7]: images/5-8/7.png
[8]: images/5-8/8.png
[9]: images/5-8/9.png
[10]: images/5-8/10.png
