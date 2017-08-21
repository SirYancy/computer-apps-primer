# Basic Formulas and Formatting

We will be continuing our exploration of basic Excel tools. This tutorial continues our look at **We Got Widgets** and the order the Ned Flanders placed for a variety of high-quality, only vaguely defined, high-tech gadgetry.

## Background

A spreadsheet's primary duty is to make complex calculations easier, especially very repetitive calculations like those that would be performed on large tables of data. We already know that cells can contain text or numerical data. And we have the sense that it treats these two types of data slightly differently. But the problem is, that kind of data is static. It doesn't do anything. A huge table of data might be impressive, but once someone asks you what it means, you really won't be able to aticulate much. You can make it look nice, but you can't make it dance.

So what we want to do is create dynamic data. That is, we want to be able to put data in a cell that will change if data elsewhere in the spreadsheet changes.

Let's look at some of the basics of data analysis in Excel

### Formula basics

**Formula** - A formula is a mathematical expression that uses some combination of numbers **cell references**, and mathematical symbols to generate dynamic data

Creating a formula is relatively simple and follows rules that might seem familiar if you think back to high school mathematics. here are some of the most fundamental rules:

* Each formula *must* begin with an equal sign (=)
    * Think of the equal sign as your signal to Excel that _"Math is happening here!"_
* Each formula must be some combination of numbers and cell references
    * Formulas can contain any real number and as many of them as you like. But what really makes them shine is that you can include _references_ to other cells (more on this in a bit).
* Formulas can contain all of the basic arithmetic operators
    * The five basic arithmetic operations are all valid, though they might use different symbols than you are used to (see below). Plus, you can use **parentheses** for manipulating the order of operations.
* Formulas will obey the basic mathematical **order of operations**
    * Do you remember the mnemonic device: _Please Excuse My Dear Aunt Sally_? It's a way of remembering the order of operations. All arithmetic operations in a formula will follow this order: **P**arentheses, **E**xponents, **M**ultiplication, **D**ivision, **A**ddition, **S**ubtraction. Remember that multiplication and division have the same priority and happen left-to-right. Likewise with addition and subtraction. If you're a little rusty, click [here](https://www.mathsisfun.com/operation-order-pemdas.html)

Here are some of the arithmetic operators that Excel accepts:

| Operation      | Symbol |
|----------------|--------|
| Addition       | +      |
| Subtraction    | -      |
| Multiplication | *      |
| Division       | /      |
| Exponent       | ^      |
| Grouping       | ()     |


Using these basic rules, you can create just about any simple mathematical expression that you can imagine. Try these examples on a blank spreadsheet (don't forget to use the correct symbols and to start with an equal sign):

* `6 + 7 x 8`
* `16 &divide; 8 - 2`
* `(25 - 11) x 3`

### Cell References

In order to take full advantage of Excel, an important thing to get used to is the concept of a **cell reference**. You can use the addresses of other cells as though they were numbers and Excel will treat those references as though they were the values in the referenced cell. That way, if you cange the value of the referenced cell, the result of the formula will change as well.

## Tutorial

In this tutorial, we are going to create some dynamic content by using formulas. We will use the same file that you used in the last tutorial, so hopefully, you did not delete it or lose it. Go ahead and open it now and we'll get started.

### Adding a Cost Column

Our next step in making this a useful spreadsheet is to find out just how much Ned Flanders spent. With just a little bit of practice, you'll be able to do this in less than a minute, but let's take this step by step. First, let's look at each line item. Ned ordered four "rockwell retro encabulators" at $12.45 each. How much is that? Sure, you could do it longhand or even pull out your calculator and then type in the result, but this is tedious. Excel _is_ a calculator and it will do all of this _for_ you. First of all, we need to be sure we know exactly what mathematical operation we need to perform. Here, we have 4 items at $12.45 each and so, we are multiplying 12.45 by 4. But, rather than multiply the two number, let's multiply two _cell references_. Let's see what we mean: 

1. Select cell **G10**. Type the new heading **COST** and press **Enter**.
1. Now, in cell **G11**, you are going to enter your first formula. Type `=F11*E11`. Remember that the "*" is the Excel multiplication operator. Press **Enter** and observe the result. <br> ![1][1]

### Copying and Pasting Formulae

You could pretty quickly just repeat this process in the remaining four cells. However, this is not a pratical solution if you had a file with even a few dozen rows (not to mention a few thousand). There are two primary ways of accomplishing this and it all comes down to personal preference. You can either **copy-and-paste** or you can use the **Fill Handle**. We'll experiment with both. First, copy and paste:

1. Select cell **G11** again.
1. Copy the contents of the cell by pressing **Ctrl-c** on the keyboard, or clicking on the **Copy** tool on the ribbon in the **Home** tab.
1. Click on cell **C12**.
1. Paste your formula into this cell by pressing **Ctrl-v** on the keyboard, or clicking the **Paste** button on the far left of the ribbon.

Why didn't it just copy the previous cell exactly? Well, as it turns out, Excel is pretty smart. Its default behavior when you copy and paste a formula is to interpret cell references (like **F11** and **E11** in this case), _relative_ to the cell where the formula is being pasted. Think of it this way. From Excel's point of view, cell **G11** is multiplying the two cells to left of it. When you paste this formula into cell **G12**, it will do the same thing only it will multiply the two cells to the left of _it_, that is, **F12** and **E12**. This behavior is very, very important to our understanding of Excel and learning how to make it do what we want. Let's look at an even quicker way of handling this problem

### Use the Fill Handle



<!-- Images -->
[1]: images/tutorial1-2/1.png
