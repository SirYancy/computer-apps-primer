# Tables and Data

We need to populate the database and its tables with actual data in order for this to be interesting. So let's start looking into that, but first, we have to make a couple of minor changes to our tables. 

# Fixing Some Problems

We all make mistakes. And we're going to correct them. There is something amiss with how we are formatting our dates. I had wanted us to use the input mask to make our dates look how we want, but there are two main problems with it. First, it is incredibly difficult to find exact release dates for vinyl records, so our data would be incomplete. So we're going to restrict it just to the year. Second, there's something buggy about the input mask as we implemented it. It's not accepting any dates and honestly, I can't be bothered to figure out why.

Lastly, we are going to import most of our data from another sheet, which 
