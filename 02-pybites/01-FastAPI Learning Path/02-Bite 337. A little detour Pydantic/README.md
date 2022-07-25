# Enunciado

https://codechalleng.es/bites/337/

If you are new to typing / type annotations, maybe you want to complete this Bite first, and/or read our article series.

https://pybit.es/articles/code-better-with-type-hints-part-1/

https://pydantic-docs.helpmanual.io/


In this Bite you are going to define your first Pydantic Food model.

A model is a class with one or more (typed) attributes. To get all Pydantic's goodness we'll need to subclass Pydantic's BaseModel class, Pydantic's homepage shows you how and it's probably enough detail to solve this Bite.

This is the Food model you'll define now and use in upcoming Bites. Our tests will use and test it.

|Attribute| 	Type| 	Example|
|---------|---------|----|
id| 	int| 	1
name| 	str| 	oatmeal
serving_size| 	str| 	100 grams
kcal_per_serving *| 	int| 	336
protein_grams| 	float| 	13.2
fibre_grams| 	float| 	10.1

```
* kcal = calories

** fibre_grams is an optional value which defaults to 0.
````

We'll come back to Pydantic in a later Bite to define two more models to track food intake for a user day by day. For we won't overload you with object relationships that multiple models inevitably introduce. Step by step!

In the following Bites we'll use this Pydantic model to build the API's CRUD (create-read-update-delete) actions around it.

Have fun with Pydantic!