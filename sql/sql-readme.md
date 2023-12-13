# Summary

The focus of this module is to show you can craft SQL on a (sqlite3) DB with multiple tables. The script to create fake data ([db-gen.py](./db-gen.py)) and DB are already pre-created. The sqlite3 database `test.db` has already been created in this directory. We will write prompts to ask questions about this database.

# Pre-work

Here's the steps I took to get to a script that generates fake data. As a matter of requirements, I took the approach to design the back-end data first, then work toward the business logic. This is a common approach in the industry.

## Create an ERD from the table requirements.

Let's get a nice visualization and make sure we got our data model correct. Nothing else will matter if that's not right.

**Prompt**

```
Create me an ERD in mermaid format with the following requirements:

Table called User with fields:
    eamil_address - string
    first_name - string
    last_name - string
    customer_id (integer) - primary key 
Table called Orders:
    customer_id (integer) - primary key
    purchase_date (date-time)
    purchase_amt_dollars (float)
    proudct_id (integer) - foreign key 
Table called Products:
    product_id (primary_key, integer)
    product_name (string)

The customer has a one to many relationship to Orders with customer_id The Order table has a one to many relationship with Products with product_id
```

**Result**

Our relationship looks good and we have foreign key relationship we can join data on (customer_id and product_id).

```mermaid
erDiagram
    User ||--o{ Orders : "places"
    Orders ||--o{ Products : "contains"
    User {
        int customer_id
        string email_address
        string first_name
        string last_name
    }
    Orders {
        int customer_id
        datetime purchase_date
        float purchase_amt_dollars
        int product_id
    }
    Products {
        int product_id
        string product_name
    }
```

**TIP** Try the explain here on an inline Copilot prompt. For example:

* Highlight `User ||--o{ Orders : "places"`
* In the Copilot prompt, type `/explain places`

# Generate fake data

Now that we have our data model, let's generate some fake data. We'll use a python library called Faker to do this. We'll also use a python library called sqlite3 to create our DB and insert the data. We need to be careful on the prompt here to clarify the range of values for the custom_id and product_ids so that joins will return results.

**Prompt**

This was a "few shot" prompt that required me to really refine the results I wanted. In the end, this prompt generated fake data that would replicate real work scenarios so table joins would work.

```
create python code that will generate test data for all 3 databases. Create 10 rows in User, 50 rows in Orders, and 20 rows in products. generate the DB in the same directory as the script. User table customer_id must be unique with value from 1 to 20. The Orders table must only use customer_ids from 1 to 20 but can be duplicated.
```

**Result**

See [db-gen.py](./db-gen.py)


# Exploring the module

## Pre-requisites

Be sure to have `sqlite3` installed on the command line.

## Running the module

`sqlite3 test.db < <script name>`

Now we can explore how we can ask questions if fairly plain english to generate SQL to pull insights from the data. There are several scripts to explore in this module's folder.

We have 3 scripts for which we can generate prompts:

* [user_count.sql](./user_count.sql)
* [products-per-customer-product-name.sql](./products-per-customer-product-name.sql)
* [purchases-per-customer.sql](./purchases-per-customer.sql)

Open each of the scripts to see the prompts. Think of some of your own!


# References

* Github Copilot for SQL Developers: https://techcommunity.microsoft.com/t5/azure-sql-blog/github-copilot-for-sql-developers-turbocharge-your-sql/ba-p/3875915