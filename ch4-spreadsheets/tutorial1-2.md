# Basic Formulas and Formatting

We will be continuing our exploration of basic Excel tools. This tutorial continues our look at **We Got Widgets** and the order the Ned Flanders placed for a variety of high-quality, only vaguely defined, high-tech gadgetry.

## Tutorial

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
