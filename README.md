# *Yellow is the new black*

[Our data story](https://nicolasfontbonne.github.io/)

# Abstract
The creation and propagation of false information has existed since the dawn of time.
Behind these misleading elements are often hidden political or financial intentions, in order to gain credit or make competitors lose it.
With the advent of the Internet and the ever faster and more direct flow of information, it is becoming easier every day to deceive your fellow citizens and to be fooled.
The term *fake news* took on a new dimension during the 2016 American presidential election, when Donald Trump used it extensively to describe the media coverage about himself. In this instantaneous era, it becomes crucial to be able to be critical of the information received. With this work, we want to highlight the risks related to the propagation of false information by using the fakes news themselves, from the Liar database. The power that these fake new vehicles hold is mostly in the use and resonance we make of them. Our credulity becomes credibility, it's up to us to turn the equation the other way around!

# Research questions
Through this work, we hope to :
1. Determine which are the main **subjects** falsely propagated in the United States.
1. What are the preferred **formats** for which topics?
1. What are the most prominent **professions** among the liars?
1. Highlight which political **parties** tend to lie the most.
1. Show how false information can spread through the internet.
1. Are statements in **debates** more likely to be lies, compared to other speeches?
1. Compare distribution of fake news between traditional press, speeches and social media
1. Is large credit history count connected with strong positions of power?
1. What is the dominating level of falsehood (half-true, mostly-true, etc) and how does it change in different contexts (job title, venue)?
1. What is the prevalent sentiment of fake-news stories: i.e fear, anger, joy?
1. Visualise rise of false statements before elections.
1. Are buzzwords, fillers and weasel words usually used in fake statements?

# Dataset
The database is [easily accessible](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip). This database contains three sets, as it is originally intended to detect false information through automated learning algorithms.
By combining all the available sets, the dataset consists of 12800 short quotes extracted from the [Politifact site](https://www.politifact.com/truth-o-meter/).
Each line corresponds to a unique quote whose veracity has been assessed and identified by a Politifact contributor.
A lot of information can be accessed in addition to the quotation itself, such as the speaker's political affiliation, geographical origin, history in the database and more.
The database therefore contains a large part of text elements of varying sizes. Since almost every intervention has been made in a unique context, we will need to determine how to group the quotes into various more general categories.

With the help of the [Politifact API](https://www.politifact.com//api/v/2/statement/2635/?format=json), we will be able to access more information if necessary, especially useful for visualization aspects such as photos of the different listeners.

We will also have to keep in mind that this database is not exhaustive and is certainly subject to significant biases.

# Our final data story:
You can access the webpage of our final data story and lies through [this link](https://nicolasfontbonne.github.io/). We hope you'll enjoy reading it!


# Team members and contributions:
 
* Konstantinos Koukas: Relationship model, graph visualisation (part 2), poster design and organisation...
* Jeremy Wanner: NLP analysis, content of abstract and part 3 of the report, poster design and organisation...
* Nicolas Fontbonne: Time and distribution analysis (part 1, intro), website architecture and graphical design, poster design and organisation...

# Remerciements
This study would not have been possible without the tremendous work done by Politifact and later by William Yang Wang. Separating what is true from what is false is not always easy, and the energy required to do so and to alert fellow citizens about it is enormous. A huge thank you for making a ready-to-use study topic available, and with it the many “rire jaunes” that have punctuated our work.
And final word for the amazing working team of the ADA course, Westeros TAs and Master, thank you!
