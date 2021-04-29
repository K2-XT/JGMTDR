//
//  Recipe.swift
//  JGMTDR
//
//  Created by Payton Pehrson on 11/9/20.
//  Copyright © 2020 Payton Pehrson. All rights reserved.
//

import UIKit

class Recipe: Codable {
    var id: Int
    var title: String
    var date: Date
    var diet: String
    var ingredients: String
    var instructions: String
    
    init(id: Int, title: String, diet: String, ingredients: String, instructions: String) {
        self.id = id
        self.title = title
        self.date = Date()
        self.diet = diet
        self.ingredients = ingredients
        self.instructions = instructions
    }
    
    //So... I'm not... entirely sure... that I need this? I'm including it just in case it can't tell what keys match to what, even though they're all the same title.
    enum CodingKeys: String, CodingKey {
        case id
        case title
        case date
        case diet
        case ingredients
        case instructions
    }
    
    convenience init() {
        self.init(id: 0, title: "Here Is A Test Recipe", diet: "Vegan", ingredients: "1 Cup of Love", instructions: "Make it with Love")
    }
}
