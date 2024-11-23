this is a hackathon project for hackatum 2024 hubert burda media challenge


we are using nuxt 3 with shadcn ui and tailwind css for the frontend

the backend is a python app

the challenge is to create a web app that allows you to generate articles in real time for efahrer.com a magazine primarily focused on electric cars and other sustainable / electric energy topics

typically the news production process works like this:

first discover topics
then select news
then do research
then write article
then get a good image
then review article
then publish article

this takes many hours and many people

we want to automate this process as much as possible with generative ai.

the core function of the app is to generate articles in real time based on a set magazine topics (in this case electric cars, sustainable energy, etc.)

we are provided with a rss feed of articles from given news sites related to our topic. this is given by the challenge organizers.

our job is to create articles based on the rss feed basically and then make a web app that allows you to see, review and publish the articles and get insights.

these insights could be for example:
- review score
- sentiment
- topics
- image
- trending topics
- ...

the core components of the article generation are:
 1) source aggregation
    - get the rss feed and select topics and related articles
2) content selection and enrichment
    - select and analyze with ai
    - enrich with ai (eg add more data statistics opinions etc.)
3) gen ai creation
    - write news article
    - engaging article and images


the value will be the time saved and the professional quality of the articles.


the frontend will be a web app that allows you to see, review and publish the articles and get insights
so like a dashboard basically for the editors and journalists to oversee the process and get insights and speed up the process of the whole news production.

