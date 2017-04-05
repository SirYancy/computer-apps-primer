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

Next, create appropriate relationships. **Hint:** Anything that was labeled as a Foreign Key needs to have a relationship.  After that, let's populate them with some data.

## Import Data

All of the data can be found in the [pets.xlsx file][pets] (Right-click and press **Save target as...**). Run through the steps (as seen in the [last tutorial](5-4-tables-2.md)) to bring the data from an Excel spreadsheet into these two new tables. There are about 300 records for vet visits and a corresponding invoice record for each visit.

## Create a Query

<!-- Files -->
[start]: vet3_start.accdb
[pets]: res/pets.xlsx

<!-- Images -->
[1]: images/5-5/1.png
