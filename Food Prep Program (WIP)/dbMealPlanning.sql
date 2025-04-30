-- --------------------------------------------------------------------------------
-- Name: Nicholas Colvin
-- Abstract: Meal Planning Database!
-- --------------------------------------------------------------------------------
DROP DATABASE IF EXISTS dbmealplanning;
CREATE DATABASE dbmealplanning;
USE dbmealplanning;

-- DROP STATEMENTS
DROP TABLE IF EXISTS IngredientsRecipes;
DROP TABLE IF EXISTS IngredientsUsers;
DROP TABLE IF EXISTS Ingredients;
DROP TABLE IF EXISTS IngredientTypes;
DROP TABLE IF EXISTS RecipesUsers;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Recipes;

-- --------------------------------------------------------------------------------
-- Step #1 : Create Tables
-- --------------------------------------------------------------------------------

CREATE TABLE Users(
  intUserID INT NOT NULL,
  strUser VARCHAR(50) NOT NULL,
  PRIMARY KEY (intUserID)
);

CREATE TABLE IngredientsUsers(
  intIngredientUserID INT NOT NULL,
  intIngredientID INT NOT NULL,
  intUserID INT NOT NULL,
  PRIMARY KEY (intIngredientUserID)
);

CREATE TABLE Ingredients(
  intIngredientID INT NOT NULL,
  strIngredient VARCHAR(50) NOT NULL,
  intIngredientTypeID INT NOT NULL,
  PRIMARY KEY (intIngredientID)
);

CREATE TABLE IngredientTypes(
  intIngredientTypeID INT NOT NULL,
  strType VARCHAR(50) NOT NULL,
  PRIMARY KEY (intIngredientTypeID)
);

CREATE TABLE Recipes(
  intRecipeID INT NOT NULL,
  strRecipeName VARCHAR(50) NOT NULL,
  intServingSize INT NOT NULL,
  strCookTime VARCHAR(50) NOT NULL,
  strDirections VARCHAR(255) NOT NULL,
  PRIMARY KEY (intRecipeID)
);

CREATE TABLE IngredientsRecipes(
  intIngredientRecipeID INT NOT NULL,
  intIngredientID INT NOT NULL,
  intRecipeID INT NOT NULL,
  PRIMARY KEY (intIngredientRecipeID)
);

CREATE TABLE RecipesUsers(
  intRecipeUserID INT NOT NULL,
  intRecipeID INT NOT NULL,
  intUserID INT NOT NULL,
  PRIMARY KEY (intRecipeUserID)
);

-- --------------------------------------------------------------------------------
-- Step #2 : Establish Referential Integrity
-- --------------------------------------------------------------------------------
-- CHILD           			 PARENT               ID
-- 1 IngredientsRecipes     Recipes               intRecipeID
-- 2 IngredientsRecipes     Ingredients           intIngredientID
-- 3 Ingredients            IngredientTypes       intIngredientTypeID
-- 4 IngredientsUsers       Ingredients           intIngredientID
-- 5 IngredientsUsers       Users                 intUserID
-- 6 RecipesUsers           Recipes               intRecipeID
-- 7 RecipesUsers           Users                 intUserID


-- 1
ALTER TABLE IngredientsRecipes ADD CONSTRAINT IngredientsRecipes_Recipes_FK
FOREIGN KEY (intRecipeID) REFERENCES Recipes(intRecipeID);
-- 2
ALTER TABLE IngredientsRecipes ADD CONSTRAINT IngredientsRecipes_Ingredients_FK
FOREIGN KEY (intIngredientID) REFERENCES Ingredients(intIngredientID);
-- 3
ALTER TABLE Ingredients ADD CONSTRAINT Ingredients_IngredientTypes_FK
FOREIGN KEY (intIngredientTypeID) REFERENCES IngredientTypes(intIngredientTypeID);
-- 4
ALTER TABLE IngredientsUsers ADD CONSTRAINT IngredientsUsers_Ingredients_FK
FOREIGN KEY (intIngredientID) REFERENCES Ingredients(intIngredientID);
-- 5
ALTER TABLE IngredientsUsers ADD CONSTRAINT IngredientsUsers_Users_FK
FOREIGN KEY (intUserID) REFERENCES Users(intUserID);
-- 6
ALTER TABLE RecipesUsers ADD CONSTRAINT RecipesUsers_Recipes_FK
FOREIGN KEY (intRecipeID) REFERENCES Recipes(intRecipeID);
-- 7
ALTER TABLE RecipesUsers ADD CONSTRAINT RecipesUsers_Users_FK
FOREIGN KEY (intUserID) REFERENCES Users(intUserID);

-- --------------------------------------------------------------------------------
-- Step #3 : Inserts
-- --------------------------------------------------------------------------------

INSERT INTO Users(intUserID, strUser) VALUES
(1, "Nick"),
(2, "Zach"),
(3, "Becky"),
(4, "John");

INSERT INTO IngredientTypes(intIngredientTypeID, strType) VALUES
(1, "Vegetables"),
(2, "Fruits"),
(3, "Grains"),
(4, "Proteins"),
(5, "Dairy"),
(6, "Spices");


