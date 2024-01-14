# Superheroes API

## Project Overview

This Superheroes API is a Flask-based web application that allows users to track superheroes and their superpowers. The API provides endpoints to retrieve information about superheroes, their powers, and the relationships between them. It also allows users to update the description of a power and create new associations between superheroes and powers.

## Features Implemented
- **Models**: The application includes three models: `Hero`, `Power`, and `HeroPower`. The `Hero` and `Power` models represent superheroes and their powers, respectively. The `HeroPower` model represents the many-to-many relationship between heroes and powers, with an additional `strength` attribute that can be 'Strong', 'Weak', or 'Average'.
- **Validations**: The application includes validations on the `HeroPower` and `Power` models. For `HeroPower`, the `strength` must be one of the following values: 'Strong', 'Weak', 'Average'. For `Power`, the `description` must be present and at least 20 characters long.
- **Routes**: The application provides several routes to interact with the data:
    - `GET /heroes`: Returns a list of all heroes.
    - `GET /heroes/:id`: Returns a specific hero and their powers.
    - `GET /powers`: Returns a list of all powers.
    - `GET /powers/:id`: Returns a specific power.
    - `PATCH /powers/:id`: Updates the description of a power.
    - `POST /hero_powers`: Creates a new association between a hero and a power.
    
    The API returns data in JSON format.

## What Users Can Accomplish

With the Superheroes API, users can:

- Retrieve a list of all superheroes and their details.
- Retrieve a specific superhero along with their superpowers.
- Retrieve a list of all superpowers and their details.
- Retrieve a specific superpower.
- Update the description of a specific superpower.
- Create a new association between a superhero and a superpower, with a specified strength level.



