//
//  ViewController.swift
//  JGMTDR
//
//  Created by Payton Pehrson on 11/9/20.
//  Copyright © 2020 Payton Pehrson. All rights reserved.
//

import UIKit

class RecipePreviewsController: UITableViewController {
    var store: RecipeStore!
    
    //DateFormatter
    let dateFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateStyle = .short
        formatter.timeStyle = .none
        return formatter
    }()

    //Tell the table the number of rows it should display
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        //It should display how many recipes we have of course.
        return store.allRecipes.count
    }
    
    //This function determines what goes into our row cells
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        //Create a cell via dequeueReusableCell at the indexPath based on the RecipeCell from the story board, and cast it to the class of RecipeCell, if you can't crash.
        let cell = tableView.dequeueReusableCell(withIdentifier: "RecipeCell", for: indexPath) as! RecipeCell
        let recipe = store.allRecipes[indexPath.row]
        cell.titleLabel.text = recipe.title
        cell.dateLabel.text = dateFormatter.string(from: recipe.date)
        cell.dietLabel.text = recipe.diet
        return cell
    }
    
    //Initial view loading function
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.rowHeight = UITableView.automaticDimension
        tableView.estimatedRowHeight = 95
        //So now we call fetchRecipes sending a recipesResult in.
        store.fetchRecipes {
            (recipesResult) in
            //Let recipes' state determine our next action
            switch recipesResult {
            //If success, print our count
            case let .success(recipes):
                print("Successfully found \(recipes.count) recipes.")
                //Assign our successful fetch to our store.
                self.store.allRecipes = recipes
                //Reload our table to reflect our brand new recipes
                self.tableView.reloadData()
            //If failure, print our error that we've passed down since fetch I believe.
            case let .failure(error):
                print("Error fetching recipes: \(error)")
            }
        }
        
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        switch segue.identifier {
        case "showRecipe":
            if let row = tableView.indexPathForSelectedRow?.row {
                let recipe = store.allRecipes[row]
                let recipeViewController = segue.destination as! RecipeViewController
                recipeViewController.recipe = recipe
            }
        default:
            preconditionFailure("Unexpected segue identifier.")
        }
    }


}

