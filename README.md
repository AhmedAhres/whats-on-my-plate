# What's on my plate?
An analysis of what we eat depending on where we live.

# Abstract
We are what we eat and the food system drives everything. Nowadays, there are endless range of products being sold in all over the world differing from one country to another. In this sense, different countries have a different impact on their population and on the environment depending on the products being sold and produced.
The aim of this project is to analyze what we eat depending on where we live.

Our goal is to collect data on the origin, eco-friendliness and healthiness to show what we eat in different countries. 
Through our analysis, we hope to give more information to the user about what he/she eats depending on the country where he/she lives.  

# Data Story
The data story can be found in https://ahmedahres.github.io/whats-on-my-plate/

# Research questions
We will guide our work with the following questions:

- What is the proportion of imported/exported products per country?
- Which countries contribute most to the environment through eco-friendly packages?
- Which countries have the largest variety of organic-labeled products?
- How healthy do we eat in the different countries?

These questions will then be used to answer the question stated in the title:

- What's on my plate?

The aim is to provide, depending on the country the user lives in, data about the origin and characteristics of the food he/she eats. It can also be interesting for the user to see information about his/her country of origin (in case the user lives in a different country).

# Datasets
In order to answer these research questions, we will be looking at the ***Open Food Facts*** database. This dataset provides us with information about the ingredients, category, nutrition score, countries where sold and produced for every product in the supermarkets worldwide. For example, by analyzing where a certain product is produced and sold, we can answer questions regarding trading between the different countries. Moreover, we will be using the data-set containing for the geographical position of the center of each country. The data-set was taken from the following link: https://developers.google.com/public-data/docs/canonical/countries_csv?fbclid=IwAR11sd1ArI7yBbHAJvsvNCUmOaxdwf__o5bd1w8RepWD47NrVO30vN8Ka_0

# A list of internal milestones up until project milestone 2
- Understand how to deal with large amount of data (1.7 GB)
- Understand the structure of the ***Open Food Facts*** features and labels, and explore its data.
- Think about what would be the best manner to visualize the results of the research questions
- Data cleaning and data analysis of the research questions
- Interpreting the preliminary results, and draw hypothesis of why it is the case.
- Comment and debug the code
- Set up our goals and plans for the next milestone.


# Timeline of the progress:

## November 4th:
    - Download the Open Food Facts data
    - Figure out how to access and manipulate the ADA cluster
    - Set up the Github repository and skeleton of our project (Jupyter notebook or Spark Cluster)
    - Skim over the structure of the data provided by openfoodfacts.org and the official description on their website
    - Come up with research questions related to our data set of choice

## November 11th:
    - Cleaning the openfoodfacts dataset i.e., deleting the unnecessary columns for out research questions and replacing NaN

## November 18th: 
    - Explore the data available after the cleaning, and analyse the data related to our research questions
    - Interpreting the preliminary results, and draw hypothesis related to our research questions.

## November 25th:
    - Decide on the focus of our projects from the different research question and analysis of the data done so far.
    - Clean, Comment and debug the code for submission
    - Set up our goals and plans for the next milestone.

## December 2nd:
    - Explore the possibility to generate more data from the data that we already have linked to our research question.
    - Explore the possibility to predict some features that are missing in our data.
    - Drafting the outline for our report/data story
    - Continuously enhancing our data exploration/analysis/cleaning.
    - Start working on answering our research questions
    
## December 9th:
    - Continuously enhancing our data exploration/analysis/cleaning.
    - Work on the report/data story.
    
## December 16th:
    - Finalize the project and the report.
    - Start working on the poster and presentation.

# Options to consider:
Enhance our data with more external sources of data.

# Contibution of each member
- Ahmed Ahres: Design and creation of all the data story, packaging research question, maintaining the notebook up-to-date (in case of major changes).
- Ali El Abridi:
- Mathias Gonçalves: Most of the data cleaning and exploration, the import/export question.
