//
//  RecipeViewController.swift
//  JGMTDR
//
//  Created by Payton Pehrson on 11/18/20.
//  Copyright © 2020 Payton Pehrson. All rights reserved.
//

import UIKit

class RecipeViewController: UIViewController {
    
    @IBOutlet var titleLabel: UILabel!
    @IBOutlet var dateLabel: UILabel!
    @IBOutlet var dietLabel: UILabel!
    @IBOutlet var recipeContentView: UITextView!
    
    
    //DateFormatter
    let dateFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateStyle = .short
        formatter.timeStyle = .none
        return formatter
    }()
    
    //The recipe that we may have been passed.
    var recipe: Recipe!
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        titleLabel.text = recipe.title
        dateLabel.text = dateFormatter.string(from: recipe.date)
        dietLabel.text = recipe.diet
        recipeContentView.text = recipe.ingredients + "\n \n" + recipe.instructions
        
        //scrollView.isScrollEnabled = true
        //scrollView.contentSize = contentView.frame.size
    }
    
}
