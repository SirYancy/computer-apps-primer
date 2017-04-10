# Database Tools and Queries

It's time to ramp up the complexity of our database a little bit. There is some much needed functionality that it is sorely lacking. If we are running a veterinary clinic, we are going to need some way of keeping track of all two more crucial things: vet visits and invoices for billing.

![diagram][1]

## Just Two More Tables

If your database has been compromised in some way, you can download an in-progress version [here][start] (Right-click and press **Save link as...**).

First, create a table called **Visit** with the following design in your database. Don't worry about populating it with data. That will be supplied for you.

| Field Name | Data Type  | Description | Field Properties                       |
|------------|------------|-------------|----------------------------------------|
| ID         | AutoNumber | Primary Key |                                        |
| PatientID  | Number     | Foreign Key | Caption: Patient ID                    |
| VisitDate  | Date       |             | Caption: Visit Date, Format: Short Date |
| Reason     | Short Text |             |                                        |
| WalkIn     | Yes/No     |             | Caption: Walk-in?                      |

Second, create a table called **Invoice** with the following desgin in your database. Again, the data will be provided for you.

| Field Name | Data Type  | Description | Field Properties                        |
|------------|------------|-------------|-----------------------------------------|
| ID         | AutoNumber | Primary Key |                                         |
| VisitID    | Number     | Foreign Key | Caption: Visit ID                       |
| Amount     | Currency   |             | Format: Currency, Decimal Places: 2     |
| DueDate    | Date       |             | Caption Due Date, Format: Short Date    |
| Paid       | Yes/No     |             | Caption: Is Paid?                       |

Next, create appropriate relationships. You're on your own for this, but if you get stuck, just look back through the last tutorial and give it a little thought and you should see what you need to do. **Do not forget to do this!**

<div class="alert alert-info"><strong>Hint:</strong> Anything that was labeled as a Foreign Key needs to have a relationship.  After that, let's populate them with some data.</div>

## Import Data

All of the data can be found in the [pets.xlsx file][pets] (Right-click and press **Save target as...**). There are about 300 records for vet visits and a corresponding invoice record for each visit. If you need a refresher, look over the steps (as seen in the [last tutorial](5-4-tables-2.md)) to bring the data from an Excel spreadsheet into these two new tables. There are about 300 records for vet visits and a corresponding invoice record for each visit. The only thing you really want to look out for is to make sure you are appending to the correct table and taking the data from the correct sheet.

# Build more Queries

Once you have the two new tables populated, let's build a couple more queries. Let's say we want to know which invoices are past due.

1. In the **Create** tab, click the **Query Design** button.
2. In the **Show Table** dialogue, add, the _Customer_, _Pet_, _Visit_, and _Invoice_ tables. You will not actually be using any of the fields from the _Pet_ table, however, you still need it here in order for the relationships to be valid. <br> ![query design][2]
3. We want to personally call all of these customers, so we will add the _CustomerName_ and _PhoneNumber_ fields from the _Customer_ table. Also, we will add, from the _Invoice_ table, the _Amount_, _DueDate_, and _Paid_ fields. <br> ![fields][3]
4. To start, enter **False**  in the _Criteria_ box of the _Paid_ field. Since we know that they will all be unpaid, you can uncheck the _Show_ box for this field as well.
5. Now, we want to create a calculated field that will display a message if the field is, in fact, overdue. So this field will be calculated based on today's date. Select the first empty query field name: <br> ![IIF][4]
6. We are going to use the `IIF()` function, which is functionally the same as the `IF()` funtion from Excel. It takes the following form: `IIF( <<test>>, <<value if true>>, <<if false>>)`. Notice that just like Excel, a function always had a name and parentheses that take parameters separated by commas.
  1. In this case, the `IIF()` function takes three parameters, a logical test (which should be either true or false), a "true" output, and a "false" output. The syntax for the final function looks like this:
  1. `IIf([DueDate]<Date(),"OVERDUE","")`
  1. So in this function, we are testing that the current DueDate is less than today's date (that is today's date is after it), and if it is, we are outputting "OVERDUE" and outputting nothing if it's not overdue using empty quotation marks as the third parameter. <br> ![func][5]
2. Notice that Access tags `Expr1:` to the beginning of your function when you hit **Enter**. Just delete that and replace it with `Overdue:` to make it look nicer. <br> ![finished func][6]
3. Lastly, change the **Sort** value in the **DueDate** field to _Ascending_.
3. Run the query and observe the results.
4. Save the Query as OverdueInvoiceQuery and close it.

<div class="alert alert-info"><strong>Note:</strong> There are so many overdue invoices for one of two reasons: 1) our veterinary clinic is way too nice to people or 2) that's just how the random data I generated turned out.</div>

## One More query

For your last query, here's a little test. Using all of the database query tools we've looked at, you should be able to complete this more or less on your own:

1. Create a query with customer names and phone numbers, that outputs a list of all of the pets that came to an office visit to receive shots in the month of April in any year. It should look roughly like this: <br> ![7][7]
2. Name it AprilShotsQuery and close it.

Now, save your database, run Compact & Repair, and turn it in to the portal.

<!-- Files -->
[start]: res/vet4_start.accdb
[pets]: res/pets.xlsx

<!-- Images -->
[1]: images/5-6/1.png
[2]: images/5-6/2.png
[3]: images/5-6/3.png
[4]: images/5-6/4.png
[5]: images/5-6/5.png
[6]: images/5-6/6.png
[7]: images/5-6/7.png
