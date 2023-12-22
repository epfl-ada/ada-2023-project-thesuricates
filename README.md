# :movie_camera: Budget Battles: Maximizing Returns in Filmmaking Odyssey

## Datastory
Follow us in this cinematographic odyssey by discovering our [datastory](https://tomasvddc.github.io/)

## Abstract
The film industry is a growing industry of $42.2 billion in 2019 in theatrical box office alone. Including home entertainment, it reached [$139 billion in 2018](https://en.wikipedia.org/wiki/Film_industry). However, a big budget doesn't always mean an important ***return on investment*** (ROI). In 2002, the film ***The Adventures of Pluto Nash*** cost $100 million to produce but generated only [$7 million](https://en.wikipedia.org/wiki/The_Adventures_of_Pluto_Nash). This example shows that a high budget is not always synonymous with a profitable return. Is this also true for low-budget films? That's what two producer friends with very different wallets ask themselves over a drink. "I bet I can multiply my investment a lot more than you can with my big-budget film!". "We'll see about that!" replies the other with modesty. Let's follow these two friends on their existing adventure and see what we can do to help! This story will take us to the core of the movie industry by exploring interesting parameters of the [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) and finding the best choices for both `high` and `low` budget producers.

## :thought_balloon: Research Questions
The main metric that we will use in this project to measure the profitability of a movie will be the `multiplier` between the initial cost and the box office revenue. This technique allows us to cancel the effect of inflation and thus compare older movies with the new ones using the same metric. During our analysis, we will try to answer the following questions:
1. Which characteristics/features of a movie have a significant effect on its box office revenue with respect to its cost (`multiplier`)?
2. Is there a common ***strategy*** among low and high budget movies to maximize their multipliers or is it different? If so, in which aspect(s) of the movie?
3. Is it generally sufficient to **increase the budget** of a given movie to increase its multiplier?

## :file_folder: Additional Datasets
* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page?uselang=fr): using the ***WikiPageID*** feature present in the [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/), we can extend the latter with essential missing features for our analysis. It is a convenient and reliable source to get structured movie data such as `cost` and `currencyCode`, two crucial parameters to compute the `multiplier` for a given movie. This data can be found in our repository under the name film_wiki_data_formatted.csv.
* [Conversion rates](ADD_SOURCE_HERE): as explained earlier, the extracted costs are not necessarily in ***USD***. This makes sense because many movies are indeed not produced in the United States. It follows that conversion rates data was necessary to conduct a proper analysis over the costs of movies that are produced in various currencies. The conversion rates of INSERT_TIME_HERE are stored in usd_conversion_rates.json.
* [TMDB](https://www.themoviedb.org/): even by using Wikidata, we are still missing information about the cost of many movies. We are considering using the TMDB database to extend our `cost` feature to more movies of our current dataset.

## 🛠️: Methods

### Preprocessing

In the initial phase, we preprocess, clean, and merge datasets, using [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page?uselang=fr) and potentially [TMDB](https://www.themoviedb.org/) for enrichment. We standardize currencies to ***USD*** for data uniformity. The resulting dataset includes all films with `cost` and `Box_office_revenue` information, crucial for our analysis. As an additional step, we'll identify and remove potential outliers using confidence intervals, ensuring dataset integrity.

### Separation of Low and High Budget Films

To distinguish between `low` and `high`-budget films, we categorize films into five-year groups based on their release dates. The top 25% of films with the highest budgets and the bottom 25% with the lowest budgets are then identified within each time frame. This process mitigates the impact of ***inflation*** on budget categorization. Subsequently, all high-budget films from different periods will be regrouped into a single high-budget category, and the same will be done for low-budget films. The focus will then shift to analyzing the `multiplier` for each film. The use of the multiplier helps neutralize inflation effects within each category, ensuring a fair comparison across different years. 

### Regression

Regression analysis will be employed to identify optimal strategies for both budget categories. We will specifically select features that producers can influence, such as the film's runtime, number of actors, and genre. Using these impactful features, we will train the model to ***predict*** the `multiplier` between the initial cost and box office revenue. This will allow us to determine the features necessary to achieve the ***optimum multiplier*** for each budget category. The analysis will be conducted separately for low and high-budget films, highlighting differences in feature selection strategies and maximum expected values of the multiplier. 

In this part we will then navigate through the process of choosing the right regression model and its parameters, assess the significance of the features, and optimize the goodness-of-fit statistic R^2.

### Optimization 
The optimization phase involves fine-tuning parameters, or strategies, to maximize the output, which, in this context, is the `multiplier`. Our goal is to identify the most effective strategies for both low and high-budget scenarios.


### Statistical Tests

Statistical tests are employed to assess the significance of differences in ***Return on Investment*** (ROI) between low and high-budget films. Through t-tests, we determine whether observed disparities in ROI are statistically significant or mere products of chance. Additionally, employing an F-test allows us to evaluate if the strategies used for low and high-budget films are statistically similar.



## 📆: Proposed timeline
![Alt text](timeline_m2&3.png)

## 🤝: Organization within the team
<table class="tg" style="table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 16px">
<col style="width: 180px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax">Teammate</th>
    <th class="tg-0lax">Milestone 2</th>
    <th class="tg-0lax">Milestone 3</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Diogo</td>
    <td>
        <ul>
            <li>Data collection from other datasets</li>
            <li>Formatting the data ang merging with our dataset</li>
        </ul>
    </td>
    <td>
        <ul>
            <li>Acquire and merge data with TMDB </li>
            <li>Data Story</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Charlotte</td>
    <td>
        <ul>
            <li>Cleaning and merging the datasets</li>
            <li>Clustering of the high and low budgets</li>
        </ul>
    </td>
    <td>
        <ul>
            <li>Optimization of the output, Statistical analysis</li>
            <li>Visualization Tasks</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Tomas</td>
    <td>
        <ul>
            <li>Cleaning and merging the datasets</li>
            <li>Clustering of the high and low budgets</li>
        </ul>
    </td>
    <td>
        <ul>
            <li>Optimization of the output, Statistical analysis</li>
            <li>Visualization Tasks</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Léo</td>
    <td>
        <ul>
            <li>Writing the Readme</li>
            <li>Performing initial analysis on the data</li>
        </ul>
    </td>
    <td>
        <ul>
            <li>Perform Regression</li>
            <li>Answer research question</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0lax">Joanna</td>
    <td>
        <ul>
            <li>Writing the Readme</li>
            <li>Performing initial analysis on the data</li>
        </ul>
    </td>
    <td>
        <ul>
            <li>Perform Regression</li>
            <li>Answer research question</li>
        </ul>
    </td>
  </tr>
</tbody>
</table>
