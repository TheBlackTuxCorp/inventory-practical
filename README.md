# TBT Backend SWE Practical

Thank you for interviewing with us! We'd like to ask you to do a brief, take-home exercise as part of the interview process. Most candidates complete it within 2 hours; please do not feel the need to spend more time than that. It can be completed in any language.

#### Guidelines

This exercise simulates solving a problem like you would on the job. Since we're replicating actual working conditions:

* The choice of programming language and tools is up to you.
* You can use any open source libraries that are suitable and helpful.
* Use of any references, websites, manuals, online code fragments, etc. is permissible
* Wholesale copying of complete solution found online is not permitted.
* Likewise, getting help actively from a 3rd party is not permitted. This should be your work.
* We value delivering working software highly. Your first priority should be getting to a working solution.

#### Evaluation

Your solution will be evaluated along these themes:

* **Correctness** - Your code should pass the sample test cases and other test cases you can think of. Handle edge cases sensibly. Don't worry about thread-safety or rogue input that doesn't adhere to the problem as defined below.
* **Clean Code** - Your code should be easy to understand and read. It should be modularized/encapsulated where appropriate. The code should follow the style guidelines of your chosen language. Write as if your code will be maintained and extended in the future. Use comments judiciously and sensibly.
* **Performance** - If you can make your solution's complexity better, please do so!
Remember, if you get really stuck, try and make progress however you can. Focus on simple test cases first, reduce the problem to less complex components, and ask your interviewer for how to prioritize your time.

#### Logistics

* When you are ready, commit your code.
* If you have any questions about the problem, feel free to ask your moderator.

## Inventory Management Problem

Unsurprisingly, inventory management is one of our most complicated problems. You are going to solve an idealized form of this problem for us. In this problem, you are matching a stock of tuxedos to the inventory required for an event.

Our warehouse has been stocked with 30 tuxedos in total (10 small, 10 medium, and 10 large). Each size is further split evenly in to a style, either version A or version B (5 small/version A, 5 medium/version A, 5 large/version A, 5 small/version B, 5 medium/version B, and 5 large/version B). Each rental is for 3 days and a particular tuxedo can only be used for one event during those 3 days.

You will be given a series of events defined by the day the event occurs and how many of each size of tuxedo will be required. Your program should read the events from a file. Specifically, an event is a comma separated list of the day of event, required small tuxedos, required medium tuxedos, and required large tuxedos. The day and number of tuxedos required will always be an integer.

For example, a single event that occurs on day 5 that requires 1 medium and 2 large tuxedos would be expressed like this:

    5,0,1,2

The input for two events with the same required tuxedos on the same day (still the 5th day) would be expressed like this:

    5,0,1,2
    5,0,1,2

Your task is to determine if we can provide our customers the tuxedos they require, or if we will need to purchase more tuxedos to meet customer demand. There is one additional requirement: in order to keep the look consistent, all tuxedos for a particular event must be the same style. Your program should respond with "sufficient inventory" or "buy more tuxedos".

Additional test cases can be found in the sample-inputs directory.

Some input parsing code has been provided for you in `/javascript` and `/python`; see the READMEs within each language directory for instructions on how to use the provided parsers.