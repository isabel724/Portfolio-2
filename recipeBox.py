recipeBox = {"Shrimp Avocado Salad": [["1/4 cup mayonnaise","2 stalks celery, thinly sliced","3 tablespoons chopped celery leaves","3 tablespoons finely chopped fresh cilantro", "kosher salt", "freshly ground pepper","1 1/2 limes","1 1/2 pounds large shrimp, peeled and deveined","1 tablespoon vegetable oil","2 hass avocados, diced","1 5-ounce package baby kale salad mix (about 8 cups)","1 small bunch radishes, thinly sliced"], ["Preheat a grill or grill pan to medium high.", "Make the dressing. Combine the mayonnaise, celery leaves, 2 tablespoons chopped cilantro, 1 tablespoon water, 1/2 teaspoon salt and a few grinds of pepper in a large bowl. Grate in the zest of 1 lime and squeeze in the juice.", "Toss the shrimp with the vegetable oil, 1/4 teaspoon salt and a few grinds of pepper in a bowl. Arrange the shrimp on the grill and cook until pink and just firm, about 2 minutes per side. Transfer to the bowl with the dressing; squeeze in the juice of the remaining 1/2 lime.", "Add the sliced celery, avocados, salad mix and radishes to the bowl with the shrimp; toss to coat. Top with the remaining 1 tablespoon chopped cilantro."]], "Chicken Tetrazzini": [["9 tablespoons butter", "2 tablespoons olive oil", "4 boneless skinless chicken breasts", "2 1/4 teaspoons salt", "1 1/4 teaspoons freshly ground black pepper", "1 pound white mushrooms, sliced", "1 large onion, finely chopped", "5 cloves garlic, minced", "1 tablespoon chopped fresh thyme leaves", "1/2 cup dry white wine", "1/3 cup all-purpose flour", "4 cups whole milk, room temperature", "1 cup heavy whipping cream, room temperature", "1 cup chicken broth", "1/8 teaspoon ground nutmeg", "12 ounces linguine", "3/4 cup frozen peas", "1/4 cup chopped fresh Italian parsley leaves", "1 cup grated Parmesan", "1/4 cup dried Italian-style breadcrumbs"], ["Preheat the oven to 450 degrees F.", "Spread 1 tablespoon of butter over a 13 by 9 by 2-inch baking dish. Melt 1 tablespoon each of butter and oil in a deep large nonstick frying pan over medium-high heat. Sprinkle the chicken with 1/2 teaspoon each of salt and pepper. Add the chicken to the hot pan and cook until pale golden and just cooked through, about 4 minutes per side. Transfer the chicken to a plate to cool slightly. Coarsely shred the chicken into bite-size pieces and into a large bowl.", "Meanwhile, add 1 tablespoon each of butter and oil to the same pan. Add the mushrooms and saute over medium-high heat until the liquid from the mushrooms evaporates and the mushrooms become pale golden, about 12 minutes. Add the onion, garlic, and thyme, and saute until the onion is translucent, about 8 minutes. Add the wine and simmer until it evaporates, about 2 minutes. Transfer the mushroom mixture to the bowl with the chicken.", "Melt 3 more tablespoons butter in the same pan over medium-low heat. Add the flour and whisk for 2 minutes. Whisk in the milk, cream, broth, nutmeg, remaining 1 3/4 teaspoons salt, and remaining 3/4 teaspoon pepper. Increase the heat to high. Cover and bring to a boil. Simmer, uncovered, until the sauce thickens slightly, whisking often, about 10 minutes.", "Bring a large pot of salted water to a boil. Add the linguine and cook until it is tender but still firm to the bite, stirring occasionally, about 9 minutes. Drain. Add the linguine, sauce, peas, and parsley to the chicken mixture. Toss until the sauce coats the pasta and the mixture is well blended.", "Transfer the pasta mixture to the prepared baking dish. Stir the cheese and breadcrumbs in a small bowl to blend. Sprinkle the cheese mixture over the pasta. Dot with the remaining 3 tablespoons of butter. Bake, uncovered, until golden brown on top and the sauce bubbles, about 25 minutes."]]}

print ("What recipe would you like to see?")
recipes = list(recipeBox.keys())
for x in range(len(recipes)):
    print (recipes[x])

recipe = ""
while recipe not in recipes:
    recipe = input ("Recipe Name: ").title()

print (recipe)
print()

print ("Ingredients:")
for y in recipeBox[recipe][0]:
    print (y)
print()

print ("Directions:")
for y in range(len(recipeBox[recipe][1])):
    print (str(y+1) + ". " + recipeBox[recipe][1][y])
