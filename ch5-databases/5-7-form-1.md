# Database Tools and Forms

If you are the only user of a database, you don't have to worry that much about things getting out of hand. However, if you are working with a group, the _last_ thing you want is for other people to have access to the inner workings of your database. Protecting it from harm is your number two job after designing, maintaining, and updating. And you would not believe just how much damage a well-meaning coworker can visit upon your database without thinking.

So how do we solve this problem? **Access** has a system for building **Forms**. A **Form** in Access is a designed user interface which your users can interact with which keeps a layer between them and your databases more fragile components.

## Building your first Form

If necessary, download the [in-progress file].

You run a veterinary office, so you're going to need a way for the receptionist to input new customers into the database. So the first **Form** we'll build will be a form for creating a new _Customer_.

1. Open your database and under the **Create** tab, in the **Forms** group, click the **From Wizard** tool. For Queries and Tables, we built them from scratch. But for Forms, we'll find it a lot easier to let Access do the hard work.<br> ![1][1]
2. In the **Tables/Queries** dropdown, select _Table: Customer_. Add all of the available fields (Except NumOfPets, we will probably delete this field later as it has become superfluous). When complete, it should look like this: <br> ![2][2]
3. Hit **Next**. In the next step, select the _Columnar_ layout and hit **Next**.
4. Title it **Customer Form** and check the "_Modify the form's design_" radio button. Click **Finish**. <br> ![3][3] <br> What you see now is the **Design View**, where you can change the layout, add more fields, edit those fields, and change styles.
5. In the **Design** tab, change the **Theme** of the Form to something other than the default. <br> ![4][4]
6. **Save** the form and click the **Views** button in the **Views** group. You should now be in _Form View_. From here, you can create new records in your database and review existing ones. Take a look around.
    7. The main area of the form is in the middle of the screen. It typically shows the first record in the databse by default.
    8. At the bottom of the screen, you should see some basic controls. The arrows allow you to navigate record by record. The Search box allows you to search the table. And finally, the arrow with the star allows you to create a new record. <br> ![5]
9. Press the button to add a new record. Fill it in with whatever information you wish. The ID number should be whatever the number at the bottom of the screen is: ![6]
10. Save the form and close it.

## Customers Need Pets

Now, our customers need to have pets, otherwise they have no business going to a vet. So, we will add a pet Form. The only difference is, we're going to treat this one a little differently. Follow along:

1. In the **Create** tab, click **Form Wizard** again.
2. From the drop down, select _Table: Pet_. Add only the _PetName_ and _Birthday_ fields. We'll handle _Species_ separately since it's a foreign key (trust me). <br> ![7] <br> Click **Next**.**
3. Change the layout to _Datasheet_. We use this layout so that we may display multiple records at once. Click **Next**.
4. Check the radio button that says "_Modify the form's design_". Click **Finish**.
5. You will now be in the **Form Design Tools: Design** tab. The ribbon is dominated by a box which has different controls that we can add to our Form. We are going to add a control for the pet's species. We want this to be a dropdown picker so in the **Controls** box, click the _Combo Box_ button. <br> ![8]
6. Click in the form to the right of the PetName field. A dialogue will open. Use the following options:
    7. Check the radio button to _get the value from another table or query_. <br> ![9]
    8. Select **Table: Species** Hit **Next**.
    9. Add just the _SpeciesName_ field. Hit **Next**.
    10. Sort by _SpeciesName_ in _Ascending_ order. Hit **Next**.
    11. Leave _Hide key column_ checked. Click **Next**.
    12. You want to store the value in the _Species_ field.<br> ![10]
    13. Name it Species. Click **Finish**.
14. Moving and adjusting new forms can be frustrating. Move it around until it's in a logical place. Here's how I set mine up: <br> ![11]
15. Save it and go the **Form View**. Here you can add new pets, but it is missing a crucial piece of the Pet item. There is no way to assign an owner. Well, we're going to do that next. <br> ![12]

## Creating a Sub Form

So, consider the following question: Is there ever going to be a situtation where a new customer will not already be a pet owner? In all likelihood, the answer to this is _no_. Thus, we can actually combine the Customer Form with the Pet Form so that when a new customer is registered, we can also register all of their pets without having to switch to another form. This is accomplished as follows.

1. Open the _Customer Form_.
2. Switch to **Design View** (**Home** tab)
3. In the left panel, select the _Pet Form_ and drag and drop it right into the Customer Form, directly underneath the _Email Address_ field. **Note**: if for some reason it ends up in the _Form Footer_ area, scoot it up until it's in the _Detail_ area. At this point, you may have to resize a few things until it all fits, but the end result will look something like this: <br> ![13].
4. Switch back to Form View. Click through the entires and see their pets appear in the bottom sub-form. Try adding a new Customer and give that customer a pet or two.

When you are finished, save everything. Compact & Repair your database. Upload it to the portal.

<!-- Links -->
[in-progress file]: res/vet5_forms_start.accdb

<!-- images -->
[1]: images/5-7/1.png
[2]: images/5-7/2.png
[3]: images/5-7/3.png
[4]: images/5-7/4.png
[5]: images/5-7/5.png
[6]: images/5-7/6.png
[7]: images/5-7/7.png
[8]: images/5-7/8.png
[9]: images/5-7/9.png
[10]: images/5-7/10.png
[11]: images/5-7/11.png
[12]: images/5-7/12.png
[13]: images/5-7/13.png
