# Agentic AI Project

A project that uses Microsoft AutoGen and allows AI agents to make clothing, activity, and meal recommendations to a user based on the weather conditions at their current location.

## Agents

### ClothingAssistant
- **Purpose:** Suggests relevant clothing items based on current weather conditions.
- **Functionality:**
  - Provides at least three clothing recommendations in a bulleted list.
  - Analyzes weather data and generates suggestions without human input.

### ActivityAssistant
- **Purpose:** Recommends activities based on current weather and nearby attractions.
- **Functionality:**
  - Provides at least three activity recommendations in a bulleted list.
  - Considers weather conditions and local points in location.

### MealAssistant
- **Purpose:** Offers meal recommendations based on location, time of day, and season.
- **Functionality:**
  - Suggests at least three cuisines or dining spots in a bulleted list.
  - Leverages time and seasonal preferences.

### UserProxy
- **Purpose:** Simulates the user seeking advice for planning their day.
- **Functionality:**
  - Acts as a bridge to provide inputs and retrieve responses from the assistant agents.
  - Operates autonomously with minimal human interaction.

## Dependencies

- `autogen`
- `python-dotenv`
- `flaml[automl]`

Install dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Paste your [Groq](https://groq.com/) API key in the `.env` file:

```
GROQ_API_KEY=...
```

## Execution

```sh
python3 main.py
```

## Authors

We are the yellow group.

- Nataniel Farzan (Lead)
- Drew Floyd (Product Owner)
- Jonathan Vergonio (QA)
- Ben Fellows (Dev)
- Ryan Jewik (Dev)

## References

- https://github.com/microsoft/autogen
- https://microsoft.github.io/autogen/0.2/docs/tutorial/tool-use
- https://github.com/chubin/wttr.in
- https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
