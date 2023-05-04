# Repository for Labs
## CMPSC 441 and GAME 450

This repository will contain code for all the lab sessions for the course. New folders will be added to 'src' folder with the name of the lab. 

**********************************************************************************************************************************************
                                        run game from lab 11 agent_environment
**********************************************************************************************************************************************


==============================================================================================================================================
                                                            Report
===============================================================================================================================================


Abstract:
Artificial intelligence (AI) has become an integral part of modern video games, providing realistic and engaging gameplay experiences for players. This paper provides an overview of the different types of AI used in games, including rule-based systems, decision trees, and machine learning algorithms. It also discusses the specific challenges associated with designing AI for games, such as balancing AI difficulty, ensuring player enjoyment, and dealing with unpredictable player behavior.
The paper explores some of the most popular applications of AI in games, such as non-player character (NPC) behavior, procedural content generation, and player modeling. NPC behavior involves designing AI to control the actions of computer-controlled characters in a game, creating more lifelike and challenging opponents. Procedural content generation uses AI algorithms to generate game content such as levels, quests, and enemies, providing a more dynamic and varied gameplay experience. Player modeling uses AI to analyze player behavior and tailor the game experience to individual preferences, enhancing player engagement and satisfaction.
The paper also discusses some of the ethical and social implications of using AI in games, such as the potential for AI to reinforce negative stereotypes or perpetuate bias. It highlights the need for game developers to carefully consider the ethical implications of their AI design choices and to strive for fairness, transparency, and inclusivity.
Overall, this paper provides an in-depth overview of the role of AI in modern video games, highlighting the challenges and opportunities associated with designing and implementing AI in games, and the potential impact of AI on player experience and society as a whole.

AI Components:

1.	Fitness algorithm
2.	Purlin noise
3.	Text Generation

Problem Solved by AI:

Fitness algorithm:

In the context of fitness algorithms used in game development, fitness values are used to evaluate the effectiveness of a particular solution or decision in achieving a desired outcome. In the case of generating cities on an elevation map, fitness values can be used to evaluate the suitability of a particular location for a city based on factors such as elevation, proximity to resources, and distance to other cities.

To use fitness values to generate cities on an elevation map, game developers first define a set of criteria that determine the suitability of a particular location for a city. These criteria might include factors such as the elevation of the terrain, the proximity to natural resources such as water and food, and the distance to other cities.

Once the criteria have been defined, the fitness algorithm can be used to generate a set of potential city locations on the elevation map, and assign fitness values to each location based on how well it meets the defined criteria. Locations that meet the criteria more closely will receive higher fitness values, while locations that are less suitable will receive lower fitness values.

The algorithm can then use these fitness values to select the most suitable location for each city, based on the desired number and size of cities. This approach can help to ensure that the cities are placed in locations that are both realistic and strategically advantageous, based on the terrain and available resources.

The fitness algorithm requires inputs such as cities, index, elevation, and size. The function will evaluate the suitability of the city based on its elevation, distance from other cities, and other criteria. Specifically, it will check if the city's elevation is too low or high and if it is located at a suitable distance from other cities. The algorithm will then generate a fitness value based on these evaluations, indicating how suitable the location is for a city.
Overall, fitness algorithms can be a powerful tool for generating cities on an elevation map, as they can evaluate the suitability of potential locations based on a set of defined criteria. By using fitness values to select the most suitable locations for cities, game developers can create game worlds that feel more realistic and immersive, while also maintaining a balance between gameplay and strategic considerations.

Perlin Noise:

Perlin noise is a type of gradient noise that is often used in computer graphics and game development to create natural-looking textures and patterns. It was developed by Ken Perlin in 1983 and has since become a widely-used algorithm for generating random patterns that mimic the randomness and complexity of natural phenomena.

In the context of map making in games, Perlin noise can be used to create terrain heightmaps, which define the elevations and contours of the virtual landscape. By applying Perlin noise to a 2D grid of values, game developers can create a realistic and randomized terrain that mimics the look and feel of natural environments, such as mountains, valleys, and hills.

The basic principle behind Perlin noise is to combine multiple layers of randomized gradient vectors, with each layer representing a different level of detail or frequency. The gradient vectors are then used to calculate a value for each point in the 2D grid, based on its distance and orientation relative to the nearby vectors.

The result is a smooth and continuous gradient of values that produces a randomized pattern that is both visually appealing and mathematically coherent. The randomness of Perlin noise can be controlled through various parameters, such as the number of layers, the frequency of the gradients, and the amplitude of the values.

In the context of game development, Perlin noise can be used to create heightmaps that define the elevation and terrain features of the game world. These heightmaps can then be used to generate realistic 3D terrain models, which can be further refined and modified using various tools and techniques.

In the game, the Perlin noise algorithm is used in the "get_elevation" function. This function requires only the size of the map and a parameter called "octaves." The algorithm creates a Perlin noise that is based on a seed that remains constant within the function, as well as the octaves parameter. Once the Perlin noise is generated, it populates the elevation based on the size of the map. The function then outputs the newly generated landscape as a NumPy array.

Overall, Perlin noise is a powerful algorithm that can be used to generate randomized patterns and textures that mimic the complexity and randomness of natural environments. By using Perlin noise to create heightmaps, game developers can create realistic and immersive game worlds that are both visually appealing and mathematically coherent.

Text AI:

Text AI, also known as natural language generation (NLG), is a type of AI that is used to generate human-like text. It works by analyzing large amounts of text data and identifying patterns and structures, which it can then use to generate new text that is similar in style and tone to the original data.

In the context of game development, text AI can be used to generate dialog for characters in battle scenarios. This can be particularly useful in games where there are a large number of characters or where the dialog options are complex and dynamic.

By using text AI, game developers can create dialog that feels more natural and engaging for players, as the AI can generate responses that are tailored to the player's actions and choices. This can help to enhance the player's immersion in the game world and make the battles feel more realistic and dynamic.

There are several ways that text AI can be used to generate dialog in battle scenarios. One approach is to use pre-written dialog data as a training dataset for the AI, which it can then use to generate new responses based on the player's actions and choices.

Another approach is to use machine learning algorithms to analyze the player's behavior and preferences in real-time, and generate dialog responses that are tailored to those preferences. This approach can be particularly effective in games where the dialog options are complex and dynamic, as the AI can adapt to the player's choices and generate responses that feel more natural and engaging.

In the game, the natural language generation (NLG) system created by Salesken only requires a prompt as an input. This prompt is determined by the action taken by the player. The NLG system then generates dialogue that responds to the player's action as an output.
Overall, text AI is a powerful tool that can be used to enhance the player's experience in battle scenarios, by generating dialog that is tailored to their actions and choices. By using text AI to create dynamic and engaging dialog, game developers can create games that feel more immersive and engaging for players.




Appendix:
Transcript of chat GPT

User
can you write a 250 word abstract

ChatGPT
Abstract:

This paper provides an overview of the current state of the art in artificial intelligence and its applications across various domains. The rapid development of machine learning algorithms and big data has led to significant advances in the field of AI, making it a key driver of innovation and change across industries. The paper discusses the different types of AI, including rule-based systems, expert systems, and machine learning algorithms, and their applications in areas such as finance, healthcare, and transportation.

One of the main challenges facing the AI community is the need to ensure that these systems are ethical, transparent, and unbiased. As AI becomes more pervasive in our lives, it is important to address issues such as algorithmic bias and the impact of AI on employment and society as a whole. The paper discusses some of these challenges and highlights the need for continued research in these areas.

Another important topic covered in this paper is the development of human-like AI, often referred to as artificial general intelligence (AGI). While current AI systems are highly specialized and focused on specific tasks, the development of AGI could potentially lead to systems that can reason, plan, and learn across a wide range of domains. The paper discusses some of the challenges and opportunities associated with the development of AGI, including ethical concerns and the potential impact on society.

Overall, the paper provides a comprehensive overview of the current state of the art in AI and highlights some of the key challenges and opportunities facing the field in the years to come.





User
can you make the abstract about ai in games
ChatGPT
Abstract:

Artificial intelligence (AI) has become an integral part of modern video games, providing realistic and engaging gameplay experiences for players. This paper provides an overview of the different types of AI used in games, including rule-based systems, decision trees, and machine learning algorithms. It also discusses the specific challenges associated with designing AI for games, such as balancing AI difficulty, ensuring player enjoyment, and dealing with unpredictable player behavior.

The paper explores some of the most popular applications of AI in games, such as non-player character (NPC) behavior, procedural content generation, and player modeling. NPC behavior involves designing AI to control the actions of computer-controlled characters in a game, creating more lifelike and challenging opponents. Procedural content generation uses AI algorithms to generate game content such as levels, quests, and enemies, providing a more dynamic and varied gameplay experience. Player modeling uses AI to analyze player behavior and tailor the game experience to individual preferences, enhancing player engagement and satisfaction.

The paper also discusses some of the ethical and social implications of using AI in games, such as the potential for AI to reinforce negative stereotypes or perpetuate bias. It highlights the need for game developers to carefully consider the ethical implications of their AI design choices and to strive for fairness, transparency, and inclusivity.

Overall, this paper provides an in-depth overview of the role of AI in modern video games, highlighting the challenges and opportunities associated with designing and implementing AI in games, and the potential impact of AI on player experience and society as a whole.


What is the fitness algorithm

ChatGPT
A fitness algorithm is a computational method used in evolutionary computing and genetic programming to evaluate the fitness of individuals in a population. In evolutionary computing, individuals are often represented as strings of binary or real-valued numbers, which are combined and mutated to generate new individuals in successive generations.

The fitness algorithm is used to determine how well an individual solution performs a given task or solves a problem. This is typically done by comparing the output of the individual to a known target or optimal solution, and assigning a fitness score based on the degree of similarity or error between the two.

The fitness algorithm can vary depending on the specific problem being solved and the representation of individuals in the population. In some cases, the fitness function may be relatively simple, such as counting the number of correct solutions or minimizing a specific error metric. In other cases, the fitness function may be more complex, involving multiple objectives and constraints that need to be optimized simultaneously.

Overall, the fitness algorithm is a crucial component of evolutionary computing, as it determines which individuals are selected for reproduction and which are eliminated from the population, driving the evolution of solutions over time.





User
how can fitness ai help solve a way to create realistic cities
ChatGPT
Fitness AI can help solve the problem of creating realistic cities by using evolutionary computing techniques to generate and evaluate a large number of potential city designs.

One approach to this problem would be to represent different aspects of the city, such as road networks, building placement, and land use patterns, as parameters in an optimization problem. The fitness function would then be used to evaluate the quality of each design based on a set of criteria, such as traffic flow, accessibility, and visual appeal.

The fitness algorithm would then be used to generate a large population of potential solutions, with each solution represented by a set of parameter values that define the city design. These solutions would then be evaluated using the fitness function, and the best-performing solutions would be selected for reproduction and mutation to generate new candidate designs.

Over successive generations, the evolutionary process would converge on better and better city designs that meet the desired criteria. This approach has the advantage of being able to explore a wide range of possible city designs and trade-offs between different objectives, without the need for manual design or optimization.

Fitness AI can also incorporate data and feedback from real cities to improve the realism and accuracy of the generated designs. For example, data on traffic patterns or building heights could be used to inform the fitness function and guide the optimization process towards more realistic and functional city designs.

Overall, fitness AI has the potential to significantly improve the efficiency and quality of urban design, by leveraging the power of evolutionary computing to generate and optimize complex city models.





User
how can fitness ai help solve a way to create realistic spread cities
ChatGPT
Fitness AI can also help solve the problem of creating realistic spread cities by using evolutionary computing techniques to generate and evaluate potential city designs that are optimized for factors such as population density, transportation infrastructure, and land use patterns.

One approach to this problem would be to represent the city as a set of parameters, such as the location and density of residential, commercial, and industrial zones, as well as the placement and capacity of transportation infrastructure. The fitness function would then be used to evaluate the quality of each design based on a set of criteria, such as commute time, accessibility, and overall population density.

The fitness algorithm would then be used to generate a large population of potential solutions, with each solution represented by a set of parameter values that define the city design. These solutions would then be evaluated using the fitness function, and the best-performing solutions would be selected for reproduction and mutation to generate new candidate designs.

Over successive generations, the evolutionary process would converge on better and better city designs that meet the desired criteria for spread cities. This approach has the advantage of being able to explore a wide range of possible city designs and trade-offs between different objectives, without the need for manual design or optimization.

Fitness AI can also incorporate real-world data and feedback from existing spread cities to improve the realism and accuracy of the generated designs. For example, data on population density or traffic patterns could be used to inform the fitness function and guide the optimization process towards more realistic and functional spread city designs.

Overall, fitness AI has the potential to significantly improve the efficiency and quality of urban design for spread cities, by leveraging the power of evolutionary computing to generate and optimize complex city models that meet the desired criteria.





User
can you focus more on the location of cities
ChatGPT
Yes, fitness AI can also help in the location and placement of cities, particularly in determining the optimal location for a new city or settlement.

One approach to this problem would be to use geographic information systems (GIS) data to represent the landscape, terrain, and environmental factors that can impact the suitability of a location for a new city. The fitness function would then be used to evaluate the quality of each potential location based on a set of criteria, such as proximity to natural resources, availability of transportation infrastructure, and accessibility to key markets.

The fitness algorithm would then be used to generate a large population of potential locations, with each location represented by a set of parameter values that define the geographic coordinates and environmental characteristics of the site. These locations would then be evaluated using the fitness function, and the best-performing locations would be selected for further evaluation and analysis.

Over successive generations, the evolutionary process would converge on better and better locations for the new city, taking into account a wide range of environmental and economic factors. This approach has the advantage of being able to explore a large number of potential locations and trade-offs between different objectives, without the need for manual analysis or optimization.

Fitness AI can also incorporate real-world data and feedback from existing cities to improve the realism and accuracy of the generated designs. For example, data on population density or economic activity could be used to inform the fitness function and guide the optimization process towards more realistic and functional city locations.

Overall, fitness AI has the potential to significantly improve the efficiency and quality of urban planning, by leveraging the power of evolutionary computing to generate and optimize complex city models that meet the desired criteria for location and placement.





User
can you use games and make it shorter
ChatGPT
Yes, fitness AI can be applied in city-building simulation games to create realistic and optimized cities.

In city-building simulation games, the player is typically presented with a virtual environment and a set of tools to construct and manage a city. Fitness AI can be used to automate the process of designing and optimizing a city, by generating a large number of potential designs and evaluating their fitness based on a set of criteria, such as population density, transportation efficiency, and overall economic performance.

The game engine can then use the best-performing designs generated by the fitness AI algorithm as a starting point for the player's city, with the option to further customize and improve the design through manual editing and refinement.

By incorporating fitness AI into city-building simulation games, players can quickly and easily create optimized and realistic cities that meet a wide range of criteria, without the need for manual analysis or optimization. This can help make the game more engaging and challenging, while also providing players with a deeper understanding of urban planning principles and concepts.





User
can you explain how fitness ai can generate cities on relistic locations in a game
ChatGPT
Sure! In a city-building simulation game, fitness AI can generate cities on realistic locations by using a combination of real-world geographic data and virtual terrain models.

The first step would be to obtain real-world geographic data, such as satellite imagery, topographical maps, and land use information, and convert it into a format that can be used by the game engine. This data can be used to create a virtual terrain model that accurately reflects the landscape and environmental conditions of the chosen location.

Next, the fitness algorithm would be used to generate a large number of potential city designs, with each design represented by a set of parameter values that define the location, size, and layout of different zones and infrastructure components, such as residential, commercial, industrial, and transportation zones.

The fitness function would then be used to evaluate the quality of each city design based on a set of criteria, such as population density, traffic congestion, access to natural resources, and overall economic performance. The best-performing city designs would be selected for further refinement and integration into the game engine.

Once the best-performing city design is selected, it can be automatically integrated into the virtual





User
can you explain how fitness algorithms can generate cites so the are not in non realistic locations
ChatGPT
Yes, fitness algorithms can be used to generate cities in realistic locations by taking into account a wide range of geographic, environmental, and economic factors.

The first step in this process is to define the criteria that will be used to evaluate the fitness of each potential city location. These criteria might include factors such as proximity to natural resources, availability of transportation infrastructure, accessibility to key markets, and suitability for residential, commercial, and industrial development.

The fitness algorithm would then generate a large population of potential city locations, with each location represented by a set of parameter values that define the geographic coordinates and environmental characteristics of the site. The fitness function would then be used to evaluate the quality of each location based on the defined criteria.

Locations that do not meet the specified criteria or are considered non-realistic would be assigned a lower fitness score, while locations that meet the criteria and are considered more realistic would be assigned a higher fitness score. Over successive generations, the evolutionary process would converge on better and better locations for the city, taking into account a wide range of environmental and economic factors.

To ensure that the generated cities are realistic and functional, the fitness algorithm can also incorporate feedback and data from existing cities, such as population density or economic activity, into the fitness function. This can help to guide the optimization process towards designs that are more realistic and functional, and can provide a basis for validating the generated designs against real-world data.

Overall, fitness algorithms can be an effective tool for generating cities in realistic locations, by leveraging the power of evolutionary computing to evaluate a wide range of potential locations and trade-offs between different objectives, and by incorporating real-world data and feedback to improve the accuracy and realism of the generated designs.





User
can you explain what perlin noice and how it solves the problem of map making in games
ChatGPT
Perlin noise is a type of gradient noise that is often used in computer graphics and game development to create natural-looking textures and patterns. It was developed by Ken Perlin in 1983 and has since become a widely-used algorithm for generating random patterns that mimic the randomness and complexity of natural phenomena.

In the context of map making in games, Perlin noise can be used to create terrain heightmaps, which define the elevations and contours of the virtual landscape. By applying Perlin noise to a 2D grid of values, game developers can create a realistic and randomized terrain that mimics the look and feel of natural environments, such as mountains, valleys, and hills.

The basic principle behind Perlin noise is to combine multiple layers of randomized gradient vectors, with each layer representing a different level of detail or frequency. The gradient vectors are then used to calculate a value for each point in the 2D grid, based on its distance and orientation relative to the nearby vectors.

The result is a smooth and continuous gradient of values that produces a randomized pattern that is both visually appealing and mathematically coherent. The randomness of Perlin noise can be controlled through various parameters, such as the number of layers, the frequency of the gradients, and the amplitude of the values.

In the context of game development, Perlin noise can be used to create heightmaps that define the elevation and terrain features of the game world. These heightmaps can then be used to generate realistic 3D terrain models, which can be further refined and modified using various tools and techniques.

Overall, Perlin noise is a powerful algorithm that can be used to generate randomized patterns and textures that mimic the complexity and randomness of natural environments. By using Perlin noise to create heightmaps, game developers can create realistic and immersive game worlds that are both visually appealing and mathematically coherent.





User
can you explain what text ai text generation is and how it solves creating dialog in battle for games
ChatGPT
Text AI, also known as natural language generation (NLG), is a type of AI that is used to generate human-like text. It works by analyzing large amounts of text data and identifying patterns and structures, which it can then use to generate new text that is similar in style and tone to the original data.

In the context of game development, text AI can be used to generate dialog for characters in battle scenarios. This can be particularly useful in games where there are a large number of characters or where the dialog options are complex and dynamic.

By using text AI, game developers can create dialog that feels more natural and engaging for players, as the AI can generate responses that are tailored to the player's actions and choices. This can help to enhance the player's immersion in the game world and make the battles feel more realistic and dynamic.

There are several ways that text AI can be used to generate dialog in battle scenarios. One approach is to use pre-written dialog data as a training dataset for the AI, which it can then use to generate new responses based on the player's actions and choices.

Another approach is to use machine learning algorithms to analyze the player's behavior and preferences in real-time, and generate dialog responses that are tailored to those preferences. This approach can be particularly effective in games where the dialog options are complex and dynamic, as the AI can adapt to the player's choices and generate responses that feel more natural and engaging.

Overall, text AI is a powerful tool that can be used to enhance the player's experience in battle scenarios, by generating dialog that is tailored to their actions and choices. By using text AI to create dynamic and engaging dialog, game developers can create games that feel more immersive and engaging for players.





User
can you explain fitness values and how it can solve placement of cities on a elevation map
ChatGPT
In the context of fitness algorithms used in game development, fitness values are used to evaluate the effectiveness of a particular solution or decision in achieving a desired outcome. In the case of generating cities on an elevation map, fitness values can be used to evaluate the suitability of a particular location for a city based on factors such as elevation, proximity to resources, and distance to other cities.

To use fitness values to generate cities on an elevation map, game developers first define a set of criteria that determine the suitability of a particular location for a city. These criteria might include factors such as the elevation of the terrain, the proximity to natural resources such as water and food, and the distance to other cities.

Once the criteria have been defined, the fitness algorithm can be used to generate a set of potential city locations on the elevation map, and assign fitness values to each location based on how well it meets the defined criteria. Locations that meet the criteria more closely will receive higher fitness values, while locations that are less suitable will receive lower fitness values.

The algorithm can then use these fitness values to select the most suitable location for each city, based on the desired number and size of cities. This approach can help to ensure that the cities are placed in locations that are both realistic and strategically advantageous, based on the terrain and available resources.

Overall, fitness algorithms can be a powerful tool for generating cities on an elevation map, as they can evaluate the suitability of potential locations based on a set of defined criteria. By using fitness values to select the most suitable locations for cities, game developers can create game worlds that feel more realistic and immersive, while also maintaining a balance between gameplay and strategic considerations.





User
can you clean up this paragraph? In the game The perlin noice algorithm is used in the get_elevation function. The function just need the size of the map and a wave called octaves. It creates a Perlin noice that requires a seed that remains constant in the function and the octave. Once the perlin noice is created it will the populate the elevation based on the size. It will the output the freshly generated landscape in a np array
ChatGPT
In the game, the Perlin noise algorithm is used in the "get_elevation" function. This function requires only the size of the map and a parameter called "octaves." The algorithm creates a Perlin noise that is based on a seed that remains constant within the function, as well as the octaves parameter. Once the Perlin noise is generated, it populates the elevation based on the size of the map. The function then outputs the newly generated landscape as a NumPy array.





User
can you fix this paragraph? In the game the NGL created by salesken will only need a prompt as an input. The prompt will be determined by the action of the player. It will output dialogue that will respond to the action taken.
ChatGPT
In the game, the natural language generation (NLG) system created by Salesken only requires a prompt as an input. This prompt is determined by the action taken by the player. The NLG system then generates dialogue that responds to the player's action as an output.





User
can you fix this paragraph?The fitness value will require the cities, index, elevation, and size as inputs. The function will check to see if the cities elevation is to low or high. It will also check if the cities are at a nice distance. It will then generate a fitness value based on the evaluations.
ChatGPT
The fitness algorithm requires inputs such as cities, index, elevation, and size. The function will evaluate the suitability of the city based on its elevation, distance from other cities, and other criteria. Specifically, it will check if the city's elevation is too low or high and if it is located at a suitable distance from other cities. The algorithm will then generate a fitness value based on these evaluations, indicating ho